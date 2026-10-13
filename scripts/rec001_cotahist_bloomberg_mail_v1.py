#!/usr/bin/env python3
import hashlib, io, json, os, sqlite3, tempfile, urllib.request, zipfile
from collections import Counter

B3_ZIP = "dados/cotahist/raw/anual/COTAHIST_A2026.ZIP"
BLOOM_ZIP_URL = "https://raw.githubusercontent.com/carlos-andrade/BLOOMBERG_MAIL/main/EMAILS_RECEBIDOS/INGESTAO/005/RAW/COTAHIST_A2026.ZIP"
OUT = "dados/cotahist/quality/COTAHIST_A2026_REC001_BLOOMBERG_MAIL_V1.json"

def sha256_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""): h.update(b)
    return h.hexdigest()

def inspect_zip(path):
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        names=z.namelist()
        member=next((n for n in names if n.upper().endswith("COTAHIST_A2026.TXT")), None)
        if not member: raise RuntimeError("COTAHIST_A2026.TXT ausente")
        info=z.getinfo(member)
        return bad, member, info.file_size

def stream_stats(path):
    with zipfile.ZipFile(path) as z:
        member=next(n for n in z.namelist() if n.upper().endswith("COTAHIST_A2026.TXT"))
        with z.open(member) as f:
            count=0; dates=[]; first00=None; first01=None; last01=None; trailer99=None; member_sha=hashlib.sha256()
            for raw in f:
                member_sha.update(raw)
                line=raw.rstrip(b"\r\n")
                if len(line)!=245: raise RuntimeError(f"record length {len(line)}")
                typ=line[:2].decode("ascii","replace")
                if typ=="00" and first00 is None: first00=line.decode("latin-1")
                elif typ=="01":
                    count+=1
                    if first01 is None: first01=line.decode("latin-1")
                    last01=line.decode("latin-1")
                    dates.append(line[2:10].decode("ascii","replace"))
                elif typ=="99": trailer99=line.decode("latin-1")
            return {"record01_count":count,"first_record00":first00,"first_record01":first01,
                    "last_record01":last01,"trailer_record99":trailer99,
                    "date_min":min(dates) if dates else None,"date_max":max(dates) if dates else None,
                    "member_sha256":member_sha.hexdigest()}

def iter_record01_lines(handle):
    """Yield only negotiated COTAHIST detail records; ignore period-specific header/trailer."""
    for raw in handle:
        if raw[:2] == b"01":
            yield raw


def describe_record(raw, position):
    return {
        "record01_position": position,
        "date": raw[2:10].decode("ascii", "replace"),
        "codbdi": raw[10:12].decode("ascii", "replace").strip(),
        "codneg": raw[12:24].decode("latin-1", "replace").strip(),
        "tpmerc": raw[24:27].decode("ascii", "replace").strip(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "prefix": raw[:48].decode("latin-1", "replace"),
    }


def scan_target_tickers(path, targets):
    found = {ticker: [] for ticker in targets}
    with zipfile.ZipFile(path) as archive:
        member = next(n for n in archive.namelist() if n.upper().endswith("COTAHIST_A2026.TXT"))
        with archive.open(member) as handle:
            position = 0
            for raw in iter_record01_lines(handle):
                position += 1
                ticker = raw[12:24].decode("latin-1", "replace").strip()
                if ticker in found and len(found[ticker]) < 20:
                    found[ticker].append(describe_record(raw, position))
    return found


def compare_streams(b3_path, bloom_path):
    with zipfile.ZipFile(b3_path) as a, zipfile.ZipFile(bloom_path) as b:
        an=next(n for n in a.namelist() if n.upper().endswith("COTAHIST_A2026.TXT"))
        bn=next(n for n in b.namelist() if n.upper().endswith("COTAHIST_A2026.TXT"))
        with a.open(an) as fa, b.open(bn) as fb:
            ia=iter_record01_lines(fa)
            ib=iter_record01_lines(fb)
            position=0
            mismatches=[]
            previous_a=[]
            previous_b=[]
            while True:
                ra=next(ia, None)
                rb=next(ib, None)
                if ra is None or rb is None:
                    b3_exhausted = ra is None
                    bloom_exhausted = rb is None
                    break
                position += 1
                if ra != rb:
                    context_a = [describe_record(raw, pos) for pos, raw in previous_a]
                    context_b = [describe_record(raw, pos) for pos, raw in previous_b]
                    context_a.append(describe_record(ra, position))
                    context_b.append(describe_record(rb, position))
                    for _ in range(5):
                        next_a = next(ia, None)
                        next_b = next(ib, None)
                        if next_a is not None:
                            position_a = context_a[-1]["record01_position"] + 1
                            context_a.append(describe_record(next_a, position_a))
                        if next_b is not None:
                            position_b = context_b[-1]["record01_position"] + 1
                            context_b.append(describe_record(next_b, position_b))
                    mismatches.append({
                        "record01_position": position,
                        "b3_date": ra[2:10].decode("ascii", "replace"),
                        "bloomberg_date": rb[2:10].decode("ascii", "replace"),
                        "b3_sha256": hashlib.sha256(ra).hexdigest(),
                        "bloomberg_sha256": hashlib.sha256(rb).hexdigest(),
                        "b3_prefix": ra[:40].decode("latin-1", "replace"),
                        "bloomberg_prefix": rb[:40].decode("latin-1", "replace"),
                        "context_window": {"b3": context_a, "bloomberg_mail": context_b},
                    })
                    break
                previous_a.append((position, ra))
                previous_b.append((position, rb))
                if len(previous_a) > 3:
                    previous_a.pop(0)
                if len(previous_b) > 3:
                    previous_b.pop(0)
            return {
                "common_record01_prefix": position if not mismatches else position - 1,
                "first_difference": mismatches[0] if mismatches else None,
                "b3_exhausted": b3_exhausted if not mismatches else False,
                "bloomberg_exhausted": bloom_exhausted if not mismatches else False,
                "comparison_unit": "record type 01 only; period-specific type 00 headers and type 99 trailers excluded",
            }


def compare_record01_multiset(b3_path, bloom_path, database_path):
    """Compare exact type-01 record payloads as a multiset, independent of ordering."""
    connection = sqlite3.connect(database_path)
    connection.execute("PRAGMA journal_mode=OFF")
    connection.execute("PRAGMA synchronous=OFF")
    connection.execute("PRAGMA temp_store=FILE")
    connection.execute("CREATE TABLE records (source INTEGER NOT NULL, digest BLOB NOT NULL, n INTEGER NOT NULL, PRIMARY KEY(source, digest)) WITHOUT ROWID")
    upsert = "INSERT INTO records(source,digest,n) VALUES(?,?,1) ON CONFLICT(source,digest) DO UPDATE SET n=n+1"

    def load(path, source):
        total = 0
        batch = []
        with zipfile.ZipFile(path) as archive:
            member = next(n for n in archive.namelist() if n.upper().endswith("COTAHIST_A2026.TXT"))
            with archive.open(member) as handle:
                for raw in iter_record01_lines(handle):
                    payload = raw.rstrip(b"\\r\\n")
                    batch.append((source, hashlib.sha256(payload).digest()))
                    total += 1
                    if len(batch) >= 10000:
                        connection.executemany(upsert, batch)
                        connection.commit()
                        batch.clear()
                if batch:
                    connection.executemany(upsert, batch)
                    connection.commit()
        return total

    b3_total = load(b3_path, 0)
    bloom_total = load(bloom_path, 1)
    query = """
        SELECT COUNT(*) AS digest_count,
               COALESCE(SUM(CASE WHEN a.n > COALESCE(b.n,0) THEN a.n-COALESCE(b.n,0) ELSE 0 END),0) AS missing_multiplicity
        FROM (SELECT digest,n FROM records WHERE source=0) a
        LEFT JOIN (SELECT digest,n FROM records WHERE source=1) b ON a.digest=b.digest
    """
    digest_count, missing_multiplicity = connection.execute(query).fetchone()
    b3_unique = connection.execute("SELECT COUNT(*) FROM records WHERE source=0").fetchone()[0]
    bloom_unique = connection.execute("SELECT COUNT(*) FROM records WHERE source=1").fetchone()[0]
    b3_only = connection.execute("""
        SELECT a.digest, a.n, COALESCE(b.n,0)
        FROM (SELECT digest,n FROM records WHERE source=0) a
        LEFT JOIN (SELECT digest,n FROM records WHERE source=1) b ON a.digest=b.digest
        WHERE a.n > COALESCE(b.n,0) LIMIT 20
    """).fetchall()
    bloom_only = connection.execute("""
        SELECT b.digest, b.n, COALESCE(a.n,0)
        FROM (SELECT digest,n FROM records WHERE source=1) b
        LEFT JOIN (SELECT digest,n FROM records WHERE source=0) a ON a.digest=b.digest
        WHERE b.n > COALESCE(a.n,0) LIMIT 20
    """).fetchall()
    missing_from_b3 = connection.execute("""
        SELECT COALESCE(SUM(CASE WHEN b.n > COALESCE(a.n,0) THEN b.n-COALESCE(a.n,0) ELSE 0 END),0)
        FROM (SELECT digest,n FROM records WHERE source=1) b
        LEFT JOIN (SELECT digest,n FROM records WHERE source=0) a ON a.digest=b.digest
    """).fetchone()[0]
    connection.close()
    return {
        "method": "SHA-256 multiset of type-01 payload bytes with line terminators excluded; duplicate multiplicity preserved; ordering ignored",
        "b3_record01_count": b3_total,
        "bloomberg_mail_record01_count": bloom_total,
        "b3_unique_payload_hashes": b3_unique,
        "bloomberg_mail_unique_payload_hashes": bloom_unique,
        "b3_records_missing_from_bloomberg_multiplicity": int(missing_multiplicity),
        "bloomberg_records_missing_from_b3_multiplicity": int(missing_from_b3),
        "bloomberg_contains_all_b3_records_as_exact_payload_multiset": missing_multiplicity == 0,
        "unordered_multiset_exact_match": missing_multiplicity == 0 and missing_from_b3 == 0,
        "b3_only_hash_count_sample": [
            {"sha256": row[0].hex(), "b3_count": row[1], "bloomberg_count": row[2]} for row in b3_only
        ],
        "bloomberg_only_hash_count_sample": [
            {"sha256": row[0].hex(), "bloomberg_count": row[1], "b3_count": row[2]} for row in bloom_only
        ],
        "interpretation_limit": "A multiset match proves payload equality independent of ordering, not equal source ordering or a promotion decision."
    }


def main():
    with tempfile.TemporaryDirectory() as td:
        bloom=os.path.join(td,"COTAHIST_A2026.ZIP")
        req=urllib.request.Request(BLOOM_ZIP_URL,headers={"User-Agent":"BLOOMBERG_MAIL-REC001-B3/1.0"})
        with urllib.request.urlopen(req,timeout=120) as r, open(bloom,"wb") as out:
            for chunk in iter(lambda:r.read(1024*1024),b""): out.write(chunk)
        b3_sha=sha256_file(B3_ZIP); bloom_sha=sha256_file(bloom)
        b3_zip_bad,b3_member,b3_member_size=inspect_zip(B3_ZIP)
        bloom_zip_bad,bloom_member,bloom_member_size=inspect_zip(bloom)
        b3_stats=stream_stats(B3_ZIP); bloom_stats=stream_stats(bloom)
        cmp=compare_streams(B3_ZIP,bloom)
        multiset = compare_record01_multiset(B3_ZIP, bloom, os.path.join(td, "rec001-record-multiset.sqlite"))
        diagnostics = {}
        if cmp["first_difference"]:
            first = cmp["first_difference"]
            tickers = sorted({first["b3_prefix"][12:24].strip(), first["bloomberg_prefix"][12:24].strip()})
            diagnostics = {
                "purpose": "Diagnosticar se a primeira divergência decorre de registo ausente, ticker distinto ou deslocamento local; não altera o critério byte-a-byte.",
                "target_tickers": tickers,
                "b3_occurrences": scan_target_tickers(B3_ZIP, tickers),
                "bloomberg_mail_occurrences": scan_target_tickers(bloom, tickers),
                "interpretation_limit": "A presença de um ticker noutra posição não prova equivalência semântica nem autoriza promoção automática."
            }
        if cmp["first_difference"] is None and cmp["b3_exhausted"] and not cmp["bloomberg_exhausted"]:
            result = "PASS_OVERLAP_EXACT"
        elif cmp["first_difference"] is None and cmp["b3_exhausted"] and cmp["bloomberg_exhausted"]:
            result = "PASS_EXACT"
        elif multiset["bloomberg_contains_all_b3_records_as_exact_payload_multiset"] and bloom_stats["record01_count"] > b3_stats["record01_count"]:
            result = "PASS_OVERLAP_CONTENT_EXACT_ORDER_VARIANCE"
        else:
            result = "FAIL_CONTENT_DIVERGENCE"
        evidence={"schema_version":"1.0-rec001-b3-cross-repo","result":result,"raw_preserved":True,
          "b3_snapshot":{"path":B3_ZIP,"zip_sha256":b3_sha,"member":b3_member,"member_size":b3_member_size,"zip_integrity":b3_zip_bad is None,"stats":b3_stats},
          "bloomberg_mail_raw":{"url":BLOOM_ZIP_URL,"zip_sha256":bloom_sha,"member":bloom_member,"member_size":bloom_member_size,"zip_integrity":bloom_zip_bad is None,"stats":bloom_stats},
          "comparison":cmp,
          "unordered_content_reconciliation":multiset,
          "divergence_diagnostics":diagnostics,
          "interpretation":"PASS_OVERLAP_EXACT means the ordered B3 type-01 stream is an exact prefix. PASS_OVERLAP_CONTENT_EXACT_ORDER_VARIANCE means every B3 type-01 payload occurs in BLOOMBERG_MAIL with at least the same multiplicity, but source order differs; content reconciliation passes while promotion remains blocked for explicit order-variance review. Additional Bloomberg rows are not automatically classified as temporal-only without date-level reconciliation.",
          "promotion_impact":"BLOCKED_ORDER_VARIANCE_REVIEW" if result == "PASS_OVERLAP_CONTENT_EXACT_ORDER_VARIANCE" else ("REC001_B3_ELIGIBLE_FOR_REVIEW" if result.startswith("PASS_") else "BLOCKED_CONTENT_DIVERGENCE")}
        os.makedirs(os.path.dirname(OUT),exist_ok=True)
        with open(OUT,"w",encoding="utf-8") as f: json.dump(evidence,f,ensure_ascii=False,indent=2); f.write("\n")
if __name__=="__main__": main()

# controlled trigger 2026-10-08
