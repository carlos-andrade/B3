#!/usr/bin/env python3
import csv, hashlib, json, zipfile
from collections import Counter
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT = Path("dados/cotahist/quality/COTAHIST_1986_FASE08P_TRANSICAO_VIGOR_0910_1310_V1.json")

def s(line,a,b): return line[a-1:b]
def price(line,a,b): return int(s(line,a,b))/100.0
def num(line,a,b): return int(s(line,a,b))

rows=[]
with zipfile.ZipFile(RAW) as z:
    name=[n for n in z.namelist() if not n.endswith("/")][0]
    with z.open(name) as f:
        for n,raw in enumerate(f,1):
            line=raw.decode("latin-1").rstrip("\r\n")
            if len(line)!=245 or line[:2]!="01": continue
            codneg=s(line,13,24).strip()
            codisi=s(line,231,242).strip()
            if codneg!="VGO 2" and codisi!="VGORACPP": continue
            rows.append({
                "source_line":n,"date":s(line,3,10),"codbdi":s(line,11,12),
                "codneg":codneg,"tpmerc":s(line,25,27),"nomres":s(line,28,39).strip(),
                "especi":s(line,40,49).strip(),"prazot":s(line,50,52).strip(),
                "preab":price(line,57,69),"premax":price(line,70,82),
                "premin":price(line,83,95),"premed":price(line,96,108),
                "preult":price(line,109,121),"totneg":num(line,133,139),
                "quatot":num(line,140,151),"voltot":num(line,153,170)/100.0,
                "fatcot":num(line,211,217),"codisi":codisi,"dimes":s(line,243,245)
            })

focus_dates={"19861009","19861010","19861013"}
focus=[r for r in rows if r["date"] in focus_dates]
vgo=[r for r in focus if r["codneg"]=="VGO 2"]
target=[r for r in vgo if r["date"]=="19861010" and r["prazot"]=="060" and r["especi"]=="PP *C05"]

def profile(r):
    return {k:r[k] for k in ["date","source_line","codbdi","codneg","tpmerc","especi","prazot","codisi","dimes","preab","premax","premin","premed","preult","totneg","quatot","voltot","fatcot"]}

def key_without_stats(r):
    return (r["date"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dimes"],r["especi"],r["prazot"])

groups={}
for r in focus:
    groups.setdefault(key_without_stats(r),[]).append(r)

result={
 "schema_version":"1.0.0","status":"FASE_08P_TRANSICAO_VIGOR_0910_1310_1986",
 "raw_file":RAW.name,"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "scope":{"dates":sorted(focus_dates),"codneg":"VGO 2","codisi":"VGORACPP"},
 "rows": [profile(r) for r in focus],
 "daily_summary":[
   {"date":d,"rows":len([r for r in vgo if r["date"]==d]),
    "especi":dict(Counter(r["especi"] for r in vgo if r["date"]==d)),
    "dimes":dict(Counter(r["dimes"] for r in vgo if r["date"]==d)),
    "term_prazot":dict(Counter(r["prazot"] for r in vgo if r["date"]==d and r["tpmerc"]=="030")),
    "market":dict(Counter(f"{r['codbdi']}|{r['tpmerc']}|{r['prazot']}" for r in vgo if r["date"]==d))
   } for d in sorted(focus_dates)
 ],
 "target_rows":[profile(r) for r in target],
 "same_structural_key_groups":[
   {"key":list(k),"rows":[profile(r) for r in rs]}
   for k,rs in sorted(groups.items()) if len(rs)>1
 ],
 "interpretation":{
   "fact":[
     "The comparison is restricted to preserved RAW records for VGO 2/VGORACPP on 09/10, 10/10 and 13/10/1986.",
     "Target rows 140808 and 140809 are preserved as distinct records.",
     "No Type code is inferred from C05."
   ],
   "test":[
     "Whether the anomaly appears as a one-day transition in ESPECI, DIMES, PRAZOT or market context.",
     "Whether multiple structural-statistical profiles coexist for VGO 2 in the three-session window."
   ],
   "not_determined":[
     "Historical meaning of Type, C05 and DIMES 104.",
     "Economic or operational reason for the target collision."
   ]
 }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","focus_rows":len(focus),"target_rows":len(target),"collision_groups":sum(1 for rs in groups.values() if len(rs)>1)}))
