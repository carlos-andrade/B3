#!/usr/bin/env python3
import json, sys
p=sys.argv[1]; out=sys.argv[2]
with open(p,encoding="utf-8") as f: d=json.load(f)
summary={
 "schema_version":"1.0.0",
 "source_schema":d.get("schema_version"),
 "status":d.get("status"),
 "escopo":d.get("escopo"),
 "anos_processados":d.get("anos_processados"),
 "anos_com_erro_estrutural":d.get("anos_com_erro_estrutural"),
 "anos_com_duplicidade_registro_exato":d.get("anos_com_duplicidade_registro_exato"),
 "anos_com_duplicidade_identidade_instrumento":d.get("anos_com_duplicidade_identidade_instrumento"),
 "anos_com_inconsistencia_ohlc":d.get("anos_com_inconsistencia_ohlc"),
 "primeira_data_global":d.get("primeira_data_global"),
 "ultima_data_global":d.get("ultima_data_global"),
 "resumo_por_ano":[
  {
   "ano":r["ano"],"registros_tipo_01_validos":r["registros_tipo_01_validos"],
   "linhas_comprimento_diferente_245":r["linhas_comprimento_diferente_245"],
   "linhas_nao_tipo_01":r["linhas_nao_tipo_01"],
   "datas_unicas":r["datas_unicas"],"primeira_data":r["primeira_data"],"ultima_data":r["ultima_data"],
   "candidatos_intervalo_longo_total":r["candidatos_intervalo_longo_total"],
   "duplicidade_registro_exato_grupos":r["duplicidade_registro_exato_grupos"],
   "duplicidade_registro_exato_excesso_linhas":r["duplicidade_registro_exato_excesso_linhas"],
   "duplicidade_identidade_instrumento_grupos":r["duplicidade_identidade_instrumento_grupos"],
   "duplicidade_identidade_instrumento_excesso_linhas":r["duplicidade_identidade_instrumento_excesso_linhas"],
   "inconsistencias_ohlc":r["inconsistencias_ohlc"]
  } for r in d["por_ano"]
 ]
}
with open(out,"w",encoding="utf-8") as f: json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps({k:summary[k] for k in summary if k!="resumo_por_ano"},ensure_ascii=False,indent=2))
# refresh 2026-09-24T10:26+01:00
