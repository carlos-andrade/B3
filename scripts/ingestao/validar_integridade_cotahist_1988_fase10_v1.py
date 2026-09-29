#!/usr/bin/env python3
"""Fase 10 — validação de integridade RAW/NORMALIZED do COTAHIST 1988.

Fail-closed: não corrige dados e não altera o RAW. Confere os hashes registrados
no manifest, o objeto LFS normalizado, estrutura CSV, cardinalidade e domínio
temporal.
"""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

YEAR = 1988
ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "dados/cotahist/raw/anual/COTAHIST_A1988.ZIP"
NORMALIZED = ROOT / "dados/cotahist/normalized/anual/COTAHIST_A1988.csv"
MANIFEST = ROOT / "dados/cotahist/normalized/manifests/COTAHIST_A1988_quality.json"
OUT = ROOT / "dados/cotahist/quality/COTAHIST_1988_FASE10_INTEGRIDADE_V1.json"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    failures = []
    evidence = {
        "schema_version": "1.0.0",
        "phase": "FASE_10",
        "year": YEAR,
        "raw_path": str(RAW.relative_to(ROOT)),
        "normalized_path": str(NORMALIZED.relative_to(ROOT)),
        "manifest_path": str(MANIFEST.relative_to(ROOT)),
        "raw_immutable": True,
        "correction_applied": False,
    }

    for p in (RAW, NORMALIZED, MANIFEST):
        if not p.is_file():
            failures.append(f"missing:{p.relative_to(ROOT)}")
    if failures:
        evidence["status"] = "FAIL"
        evidence["failures"] = failures
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        raise SystemExit("FAIL-CLOSED: " + ", ".join(failures))

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    raw_hash = sha256(RAW)
    normalized_hash = sha256(NORMALIZED)

    evidence["hashes"] = {
        "raw_sha256_actual": raw_hash,
        "raw_sha256_manifest": manifest.get("raw_sha256"),
        "normalized_sha256_actual": normalized_hash,
        "normalized_sha256_manifest": manifest.get("normalized_sha256"),
    }
    evidence["hash_match"] = {
        "raw": raw_hash == manifest.get("raw_sha256"),
        "normalized": normalized_hash == manifest.get("normalized_sha256"),
    }

    try:
        rel = str(NORMALIZED.relative_to(ROOT))
        lfs_all = subprocess.run(
            ["git", "lfs", "ls-files", "-l"],
            cwd=ROOT, text=True, capture_output=True, check=True
        ).stdout.splitlines()
        matching = [line for line in lfs_all if rel in line]
        attr = subprocess.run(
            ["git", "check-attr", "filter", "--", rel],
            cwd=ROOT, text=True, capture_output=True, check=True
        ).stdout.strip()
        evidence["git_lfs"] = {
            "tracked": bool(matching),
            "entry": matching[0] if matching else "",
            "tracked_entries_count": len(lfs_all),
            "filter_attribute": attr,
        }
    except Exception as exc:
        evidence["git_lfs"] = {"tracked": False, "error": str(exc)}


    with zipfile.ZipFile(RAW) as z:
        members = [n for n in z.namelist() if not n.endswith("/")]
        evidence["raw_zip"] = {
            "member_count": len(members),
            "members": members[:10],
        }
        if len(members) != 1:
            failures.append("raw_zip_member_count_not_one")
        else:
            with z.open(members[0]) as f:
                data_rows = 0
                bad_lengths = 0
                for b in f:
                    if b.startswith(b"01"):
                        data_rows += 1
                        if len(b.rstrip(b"\r\n")) != 245:
                            bad_lengths += 1
                evidence["raw_zip"]["type01_records"] = data_rows
                evidence["raw_zip"]["type01_bad_length_records"] = bad_lengths
                if data_rows <= 0:
                    failures.append("raw_zip_no_type01_records")
                if bad_lengths:
                    failures.append("raw_zip_type01_bad_length")

    with NORMALIZED.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        rows = 0
        invalid_dates = 0
        outside_year = 0
        first_date = None
        last_date = None
        for row in reader:
            rows += 1
            if len(row) != 25:
                failures.append(f"normalized_column_count:{len(row)}")
                if len(failures) > 20:
                    break
            if row:
                d = row[0]
                if first_date is None:
                    first_date = d
                last_date = d
                try:
                    if len(d) != 10 or d[4] != "-" or d[7] != "-":
                        raise ValueError
                    year = int(d[:4]); month = int(d[5:7]); day = int(d[8:10])
                    import datetime
                    datetime.date(year, month, day)
                    if year != YEAR:
                        outside_year += 1
                except Exception:
                    invalid_dates += 1

    evidence["normalized"] = {
        "header": header,
        "column_count": len(header),
        "row_count": rows,
        "first_date": first_date,
        "last_date": last_date,
        "invalid_dates": invalid_dates,
        "dates_outside_year": outside_year,
        "manifest_row_count": manifest.get("linhas_normalized"),
        "manifest_field_count": manifest.get("campos"),
    }

    checks = {
        "manifest_status_validated": manifest.get("status") == "VALIDADO",
        "parser_version_1_1_0": manifest.get("parser_version") == "1.1.0",
        "raw_hash_matches_manifest": evidence["hash_match"]["raw"],
        "normalized_hash_matches_manifest": evidence["hash_match"]["normalized"],
        "raw_zip_single_member": evidence["raw_zip"]["member_count"] == 1,
        "raw_type01_positive": evidence["raw_zip"].get("type01_records", 0) > 0,
        "raw_type01_length_245": evidence["raw_zip"].get("type01_bad_length_records", 1) == 0,
        "normalized_header_25": len(header) == 25,
        "normalized_rows_match_manifest": rows == manifest.get("linhas_normalized"),
        "normalized_invalid_dates_zero": invalid_dates == 0,
        "normalized_dates_inside_1988": outside_year == 0,
        "normalized_lfs_tracked": evidence["git_lfs"].get("tracked", False),
    }
    evidence["checks"] = checks
    failures.extend([name for name, ok in checks.items() if not ok])
    failures = list(dict.fromkeys(failures))
    evidence["status"] = "VALIDADO" if not failures else "FAIL"
    evidence["failures"] = failures
    evidence["decision"] = (
        "FASE_10_CONCLUIDA_E_RELEASE_NORMALIZADO_AUTORIZADO"
        if not failures else
        "FASE_10_BLOQUEADA_FAIL_CLOSED"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": evidence["status"],
        "phase": evidence["phase"],
        "failures": failures,
        "raw_sha256": raw_hash,
        "normalized_sha256": normalized_hash,
        "rows": rows,
    }, ensure_ascii=False))

    if failures:
        raise SystemExit("FAIL-CLOSED: " + ", ".join(failures))

if __name__ == "__main__":
    main()
