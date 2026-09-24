#!/usr/bin/env python3
"""Reconciliação semântica COTAHIST 1986; não altera RAW/NORMALIZED."""
from __future__ import annotations
import argparse,json,zipfile
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path
FIELDS=["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
def parse(raw):
 b=raw.rstrip(b"\r\n")
 if len(b)!=245 or b[:2]!=b"01": return None
 def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
 vals=[s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56)]
 for a,z in [(57,69),(70,82),(83,95),(96,108),(109,121),(122,134),(135,147)]: 
  x=s(a,z); vals.append(Decimal(x)/100 if x else None)
 vals += [int(s(148,152)) if s(148,152) else None,int(s(153,170)) if s(153,170) else None,Decimal(s(171,188))/100 if s(171,188) else None,Decimal(s(189,201))/100 if s(189,201) else None,s(202,202),s(203,210),int(s(211,217)) if s(211,217) else None,Decimal(s(218,230))/Decimal(10**6) if s(218,230) else None,s(231,242),s(243,245)]
 return dict(zip(FIELDS,vals))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); ap.add_argument("--sample-per-code",type=int,default=10); a=ap.parse_args()
 tp=Counter(); bdi=Counter(); pairs=Counter(); keys=Counter(); samples=defaultdict(list); ohlc=[]; volume=[]; dates=Counter()
 with zipfile.ZipFile(a.zip) as z:
  members=[x for x in z.namelist() if not x.endswith("/")]
  if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
  with z.open(members[0]) as f:
   for raw in f:
    r=parse(raw)
    if not r: continue
    tp[r["tpmerc"]]+=1; bdi[r["codbdi"]]+=1; pairs[(r["tpmerc"],r["codbdi"])]+=1
    key=(r["data_pregao"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dismes"]); keys[key]+=1; dates[r["data_pregao"]]+=1
    if len(samples[r["tpmerc"]])<a.sample_per_code: samples[r["tpmerc"]].append({k:r[k] for k in ("data_pregao","codbdi","codneg","tpmerc","nomres","especi","preabe","premax","premin","preult","totneg","quatot","voltot","codisi","dismes")})
    h,l,o,c=r["premax"],r["premin"],r["preabe"],r["preult"]
    if None not in (h,l,o,c) and (h<l or o>h or o<l or c>h or c<l):
     ohlc.append({k:r[k] for k in ("data_pregao","codbdi","codneg","tpmerc","nomres","especi","preabe","premax","premin","preult","totneg","quatot","voltot","codisi","dismes")})
    q,v,avg=r["quatot"],r["voltot"],r["premed"]
    if q and v is not None and avg is not None and avg>0:
     expected=avg*Decimal(q); rel=abs(v-expected)/expected if expected else None
     volume.append({"data_pregao":r["data_pregao"],"codneg":r["codneg"],"tpmerc":r["tpmerc"],"quatot":q,"premed":str(avg),"voltot":str(v),"expected_premed_x_quatot":str(expected),"relative_difference":str(rel)})
 out={"schema_version":"1.0.0","status":"RECONCILIACAO_SEMANTICA_1986_INICIAL","raw_file":Path(a.zip).name,"tpmerc_counts":dict(sorted(tp.items())),"codbdi_counts":dict(sorted(bdi.items())),"tpmerc_codbdi_matrix":[{"tpmerc":x,"codbdi":y,"rows":n} for (x,y),n in sorted(pairs.items())],"candidate_logical_key":["data_pregao","codbdi","codneg","tpmerc","codisi","dismes"],"candidate_key_groups_repeated":sum(n>1 for n in keys.values()),"unique_trading_dates":len(dates),"ohlc_inconsistency_count":len(ohlc),"ohlc_examples":ohlc[:100],"volume_validation_sample_count":len(volume),"volume_validation_samples":volume[:100],"tpmerc_samples":dict(samples),"interpretation":"Inventário e amostragem; nenhum código ou chave é declarado semanticamente definitivo nesta etapa."}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str)+"\n",encoding="utf-8")
 print(json.dumps({"status":out["status"],"tpmerc":out["tpmerc_counts"],"codbdi":out["codbdi_counts"],"ohlc":len(ohlc),"dates":len(dates)},ensure_ascii=False))
if __name__=="__main__": main()
