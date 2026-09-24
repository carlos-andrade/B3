#!/usr/bin/env python3
"""FASE 07C — Semântica histórica do CODBDI no COTAHIST 1986."""
from __future__ import annotations
import argparse,json,zipfile
from collections import Counter,defaultdict
from datetime import datetime

CODBDI_B3={
"02":"LOTE PADRÃO","05":"SANCIONADAS PELOS REGULAMENTOS BM&FBOVESPA","06":"CONCORDATÁRIAS",
"07":"RECUPERAÇÃO EXTRAJUDICIAL","08":"RECUPERAÇÃO JUDICIAL","09":"RAET - REGIME DE ADMINISTRAÇÃO ESPECIAL TEMPORÁRIA",
"10":"DIREITOS E RECIBOS","11":"INTERVENÇÃO","12":"FUNDOS IMOBILIÁRIOS","14":"CERT.INVEST/TIT.DIV.PUBLICA",
"18":"OBRIGAÇÕES","22":"BÔNUS (PRIVADOS)","26":"APÓLICES/BÔNUS/TÍTULOS PÚBLICOS",
"32":"EXERCÍCIO DE OPÇÕES DE COMPRA DE ÍNDICES","33":"EXERCÍCIO DE OPÇÕES DE VENDA DE ÍNDICES",
"38":"EXERCÍCIO DE OPÇÕES DE COMPRA","42":"EXERCÍCIO DE OPÇÕES DE VENDA","46":"LEILÃO DE NÃO COTADOS",
"48":"LEILÃO DE PRIVATIZAÇÃO","49":"LEILÃO DO FUNDO RECUPERAÇÃO ECONÔMICA ESPÍRITO SANTO",
"50":"LEILÃO","51":"LEILÃO FINOR","52":"LEILÃO FINAM","53":"LEILÃO FISET","54":"LEILÃO DE AÇÕES EM MORA",
"56":"VENDAS POR ALVARÁ JUDICIAL","58":"OUTROS","60":"PERMUTA POR AÇÕES","61":"META","62":"MERCADO A TERMO",
"66":"DEBÊNTURES COM DATA DE VENCIMENTO ATÉ 3 ANOS","68":"DEBÊNTURES COM DATA DE VENCIMENTO MAIOR QUE 3 ANOS",
"70":"FUTURO COM RETENÇÃO DE GANHOS","71":"MERCADO DE FUTURO","74":"OPÇÕES DE COMPRA DE ÍNDICES",
"75":"OPÇÕES DE VENDA DE ÍNDICES","78":"OPÇÕES DE COMPRA","82":"OPÇÕES DE VENDA","83":"BOVESPAFIX","84":"SOMA FIX"
}
def parse(raw):
 b=raw.rstrip(b"\r\n")
 if len(b)!=245 or b[:2]!=b"01": return None
 def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
 return {"data_pregao":s(3,10),"codbdi":s(11,12),"codneg":s(13,24),"tpmerc":s(25,27)}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
 counts=Counter(); dates=defaultdict(set); codneg=defaultdict(set); tpmerc=defaultdict(Counter); rows=0
 with zipfile.ZipFile(a.zip) as z:
  members=[x for x in z.namelist() if not x.endswith("/")]
  if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
  with z.open(members[0]) as f:
   for raw in f:
    r=parse(raw)
    if not r: continue
    rows+=1; c=r["codbdi"]; counts[c]+=1; dates[c].add(r["data_pregao"]); codneg[c].add(r["codneg"]); tpmerc[c][r["tpmerc"]]+=1
 observed=sorted(counts); unknown=[c for c in observed if c not in CODBDI_B3]
 result={"schema_version":"1.0.0","status":"FASE_07C_CODBDI_1986_ANALISE","generated_at_utc":datetime.utcnow().replace(microsecond=0).isoformat()+"Z","raw_file":"COTAHIST_A1986.ZIP","rows":rows,
 "source_document":{"institution":"B3","document":"LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS","revision":"02","date":"2020-10-05","field":"CODBDI","positions":"11-12","source_url":"https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf"},
 "mapping_basis":"Tabela de CODBDI do layout oficial B3; a documentação posterior não prova isoladamente a semântica em 1986.",
 "observed_codes":{c:{"rows":counts[c],"trading_dates":len(dates[c]),"distinct_codneg":len(codneg[c]),"description_b3_layout":CODBDI_B3.get(c),"mapping_status":"DOCUMENTADO_NO_LAYOUT_B3" if c in CODBDI_B3 else "NAO_MAPEADO","tpmerc_distribution":dict(sorted(tpmerc[c].items()))} for c in observed},
 "unknown_codes":unknown,"coverage":{"observed_code_count":len(observed),"documented_code_count":sum(c in CODBDI_B3 for c in observed),"unknown_code_count":len(unknown),"all_observed_codes_documented":not unknown},
 "governance":{"raw_unchanged":True,"normalized_unchanged":True,"economic_identity_not_inferred_from_codbdi":True,"historical_semantics_1986_requires_temporal_validation":True}}
 with open(a.output,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2); f.write("\n")
if __name__=="__main__": main()
