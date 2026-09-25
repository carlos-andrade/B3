#!/usr/bin/env python3
"""FASE 09B — Detecta multiplicidade estrutural em COTAHIST 1986."""
from __future__ import annotations
import hashlib, json, sys
from collections import Counter, defaultdict
from pathlib import Path

FIELDS={"dt":(2,9),"codbdi":(11,12),"codneg":(13,24),"tpmerc":(25,27),
"especi":(40,49),"prazot":(50,52),"preab":(57,69),"premax":(70,82),
"premin":(83,95),"premed":(96,108),"preult":(109,121),"totneg":(148,152),
"quatot":(153,170),"voltot":(171,188),"codisi":(231,242),"dimes":(243,245)}

def get(line,name):
    a,b=FIELDS[name]; return line[a-1:b].strip()

def k_partial(r): return (r["dt"],r["codbdi"],r["codneg"],r["tpmerc"],r["prazot"])
def k_struct(r): return (r["dt"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dimes"],r["especi"],r["prazot"])
def stats(r): return {n:r[n] for n in ("totneg","quatot","voltot","preab","premax","premin","premed","preult")}

def main(path):
    raw=Path(path).read_bytes(); sha=hashlib.sha256(raw).hexdigest()
    gp,gt=defaultdict(list),defaultdict(list); records=0
    for raw_line in raw.splitlines():
        line=raw_line.decode("latin-1","replace")
        if len(line)<245 or line[:2]!="01": continue
        records+=1; r={n:get(line,n) for n in FIELDS}
        if r["tpmerc"]=="030": gp[k_partial(r)].append(r); gt[k_struct(r)].append(r)
    pm=[]; fc=[]
    for k,rows in gp.items():
        if len(rows)>1:
            c=Counter(json.dumps(stats(x),sort_keys=True) for x in rows)
            pm.append({"key":k,"rows":len(rows),"distinct_stat_profiles":len(c),"profiles":c})
    for k,rows in gt.items():
        if len(rows)>1:
            c=Counter(json.dumps(stats(x),sort_keys=True) for x in rows)
            fc.append({"key":k,"rows":len(rows),"distinct_stat_profiles":len(c),"profiles":c})
    out={"schema_version":"1.0.0","raw_sha256":sha,"records_type_01":records,
         "term_partial_key_groups":len(gp),"term_partial_multiple_groups":len(pm),
         "term_partial_multiple_groups_with_stat_difference":sum(x["distinct_stat_profiles"]>1 for x in pm),
         "term_full_k4_groups":len(gt),"term_full_k4_collisions":len(fc),
         "term_full_k4_collisions_with_stat_difference":sum(x["distinct_stat_profiles"]>1 for x in fc),
         "partial_examples":pm[:200],"full_collision_examples":fc[:50],
         "governance":{"raw_changed":False,"rows_deleted":False,"rows_consolidated":False,"semantic_recode":False}}
    print(json.dumps(out,ensure_ascii=False,indent=2,default=dict))

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Uso: analisar_multiplicidade_term_1986_v1.py <arquivo_raw>")
    main(sys.argv[1])
