#!/usr/bin/env python3
import hashlib,json,zipfile
from collections import Counter,defaultdict
from pathlib import Path

RAW=Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT=Path("dados/cotahist/quality/COTAHIST_1986_FASE08G_RECORRENCIA_PERFIS_K4_V1.json")

def s(x,a,b): return x[a-1:b]
def dec(x,scale=1):
    x=x.strip()
    return int(x)/scale if x else 0.0
def parse():
    rows=[]
    with zipfile.ZipFile(RAW) as z:
        name=next(n for n in z.namelist() if not n.endswith("/"))
        with z.open(name) as f:
            for n,b in enumerate(f,1):
                x=b.decode("latin-1").rstrip("\r\n")
                if len(x)!=245 or x[:2]!="01": continue
                rows.append({"line":n,"date":s(x,3,10),"codbdi":s(x,11,12),"codneg":s(x,13,24).strip(),
                "tpmerc":s(x,25,27),"especi":s(x,40,49).strip(),"prazot":s(x,50,52).strip(),
                "preab":dec(s(x,57,69),100),"premax":dec(s(x,70,82),100),"premin":dec(s(x,83,95),100),
                "premed":dec(s(x,96,108),100),"preult":dec(s(x,109,121),100),
                "totneg":int(s(x,148,152).strip() or 0),"quatot":int(s(x,153,170).strip() or 0),
                "voltot":dec(s(x,171,188),100),"preexe":dec(s(x,189,201),100),
                "indopc":s(x,202,202),"datven":s(x,203,210),"fatcot":int(s(x,211,217).strip() or 0),
                "ptoexe":dec(s(x,218,230),1000000),"codisi":s(x,231,242).strip(),"dimes":s(x,243,245).strip()})
    return rows
def k4(r):
    return (r["date"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dimes"],r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"])
def prof(r):
    f=r["fatcot"]; q=r["quatot"]; v=r["voltot"]
    implied=v/q if q else None
    return {"totneg":r["totneg"],"preab":r["preab"],"premax":r["premax"],"premin":r["premin"],"premed":r["premed"],"preult":r["preult"],
            "quatot":q,"voltot":v,"fatcot":f,"implied":implied,
            "implied_minus_med":(implied-r["premed"]/f) if implied is not None and f else None}
def compact(r): return {k:r[k] for k in ["line","date","codbdi","codneg","tpmerc","especi","prazot","preab","premax","premin","premed","preult","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dimes"]}

rows=parse()
by=defaultdict(list)
for r in rows: by[k4(r)].append(r)
dups=[g for g in by.values() if len(g)>1]

# Statistical profile families: normalize each record by its own quotation factor and quantity.
# Exact profile: TOTNEG + price vector + implied price (rounded to 12 decimals).
families=defaultdict(list)
for r in rows:
    f=r["fatcot"]
    p=(r["totneg"],r["preab"]/f,r["premax"]/f,r["premin"]/f,r["premed"]/f,r["preult"]/f,
       round(r["voltot"]/r["quatot"],12) if r["quatot"] else None)
    families[p].append(r)

# Target profile and progressively relaxed matches.
target=[r for g in dups for r in g if r["line"] in (140808,140809)]
def rel(r):
    f=r["fatcot"]; q=r["quatot"]
    return (r["totneg"],round(r["preab"]/f,6),round(r["premax"]/f,6),round(r["premin"]/f,6),round(r["premed"]/f,6),round(r["preult"]/f,6),
            round(r["voltot"]/q,9) if q else None)
relaxed=[]
for tr in target:
    matches=[r for r in rows if r["line"]!=tr["line"] and rel(r)==rel(tr)]
    relaxed.append({"target_line":tr["line"],"match_count":len(matches),"matches":[compact(r) for r in matches[:20]]})

# Compare collision group to ordinary rows with same date/market/codneg but different K4.
context=[]
for tr in target:
    m=[r for r in rows if r["line"]!=tr["line"] and r["date"]==tr["date"] and r["codbdi"]==tr["codbdi"] and r["codneg"]==tr["codneg"] and r["tpmerc"]==tr["tpmerc"]]
    context.append({"target_line":tr["line"],"count":len(m),"rows":[compact(r) for r in m[:50]]})

# For all duplicate K4 groups, compare statistical signatures.
dup_summary=[]
for g in dups:
    dup_summary.append({"size":len(g),"lines":[r["line"] for r in g],"date":g[0]["date"],"codneg":g[0]["codneg"],
                        "k4":list(k4(g[0])),"profiles":[prof(r) for r in g],
                        "statistics_differ":len({json.dumps(prof(r),sort_keys=True) for r in g})>1})

result={"schema_version":"1.0.0","status":"FASE_08G_RECORRENCIA_PERFIS_K4_1986_ANALISE",
"raw_file":RAW.name,"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"records_type01":len(rows),
"duplicate_k4_groups":len(dups),"duplicate_k4_rows":sum(len(g) for g in dups),
"duplicate_groups":dup_summary,
"target_profile_recurrence":relaxed,
"target_same_date_market_codneg":context,
"profile_family_counts":{"unique_exact_profiles":len(families),"records_in_recurrent_exact_profiles":sum(len(g) for g in families.values() if len(g)>1),
"recurrent_exact_profile_families":sum(1 for g in families.values() if len(g)>1),"max_family_size":max((len(g) for g in families.values()),default=0)},
"governance":{"raw_changed":False,"rows_deleted":False,"rows_consolidated":False,"economic_identity_inferred":False,"causal_explanation_inferred":False,
"method":"exact K4 recurrence + normalized statistical-profile recurrence + same-date/context comparison"}}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","records":len(rows),"duplicate_k4_groups":len(dups),"target_rows":len(target),"exact_profiles":len(families)}))
