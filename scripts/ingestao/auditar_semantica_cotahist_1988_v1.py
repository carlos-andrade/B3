#!/usr/bin/env python3
"""COTAHIST 1988 — semantica observacional inicial, fail-closed."""
import hashlib,json,zipfile
from collections import Counter,defaultdict
from datetime import datetime
from pathlib import Path
YEAR="1988"; RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_SEMANTICA_V1.json")
FIELDS=[("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),("preexe",189,201),("indopc",202,202),("datven",203,210),("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)]
def read():
 rows=[]; lengths=Counter(); invalid=[]; members=[]
 with zipfile.ZipFile(RAW) as z:
  members=[n for n in z.namelist() if not n.endswith("/")]
  if len(members)!=1: raise SystemExit(f"RAW ambiguo: {members}")
  with z.open(members[0]) as f:
   for n,b in enumerate(f,1):
    line=b.decode("latin-1").rstrip("\r\n"); lengths[len(line)]+=1
    if line[:2]!="01": continue
    if len(line)!=245: raise SystemExit(f"tipo 01 fora de 245 bytes: linha {n}")
    r={name:line[a-1:b].strip() for name,a,b in FIELDS}; r["_line"]=n; rows.append(r)
    d=r["data_pregao"]
    if len(d)!=8 or not d.isdigit():
     invalid.append({"line":n,"value":d})
    else:
     try: datetime.strptime(d,"%Y%m%d")
     except ValueError: invalid.append({"line":n,"value":d})
 return rows,lengths,invalid,members[0]
rows,lengths,invalid,member=read()
def dist(field): return Counter(r[field] for r in rows)
def top(field,n=25): return sorted(dist(field).items(),key=lambda x:(-x[1],x[0]))[:n]
# Contexto observavel: combinacoes de codigos, sem atribuir significado economico.
contexts=Counter((r["tpmerc"],r["codbdi"]) for r in rows)
prazot_by_pair=defaultdict(Counter)
for r in rows: prazot_by_pair[(r["tpmerc"],r["codbdi"])][r["prazot"]]+=1
result={"schema_version":"1.0.0","status":"FASE_SEMANTICA_INICIAL_1988","year":1988,
"raw_file":str(RAW),"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"zip_member":member,
"records_type01":len(rows),"physical_line_lengths":dict(sorted(lengths.items())),"invalid_trade_date_records":len(invalid),
"field_inventory":{n:{"start":a,"end":b,"width":b-a+1} for n,a,b in FIELDS},
"domains":{f:{"distinct":len(dist(f)),"top":top(f)} for f in ("codbdi","tpmerc","codneg","codisi","dimes","especi","prazot","indopc")},
"observed_context":{"tpmerc_codbdi_distinct":len(contexts),"tpmerc_codbdi_top":[{"tpmerc":a,"codbdi":b,"count":c} for (a,b),c in contexts.most_common(50)],
"prazot_by_tpmerc_codbdi":[{"tpmerc":a,"codbdi":b,"prazot_top":list(c.most_common(20))} for (a,b),c in sorted(prazot_by_pair.items())]},
"semantic_gates":{"record_type_01_245_bytes":len(rows)>0 and set(lengths).issubset({245}),
"trade_date_valid":len(invalid)==0,"tpmerc_observed":len(dist("tpmerc"))>0,"codbdi_observed":len(dist("codbdi"))>0,
"economic_meaning_not_asserted":True},
"assessment":{"status":"OBSERVACIONAL","economic_meaning_of_codes":"NAO_CERTIFICADO_NESTA_FASE",
"primary_historical_evidence_required_for_interpretation":True,"next_gate":["integridade dos campos","OHLC","quantidade/volume","calendario",
"evidencia historica primaria para interpretacoes economicas"]}}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
failed=[k for k,v in result["semantic_gates"].items() if not v]
print(json.dumps({"status":"OK" if not failed else "GATES_FAILED","failed":failed,"records":len(rows),"output":str(OUT)},ensure_ascii=False))
if failed: raise SystemExit("GATES FAILED: "+", ".join(failed))
