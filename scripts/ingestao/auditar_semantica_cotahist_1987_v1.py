#!/usr/bin/env python3
"""COTAHIST 1987 — auditoria semantica inicial.

Fail-closed: mede semantica observavel no RAW e NAO atribui significado
historico que nao esteja demonstrado pela propria fonte.
"""
import csv, hashlib, json, zipfile
from collections import Counter
from pathlib import Path

YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_SEMANTICA_V1.json")

FIELDS=[
 ("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
 ("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
 ("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
 ("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
 ("preexe",189,201),("indopc",202,202),("datven",203,210),
 ("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)
]

def sl(line,a,b): return line[a-1:b]
def norm(line):
    return {name:sl(line,a,b).strip() for name,a,b in FIELDS}

if not RAW.exists():
    raise SystemExit(f"RAW ausente: {RAW}")

rows=[]
physical_lengths=Counter()
invalid_date=[]
with zipfile.ZipFile(RAW) as z:
    members=[n for n in z.namelist() if not n.endswith("/")]
    if len(members)!=1:
        raise SystemExit(f"RAW ambiguo: {len(members)} arquivos no ZIP")
    with z.open(members[0]) as f:
        for n,b in enumerate(f,1):
            line=b.decode("latin-1").rstrip("\r\n")
            physical_lengths[len(line)]+=1
            if line[:2]!="01":
                continue
            if len(line)!=245:
                raise SystemExit(f"registro tipo 01 com tamanho {len(line)} na linha {n}")
            r=norm(line); r["source_line"]=n; rows.append(r)
            if r["data_pregao"] and (len(r["data_pregao"])!=8 or not r["data_pregao"].isdigit()):
                invalid_date.append(r)

def counts(field):
    return dict(sorted(Counter(r[field] for r in rows).items()))

def sample(field,n=25):
    return sorted(counts(field).items(), key=lambda x:(-x[1],x[0]))[:n]

result={
 "schema_version":"1.0.0",
 "status":"FASE_SEMANTICA_INICIAL_1987",
 "year":1987,
 "raw_file":str(RAW),
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "zip_member":members[0],
 "records_type01":len(rows),
 "physical_line_lengths":dict(sorted(physical_lengths.items())),
 "invalid_trade_date_records":len(invalid_date),
 "field_inventory":{name:{"start":a,"end":b,"width":b-a+1} for name,a,b in FIELDS},
 "domains":{
   "codbdi":{"distinct":len(counts("codbdi")),"top":sample("codbdi")},
   "tpmerc":{"distinct":len(counts("tpmerc")),"top":sample("tpmerc")},
   "codneg":{"distinct":len(counts("codneg")),"top":sample("codneg")},
   "codisi":{"distinct":len(counts("codisi")),"top":sample("codisi")},
   "dimes":{"distinct":len(counts("dimes")),"top":sample("dimes")},
   "especi":{"distinct":len(counts("especi")),"top":sample("especi")},
   "prazot":{"distinct":len(counts("prazot")),"top":sample("prazot")}
 },
 "semantic_gates":{
   "record_type_01_245_bytes":len(rows)>0 and set(physical_lengths).issubset({245}),
   "trade_date_8_digits":len(invalid_date)==0,
   "tpmerc_observed":len(counts("tpmerc"))>0,
   "codbdi_observed":len(counts("codbdi"))>0,
   "logical_identity_not_asserted_without_historical_evidence":True
 },
 "assessment":{
   "status":"OBSERVACIONAL",
   "economic_meaning_of_codes":"NAO_CERTIFICADO_NESTA_FASE",
   "next_gate":[
      "reconciliar amostras RAW x NORMALIZED",
      "auditar chave logica 1987",
      "auditar tpmerc e codbdi por distribuicao e contexto",
      "auditar OHLC, quantidade e volume",
      "auditar calendario",
      "documentar evidencia historica contemporanea quando houver interpretacao economica"
   ]
 }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
failed=[k for k,v in result["semantic_gates"].items() if not v]
if failed: raise SystemExit("GATES FAILED: "+", ".join(failed))
print(json.dumps({"status":"OK","output":str(OUT),"records_type01":len(rows),"raw_sha256":result["raw_sha256"]},ensure_ascii=False))
