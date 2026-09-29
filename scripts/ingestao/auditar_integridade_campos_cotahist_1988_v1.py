#!/usr/bin/env python3
"""COTAHIST 1988 — auditoria estrutural de integridade dos campos. Fail-closed."""
import hashlib,json,zipfile
from collections import Counter
from pathlib import Path
YEAR="1988"; RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_INTEGRIDADE_CAMPOS_V1.json")
FIELDS=[("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),("preexe",189,201),("indopc",202,202),("datven",203,210),("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)]
NUMERIC={"data_pregao","codbdi","tpmerc","prazot","preab","premax","premin","premed","preult","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","dimes"}
CONTROL=set(range(32))|{127}
records=0; issues=Counter(); samples=[]; numeric_non_digits=Counter(); blank_numeric=Counter()
with zipfile.ZipFile(RAW) as z:
 members=[n for n in z.namelist() if not n.endswith("/")]
 if len(members)!=1: raise SystemExit(f"RAW ambiguo: {members}")
 with z.open(members[0]) as f:
  for no,b in enumerate(f,1):
   line=b.rstrip(b"\r\n")
   if line[:2]!=b"01": continue
   records+=1
   if len(line)!=245: raise SystemExit(f"tipo 01 fora de 245 bytes: linha {no}")
   for name,a,end in FIELDS:
    raw=line[a-1:end]
    bad=[x for x in raw if x in CONTROL]
    if bad:
     issues[name]+=1
     if len(samples)<200: samples.append({"line":no,"field":name,"raw_hex":raw.hex(),"bad_bytes":[f"{x:02x}" for x in sorted(set(bad))]})
    if name in NUMERIC:
     stripped=raw.strip()
     if not stripped: blank_numeric[name]+=1
     elif not stripped.isdigit(): numeric_non_digits[name]+=1
result={"schema_version":"1.0.0","status":"AUDITORIA_INTEGRIDADE_CAMPOS_1988","raw_file":str(RAW),"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"type01_record_count":records,
"fields_with_control_bytes":dict(issues),"control_byte_sample":samples,
"numeric_fields_non_digit":dict(numeric_non_digits),"numeric_fields_blank":dict(blank_numeric),
"fail_closed_gates":{"records_positive":records>0,"fixed_record_length_245":records>0,"no_control_bytes":sum(issues.values())==0,"numeric_fields_clean":sum(numeric_non_digits.values())==0},
"interpretation":"Diagnostico estrutural. Anomalias de bytes ou campos numericos nao recebem significado economico nem sao corrigidas automaticamente."}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK" if all(result["fail_closed_gates"].values()) else "ANOMALIES","records":records,"control":dict(issues),"non_digits":dict(numeric_non_digits)}))
if not result["fail_closed_gates"]["records_positive"]: raise SystemExit("NO RECORDS")
