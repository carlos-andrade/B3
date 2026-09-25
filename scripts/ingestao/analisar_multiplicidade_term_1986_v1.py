#!/usr/bin/env python3
"""FASE 09B — Detecta multiplicidade estrutural em COTAHIST 1986.

Uso:
  python analisar_multiplicidade_term_1986_v1.py <arquivo_raw>

A análise é somente leitura. Não altera o RAW.
"""
from __future__ import annotations
import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

FIELDS = {
    "dt": (2, 9),
    "codbdi": (11, 12),
    "codneg": (13, 24),
    "tpmerc": (25, 27),
    "especi": (40, 49),
    "prazot": (50, 52),
    "preab": (57, 69),
    "premax": (70, 82),
    "premin": (83, 95),
    "premed": (96, 108),
    "preult": (109, 121),
    "totneg": (148, 152),
    "quatot": (153, 170),
    "voltot": (171, 188),
    "codisi": (231, 242),
    "dimes": (243, 245),
}

def get(line: str, name: str) -> str:
    a, b = FIELDS[name]
    return line[a-1:b].strip()

def k_partial(r):
    return (r["dt"], r["codbdi"], r["codneg"], r["tpmerc"], r["prazot"])

def k_struct(r):
    return (r["dt"], r["codbdi"], r["codneg"], r["tpmerc"],
            r["codisi"], r["dimes"], r["especi"], r["prazot"])

def stats(r):
    return {
        "totneg": get(r, "totneg"),
        "quatot": get(r, "quatot"),
        "voltot": get(r, "voltot"),
        "preab": get(r, "preab"),
        "premax": get(r, "premax"),
        "premin": get(r, "premin"),
        "premed": get(r, "premed"),
        "preult": get(r, "preult"),
    }

def main(path: str):
    p = Path(path)
    raw = p.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    groups_partial = defaultdict(list)
    groups_term = defaultdict(list)
    records = 0

    for raw_line in raw.splitlines():
        line = raw_line.decode("latin-1", errors="replace")
        if len(line) < 245 or line[0:2] != "01":
            continue
        records += 1
        r = {name: get(line, name) for name in FIELDS}
        if r["tpmerc"] == "030":
            groups_partial[k_partial(r)].append(r)
            groups_term[k_struct(r)].append(r)

    partial_multi = []
    for k, rows in groups_partial.items():
        if len(rows) > 1:
            stat_profiles = Counter(json.dumps(stats(x), sort_keys=True) for x in rows)
            partial_multi.append({
                "key": k,
                "rows": len(rows),
                "distinct_stat_profiles": len(stat_profiles),
                "profiles": stat_profiles,
            })

    structural_collision = []
    for k, rows in groups_term.items():
        if len(rows) > 1:
            profiles = Counter(json.dumps(stats(x), sort_keys=True) for x in rows)
            structural_collision.append({
                "key": k,
                "rows": len(rows),
                "distinct_stat_profiles": len(profiles),
                "profiles": profiles,
            })

    out = {
        "schema_version": "1.0.0",
        "raw_sha256": sha,
        "records_type_01": records,
        "term_partial_key_groups": len(groups_partial),
        "term_partial_multiple_groups": len(partial_multi),
        "term_partial_multiple_groups_with_stat_difference": sum(
            x["distinct_stat_profiles"] > 1 for x in partial_multi
        ),
        "term_full_k4_groups": len(groups_term),
        "term_full_k4_collisions": len(structural_collision),
        "term_full_k4_collisions_with_stat_difference": sum(
            x["distinct_stat_profiles"] > 1 for x in structural_collision
        ),
        "partial_examples": partial_multi[:200],
        "full_collision_examples": structural_collision[:50],
        "governance": {
            "raw_changed": False,
            "rows_deleted": False,
            "rows_consolidated": False,
            "semantic_recode": False,
        },
    }
    print(json.dumps(out, ensure_ascii=False, indent=2, default=lambda x: dict(x)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Uso: analisar_multiplicidade_term_1986_v1.py <arquivo_raw>")
    main(sys.argv[1])
