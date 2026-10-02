#!/usr/bin/env python3
import base64
import csv
import datetime as dt
import hashlib
import json
import zipfile
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1998.ZIP")
NORMALIZED = Path("dados/cotahist/normalized/anual/COTAHIST_A1998.csv")
OUT = Path("dados/cotahist/quality/COTAHIST_1998_FASE06_RECONCILIACAO_OHLC_V1.json")

TARGETS = [
    {"date": "19980716", "codneg": "ELET6T"},
    {"date": "19981015", "codneg": "RCTB40T"},
    {"date": "19981204", "codneg": "CMIG4T"},
]

FIELDS = [
    ("data_pregao", 3, 10, "date"),
    ("codbdi", 11, 12, "text"),
    ("codneg", 13, 24, "text"),
    ("tpmerc", 25, 27, "text"),
    ("nomres", 28, 39, "text"),
    ("especi", 40, 49, "text"),
    ("prazot", 50, 51, "text"),
    ("modref", 52, 52, "text"),
    ("preabe", 57, 69, "price"),
    ("premax", 70, 82, "price"),
    ("premin", 83, 95, "price"),
    ("premed", 96, 108, "price"),
    ("preult", 109, 121, "price"),
    ("preofc", 122, 134, "price"),
    ("preofv", 135, 147, "price"),
    ("totneg", 148, 152, "int"),
    ("quatot", 153, 170, "int"),
    ("voltot", 171, 188, "volume"),
    ("preexe", 189, 201, "price"),
    ("indopc", 202, 202, "text"),
    ("datven", 203, 210, "date"),
    ("fatcot", 211, 217, "price"),
    ("ptoexe", 218, 224, "price"),
    ("codisi", 225, 236, "text"),
    ("dismes", 237, 245, "text"),
]

def text(b, a, z):
    return b[a-1:z].decode("latin-1").strip()

def parse(b, kind, a, z):
    v = text(b, a, z)
    if not v:
        return ""
    if kind == "price":
        return f"{int(v) / 100:.2f}"
    if kind == "int":
        return str(int(v))
    if kind == "volume":
        return f"{int(v) / 100:.2f}"
    if kind == "date":
        return v
    return v

def normalized_value(row, field):
    v = row.get(field, "")
    if field in {"preabe","premax","premin","premed","preult","preofc","preofv","preexe","fatcot","ptoexe"}:
        return f"{float(v):.2f}" if v else ""
    if field == "voltot":
        return f"{float(v):.2f}" if v else ""
    return v.strip()

def main():
    if not RAW.exists() or not NORMALIZED.exists():
        raise SystemExit("FAIL-CLOSED: RAW ou NORMALIZED ausente")

    raw_sha = hashlib.sha256(RAW.read_bytes()).hexdigest()
    normalized_sha = hashlib.sha256(NORMALIZED.read_bytes()).hexdigest()

    with zipfile.ZipFile(RAW) as z:
        members = z.namelist()
        payload = z.read(members[0])
    raw_records = payload.splitlines()
    type01 = [(i, b) for i, b in enumerate(raw_records) if b[:2] == b"01"]

    raw_hits = {}
    for idx, b in type01:
        key = (text(b,3,10), text(b,13,24))
        if key in {(x["date"], x["codneg"]) for x in TARGETS}:
            raw_hits[key] = (idx, b)

    with NORMALIZED.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        normalized_hits = {}
        for rownum, row in enumerate(reader):
            key = (row["data_pregao"].replace("-", ""), row["codneg"].strip())
            if key in {(x["date"], x["codneg"]) for x in TARGETS}:
                normalized_hits[key] = (rownum, row)

    records = []
    overall_match = True
    for target in TARGETS:
        key = (target["date"], target["codneg"])
        if key not in raw_hits or key not in normalized_hits:
            overall_match = False
            records.append({
                "target": target,
                "status": "MISSING",
                "raw_found": key in raw_hits,
                "normalized_found": key in normalized_hits,
            })
            continue

        raw_idx, raw_b = raw_hits[key]
        norm_idx, norm_row = normalized_hits[key]
        raw_values = {name: parse(raw_b, kind, a, z) for name,a,z,kind in FIELDS}
        normalized_values = {name: normalized_value(norm_row, name) for name,_,_,_ in FIELDS}
        mismatches = []
        for name, _, _, _ in FIELDS:
            if raw_values[name] != normalized_values[name]:
                mismatches.append({
                    "field": name,
                    "raw": raw_values[name],
                    "normalized": normalized_values[name],
                })

        ohlc = {k: raw_values[k] for k in ("preabe","premax","premin","premed","preult")}
        record = {
            "target": target,
            "status": "MATCH" if not mismatches else "MISMATCH",
            "raw_record_index": raw_idx,
            "normalized_row_index": norm_idx,
            "raw_record_sha256": hashlib.sha256(raw_b).hexdigest(),
            "raw_record_length": len(raw_b),
            "raw_record_base64": base64.b64encode(raw_b).decode("ascii"),
            "raw_fields": raw_values,
            "normalized_fields": normalized_values,
            "field_mismatches": mismatches,
            "ohlc": ohlc,
            "ohlc_rule_observation": {
                "preult_lt_premin": float(ohlc["preult"]) < float(ohlc["premin"]),
                "preult_gt_premax": float(ohlc["preult"]) > float(ohlc["premax"]),
                "premin_le_premed_le_premax": float(ohlc["premin"]) <= float(ohlc["premed"]) <= float(ohlc["premax"]),
            },
        }
        if mismatches:
            overall_match = False
        records.append(record)

    evidence = {
        "schema_version": "1.0.0",
        "year": 1998,
        "phase": "FASE06_RECONCILIACAO_OHLC",
        "status": "VALIDADO" if overall_match and len(records) == 3 else "ANALISE_REQUERIDA",
        "decision": "PARSER_FIDELIDADE_CONFIRMADA_SEM_LIBERACAO" if overall_match and len(records) == 3 else "BLOQUEADO_PARA_FASE07",
        "purpose": "Reconciliar os tres registros TERM que apresentam PREULT fora do intervalo PREMIN-PREMAX, comparando bytes RAW, campos parseados e NORMALIZED.",
        "raw_path": str(RAW),
        "normalized_path": str(NORMALIZED),
        "raw_sha256": raw_sha,
        "normalized_sha256": normalized_sha,
        "targets": TARGETS,
        "record_field_contract": [x[0] for x in FIELDS],
        "official_b3_layout": {
            "source": "https://www.b3.com.br/data/files/65/50/AD/26/29C8B51095EE46B5790D8AA8/HistoricalQuotations_B3.pdf",
            "tpmerc_030": "TERM",
            "premax": "highest floor price",
            "premin": "lowest floor price",
            "preult": "last negotiated price"
        },
        "reconciliation": records,
        "conclusion": (
            "Os bytes RAW e a NORMALIZED devem ser identicos semanticamente nos 25 campos para confirmar fidelidade do parser. "
            "Mesmo com fidelidade confirmada, a anomalia PREULT < PREMIN permanece uma característica a explicar do dado histórico TERM; "
            "esta evidência nao autoriza, por si só, relaxar a regra OHLC nem liberar a FASE07."
            if overall_match and len(records) == 3 else
            "Há divergencia ou ausência entre RAW e NORMALIZED; a FASE07 permanece bloqueada até correção e nova validação."
        ),
        "validated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    OUT.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": evidence["status"],
        "decision": evidence["decision"],
        "records": [(r["target"], r["status"], r.get("raw_record_index")) for r in records],
        "raw_sha256": raw_sha,
        "normalized_sha256": normalized_sha,
    }, ensure_ascii=False))
    if not overall_match or len(records) != 3:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
