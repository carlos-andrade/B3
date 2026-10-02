#!/usr/bin/env python3
"""Valida integridade independente do COTAHIST NORMALIZED 1996 — FASE 10."""
from __future__ import annotations
import csv, hashlib, json, subprocess, zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YEAR = 1996
RAW = ROOT / "dados/cotahist/raw/anual/COTAHIST_A1996.ZIP"
NORM = ROOT / "dados/cotahist/normalized/anual/COTAHIST_A1996.csv"
MANIFEST = ROOT / "dados/cotahist/normalized/manifests/COTAHIST_A1996_quality.json"
EVIDENCE = ROOT / "dados/cotahist/quality/COTAHIST_1996_FASE10_INTEGRIDADE_V1.json"
FIELDS = [
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

def main() -> None:
    failures = []
    for path in (RAW, NORM, MANIFEST):
        if not path.is_file():
            failures.append(f"missing: {path}")
    if failures:
        raise SystemExit("FAIL-CLOSED: " + "; ".join(failures))

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    raw_hash = sha256(RAW)
    normalized_hash = sha256(NORM)

    if raw_hash != manifest.get("raw_sha256"):
        failures.append("raw_sha256 mismatch")
    if normalized_hash != manifest.get("normalized_sha256"):
        failures.append("normalized_sha256 mismatch")

    pathspec = "dados/cotahist/normalized/anual/COTAHIST_A1996.csv"
    attr = subprocess.run(
        ["git", "check-attr", "filter", "--", pathspec],
        capture_output=True, text=True, check=True
    ).stdout.strip()
    pointer = subprocess.run(
        ["git", "cat-file", "-p", f"HEAD:{pathspec}"],
        capture_output=True, text=True, check=True
    ).stdout.strip()
    pointer_lines = pointer.splitlines()
    pointer_oid = next((x.split(" ", 1)[1] for x in pointer_lines if x.startswith("oid sha256:")), "")
    pointer_size = next((x.split(" ", 1)[1] for x in pointer_lines if x.startswith("size ")), "")
    lfs_tracked = (
        pointer.startswith("version https://git-lfs.github.com/spec/v1")
        and bool(pointer_oid) and bool(pointer_size) and attr.endswith("filter: lfs")
    )
    if not lfs_tracked:
        failures.append("normalized not tracked by Git LFS")

    with zipfile.ZipFile(RAW) as z:
        members = z.namelist()
        raw_data = z.read(members[0])
        lines = raw_data.splitlines()
        type01 = [line for line in lines if line[:2] == b"01"]
        bad_length = [line for line in type01 if len(line) != 245]
        if len(members) != 1:
            failures.append(f"raw zip member_count={len(members)}")
        if not type01:
            failures.append("no type-01 records")
        if bad_length:
            failures.append(f"type01_bad_length={len(bad_length)}")

    with NORM.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    header = rows[0] if rows else []
    data_rows = rows[1:]
    dates = [row[0] for row in data_rows if row]
    invalid_dates = []
    outside_year = []
    for value in dates:
        try:
            if date.fromisoformat(value).year != YEAR:
                outside_year.append(value)
        except ValueError:
            invalid_dates.append(value)

    checks = {
        "manifest_status_validated": manifest.get("status") == "VALIDADO",
        "parser_version_1_1_0": manifest.get("parser_version") == "1.1.0",
        "raw_hash_matches_manifest": raw_hash == manifest.get("raw_sha256"),
        "normalized_hash_matches_manifest": normalized_hash == manifest.get("normalized_sha256"),
        "raw_zip_single_member": len(members) == 1,
        "raw_type01_positive": len(type01) > 0,
        "raw_type01_length_245": len(bad_length) == 0,
        "normalized_header_25": len(header) == 25 and header == FIELDS,
        "normalized_rows_match_manifest": len(data_rows) == manifest.get("linhas_normalized"),
        "normalized_invalid_dates_zero": len(invalid_dates) == 0,
        "normalized_dates_inside_1996": len(outside_year) == 0,
        "normalized_lfs_tracked": lfs_tracked,
    }

    evidence = {
        "schema_version": "1.0.0",
        "phase": "FASE_10",
        "year": YEAR,
        "raw_path": "dados/cotahist/raw/anual/COTAHIST_A1996.ZIP",
        "normalized_path": "dados/cotahist/normalized/anual/COTAHIST_A1996.csv",
        "manifest_path": "dados/cotahist/normalized/manifests/COTAHIST_A1996_quality.json",
        "raw_immutable": True,
        "correction_required": False,
        "correction_applied": False,
        "hashes": {
            "raw_sha256_actual": raw_hash,
            "raw_sha256_manifest": manifest.get("raw_sha256"),
            "normalized_sha256_actual": normalized_hash,
            "normalized_sha256_manifest": manifest.get("normalized_sha256"),
        },
        "raw_zip": {
            "member_count": len(members),
            "members": members,
            "type01_records": len(type01),
            "type01_bad_length_records": len(bad_length),
        },
        "normalized": {
            "header": header,
            "column_count": len(header),
            "row_count": len(data_rows),
            "first_date": dates[0] if dates else None,
            "last_date": dates[-1] if dates else None,
            "invalid_dates": len(invalid_dates),
            "dates_outside_year": len(outside_year),
            "manifest_row_count": manifest.get("linhas_normalized"),
            "manifest_field_count": manifest.get("campos"),
        },
        "git_lfs": {
            "tracked": lfs_tracked,
            "entry": f"HEAD:{pathspec} oid {pointer_oid} size {pointer_size}" if lfs_tracked else "",
            "filter_attribute": attr,
            "pointer_oid": pointer_oid,
            "pointer_size": pointer_size,
        },
        "checks": checks,
        "status": "VALIDADO" if not failures else "INVALIDADO",
        "failures": failures,
        "decision": (
            "FASE_10_CONCLUIDA_E_RELEASE_NORMALIZADO_AUTORIZADO"
            if not failures else "FASE_10_BLOQUEADA"
        ),
    }
    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit("FAIL-CLOSED: " + json.dumps(failures, ensure_ascii=False))

if __name__ == "__main__":
    main()
