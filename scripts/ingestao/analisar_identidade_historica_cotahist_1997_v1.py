#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,zipfile
from collections import Counter,defaultdict
from pathlib import Path

FIELDS=["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
KEYS={
"K1_data_codneg_tpmerc":["data_pregao","codneg","tpmerc"],
"K2_data_codbdi_codneg_tpmerc":["data_pregao","codbdi","codneg","tpmerc"],
"K3_data_codbdi_codneg_tpmerc_codisi_dismes":["data_pregao","codbdi","codneg","tpmerc","codisi","dismes"],
"K4_contractual":["data_pregao","codbdi","codneg","tpmerc","codisi","dismes","especi","prazot","datven","preexe","indopc","ptoexe"]}

def parse(raw):
 b=raw.rstrip(b"\r\n")
 if len(b)!=245 or b[:2]!=b"01": return None
 def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
 return dict(zip(FIELDS,[s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56),s(57,69),s(70,82),s(83,95),s(96,108),s(109,121),s(122,134),s(135,147),s(148,152),s(153,170),s(171,188),s(189,201),s(202,202),s(203,210),s(211,217),s(218,230),s(231,242),s(243,245)]))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); ap.add_argument("--max-examples",type=int,default=25); a=ap.parse_args()
 counts={n:Counter() for n in KEYS}; variants=defaultdict(lambda:{"tpmerc":set(),"codbdi":set(),"codisi":set(),"dismes":set(),"especi":set()}); dates=defaultdict(set); codes={k:Counter() for k in ("codneg","codisi","tpmerc","codbdi","dismes","especi")}; rows=0
 with zipfile.ZipFile(a.zip) as z:
  members=[x for x in z.namelist() if not x.endswith("/")]
  if len(members)!=1: raise SystemExit(f"ZIP invalido: {members}")
  with z.open(members[0]) as f:
   for raw in f:
    r=parse(raw)
    if not r: continue
    rows+=1
    for c in codes: codes[c][r[c]]+=1
    dates[r["codneg"]].add(r["data_pregao"])
    for c in variants[r["codneg"]]: variants[r["codneg"]][c].add(r[c])
    for n,fs in KEYS.items(): counts[n][tuple(r[x] for x in fs)]+=1
 stats={}
 for n,c in counts.items():
  rep=[v for v in c.values() if v>1]
  stats[n]={"groups":len(c),"unique_groups":sum(v==1 for v in c.values()),"repeated_groups":len(rep),"rows_in_repeated_groups":sum(rep),"max_group_size":max(c.values(),default=0),"rows":rows}
 multi=[{"codneg":cn,"dates":len(dates[cn]),"variants":{k:sorted(v) for k,v in vv.items() if len(v)>1}} for cn,vv in variants.items() if any(len(v)>1 for v in vv)]
 multi.sort(key=lambda x:(-x["dates"],x["codneg"]))
 out={"schema_version":"1.0.0","status":"FASE_07_IDENTIDADE_HISTORICA_1997_ANALISE","raw_file":Path(a.zip).name,"rows":rows,"key_candidates":KEYS,"key_metrics":stats,
 "repeated_key_examples":{n:[{"key":list(k),"count":v} for k,v in sorted(c.items(),key=lambda x:(-x[1],str(x[0]))) if v>1][:a.max_examples] for n,c in counts.items()},
 "codneg_reuse_analysis":{"distinct_codneg":len(dates),"codneg_with_multiple_attribute_values":len(multi),"examples":multi[:a.max_examples]},
 "code_cardinality":{k:len(v) for k,v in codes.items()},
 "governance":["Nenhuma chave candidata e declarada como chave economica definitiva apenas por unicidade.","CODNEG e identificador de negociacao; sua reutilizacao exige contexto temporal e contratual.","CODBDI e TPMERC permanecem atributos classificatorios.","Atributos contratuais como DATVEN, PREEXE, INDOPC, PTOEXE, PRAZOT e ESPECI podem ser materialmente relevantes.","RAW e NORMALIZED nao sao alterados por esta analise."]}
 Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"status":out["status"],"rows":rows,"key_metrics":stats,"distinct_codneg":len(dates)},ensure_ascii=False))
if __name__=="__main__": main()
