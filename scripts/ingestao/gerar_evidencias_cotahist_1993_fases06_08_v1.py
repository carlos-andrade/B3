#!/usr/bin/env python3
"""Auditoria retrospectiva COTAHIST 1993 — FASES 06/07/08, fail-closed."""
import csv,datetime,hashlib,json,zipfile
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path

YEAR="1993"
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP"
CSV_PATH=ROOT/f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv"
Q=ROOT/"dados/cotahist/quality"
Q.mkdir(parents=True,exist_ok=True)

FIELDS=[
("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
("preexe",189,201),("indopc",202,202),("datven",203,210),("fatcot",211,217),
("ptoexe",218,230),("codisi",231,242),("dimes",243,245)]
KEY=("data_pregao","codbdi","codneg","tpmerc","codisi","dimes","especi","prazot","datven","indopc","preexe","ptoexe")
NUMERIC=("preab","premax","premin","premed","preult","totneg","quatot","voltot")

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def raw_rows():
    out=[]
    with zipfile.ZipFile(RAW) as z:
        members=[n for n in z.namelist() if not n.endswith("/")]
        if len(members)!=1: raise RuntimeError(f"RAW ambiguo: {members}")
        with z.open(members[0]) as f:
            for ln,b in enumerate(f,1):
                if not b.startswith(b"01"): continue
                x=b.rstrip(b"\\r\\n")
                if len(x)!=245: raise RuntimeError(f"linha {ln}: {len(x)} bytes")
                r={k:x[a-1:b].decode("latin-1").strip() for k,a,b in FIELDS}
                r["_line"]=ln
                out.append(r)
    return out

def norm_rows():
    with CSV_PATH.open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))

def pick(headers,*names):
    low={h.lower().strip():h for h in headers}
    for n in names:
        if n in low: return low[n]
    raise RuntimeError(f"coluna ausente: {names}")

raw=raw_rows()
norm=norm_rows()
if len(raw)!=len(norm): raise RuntimeError(f"RAW/NORMALIZED contagem divergente: {len(raw)} != {len(norm)}")
headers=norm[0].keys() if norm else []
aliases={
"data_pregao":("data_pregao","data","date"),
"codbdi":("codbdi",),"codneg":("codneg","codigo_negociacao","cod_neg"),
"tpmerc":("tpmerc",),"especi":("especi","especificacao"),
"prazot":("prazot",),"codisi":("codisi","cod_isi"),"dimes":("dimes",),
"datven":("datven","data_vencimento"),"indopc":("indopc",),
"preab":("preab","preco_abertura"),"premax":("premax","preco_maximo"),
"premin":("premin","preco_minimo"),"premed":("premed","preco_medio"),
"preult":("preult","preco_ultimo"),"totneg":("totneg","numero_negocios"),
"quatot":("quatot","quantidade_total"),"voltot":("voltot","volume_total"),
"preexe":("preexe","preco_exercicio"),"ptoexe":("ptoexe","pontos_exercicio")
}
nm={k:pick(headers,*v) for k,v in aliases.items()}

def d(s):
    s=str(s).strip().replace(",",".")
    return Decimal(s) if s else None

# F06 — RAW x NORMALIZED
critical=("data_pregao","codbdi","codneg","tpmerc","preab","premax","premin","premed","preult","totneg","quatot","voltot")
mismatches=[]
for rr,nr in zip(raw,norm):
    bad={}
    for k in critical:
        a=rr[k]; b=str(nr[nm[k]]).strip()
        if k in NUMERIC:
            try:
                da=d(a); db=d(b)
                ok=(da==db)
                if not ok and da is not None and db not in (None,Decimal(0)):
                    ratio=da/db
                    ok=ratio in {Decimal(1),Decimal(10),Decimal(100),Decimal(1000),Decimal(10000),Decimal(100000),Decimal(1000000)}
            except Exception: ok=False
        else: ok=(a==b)
        if not ok: bad[k]={"raw":a,"normalized":b}
    if bad and len(mismatches)<50: mismatches.append({"line":rr["_line"],"fields":bad})

f06={
"schema_version":"1.0.0","year":1993,"phase":"FASE06","status":"VALIDADO" if not mismatches else "BLOQUEADO",
"raw_sha256":sha(RAW),"normalized_sha256":sha(CSV_PATH),"raw_records":len(raw),"normalized_records":len(norm),
"critical_fields_checked":list(critical),"mismatch_count":sum(1 for rr,nr in zip(raw,norm) if any(
    (rr[k]!=str(nr[nm[k]]).strip()) for k in ("data_pregao","codbdi","codneg","tpmerc") )),
"mismatch_sample":mismatches,"decision":"VALIDADO" if not mismatches else "BLOQUEADO",
"note":"Comparacao reproduzivel RAW/NORMALIZED; escalas decimais numericas de 10^n sao aceitas apenas quando a razao e inteira e limitada."
}
(Q/f"COTAHIST_1993_FASE06_RECONCILIACAO_V1.json").write_text(json.dumps(f06,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")

# F07 — key/codes
groups=defaultdict(list)
for r in raw: groups[tuple(r[k] for k in KEY)].append(r)
collisions={k:v for k,v in groups.items() if len(v)>1}
distinct_stats=[]
for k,rows in collisions.items():
    sigs={tuple(r[x] for x in NUMERIC) for r in rows}
    if len(sigs)>1 and len(distinct_stats)<30:
        distinct_stats.append({"key":k,"count":len(rows),"distinct_stat_signatures":len(sigs),"lines":[r["_line"] for r in rows[:20]]})
required_empty={k:sum(1 for r in raw if not r[k]) for k in KEY}
f07={
"schema_version":"1.0.0","year":1993,"phase":"FASE07",
"status":"VALIDADO" if not collisions and not distinct_stats and all(v==0 for v in required_empty.values()) else "BLOQUEADO",
"candidate_key_fields":list(KEY),"row_count":len(raw),"distinct_key_count":len(groups),
"collision_group_count":len(collisions),"collision_row_count":sum(len(v) for v in collisions.values()),
"same_key_distinct_statistics_group_count":len(distinct_stats),"sample":distinct_stats,
"required_empty_counts":required_empty,"raw_sha256":sha(RAW),
"decision":"VALIDADO" if not collisions and not distinct_stats and all(v==0 for v in required_empty.values()) else "BLOQUEADO"
}
(Q/f"COTAHIST_1993_FASE07_IDENTIDADE_CHAVES_V1.json").write_text(json.dumps(f07,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")

# F08 — semantic/calendar structural checks
dates=[r["data_pregao"] for r in raw]
valid=[]; invalid=[]; weekend=[]
for s in dates:
    try:
        dt=datetime.datetime.strptime(s,"%Y%m%d").date()
        valid.append(dt)
        if dt.weekday()>=5: weekend.append(s)
    except ValueError: invalid.append(s)
unique=sorted(set(valid)); us=set(unique); gaps=[]
if unique:
    cur=unique[0]
    while cur<=unique[-1]:
        if cur.weekday()<5 and cur not in us: gaps.append(cur.isoformat())
        cur+=datetime.timedelta(days=1)
out_order=sum(1 for a,b in zip(dates,dates[1:]) if b<a)
tp=Counter(r["tpmerc"] for r in raw); bdi=Counter(r["codbdi"] for r in raw); dimes=Counter(r["dimes"] for r in raw)
ohlc_bad=0
for r in raw:
    try:
        op,hi,lo,mid,cl=[Decimal(r[k]) for k in ("preab","premax","premin","premed","preult")]
        if hi<max(op,lo,cl) or lo>min(op,hi,cl) or not(lo<=mid<=hi): ohlc_bad+=1
    except Exception: ohlc_bad+=1
f08_gates={
"all_dates_valid":len(valid)==len(dates),"no_weekend_dates":len(weekend)==0,
"records_chronological":out_order==0,"year_bounds":all(dt.year==1993 for dt in valid),
"ohlc_relations_valid":ohlc_bad==0,"tpmerc_observed":bool(tp),"codbdi_observed":bool(bdi)
}
f08={
"schema_version":"1.0.0","year":1993,"phase":"FASE08",
"status":"VALIDADO" if all(f08_gates.values()) else "BLOQUEADO","records":len(raw),
"first_date":min(dates) if dates else None,"last_date":max(dates) if dates else None,
"distinct_trading_dates":len(unique),"candidate_weekday_gaps":gaps,
"out_of_order_records":out_order,"invalid_dates":len(invalid),"weekend_dates":len(weekend),
"tpmerc_distribution":dict(tp),"codbdi_distribution":dict(bdi),"dimes_distribution":dict(dimes),
"ohlc_relation_violations":ohlc_bad,"gates":f08_gates,"raw_sha256":sha(RAW),
"decision":"VALIDADO" if all(f08_gates.values()) else "BLOQUEADO",
"note":"Lacunas em dias uteis sao apenas candidatas a nao-pregao; nao sao classificadas como feriados sem fonte primaria. PRAZOT e avaliado como campo preservado; este teste nao atribui significado economico adicional."
}
(Q/f"COTAHIST_1993_FASE08_SEMANTICA_CALENDARIO_V1.json").write_text(json.dumps(f08,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")

failed=[]
if mismatches: failed.append("FASE06")
if collisions or distinct_stats or any(required_empty.values()): failed.append("FASE07")
if not all(f08_gates.values()): failed.append("FASE08")
print(json.dumps({"year":1993,"records":len(raw),"fases":{"06":f06["status"],"07":f07["status"],"08":f08["status"]},"failed":failed},ensure_ascii=False))
if failed: raise SystemExit("FAIL-CLOSED: "+",".join(failed))
