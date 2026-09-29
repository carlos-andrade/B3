#!/usr/bin/env python3
"""COTAHIST 1988 — reconciliação integral RAW x NORMALIZED.

Gate fail-closed: compara todos os 167.674 registros tipo 01 usando as
mesmas regras explícitas do normalizador e registra amostra determinística
de 30 registros. Não interpreta semântica econômica.
"""
from __future__ import annotations

import csv
import hashlib
import json
import zipfile
from datetime import datetime
from decimal import Decimal
from pathlib import Path

YEAR = "1988"
RAW = Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
CSV_PATH = Path(f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv")
OUT = Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_RECONCILIACAO_RAW_NORMALIZED_V1.json")

FIELDS = [
    ("data_pregao", 3, 10, "date"),
    ("codbdi", 11, 12, "str"),
    ("codneg", 13, 24, "str"),
    ("tpmerc", 25, 27, "str"),
    ("nomres", 28, 39, "str"),
    ("especi", 40, 49, "str"),
    ("prazot", 50, 52, "str"),
    ("modref", 53, 56, "str"),
    ("preabe", 57, 69, "price"),
    ("premax", 70, 82, "price"),
    ("premin", 83, 95, "price"),
    ("premed", 96, 108, "price"),
    ("preult", 109, 121, "price"),
    ("preofc", 122, 134, "price"),
    ("preofv", 135, 147, "price"),
    ("totneg", 148, 152, "int"),
    ("quatot", 153, 170, "int"),
    ("voltot", 171, 188, "money"),
    ("preexe", 189, 201, "price"),
    ("indopc", 202, 202, "str"),
    ("datven", 203, 210, "date"),
    ("fatcot", 211, 217, "int"),
    ("ptoexe", 218, 230, "price6"),
    ("codisi", 231, 242, "str"),
    ("dismes", 243, 245, "str"),
]
HEADER = [x[0] for x in FIELDS]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def clean(raw: bytes) -> str:
    return raw.decode("latin-1").strip()

def normalize(raw: bytes, kind: str) -> str:
    value = clean(raw)
    if kind == "str":
        return value
    if kind == "date":
        if value in {"", "00000000"}:
            return ""
        return datetime.strptime(value, "%Y%m%d").strftime("%Y-%m-%d")
    if kind in {"price", "money"}:
        return str(Decimal(value) / Decimal(100)) if value else ""
    if kind == "price6":
        return str(Decimal(value) / Decimal(1000000)) if value else ""
    if kind == "int":
        return str(int(value)) if value else ""
    raise ValueError(kind)

def raw_records():
    records = []
    with zipfile.ZipFile(RAW) as zf:
        members = [n for n in zf.namelist() if not n.endswith("/")]
        if len(members) != 1:
            raise RuntimeError(f"ZIP deve conter exatamente 1 arquivo: {members}")
        with zf.open(members[0]) as src:
            for line_no, raw in enumerate(src, 1):
                line = raw.rstrip(b"\r\n")
                if line[:2] != b"01":
                    continue
                if len(line) != 245:
                    raise RuntimeError(f"Registro tipo 01 com {len(line)} bytes na linha {line_no}")
                row = {
                    name: normalize(line[start - 1:end], kind)
                    for name, start, end, kind in FIELDS
                }
                row["_line"] = line_no
                records.append(row)
    return records

raw = raw_records()
with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames or []
    missing = [h for h in HEADER if h not in headers]
    if missing:
        raise RuntimeError("Campos ausentes no NORMALIZED: " + ", ".join(missing))
    normalized = list(reader)

if len(raw) != len(normalized):
    count_gate = False
else:
    count_gate = True

field_mismatches = {field: 0 for field in HEADER}
mismatch_samples = []
for i, (rr, nr) in enumerate(zip(raw, normalized), 1):
    for field in HEADER:
        a = rr[field]
        b = str(nr.get(field, "")).strip()
        if a != b:
            field_mismatches[field] += 1
            if len(mismatch_samples) < 30:
                mismatch_samples.append({
                    "row": i,
                    "raw_line": rr["_line"],
                    "field": field,
                    "raw_expected_normalized": a,
                    "normalized": b,
                })

idxs = sorted(set(
    [0, 1, 2, 3, 4, len(raw) - 5, len(raw) - 4, len(raw) - 3, len(raw) - 2, len(raw) - 1]
    + [round(i * (len(raw) - 1) / 19) for i in range(20)]
))
sample_30 = []
for i in idxs[:30]:
    sample_30.append({
        "normalized_row": i + 1,
        "raw_line": raw[i]["_line"],
        "data_pregao": raw[i]["data_pregao"],
        "codneg": raw[i]["codneg"],
        "tpmerc": raw[i]["tpmerc"],
        "preabe": raw[i]["preabe"],
        "preult": raw[i]["preult"],
        "quatot": raw[i]["quatot"],
        "voltot": raw[i]["voltot"],
    })

all_fields_zero = all(v == 0 for v in field_mismatches.values())
result = {
    "schema_version": "1.0.0",
    "year": 1988,
    "status": "RECONCILIACAO_CONCLUIDA" if count_gate and all_fields_zero and len(sample_30) == 30 else "GATES_FAILED",
    "raw": {
        "path": str(RAW),
        "sha256": sha256(RAW),
        "type01_count": len(raw),
        "record_length_expected": 245,
    },
    "normalized": {
        "path": str(CSV_PATH),
        "sha256": sha256(CSV_PATH),
        "row_count": len(normalized),
        "columns": len(headers),
        "headers": headers,
    },
    "checks": {
        "row_count_equal": count_gate,
        "field_mismatch_counts_all_records": field_mismatches,
        "total_field_mismatches": sum(field_mismatches.values()),
        "sample_30_count": len(sample_30),
        "sample_30": sample_30,
        "mismatch_samples": mismatch_samples,
    },
    "fail_closed_gates": {
        "row_count_equal": count_gate,
        "all_25_fields_reconciled": all_fields_zero,
        "sample_30_present": len(sample_30) == 30,
        "raw_immutable_reference_recorded": True,
    },
    "governance": {
        "semantic_interpretation": False,
        "economic_release": False,
        "raw_mutation": False,
        "1987_exception_inherited": False,
        "fail_closed": True,
    },
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
failed = [k for k, v in result["fail_closed_gates"].items() if not v]
print(json.dumps({
    "status": result["status"],
    "failed_gates": failed,
    "raw_count": len(raw),
    "normalized_count": len(normalized),
    "total_field_mismatches": sum(field_mismatches.values()),
    "output": str(OUT),
}, ensure_ascii=False))
if failed:
    raise SystemExit("GATES FAILED: " + ", ".join(failed))
