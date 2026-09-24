#!/usr/bin/env python3
"""Auditoria de consistência econômica QUATOT x VOLTOT x PREULT x FATCOT no COTAHIST 1986."""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from collections import Counter
from decimal import Decimal, InvalidOperation
from pathlib import Path

def parse(raw: bytes):
    b=raw.rstrip(b"\r\n")
    if len(b)!=245 or b[:2]!=b"01": return None
    def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
    def dec(a,z,scale=2):
        x=s(a,z)
        return Decimal(x)/(Decimal(10)**scale) if x else None
    return {
      "data_pregao":s(3,10),"codbdi":s(11,12),"codneg":s(13,24),"tpmerc":s(25,27),
      "nomres":s(28,39),"especi":s(40,49),"preabe":dec(57,69),"premax":dec(70,82),
      "premin":dec(83,95),"premed":dec(96,108),"preult":dec(109,121),
      "totneg":int(s(148,152)) if s(148,152) else None,
      "quatot":int(s(153,170)) if s(153,170) else None,
      "voltot":dec(171,188),"fatcot":int(s(211,217)) if s(211,217) else None,
      "raw_sha256":hashlib.sha256(b).hexdigest()
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    total=0; valid=0; issues=[]; by_tp=Counter(); factor=Counter()
    with zipfile.ZipFile(a.zip) as z:
      members=[x for x in z.namelist() if not x.endswith("/")]
      if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
      with z.open(members[0]) as f:
        for line_no,raw in enumerate(f,1):
          r=parse(raw)
          if not r: continue
          total+=1
          if r["fatcot"] is not None: factor[str(r["fatcot"])]+=1
          q,v,p,fc=r["quatot"],r["voltot"],r["preult"],r["fatcot"]
          labels=[]
          if q is None or v is None: labels.append("MISSING_QTY_OR_VOLUME")
          elif q==0 and v!=0: labels.append("QTY_ZERO_VOLUME_NONZERO")
          elif q!=0 and v==0:
            if p is not None and fc is not None and p >= 0 and (p*q/fc) <= Decimal("0.01"):
              labels.append("VOLTOT_ZERO_COMPATIVEL_ARREDONDAMENTO_0_01")
            else:
              labels.append("QTY_NONZERO_VOLUME_ZERO")
          if p is not None and p<0: labels.append("NEGATIVE_LAST_PRICE")
          if q is not None and q<0: labels.append("NEGATIVE_QUANTITY")
          if v is not None and v<0: labels.append("NEGATIVE_VOLUME")
          if fc is not None and fc<=0: labels.append("NONPOSITIVE_FATCOT")
          if q is not None and v is not None and p is not None and fc is not None and q>0:
            implied=v/(p*q)
            # FATCOT is a quote factor, not an automatic identity between volume and price*quantity.
            if p>0:
              ratio=implied*fc
              if ratio < Decimal("0.00001") or ratio > Decimal("100000"):
                labels.append("ECONOMIC_RATIO_OUTLIER")
          if labels:
            issues.append({
              "line_number":line_no,"data_pregao":r["data_pregao"],"codbdi":r["codbdi"],
              "codneg":r["codneg"],"tpmerc":r["tpmerc"],"nomres":r["nomres"],
              "preult":str(p) if p is not None else None,"quatot":q,
              "voltot":str(v) if v is not None else None,"fatcot":fc,
              "totneg":r["totneg"],"classifications":labels,"raw_sha256":r["raw_sha256"]
            })
          else: valid+=1
    out={"schema_version":"1.1.0","status":"AUDITORIA_QUANTIDADE_VOLUME_PRECO_1986",
         "raw_file":Path(a.zip).name,"type01_records":total,"records_without_flag":valid,
         "issue_count":len(issues),"fatcot_distribution":dict(sorted(factor.items())),
         "classification_counts":dict(sorted(Counter(x for i in issues for x in i["classifications"]).items())),
         "issues":issues,
         "methodology":{
           "price_scale":"2 casas decimais no layout COTAHIST",
           "volume_scale":"2 casas decimais no layout COTAHIST",
           "quatot":"quantidade total de títulos negociados",
           "voltot":"volume total de títulos negociados",
           "fatcot":"fator de cotação; 1=unitária, 1000=lote de mil ações",
           "warning":"VOLTOT não é tratado como identidade mecânica PREULT x QUATOT. A relação econômica depende da natureza do instrumento, do preço efetivo dos negócios e do fator de cotação. Para VOLTOT=0, valores teóricos PREULT*QUATOT/FATCOT <= 0,01 são compatíveis com a resolução de duas casas decimais do campo."
         }}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":out["status"],"records":total,"issues":len(issues),"classes":out["classification_counts"],"fatcot":out["fatcot_distribution"]},ensure_ascii=False))

if __name__=="__main__": main()
