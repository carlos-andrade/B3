#!/usr/bin/env python3
import csv, io, json, os, zipfile, hashlib
from collections import Counter, defaultdict
from pathlib import Path

RAW=Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT=Path("dados/cotahist/quality/COTAHIST_1986_FASE08_SEMANTICA_K4_V1.json")

def s(line,a,b): return line[a-1:b]

rows=[]
with zipfile.ZipFile(RAW) as z:
    name=[n for n in z.namelist() if not n.endswith("/")][0]
    with z.open(name) as f:
        for n,raw in enumerate(f,1):
            line=raw.decode("latin-1").rstrip("\r\n")
            if len(line)!=245 or line[:2]!="01": continue
            r={
                "source_line":n,
                "data_pregao":s(line,3,10),
                "codbdi":s(line,11,12),
                "codneg":s(line,13,24).strip(),
                "tpmerc":s(line,25,27),
                "nomres":s(line,28,39).strip(),
                "especi":s(line,40,49).strip(),
                "prazot":s(line,50,52).strip(),
                "modref":s(line,53,56).strip(),
                "preab":s(line,57,69),
                "premax":s(line,70,82),
                "premin":s(line,83,95),
                "premed":s(line,96,108),
                "preult":s(line,109,121),
                "totneg":s(line,148,152),
                "quatot":s(line,153,170),
                "voltot":s(line,171,188),
                "preexe":int(s(line,189,201))/100 if s(line,189,201).strip() else 0.0,
                "indopc":s(line,202,202),
                "datven":s(line,203,210),
                "fatcot":s(line,211,217),
                "ptoexe":int(s(line,218,230))/1000000 if s(line,218,230).strip() else 0.0,
                "codisi":s(line,231,242).strip(),
                "dimes":s(line,243,245).strip(),
            }
            rows.append(r)

target=[r for r in rows if r["data_pregao"]=="19861010" and r["codneg"]=="VGO 2" and r["codbdi"]=="62" and r["tpmerc"]=="030"]
same_codisi=[r for r in rows if r["codisi"]=="VGORACPP"]
same_codneg=[r for r in rows if r["codneg"]=="VGO 2"]
vgor=[r for r in rows if "VGOR" in r["nomres"]]

def ctx(r):
    return {k:r[k] for k in ["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preab","preult","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dimes","source_line"]}

result={
 "schema_version":"1.0.0",
 "status":"FASE_08_SEMANTICA_K4_1986_ANALISE",
 "raw_file":RAW.name,
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "records_type01":len(rows),
 "target_rows":[ctx(r) for r in target],
 "target_count":len(target),
 "same_codisi_count":len(same_codisi),
 "same_codisi_contexts":[ctx(r) for r in same_codisi],
 "same_codneg_count":len(same_codneg),
 "same_codneg_contexts":[ctx(r) for r in same_codneg],
 "vgor_nomres_count":len(vgor),
 "codbdi_62_count":sum(r["codbdi"]=="62" for r in rows),
 "tpmerc_030_count":sum(r["tpmerc"]=="030" for r in rows),
 "semantic_assessment":{
   "CODBDI_62":{"value":"62","interpretation":"MERCADO A TERMO","confidence":"DOCUMENTED_BY_B3_LAYOUT","temporal_caveat":"layout current; historical applicability to 1986 must be treated as corroborative, not exclusive proof"},
   "TPMERC_030":{"value":"030","interpretation":"TERMO","confidence":"DOCUMENTED_BY_B3_LAYOUT","temporal_caveat":"same caveat"},
   "PRAZOT_060":{"value":"060","interpretation":"60-day term field","confidence":"FIELD_SEMANTICS_ONLY","note":"layout defines PRAZOT as term-market period in days; this does not by itself prove contract maturity mechanics in 1986"},
   "DATVEN_99991231":{"value":"99991231","interpretation":"placeholder/non-real date representation","confidence":"INFERRED_FROM_VALUE","note":"requires historical documentation before assigning economic meaning"},
   "CODISI_VGORACPP":{"value":"VGORACPP","interpretation":"1986 internal paper code, not ISIN","confidence":"VALIDATED_IN_PHASE_07D"},
   "DIMES_104":{"value":"104","interpretation":"paper distribution/rights-state sequence field","confidence":"DOCUMENTED_BY_B3_LAYOUT","temporal_caveat":"historical interpretation requires contemporary source"},
   "NOMRES_VGOR":{"value":"VGOR","interpretation":"Vigor short name in the record","confidence":"OBSERVED_IN_RAW"},
   "ESPECI_PP_C05":{"value":"PP *C05","interpretation":"paper specification plus historical notation; exact C05 meaning remains unresolved","confidence":"PARTIAL","note":"contemporary market publication confirms PP/C-code notation exists, but this evidence does not uniquely decode C05 for 1986"},
   "CODNEG_VGO_2":{"value":"VGO 2","interpretation":"historical negotiation code present in a term-market record; exact naming convention unresolved","confidence":"OBSERVED_ONLY"}
 },
 "economic_conclusion":{
   "same_K4_two_rows":True,
   "rows_have_distinct_trade_statistics":True,
   "byte_identical":False,
   "economic_identity_determined":False,
   "most_supported_hypothesis":"two historical records associated with the same contractual identity key but carrying different negotiation aggregates; source semantics are insufficient to decide whether this is a publication artifact, consolidation rule, or distinct historical record class",
   "next_evidence":"contemporary 1986 Bovespa Boletim Diário de Informações / official quotation bulletin and historical market manual"
 }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","output":str(OUT),"target_count":len(target),"same_codisi_count":len(same_codisi),"same_codneg_count":len(same_codneg)},ensure_ascii=False))
