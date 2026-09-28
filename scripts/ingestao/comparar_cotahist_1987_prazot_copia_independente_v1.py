#!/usr/bin/env python3
"""Compara byte a byte registros PRAZOT afetados de duas cópias do COTAHIST_A1987.

Uso:
  python comparar_cotahist_1987_prazot_copia_independente_v1.py <arquivo_repo> <arquivo_independente>

A comparação é fail-closed e não altera nenhum arquivo de origem.
"""
from pathlib import Path
import hashlib
import json
import sys

AFFECTED = {
    "000f20": 33,
    "9c0f20": 1,
    "000720": 1,
}

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def affected_records(p: Path):
    out = []
    with p.open("rb") as f:
        for line_no, raw in enumerate(f, 1):
            line = raw.rstrip(b"\r\n")
            if len(line) != 245 or line[:2] != b"01":
                continue
            prazot = line[49:52]
            key = prazot.hex()
            if key in AFFECTED:
                out.append((line_no, line))
    return out

def main():
    if len(sys.argv) != 3:
        raise SystemExit("uso: script <arquivo_repo> <arquivo_independente>")
    repo = Path(sys.argv[1])
    independent = Path(sys.argv[2])
    a = affected_records(repo)
    b = affected_records(independent)
    result = {
        "schema_version": "1.0.0",
        "repo_sha256": sha256(repo),
        "independent_sha256": sha256(independent),
        "repo_affected_count": len(a),
        "independent_affected_count": len(b),
        "byte_identical_affected_records": False,
        "mismatches": [],
    }
    if len(a) != len(b):
        result["mismatches"].append({
            "type": "affected_count_mismatch",
            "repo": len(a),
            "independent": len(b),
        })
    else:
        for i, ((la, ra), (lb, rb)) in enumerate(zip(a, b)):
            if ra != rb:
                result["mismatches"].append({
                    "ordinal": i + 1,
                    "repo_line": la,
                    "independent_line": lb,
                    "repo_prazot_hex": ra[49:52].hex(),
                    "independent_prazot_hex": rb[49:52].hex(),
                })
        result["byte_identical_affected_records"] = not result["mismatches"]
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["byte_identical_affected_records"] else 2)

if __name__ == "__main__":
    main()
