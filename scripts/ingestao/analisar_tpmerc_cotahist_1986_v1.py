#!/usr/bin/env python3
"""FASE 07B — Semântica histórica do TPMERC no COTAHIST 1986."""
from __future__ import annotations
import argparse, json, zipfile
from collections import Counter, defaultdict
from datetime import datetime
TPMERC_B3_2017={"010":"VISTA","012":"EXERCÍCIO DE OPÇÕES DE COMPRA","013":"EXERCÍCIO DE OPÇÕES DE VENDA","017":"LEILÃO","020":"FRACIONÁRIO","030":"TERMO","050":"FUTURO COM RETENÇÃO DE GANHO","060":"FUTURO COM MOVIMENTAÇÃO CONTÍNUA","070":"OPÇÕES DE COMPRA","080":"OPÇÕES DE VENDA"}
def parse(raw):
    b=raw.rstrip(b"\r\n")
    if len(b)!=245 or b[:2]!=b"01": return None
    def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
    return {"data_pregao":s(3,10),"codbdi":s(11,12),"codneg":s(13,24),"tpmerc":s(25,27)}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    counts=Counter(); dates=defaultdict(set); codneg=defaultdict(set); rows=0
    with zipfile.ZipFile(a.zip) as z:
        members=[x for x in z.namelist() if not x.endswith("/")];
        if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                r=parse(raw)
                if not r: continue
                rows+=1; c=r["tpmerc"]; counts[c]+=1; dates[c].add(r["data_pregao"]); codneg[c].add(r["codneg"])
    observed=sorted(counts); unknown=[c for c in observed if c not in TPMERC_B3_2017]
    result={"schema_version":"1.0.0","status":"FASE_07B_TPMERC_1986_ANALISE","generated_at_utc":datetime.utcnow().replace(microsecond=0).isoformat()+"Z","raw_file":"COTAHIST_A1986.ZIP","rows":rows,
      "source_document":{"institution":"B3","document":"LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS","revision":"01","date":"2017-04-13","source_url":"https://www.b3.com.br/data/files/C8/F3/08/B4/297BE410F816C9E492D828A8/SeriesHistoricas_Layout.pdf","field":"TPMERC","positions":"25-27"},
      "mapping_basis":"Tabela de TPMERC do layout oficial B3 consultado; não presume retroatividade histórica além da evidência documental.",
      "observed_codes":{c:{"rows":counts[c],"trading_dates":len(dates[c]),"distinct_codneg":len(codneg[c]),"description_b3_2017":TPMERC_B3_2017.get(c),"mapping_status":"DOCUMENTADO_NO_LAYOUT_B3_2017" if c in TPMERC_B3_2017 else "NAO_MAPEADO"} for c in observed},
      "unknown_codes":unknown,"coverage":{"observed_code_count":len(observed),"documented_code_count":sum(c in TPMERC_B3_2017 for c in observed),"unknown_code_count":len(unknown),"all_observed_codes_documented":not unknown},
      "governance":{"raw_unchanged":True,"normalized_unchanged":True,"economic_identity_not_inferred_from_tpmerc":True,"historical_semantics_1986_requires_temporal_validation":True}}
    with open(a.output,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2); f.write("\n")
if __name__=="__main__": main()