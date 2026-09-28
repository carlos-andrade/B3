#!/usr/bin/env python3
import csv,json,zipfile,hashlib
from pathlib import Path
YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
NORM=Path(f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_OHLC_V1.json")
stats={"records":0,"violations":[],"zero_ohlc":0}
with zipfile.ZipFile(RAW) as z:
    member=[n for n in z.namelist() if not n.endswith("/")][0]
    with z.open(member) as f:
        for ln,b in enumerate(f,1):
            if not b.startswith(b"01"): continue
            x=b.rstrip(b"\r\n")
            if len(x)!=245: raise RuntimeError(f"line {ln}: {len(x)} bytes")
            vals=[]
            for a,e in [(57,69),(70,82),(83,95),(96,108),(109,121)]:
                vals.append(int(x[a-1:e]))
            op,hi,lo,mid,cl=vals
            stats["records"]+=1
            if hi<max(op,lo,cl) or lo>min(op,hi,cl):
                stats["violations"].append({"line":ln,"open":op,"high":hi,"low":lo,"close":cl})
            if vals==[0,0,0,0,0]: stats["zero_ohlc"]+=1
result={
 "schema_version":"1.0.0","status":"OHLC_AUDITORIA_1987",
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "records":stats["records"],"violations":stats["violations"],
 "violation_count":len(stats["violations"]),"zero_ohlc_count":stats["zero_ohlc"],
 "gates":{"records_positive":stats["records"]>0,"ohlc_order_valid":not stats["violations"]},
 "note":"Auditoria estrutural das relações OHLC sobre valores brutos. Não certifica significado econômico."
}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"records":stats["records"],"violations":len(stats["violations"]),"zero_ohlc":stats["zero_ohlc"]}))
