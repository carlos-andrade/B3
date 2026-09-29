#!/usr/bin/env python3
"""Auditoria da chave logica candidata do COTAHIST 1988 — fail-closed."""
import csv,hashlib,json,zipfile
from collections import Counter,defaultdict
from pathlib import Path

YEAR="1988"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_CHAVE_LOGICA_V1.json")
FIELDS=[
("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
("preexe",189,201),("indopc",202,202),("datven",203,210),("fatcot",211,217),
("ptoexe",218,230),("codisi",231,242),("dimes",243,245)]
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
                r={k:line[a-1:b].strip() for k,a,b in FIELDS}; r["_line"]=line_no; out.append(r)
    return out

rs=rows(); groups=defaultdict(list)
for r in rs: groups[tuple((r[f] or "").strip() for f in KEY)].append(r)
collisions={k:v for k,v in groups.items() if len(v)>1}
exact=0; distinct=[]
for k,v in collisions.items():
    sigs={tuple((r[f] or "").strip() for f in STATS) for r in v}
    if len(sigs)==1: exact+=1
    else: distinct.append({"key":k,"count":len(v),"distinct_stat_signatures":len(sigs),
      "lines":[r["_line"] for r in v],"statistics":[{f:r[f] for f in STATS} for r in v[:10]]})

distributions={f:dict(Counter((r[f] or "").strip() for r in rs)) for f in ("codbdi","tpmerc","dimes","especi","prazot","indopc")}
result={
"schema_version":"1.0.0","year":1988,"status":"AUDITORIA_CHAVE_LOGICA_1988",
"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"row_count":len(rs),
"candidate_key_fields":list(KEY),"candidate_key_unique":not collisions,
"distinct_key_count":len(groups),"collision_group_count":len(collisions),
"collision_row_count":sum(len(v) for v in collisions.values()),
"exact_duplicate_group_count":exact,
"same_key_distinct_statistics_group_count":len(distinct),
"same_key_distinct_statistics_sample":distinct[:30],
"fail_closed_gates":{"row_count_positive":len(rs)>0,
"candidate_key_has_no_collisions":not collisions,
"no_same_key_distinct_statistics":not distinct},
"interpretation":"OBSERVACIONAL: chave candidata estrutural; significados economicos dos codigos nao sao certificados."
}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
failed=[k for k,v in result["fail_closed_gates"].items() if not v]
print(json.dumps({"status":"OK" if not failed else "GATES_FAILED","failed":failed,
"rows":len(rs),"collision_groups":len(collisions),"distinct_stats_groups":len(distinct),"output":str(OUT)},ensure_ascii=False))
if failed: raise SystemExit("GATES FAILED: "+", ".join(failed))
