#!/usr/bin/env python3
"""Auditoria retrospectiva COTAHIST 1993 — FASES 06/07/08, fail-closed."""
import csv
import datetime
import hashlib
import json
import zipfile
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

YEAR = "1993"
ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP"
CSV_PATH = ROOT / f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv"
Q = ROOT / "dados/cotahist/quality"
Q.mkdir(parents=True, exist_ok=True)

FIELDS = [
    ("data_pregao", 3, 10), ("codbdi", 11, 12), ("codneg", 13, 24), ("tpmerc", 25, 27),
    ("nomres", 28, 39), ("especi", 40, 49), ("prazot", 50, 52), ("modref", 53, 56),
    ("preab", 57, 69), ("premax", 70, 82), ("premin", 83, 95), ("premed", 96, 108),
    ("preult", 109, 121), ("totneg", 148, 152), ("quatot", 153, 170), ("voltot", 171, 188),
    ("preexe", 189, 201), ("indopc", 202, 202), ("datven", 203, 210), ("fatcot", 211, 217),
    ("ptoexe", 218, 230), ("codisi", 231, 242), ("dimes", 243, 245),
]
KEY = (
    "data_pregao", "codbdi", "codneg", "tpmerc", "codisi", "dimes",
    "especi", "prazot", "datven", "indopc", "preexe", "ptoexe",
)
NUMERIC = ("preab", "premax", "premin", "premed", "preult", "totneg", "quatot", "voltot")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_rows():
    out = []
    with zipfile.ZipFile(RAW) as z:
        members = [name for name in z.namelist() if not name.endswith("/")]
        if len(members) != 1:
            raise RuntimeError(f"RAW ambiguo: {members}")
        with z.open(members[0]) as f:
            for ln, raw_line in enumerate(f, 1):
                if not raw_line.startswith(b"01"):
                    continue

                # COTAHIST é registro fixo de 245 bytes; remover somente CR/LF.
                x = raw_line.rstrip(b"\r\n")
                if len(x) != 245:
                    raise RuntimeError(
                        f"linha {ln}: {len(x)} bytes; esperado 245 apos remover CR/LF"
                    )

                row = {
                    key: x[start - 1:end].decode("latin-1").strip()
                    for key, start, end in FIELDS
                }
                row["_line"] = ln
                out.append(row)
    return out


def norm_rows():
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pick(headers, *names):
    low = {h.lower().strip(): h for h in headers}
    for name in names:
        if name in low:
            return low[name]
    raise RuntimeError(f"coluna ausente: {names}")


raw = raw_rows()
norm = norm_rows()

if len(raw) != len(norm):
    raise RuntimeError(
        f"RAW/NORMALIZED contagem divergente: {len(raw)} != {len(norm)}"
    )

headers = norm[0].keys() if norm else []
aliases = {
    "data_pregao": ("data_pregao", "data", "date"),
    "codbdi": ("codbdi",),
    "codneg": ("codneg", "codigo_negociacao", "cod_neg"),
    "tpmerc": ("tpmerc",),
    "especi": ("especi", "especificacao"),
    "prazot": ("prazot",),
    "codisi": ("codisi", "cod_isi"),
    "dimes": ("dimes", "dismes"),
    "datven": ("datven", "data_vencimento"),
    "indopc": ("indopc",),
    "preab": ("preab", "preabe", "preco_abertura"),
    "premax": ("premax", "preco_maximo"),
    "premin": ("premin", "preco_minimo"),
    "premed": ("premed", "preco_medio"),
    "preult": ("preult", "preco_ultimo"),
    "totneg": ("totneg", "numero_negocios"),
    "quatot": ("quatot", "quantidade_total"),
    "voltot": ("voltot", "volume_total"),
    "preexe": ("preexe", "preco_exercicio"),
    "ptoexe": ("ptoexe", "pontos_exercicio"),
}
nm = {key: pick(headers, *values) for key, values in aliases.items()}


def decimal(value):
    value = str(value).strip().replace(",", ".")
    return Decimal(value) if value else None


def canonical_text(key, value):
    value = str(value).strip()
    if key == "data_pregao" and len(value) == 10 and value[4] == "-" and value[7] == "-":
        return value.replace("-", "")
    return value


# F06 — RAW x NORMALIZED
critical = (
    "data_pregao", "codbdi", "codneg", "tpmerc",
    "preab", "premax", "premin", "premed", "preult",
    "totneg", "quatot", "voltot",
)
mismatches = []

for raw_row, norm_row in zip(raw, norm):
    bad = {}
    for key in critical:
        raw_value = canonical_text(key, raw_row[key])
        normalized_value = canonical_text(key, norm_row[nm[key]])

        if key in NUMERIC:
            try:
                raw_decimal = decimal(raw_value)
                normalized_decimal = decimal(normalized_value)
                ok = raw_decimal == normalized_decimal

                if (
                    not ok
                    and raw_decimal is not None
                    and normalized_decimal not in (None, Decimal(0))
                ):
                    ratio = raw_decimal / normalized_decimal
                    ok = ratio in {
                        Decimal(1), Decimal(10), Decimal(100),
                        Decimal(1000), Decimal(10000), Decimal(100000),
                        Decimal(1000000),
                    }
            except Exception:
                ok = False
        else:
            ok = raw_value == normalized_value

        if not ok:
            bad[key] = {"raw": raw_value, "normalized": normalized_value}

    if bad and len(mismatches) < 50:
        mismatches.append({"line": raw_row["_line"], "fields": bad})


f06 = {
    "schema_version": "1.0.0",
    "year": 1993,
    "phase": "FASE06",
    "status": "VALIDADO" if not mismatches else "BLOQUEADO",
    "raw_sha256": sha(RAW),
    "normalized_sha256": sha(CSV_PATH),
    "raw_records": len(raw),
    "normalized_records": len(norm),
    "critical_fields_checked": list(critical),
    "mismatch_count": len(mismatches),
    "mismatch_sample": mismatches,
    "decision": "VALIDADO" if not mismatches else "BLOQUEADO",
    "normalized_header_aliases": {key: nm[key] for key in critical},
    "note": (
        "Comparacao reproduzivel RAW/NORMALIZED; datas sao comparadas em "
        "representacao canonica YYYYMMDD e escalas decimais numericas de "
        "10^n sao aceitas apenas quando a razao e inteira e limitada."
    ),
}
(Q / "COTAHIST_1993_FASE06_RECONCILIACAO_V1.json").write_text(
    json.dumps(f06, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

# F07 — key/codes
groups = defaultdict(list)
for row in raw:
    groups[tuple(row[key] for key in KEY)].append(row)

collisions = {key: rows for key, rows in groups.items() if len(rows) > 1}
distinct_stats = []

for key, rows in collisions.items():
    signatures = {tuple(row[field] for field in NUMERIC) for row in rows}
    if len(signatures) > 1 and len(distinct_stats) < 30:
        distinct_stats.append({
            "key": key,
            "count": len(rows),
            "distinct_stat_signatures": len(signatures),
            "lines": [row["_line"] for row in rows[:20]],
        })

required_empty = {
    key: sum(1 for row in raw if not row[key])
    for key in KEY
}

f07_valid = (
    not collisions
    and not distinct_stats
    and all(value == 0 for value in required_empty.values())
)

f07 = {
    "schema_version": "1.0.0",
    "year": 1993,
    "phase": "FASE07",
    "status": "VALIDADO" if f07_valid else "BLOQUEADO",
    "candidate_key_fields": list(KEY),
    "row_count": len(raw),
    "distinct_key_count": len(groups),
    "collision_group_count": len(collisions),
    "collision_row_count": sum(len(rows) for rows in collisions.values()),
    "same_key_distinct_statistics_group_count": len(distinct_stats),
    "sample": distinct_stats,
    "required_empty_counts": required_empty,
    "raw_sha256": sha(RAW),
    "decision": "VALIDADO" if f07_valid else "BLOQUEADO",
}
(Q / "COTAHIST_1993_FASE07_IDENTIDADE_CHAVES_V1.json").write_text(
    json.dumps(f07, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

# F08 — semantic/calendar structural checks
dates = [row["data_pregao"] for row in raw]
valid_dates = []
invalid_dates = []
weekend_dates = []

for value in dates:
    try:
        date_value = datetime.datetime.strptime(value, "%Y%m%d").date()
        valid_dates.append(date_value)
        if date_value.weekday() >= 5:
            weekend_dates.append(value)
    except ValueError:
        invalid_dates.append(value)

unique_dates = sorted(set(valid_dates))
unique_date_set = set(unique_dates)
weekday_gaps = []

if unique_dates:
    current = unique_dates[0]
    while current <= unique_dates[-1]:
        if current.weekday() < 5 and current not in unique_date_set:
            weekday_gaps.append(current.isoformat())
        current += datetime.timedelta(days=1)

out_of_order = sum(1 for a, b in zip(dates, dates[1:]) if b < a)

tpmerc_distribution = Counter(row["tpmerc"] for row in raw)
codbdi_distribution = Counter(row["codbdi"] for row in raw)
dimes_distribution = Counter(row["dimes"] for row in raw)

ohlc_bad = 0
for row in raw:
    try:
        op, hi, lo, mid, close = [
            Decimal(row[key])
            for key in ("preab", "premax", "premin", "premed", "preult")
        ]
        if (
            hi < max(op, lo, close)
            or lo > min(op, hi, close)
            or not (lo <= mid <= hi)
        ):
            ohlc_bad += 1
    except Exception:
        ohlc_bad += 1

f08_gates = {
    "all_dates_valid": len(valid_dates) == len(dates),
    "no_weekend_dates": len(weekend_dates) == 0,
    "records_chronological": out_of_order == 0,
    "year_bounds": all(date_value.year == 1993 for date_value in valid_dates),
    "ohlc_relations_valid": ohlc_bad == 0,
    "tpmerc_observed": bool(tpmerc_distribution),
    "codbdi_observed": bool(codbdi_distribution),
}

f08_valid = all(f08_gates.values())

f08 = {
    "schema_version": "1.0.0",
    "year": 1993,
    "phase": "FASE08",
    "status": "VALIDADO" if f08_valid else "BLOQUEADO",
    "records": len(raw),
    "first_date": min(dates) if dates else None,
    "last_date": max(dates) if dates else None,
    "distinct_trading_dates": len(unique_dates),
    "candidate_weekday_gaps": weekday_gaps,
    "out_of_order_records": out_of_order,
    "invalid_dates": len(invalid_dates),
    "weekend_dates": len(weekend_dates),
    "tpmerc_distribution": dict(tpmerc_distribution),
    "codbdi_distribution": dict(codbdi_distribution),
    "dimes_distribution": dict(dimes_distribution),
    "ohlc_relation_violations": ohlc_bad,
    "gates": f08_gates,
    "raw_sha256": sha(RAW),
    "decision": "VALIDADO" if f08_valid else "BLOQUEADO",
    "note": (
        "Lacunas em dias uteis sao apenas candidatas a nao-pregao; nao sao "
        "classificadas como feriados sem fonte primaria. PRAZOT e avaliado "
        "como campo preservado; este teste nao atribui significado economico adicional."
    ),
}
(Q / "COTAHIST_1993_FASE08_SEMANTICA_CALENDARIO_V1.json").write_text(
    json.dumps(f08, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

failed = []
if mismatches:
    failed.append("FASE06")
if not f07_valid:
    failed.append("FASE07")
if not f08_valid:
    failed.append("FASE08")

print(json.dumps({
    "year": 1993,
    "records": len(raw),
    "fases": {"06": f06["status"], "07": f07["status"], "08": f08["status"]},
    "failed": failed,
}, ensure_ascii=False))

if failed:
    raise SystemExit("FAIL-CLOSED: " + ",".join(failed))
