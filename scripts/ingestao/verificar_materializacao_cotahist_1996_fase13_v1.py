#!/usr/bin/env python3
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(".")
RAW = ROOT / "dados/cotahist/raw/anual/COTAHIST_A1996.ZIP"
MANIFEST = ROOT / "dados/cotahist/normalized/manifests/COTAHIST_A1996_quality.json"
NORMALIZED = ROOT / "dados/cotahist/normalized/anual/COTAHIST_A1996.csv"
EVIDENCE = ROOT / "dados/cotahist/quality/COTAHIST_1996_FASE13_MATERIALIZACAO_V1.json"

EXPECTED_FIELDS = [
    "data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
    "preabe","premax","premin","premed","preult","preofc","preofv","totneg",
    "quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"
]

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    failures = []
    if not RAW.exists():
        failures.append("RAW_1996_AUSENTE")
    if not MANIFEST.exists():
        failures.append("MANIFESTO_1996_AUSENTE")
    if not NORMALIZED.exists():
        failures.append("NORMALIZED_1996_AUSENTE")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    raw_sha = sha256(RAW) if RAW.exists() else None
    normalized_sha = sha256(NORMALIZED) if NORMALIZED.exists() else None

    if manifest.get("status") != "VALIDADO":
        failures.append("MANIFESTO_1996_NAO_VALIDADO")
    if manifest.get("parser_version") != "1.1.0":
        failures.append("PARSER_VERSION_DIVERGENTE")
    if manifest.get("campos") != 25:
        failures.append("CAMPOS_DIVERGENTES")
    if raw_sha and raw_sha != manifest.get("raw_sha256"):
        failures.append("RAW_SHA256_DIVERGENTE")
    if normalized_sha and normalized_sha != manifest.get("normalized_sha256"):
        failures.append("NORMALIZED_SHA256_DIVERGENTE")

    rows = 0
    fields = 0
    invalid_dates = 0
    outside_year = 0
    first_date = None
    last_date = None

    if NORMALIZED.exists():
        with NORMALIZED.open("r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            header = next(reader, [])
            fields = len(header)
            if header != EXPECTED_FIELDS:
                failures.append("HEADER_25_CAMPOS_DIVERGENTE")
            for row in reader:
                rows += 1
                if len(row) != 25:
                    fields = max(fields, len(row))
                    failures.append("REGISTRO_COM_NUMERO_DE_CAMPOS_INCORRETO")
                    continue
                d = row[0]
                try:
                    if len(d) != 10:
                        raise ValueError
                    year = int(d[:4]); month = int(d[5:7]); day = int(d[8:10])
                    import datetime as dt
                    dt.date(year, month, day)
                    if year != 1996:
                        outside_year += 1
                    if first_date is None or d < first_date: first_date = d
                    if last_date is None or d > last_date: last_date = d
                except Exception:
                    invalid_dates += 1

    if rows != manifest.get("linhas_normalized"):
        failures.append("LINHAS_NORMALIZED_DIVERGENTES")
    if invalid_dates != manifest.get("datas_invalidas", 0):
        failures.append("DATAS_INVALIDAS_DIVERGENTES")
    if outside_year != manifest.get("datas_fora_do_ano", 0):
        failures.append("DATAS_FORA_DO_ANO_DIVERGENTES")

    evidence = {
        "schema_version": "1.0.0",
        "phase": "FASE_13",
        "year": 1996,
        "purpose": "MATERIALIZACAO_NORMALIZED",
        "raw_path": str(RAW),
        "manifest_path": str(MANIFEST),
        "normalized_path": str(NORMALIZED),
        "raw_sha256_actual": raw_sha,
        "raw_sha256_manifest": manifest.get("raw_sha256"),
        "normalized_sha256_actual": normalized_sha,
        "normalized_sha256_manifest": manifest.get("normalized_sha256"),
        "rows_normalized": rows,
        "rows_manifest": manifest.get("linhas_normalized"),
        "fields": fields,
        "first_date": first_date,
        "last_date": last_date,
        "invalid_dates": invalid_dates,
        "dates_outside_year": outside_year,
        "checks": {
            "raw_present": RAW.exists(),
            "manifest_present": MANIFEST.exists(),
            "normalized_present": NORMALIZED.exists(),
            "manifest_validated": manifest.get("status") == "VALIDADO",
            "parser_1_1_0": manifest.get("parser_version") == "1.1.0",
            "fields_25": manifest.get("campos") == 25 and fields == 25,
            "raw_sha256_match": raw_sha == manifest.get("raw_sha256"),
            "normalized_sha256_match": normalized_sha == manifest.get("normalized_sha256"),
            "rows_match": rows == manifest.get("linhas_normalized"),
            "dates_valid": invalid_dates == 0 and outside_year == 0,
        },
        "failures": failures,
        "status": "VALIDADO" if not failures else "INVALIDADO",
        "decision": "NORMALIZED_1996_MATERIALIZADO" if not failures else "FASE_13_BLOQUEADA"
    }
    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit("FAIL-CLOSED: " + "; ".join(failures))

if __name__ == "__main__":
    main()
