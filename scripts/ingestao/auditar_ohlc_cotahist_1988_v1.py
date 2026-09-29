#!/usr/bin/env python3
"""COTAHIST 1988 — auditoria OHLC estrutural, fail-closed."""
import hashlib,json,zipfile
from pathlib import Path
YEAR="1988"; RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_OHLC_V1.json")
fields=[("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),("preult",109,121)]
records=0; violations=[]; zero=0; nondigit=0; negative=0
with zipfile.ZipFile(RAW) as z:
 members=[n for n in z.namelist() if not n.endswith("/")]
 if len(members)!=1: raise SystemExit(f"RAW ambiguo: {members}")
 with z.open(members[0]) as f:
  for ln,b in enumerate(f,1):
   if not b.startswith(b"01"): continue
   x=b.rstrip(b"\r\n")
   if len(x)!=245: raise SystemExit(f"line {ln}: {len(x)} bytes")
   raw=[x[a-1:e] for _,a,e in fields]
   if any(not v.strip().isdigit() for v in raw):
    nondigit+=1
    continue
   vals=[int(v) for v in raw]; op,hi,lo,mid,cl=vals; records+=1
   if any(v<0 for v in vals): negative+=1
   if hi<max(op,lo,cl) or lo>min(op,hi,cl) or not (lo<=mid<=hi):
    violations.append({"line":ln,"open":op,"high":hi,"low":lo,"mid":mid,"close":cl})
   if vals==[0,0,0,0,0]: zero+=1
result={"schema_version":"1.0.0","status":"OHLC_AUDITORIA_1988","raw_file":str(RAW),
"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"records":records,
"violation_count":len(violations),"violations":violations,"zero_ohlc_count":zero,
"nondigit_ohlc_records":nondigit,"negative_ohlc_records":negative,
"gates":{"records_positive":records>0,"ohlc_order_valid":not violations,"ohlc_numeric_clean":nondigit==0,"no_negative_ohlc":negative==0},
"note":"Auditoria estrutural das relações OHLC sobre valores brutos; nao certifica significado economico e nao altera o RAW."}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"records":records,"violations":len(violations),"zero_ohlc":zero,"nondigit":nondigit,"negative":negative}))
if records==0: raise SystemExit("NO VALID OHLC RECORDS")
