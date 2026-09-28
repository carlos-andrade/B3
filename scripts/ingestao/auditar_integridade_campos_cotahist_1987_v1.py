#!/usr/bin/env python3
"""Diagnóstico de integridade byte-a-byte dos campos COTAHIST 1987."""
import hashlib, json, zipfile
from collections import Counter
from pathlib import Path

YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_INTEGRIDADE_CAMPOS_V1.json")
FIELDS=[
 ("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
 ("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
 ("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
 ("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
 ("preexe",189,201),("indopc",202,202),("datven",203,210),
 ("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)
]
NUMERIC={"data_pregao","codbdi","tpmerc","prazot","preab","premax","premin","premed","preult","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","dimes"}
CONTROL=set(range(0,32)) | {127}
records=0
field_issues=Counter()
samples=[]
with zipfile.ZipFile(RAW) as z:
    members=[n for n in z.namelist() if not n.endswith("/")]
    if len(members)!=1: raise RuntimeError(f"RAW ambiguo: {members}")
    with z.open(members[0]) as f:
        for line_no,b in enumerate(f,1):
            if b[:2]!=b"01": continue
            records+=1
            if len(b.rstrip(b"\r\n"))!=245:
                raise RuntimeError(f"Registro tipo 01 fora de 245 bytes: linha {line_no}")
            line=b.rstrip(b"\r\n")
            for name,a,end in FIELDS:
                raw=line[a-1:end]
                bad=[x for x in raw if x in CONTROL]
                if bad:
                    field_issues[name]+=1
                    if len(samples)<100:
                        samples.append({"line":line_no,"field":name,"raw_hex":raw.hex(),"bad_bytes":[f"{x:02x}" for x in sorted(set(bad))],"decoded_latin1":raw.decode("latin-1")})
result={
 "schema_version":"1.0.0","status":"AUDITORIA_INTEGRIDADE_CAMPOS_1987",
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "type01_record_count":records,
 "fields_with_control_bytes":dict(field_issues),
 "control_byte_sample":samples,
 "fail_closed_gates":{
   "records_positive":records>0,
   "no_control_bytes_in_fixed_fields":sum(field_issues.values())==0
 },
 "interpretation":"Diagnóstico estrutural. Bytes de controle em campos fixos podem indicar dado histórico válido, deslocamento de layout ou corrupção; não recebem significado econômico automaticamente."
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK" if not field_issues else "CONTROL_BYTES_DETECTED","records":records,"fields_with_control_bytes":dict(field_issues)}))
if not result["fail_closed_gates"]["records_positive"]: raise SystemExit("NO RECORDS")
