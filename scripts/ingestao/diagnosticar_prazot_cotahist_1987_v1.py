#!/usr/bin/env python3
"""Diagnóstico contextual das ocorrências anômalas de PRAZOT no COTAHIST 1987."""
import hashlib, json, zipfile
from pathlib import Path

YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_DIAGNOSTICO_PRAZOT_V1.json")
FIELDS=[
 ("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
 ("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
 ("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
 ("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
 ("preexe",189,201),("indopc",202,202),("datven",203,210),
 ("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)
]
CONTROL=set(range(0,32)) | {127}
targets=[]
records={}
with zipfile.ZipFile(RAW) as z:
    members=[n for n in z.namelist() if not n.endswith("/")]
    if len(members)!=1: raise RuntimeError(f"RAW ambiguo: {members}")
    with z.open(members[0]) as f:
        for line_no,b in enumerate(f,1):
            if b[:2]!=b"01": continue
            line=b.rstrip(b"\r\n")
            if len(line)!=245: raise RuntimeError(f"Registro fora de 245 bytes: {line_no}")
            raw=line[49:52]
            if any(x in CONTROL for x in raw):
                targets.append(line_no)
                records[line_no]={
                    "prazot_raw_hex":raw.hex(),
                    "fields":{name:line[a-1:end].decode("latin-1") for name,a,end in FIELDS},
                    "full_record_sha256":hashlib.sha256(line).hexdigest(),
                    "raw_prefix_hex":line[:60].hex(),
                    "raw_suffix_hex":line[220:].hex()
                }
result={
 "schema_version":"1.0.0","status":"DIAGNOSTICO_PRAZOT_1987",
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "affected_record_count":len(targets),
 "affected_lines":targets,
 "records":records,
 "interpretation":"Diagnóstico contextual; não altera RAW nem NORMALIZED e não atribui significado econômico aos bytes anômalos."
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","affected_record_count":len(targets)}))
