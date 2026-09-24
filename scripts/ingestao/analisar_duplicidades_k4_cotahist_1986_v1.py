#!/usr/bin/env python3
import hashlib, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT = Path("dados/cotahist/quality/COTAHIST_1986_FASE08C_DUPLICIDADES_K4_V1.json")

FIELDS = [
    "codbdi","codneg","tpmerc","codisi","dimes","especi","prazot",
    "datven","preexe","indopc","ptoexe"
]

def s(line, a, b):
    return line[a-1:b]

def parse():
    rows = []
    with zipfile.ZipFile(RAW) as z:
        name = next(n for n in z.namelist() if not n.endswith("/"))
        with z.open(name) as f:
            for n, raw in enumerate(f, 1):
                line = raw.decode("latin-1").rstrip("\r\n")
                if len(line) != 245 or line[:2] != "01":
                    continue
                rows.append({
                    "source_line": n,
                    "data_pregao": s(line,3,10),
                    "codbdi": s(line,11,12),
                    "codneg": s(line,13,24).strip(),
                    "tpmerc": s(line,25,27),
                    "nomres": s(line,28,39).strip(),
                    "especi": s(line,40,49).strip(),
                    "prazot": s(line,50,52).strip(),
                    "preab": s(line,57,69),
                    "premax": s(line,70,82),
                    "premin": s(line,83,95),
                    "premed": s(line,96,108),
                    "preult": s(line,109,121),
                    "totneg": s(line,148,152),
                    "quatot": s(line,153,170),
                    "voltot": s(line,171,188),
                    "preexe": int(s(line,189,201))/100 if s(line,189,201).strip() else 0.0,
                    "indopc": s(line,202,202),
                    "datven": s(line,203,210),
                    "fatcot": s(line,211,217),
                    "ptoexe": int(s(line,218,230))/1000000 if s(line,218,230).strip() else 0.0,
                    "codisi": s(line,231,242).strip(),
                    "dimes": s(line,243,245).strip(),
                })
    return rows

def key_k4(r):
    return tuple(r[k] if k not in ("preexe","ptoexe") else str(r[k]) for k in (
        "data_pregao","codbdi","codneg","tpmerc","codisi","dimes","especi",
        "prazot","datven","preexe","indopc","ptoexe"))

def context(r):
    return {k:r[k] for k in [
        "source_line","data_pregao","codbdi","codneg","tpmerc","nomres","especi",
        "prazot","datven","codisi","dimes","totneg","quatot","voltot",
        "preab","premax","premin","premed","preult","fatcot"
    ]}

rows = parse()
groups = defaultdict(list)
for r in rows:
    groups[key_k4(r)].append(r)
dups = [v for v in groups.values() if len(v) > 1]

field_diff = Counter()
market = Counter()
size = Counter()
examples = []
target_found = False

for g in dups:
    size[len(g)] += 1
    diff = tuple(f for f in ("data_pregao","codbdi","codneg","tpmerc","codisi","dimes","especi","prazot","datven","preexe","indopc","ptoexe")
                 if len({str(r[f]) for r in g}) > 1)
    field_diff[diff] += 1
    market[(g[0]["codbdi"], g[0]["tpmerc"])] += 1
    if any(r["data_pregao"]=="19861010" and r["codneg"]=="VGO 2" and r["codbdi"]=="62" and r["tpmerc"]=="030" for r in g):
        target_found = True
    if len(examples) < 20:
        examples.append({
            "k4": list(key_k4(g[0])),
            "group_size": len(g),
            "differing_fields": list(diff),
            "rows": [context(r) for r in g]
        })

same_day = sum(1 for g in dups if len({r["data_pregao"] for r in g}) == 1)
cross_day = len(dups) - same_day
max_group = max((len(g) for g in dups), default=0)

result = {
    "schema_version": "1.0.0",
    "status": "FASE_08C_DUPLICIDADES_K4_1986_ANALISE",
    "raw_file": RAW.name,
    "raw_sha256": hashlib.sha256(RAW.read_bytes()).hexdigest(),
    "records_type01": len(rows),
    "k4_groups_total": len(groups),
    "duplicate_k4_groups_total": len(dups),
    "duplicate_k4_rows_total": sum(len(g) for g in dups),
    "duplicate_k4_same_day_groups": same_day,
    "duplicate_k4_cross_day_groups": cross_day,
    "max_duplicate_group_size": max_group,
    "duplicate_group_size_distribution": {str(k):v for k,v in sorted(size.items())},
    "duplicate_groups_by_market": {f"{k[0]}|{k[1]}":v for k,v in sorted(market.items())},
    "duplicate_groups_by_differing_fields": {
        "|".join(k) if k else "NONE": v for k,v in sorted(field_diff.items(), key=lambda x:(-x[1], x[0]))
    },
    "vgo2_target_collision_found": target_found,
    "vgo2_target_comparison": {
        "expected_rows": 2,
        "observed_in_collision_class": target_found,
        "interpretation": "class membership is factual; economic cause remains unresolved"
    },
    "examples_first_20": examples,
    "governance": {
        "raw_changed": False,
        "rows_deleted": False,
        "economic_identity_inferred": False,
        "purpose": "classify K4 collisions structurally before assigning historical semantics"
    }
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({
    "status":"OK",
    "records_type01":len(rows),
    "k4_groups_total":len(groups),
    "duplicate_k4_groups_total":len(dups),
    "same_day":same_day,
    "cross_day":cross_day,
    "max_group":max_group,
    "output":str(OUT)
}, ensure_ascii=False))
