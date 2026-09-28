#!/usr/bin/env python3
"""Auditoria da chave lógica candidata do COTAHIST 1987.

Objetivo: identificar colisões de identidade e separar duplicidade exata
de múltiplos registros com estatísticas de negociação distintas.
Não certifica significado econômico dos códigos.
"""
import csv, hashlib, json, zipfile
from collections import Counter,defaultdict
from pathlib import Path

YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_CHAVE_LOGICA_V1.json")
FIELDS=[
 ("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
 ("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
 ("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
 ("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
 ("preexe",189,201),("indopc",202,202),("datven",203,210),
 ("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)
]
KEY=("data_pregao","codbdi","codneg","tpmerc","codisi","dimes","especi","prazot","datven","indopc","preexe","ptoexe")
STATS=("preab","premax","premin","premed","preult","totneg","quatot","voltot")

def rows():
    out=[]
    with zipfile.ZipFile(RAW) as z:
        members=[n for n in z.namelist() if not n.endswith("/")]
        if len(members)!=1: raise RuntimeError(f"RAW ambiguo: {members}")
        with z.open(members[0]) as f:
            for line_no,b in enumerate(f,1):
                line=b.decode("latin-1").rstrip("\r\n")
                if line[:2]!="01": continue
                if len(line)!=245: raise RuntimeError(f"Registro tipo 01 fora de 245 bytes: linha {line_no}")
                r={k:line[a-1:b].strip() for k,a,b in FIELDS}
                r["_line"]=line_no
                out.append(r)
    return out

def norm(v): return (v or "").strip()

def key(r): return tuple(norm(r[f]) for f in KEY)
def stats(r): return tuple(norm(r[f]) for f in STATS)

rs=rows()
groups=defaultdict(list)
for r in rs: groups[key(r)].append(r)

collisions={k:v for k,v in groups.items() if len(v)>1}
exact_duplicate_groups=0
same_key_distinct_stats=[]
same_key_same_stats=[]
for k,v in collisions.items():
    sigs={stats(r) for r in v}
    if len(sigs)==1:
        exact_duplicate_groups+=1
        same_key_same_stats.append({"key":k,"count":len(v),"lines":[r["_line"] for r in v]})
    else:
        same_key_distinct_stats.append({
            "key":k,"count":len(v),"distinct_stat_signatures":len(sigs),
            "lines":[r["_line"] for r in v],
            "statistics":[{f:r[f] for f in STATS} for r in v[:10]]
        })

by_field={}
for f in ("codbdi","tpmerc","dimes","especi","prazot","indopc"):
    by_field[f]=Counter(norm(r[f]) for r in rs)

result={
 "schema_version":"1.0.0",
 "status":"AUDITORIA_CHAVE_LOGICA_1987",
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "row_count":len(rs),
 "candidate_key_fields":list(KEY),
 "candidate_key_unique":len(collisions)==0,
 "distinct_key_count":len(groups),
 "collision_group_count":len(collisions),
 "collision_row_count":sum(len(v) for v in collisions.values()),
 "exact_duplicate_group_count":exact_duplicate_groups,
 "same_key_distinct_statistics_group_count":len(same_key_distinct_stats),
 "same_key_distinct_statistics_sample":same_key_distinct_stats[:30],
 "exact_duplicate_groups_sample":same_key_same_stats[:30],
 "distributions":{f:dict(c) for f,c in by_field.items()},
 "fail_closed_gates":{
   "row_count_positive":len(rs)>0,
   "candidate_key_has_no_collisions":len(collisions)==0,
   "no_same_key_distinct_statistics":len(same_key_distinct_stats)==0
 },
 "interpretation":"OBSERVACIONAL: a chave é uma hipótese estrutural; significados econômicos de tpmerc/codbdi/dimes/especi não são certificados por este script."
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
failed=[k for k,v in result["fail_closed_gates"].items() if not v]
print(json.dumps({"status":"OK" if not failed else "GATES_FAILED","failed":failed,"output":str(OUT),"rows":len(rs),"collision_groups":len(collisions),"distinct_stats_groups":len(same_key_distinct_stats)},ensure_ascii=False))
if failed: raise SystemExit("GATES FAILED: "+", ".join(failed))
