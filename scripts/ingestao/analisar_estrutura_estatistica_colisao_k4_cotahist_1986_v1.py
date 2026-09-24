#!/usr/bin/env python3
import hashlib, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT = Path("dados/cotahist/quality/COTAHIST_1986_FASE08F_ESTRUTURA_ESTATISTICA_K4_V1.json")

def s(line,a,b): return line[a-1:b]
def dec(x,scale=1):
    x=x.strip()
    return int(x)/scale if x else 0.0

def parse():
    rows=[]
    with zipfile.ZipFile(RAW) as z:
        name=next(n for n in z.namelist() if not n.endswith("/"))
        with z.open(name) as f:
            for n,raw in enumerate(f,1):
                line=raw.decode("latin-1").rstrip("\r\n")
                if len(line)!=245 or line[:2]!="01": continue
                rows.append({
                    "source_line":n,"date":s(line,3,10),"codbdi":s(line,11,12),
                    "codneg":s(line,13,24).strip(),"tpmerc":s(line,25,27),
                    "nomres":s(line,28,39).strip(),"especi":s(line,40,49).strip(),
                    "prazot":s(line,50,52).strip(),"preab":dec(s(line,57,69),100),
                    "premax":dec(s(line,70,82),100),"premin":dec(s(line,83,95),100),
                    "premed":dec(s(line,96,108),100),"preult":dec(s(line,109,121),100),
                    "totneg":int(s(line,148,152).strip() or 0),
                    "quatot":int(s(line,153,170).strip() or 0),
                    "voltot":dec(s(line,171,188),100),"preexe":dec(s(line,189,201),100),
                    "indopc":s(line,202,202),"datven":s(line,203,210),
                    "fatcot":int(s(line,211,217).strip() or 0),
                    "ptoexe":dec(s(line,218,230),1000000),"codisi":s(line,231,242).strip(),
                    "dimes":s(line,243,245).strip()
                })
    return rows

def calc(r):
    q,v,f=r["quatot"],r["voltot"],r["fatcot"]
    implied=v/q if q else None
    last=r["preult"]/f if f else None
    med=r["premed"]/f if f else None
    return {
      "implied_unit_price_vtot_quatot":implied,
      "last_price_per_quotation_unit":last,
      "median_price_per_quotation_unit":med,
      "implied_vs_last_pct":((implied/last)-1)*100 if implied is not None and last else None,
      "implied_vs_median_pct":((implied/med)-1)*100 if implied is not None and med else None,
      "pre_range":r["premax"]-r["premin"],
      "price_qty_using_preult":last*q if last is not None else None,
      "voltot_minus_preult_qty":v-(last*q) if last is not None else None,
      "price_internal_consistency":bool(implied is not None and f and r["premin"]/f<=implied<=r["premax"]/f)
    }

def compact(r):
    return {k:r[k] for k in ["source_line","date","codbdi","codneg","tpmerc","nomres","especi","prazot","preab","premax","premin","premed","preult","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dimes"]}

def distribution(rs):
    vals=[r["voltot"]/r["quatot"] for r in rs if r["quatot"]]
    if not vals:return {}
    a=sorted(vals); n=len(a)
    med=a[n//2] if n%2 else (a[n//2-1]+a[n//2])/2
    return {"count":n,"min":min(a),"max":max(a),"median":med,"mean":sum(a)/n}

def patterns(rs):
    c=Counter()
    for r in rs:
        x=calc(r)
        c["totneg_1" if r["totneg"]==1 else "totneg_gt_1"]+=1
        if x["price_internal_consistency"]: c["implied_price_inside_min_max"]+=1
        if x["implied_vs_median_pct"] is not None and abs(x["implied_vs_median_pct"])<=1: c["implied_within_1pct_of_median"]+=1
    return dict(c)

rows=parse()
target=[r for r in rows if r["source_line"] in (140808,140809)]
vgo_term=[r for r in rows if r["codneg"]=="VGO 2" and r["codbdi"]=="62" and r["tpmerc"]=="030"]
term_all=[r for r in rows if r["codbdi"]=="62" and r["tpmerc"]=="030"]

by_k4=defaultdict(list)
for r in rows:
    by_k4[(r["date"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dimes"],r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"])].append(r)
collisions=[g for g in by_k4.values() if len(g)>1]

def sig(g):
    return {"size":len(g),"date":g[0]["date"],"codbdi":g[0]["codbdi"],"codneg":g[0]["codneg"],"tpmerc":g[0]["tpmerc"],
            "totneg_values":[r["totneg"] for r in g],"quatot_values":[r["quatot"] for r in g],
            "voltot_values":[r["voltot"] for r in g],"implied_prices":[calc(r)["implied_unit_price_vtot_quatot"] for r in g],
            "source_lines":[r["source_line"] for r in g]}

target_implied=calc(target[1])["implied_unit_price_vtot_quatot"]
exact019=[compact(r) for r in term_all if r["quatot"] and abs(r["voltot"]/r["quatot"]-0.19)<1e-12]
same_second=[compact(r) for r in term_all if r["quatot"] and abs(r["voltot"]/r["quatot"]-target_implied)<1e-9]

result={
 "schema_version":"1.0.0","status":"FASE_08F_ESTRUTURA_ESTATISTICA_K4_1986_ANALISE",
 "raw_file":RAW.name,"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "records_type01":len(rows),"target_row_count":len(target),
 "target_rows":[{**compact(r),"derived":calc(r)} for r in target],
 "scope_counts":{"vgo2_term_62_030":len(vgo_term),"all_term_62_030":len(term_all),"k4_collision_groups_total":len(collisions)},
 "distributions":{
   "vgo2_term_totneg":dict(Counter("1" if r["totneg"]==1 else ">1" for r in vgo_term)),
   "all_term_totneg":dict(Counter("1" if r["totneg"]==1 else ">1" for r in term_all)),
   "vgo2_term_implied_price":distribution(vgo_term),"all_term_implied_price":distribution(term_all),
   "vgo2_term_internal_price_consistency":patterns(vgo_term),"all_term_internal_price_consistency":patterns(term_all)
 },
 "target_structural_observation":{
   "row_140808":"TOTNEG=1; VOLTOT/QUATOT=0.19; PREULT/FATCOT=0.19.",
   "row_140809":"TOTNEG=4; VOLTOT/QUATOT≈0.1876105263; value lies between PREMIN/FATCOT and PREMAX/FATCOT and is close to PREMED/FATCOT.",
   "limit":"numeric structure does not establish the historical cause of the K4 collision."
 },
 "other_k4_collision_groups_sample":[sig(g) for g in collisions[:50]],
 "term_analogues":{"exact_implied_0_19_count":len(exact019),"exact_implied_0_19_sample":exact019[:20],
                   "same_implied_as_second_target_count":len(same_second),"same_implied_as_second_target_sample":same_second[:20]},
 "governance":{"raw_changed":False,"rows_deleted":False,"rows_consolidated":False,"economic_identity_inferred":False,"causal_explanation_inferred":False,
               "method":"fixed-width parse + arithmetic consistency + structural comparison"}
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","records_type01":len(rows),"target_rows":len(target),"vgo2_term":len(vgo_term),"all_term":len(term_all),"k4_collision_groups":len(collisions)}))
