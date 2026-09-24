#!/usr/bin/env python3
"""FASE 07D — CODISI no COTAHIST 1986."""
from __future__ import annotations
import argparse,json,zipfile
from collections import Counter,defaultdict
from datetime import datetime

def parse(raw):
 b=raw.rstrip(b"\r\n")
 if len(b)!=245 or b[:2]!=b"01": return None
 def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
 return {"data_pregao":s(3,10),"codbdi":s(11,12),"codneg":s(13,24),"tpmerc":s(25,27),"codisi":s(231,242)}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
 rows=0; nonblank=0; counts=Counter(); dates=defaultdict(set); codneg=defaultdict(set); by_pair=Counter(); lengths=Counter()
 with zipfile.ZipFile(a.zip) as z:
  members=[x for x in z.namelist() if not x.endswith("/")]
  if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
  with z.open(members[0]) as f:
   for raw in f:
    r=parse(raw)
    if not r: continue
    rows+=1; c=r["codisi"]; counts[c]+=1; dates[c].add(r["data_pregao"]); codneg[c].add(r["codneg"]); by_pair[(c,r["tpmerc"])]+=1; lengths[len(c)]+=1
    if c: nonblank+=1
 result={"schema_version":"1.0.0","status":"FASE_07D_CODISI_1986_ANALISE","generated_at_utc":datetime.utcnow().replace(microsecond=0).isoformat()+"Z","raw_file":"COTAHIST_A1986.ZIP","rows":rows,
 "source_document":{"institution":"B3","document":"LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS","revision":"02","date":"05/10/2020","field":"CODISI","positions":"231-242","source_url":"https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf"},
 "historical_semantics":{"official_text":"Código do papel no sistema ISIN ou código interno do papel","isin_start_date":"1995-05-15","interpretation_for_1986":"CODIGO_INTERNO_DO_PAPEL","isin_interpretation_allowed_for_1986":False},
 "observed":{"distinct_codisi_total":len(counts),"distinct_codisi_nonblank":len([c for c in counts if c]),"blank_rows":rows-nonblank,"nonblank_rows":nonblank,"length_distribution":dict(sorted(lengths.items()))},
 "codes":{c:{"rows":counts[c],"trading_dates":len(dates[c]),"distinct_codneg":len(codneg[c]),"mapping_status":"CODIGO_INTERNO_1986" if c else "BRANCO","tpmerc_distribution":dict(sorted({t:n for (cc,t),n in by_pair.items() if cc==c}.items()))} for c in sorted(counts)},
 "governance":{"raw_unchanged":True,"normalized_unchanged":True,"codisi_not_treated_as_isin_in_1986":True,"economic_identity_not_inferred_from_codisi":True,"historical_semantics_based_on_b3_documentary_cutoff":True}}
 with open(a.output,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2); f.write("\n")
if __name__=="__main__": main()
