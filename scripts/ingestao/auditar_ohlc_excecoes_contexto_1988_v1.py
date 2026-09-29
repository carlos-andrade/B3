#!/usr/bin/env python3
import json,zipfile,hashlib
from pathlib import Path
YEAR="1988"; RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP"); OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_OHLC_EXCECOES_CONTEXT_V1.json")
TARGET={9267,20374,20596,123264}
F=[("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),("preexe",189,201),("indopc",202,202),("datven",203,210),("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)]
rows=[]
with zipfile.ZipFile(RAW) as z:
 m=[n for n in z.namelist() if not n.endswith("/")][0]
 with z.open(m) as f:
  lines={n:b.rstrip(b"\r\n") for n,b in enumerate(f,1) if n in TARGET}
for n,x in lines.items():
 rows.append({"line":n,"fields":{name:x[a-1:e].decode("latin-1") for name,a,e in F},"raw_ohlc_hex":{name:x[a-1:e].hex() for name,a,e in F if name in {"preab","premax","premin","premed","preult"}},"raw_record_hex":x.hex()})
out={"schema_version":"1.0.0","raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"target_lines":sorted(TARGET),"records":rows,
"assessment":"Contexto factual das excecoes OHLC; nenhuma correcao ou reinterpretacao aplicada."}
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","records":len(rows),"output":str(OUT)}))
