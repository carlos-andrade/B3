#!/usr/bin/env python3
"""Reconciliacao deterministica RAW -> NORMALIZED para COTAHIST.

Valida se o RAW atual, processado pelo parser versionado, reproduz exatamente
o SHA-256 do NORMALIZED registrado no manifesto.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import tempfile
import zipfile
from pathlib import Path


EXPECTED_PARSER = "1.1.0"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def raw_type01_count(path: Path) -> int:
    count = 0
    with zipfile.ZipFile(path) as zf:
        members = [n for n in zf.namelist() if not n.endswith("/")]
        if len(members) != 1:
            raise ValueError(f"ZIP deve conter exatamente 1 arquivo: {members}")
        with zf.open(members[0]) as src:
            for raw in src:
                line = raw.rstrip(b"\r\n")
                if line[:2] == b"01":
                    count += 1
    return count


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--raw", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--parser", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    raw_sha = sha256(args.raw)
    independent_count = raw_type01_count(args.raw)

    with tempfile.TemporaryDirectory() as td:
        generated = Path(td) / f"COTAHIST_A{args.year}.csv"
        proc = subprocess.run(
            ["python", str(args.parser), "--zip", str(args.raw), "--output", str(generated)],
            capture_output=True, text=True, check=False,
        )
        if proc.returncode != 0:
            raise SystemExit("PARSER_FAIL\n" + proc.stdout + proc.stderr)

        generated_sha = sha256(generated)
        with generated.open(encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = sum(1 for _ in reader)

        expected_sha = manifest.get("normalized_sha256")
        expected_raw_sha = manifest.get("raw_sha256")
        expected_rows = manifest.get("linhas_normalized")
        expected_fields = manifest.get("campos")
        expected_parser = manifest.get("parser_version")

        checks = {
            "raw_sha256_match": raw_sha == expected_raw_sha,
            "parser_version_match": expected_parser == EXPECTED_PARSER,
            "raw_type01_count_match_manifest": independent_count == expected_rows,
            "generated_row_count_match_manifest": rows == expected_rows,
            "field_count_match_manifest": len(header) == expected_fields,
            "normalized_sha256_match_manifest": generated_sha == expected_sha,
        }

        result = {
            "schema_version": "1.0.0",
            "status": "RECONCILIADO" if all(checks.values()) else "REVISAR",
            "ano": args.year,
            "raw_file": str(args.raw),
            "manifest": str(args.manifest),
            "parser": str(args.parser),
            "parser_version": EXPECTED_PARSER,
            "raw_sha256": raw_sha,
            "manifest_raw_sha256": expected_raw_sha,
            "generated_normalized_sha256": generated_sha,
            "manifest_normalized_sha256": expected_sha,
            "raw_type01_count": independent_count,
            "generated_normalized_rows": rows,
            "manifest_normalized_rows": expected_rows,
            "generated_fields": len(header),
            "manifest_fields": expected_fields,
            "checks": checks,
        }

        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        if not all(checks.values()):
            raise SystemExit(2)


if __name__ == "__main__":
    main()
