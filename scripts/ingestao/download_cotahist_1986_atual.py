#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys, zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

BASE_URL="https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A{year}.ZIP"
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/"dados/cotahist/raw/anual"
MANIFEST=ROOT/"dados/cotahist/manifests/cotahist_1986_atual_manifest.json"

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def download(url,dest):
    req=Request(url,headers={"User-Agent":"B3-COTAHIST-ingestor/1.0"})
    with urlopen(req,timeout=120) as r, dest.open("wb") as f:
        while True:
            chunk=r.read(1024*1024)
            if not chunk: break
            f.write(chunk)

def validate_zip(path):
    out={"valid_zip":False,"txt_files":[],"record_size":None,"header_ok":False,"trailer_ok":False,"records":0}
    with zipfile.ZipFile(path) as z:
        txts=[n for n in z.namelist() if n.upper().endswith(".TXT")]
        out["txt_files"]=txts
        if len(txts)!=1: raise ValueError(f"ZIP deve conter 1 TXT; encontrados {len(txts)}")
        with z.open(txts[0]) as f:
            first=f.readline()
            if not first: raise ValueError("TXT vazio")
            size=len(first.rstrip(b"\r\n"))
            out["record_size"]=size
            out["header_ok"]=first[:2]==b"00"
            last=first; count=1
            for line in f:
                last=line; count+=1
                n=len(line.rstrip(b"\r\n"))
                if n!=size: raise ValueError(f"registro com {n} bytes; esperado {size}")
            out["records"]=count
            out["trailer_ok"]=last[:2]==b"99"
    if size!=245: raise ValueError(f"tamanho de registro inesperado: {size}")
    if not out["header_ok"] or not out["trailer_ok"]: raise ValueError("header/trailer inválido")
    out["valid_zip"]=True
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=int,default=1986)
    ap.add_argument("--end",type=int,default=datetime.now().year)
    args=ap.parse_args()
    RAW.mkdir(parents=True,exist_ok=True); MANIFEST.parent.mkdir(parents=True,exist_ok=True)
    old=json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    m={"project":"B3 - A BOLSA DO BRASIL","source":"B3","official_start_year":1986,
       "requested_end_year":args.end,"generated_at_utc":datetime.now(timezone.utc).isoformat(),
       "years":old.get("years",{})}
    for year in range(args.start,args.end+1):
        p=RAW/f"COTAHIST_A{year}.ZIP"; e=m["years"].setdefault(str(year),{})
        try:
            if not p.exists(): download(BASE_URL.format(year=year),p)
            info=validate_zip(p)
            e.update({"status":"validated","file":str(p.relative_to(ROOT)).replace("\\","/"),
                      "size_bytes":p.stat().st_size,"sha256":sha256(p),"validation":info,
                      "validated_at_utc":datetime.now(timezone.utc).isoformat()})
            print("[OK]",year,e["size_bytes"],e["sha256"])
        except Exception as exc:
            e.update({"status":"error","error":str(exc),
                      "attempted_at_utc":datetime.now(timezone.utc).isoformat()})
            print("[ERRO]",year,exc,file=sys.stderr)
    MANIFEST.write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__": main()
