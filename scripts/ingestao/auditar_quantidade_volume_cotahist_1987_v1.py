#!/usr/bin/env python3
import csv,json,zipfile,hashlib
from decimal import Decimal
from pathlib import Path
YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
CSV=Path(f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_AUDITORIA_QUANTIDADE_VOLUME_V1.json")
FIELDS={"totneg":(148,152),"quatot":(153,170),"voltot":(171,188)}
def field(s,a,b): return s[a-1:b]
def dec(s): return Decimal(s.strip().replace(",",".")) if s.strip() else None
stats={"records":0,"negative":{k:0 for k in FIELDS},"non_numeric":{k:0 for k in FIELDS},"zero":{k:0 for k in FIELDS},"control_bytes":{k:0 for k in FIELDS},"examples":[]}
raw=[]
with zipfile.ZipFile(RAW) as z:
    members=[n for n in z.namelist() if not n.endswith("/")]
    if len(members)!=1: raise RuntimeError(f"RAW ambiguo: {members}")
    with z.open(members[0]) as f:
        for line_no,b in enumerate(f,1):
            if not b.startswith(b"01"): continue
            x=b.rstrip(b"\r\n")
            if len(x)!=245: raise RuntimeError(f"linha {line_no}: {len(x)} bytes")
            rec={"line":line_no}
            for k,(a,bp) in FIELDS.items():
                rawb=x[a-1:bp]
                try: v=int(rawb.decode("ascii").strip() or "0")
                except Exception:
                    stats["non_numeric"][k]+=1; v=None
                if any(c<32 or c>126 for c in rawb): stats["control_bytes"][k]+=1
                if v is not None:
                    if v<0: stats["negative"][k]+=1
                    if v==0: stats["zero"][k]+=1
                rec[k]=v
            raw.append(rec); stats["records"]+=1
            if len(stats["examples"])<10 and any(rec[k] is None for k in FIELDS): stats["examples"].append(rec)
# Cross-check normalized values using the same explicit scale reconciliation policy.
with CSV.open("r",encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
headers={h.lower().strip():h for h in (rows[0].keys() if rows else [])}
def pick(*names):
    for n in names:
        if n in headers:return headers[n]
    raise RuntimeError("coluna ausente: "+str(names))
m={k:pick(k) for k in FIELDS}
mismatch={k:0 for k in FIELDS}; scale={k:{} for k in FIELDS}
if len(rows)!=len(raw): raise RuntimeError("RAW/NORMALIZED contagem divergente")
allowed={Decimal(1),Decimal(10),Decimal(100),Decimal(1000),Decimal(10000),Decimal(100000),Decimal(1000000)}
for rr,nr in zip(raw,rows):
    for k in FIELDS:
        a=Decimal(rr[k]) if rr[k] is not None else None
        b=dec(str(nr[m[k]]))
        ok=(a==b)
        if not ok and a is not None and b not in (None,Decimal(0)):
            ratio=a/b
            if ratio in allowed: ok=True; scale[k][str(ratio)]=scale[k].get(str(ratio),0)+1
        if not ok: mismatch[k]+=1
gates={
 "records_positive":stats["records"]>0,
 "all_numeric":all(v==0 for v in stats["non_numeric"].values()),
 "no_negative":all(v==0 for v in stats["negative"].values()),
 "no_control_bytes":all(v==0 for v in stats["control_bytes"].values()),
 "raw_normalized_mismatch_zero":all(v==0 for v in mismatch.values())
}
result={"schema_version":"1.0.0","status":"QUANTIDADE_VOLUME_AUDITORIA_1987","raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
"records":stats["records"],"raw_field_stats":stats,"normalized_mismatch_count":mismatch,"scales_observed":scale,
"gates":gates,"note":"Auditoria estrutural de TOTNEG, QUATOT e VOLTOT. Não infere significado econômico além da integridade dos campos."}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n",encoding="utf-8")
failed=[k for k,v in gates.items() if not v]
print(json.dumps({"status":"OK" if not failed else "GATES_FAILED","failed":failed,"records":stats["records"],"mismatch":mismatch},ensure_ascii=False))
if failed: raise SystemExit("FAIL-CLOSED: "+", ".join(failed))
