#!/usr/bin/env python3
import json, pathlib
Q=pathlib.Path("dados/cotahist/quality")
raw_sha="b99563d58d2c58ba4c910545fc969041499a45e4e2f6649829a67702193a88ee"
out={
"schema_version":"1.0.0","year":1988,"phase":9,"status":"CLASSIFICACAO_FINAL_EXCECOES_1988_CONCLUIDA","raw_sha256":raw_sha,
"method":"Consolidacao auditavel das excecoes ja evidenciadas; sem correcao retrospectiva e sem reinterpretacao economica.",
"classification":[
{"id":"PRAZOT-1988-001","count":47,"category":"EXCECAO_SEMANTICA_E_INTEGRIDADE_NAO_RESOLVIDA","field":"prazot","status":"ABERTA","evidence":["COTAHIST_1988_AUDITORIA_SEMANTICA_V1.json","COTAHIST_1988_AUDITORIA_INTEGRIDADE_CAMPOS_V1.json"],"action":"Preservar bytes RAW; nao corrigir; reabrir somente com evidencia historica primaria contemporanea ou copia independente byte-a-byte."},
{"id":"OHLC-1988-001","count":3,"lines":[9267,20374,20596],"category":"ANOMALIA_OHLC_ESCALA_INCONSISTENTE","field":"premed","status":"ABERTA","evidence":["COTAHIST_1988_CLASSIFICACAO_OHLC_V1.json","COTAHIST_1988_OHLC_EXCECOES_CONTEXT_V1.json"],"action":"Preservar valor RAW; nao aplicar divisao por 1000; exigir validacao independente/primaria antes de qualquer correcao."},
{"id":"OHLC-1988-002","count":1,"lines":[123264],"category":"ANOMALIA_OHLC_ORDEM_INCONSISTENTE","field":"preult","status":"ABERTA","evidence":["COTAHIST_1988_CLASSIFICACAO_OHLC_V1.json","COTAHIST_1988_OHLC_EXCECOES_CONTEXT_V1.json"],"action":"Preservar valor RAW; nao corrigir PREULT para PREMAX sem evidencia."},
{"id":"CAL-1988-001","count":13,"dates":["1988-01-25","1988-02-15","1988-02-16","1988-02-17","1988-03-31","1988-04-01","1988-04-18","1988-05-13","1988-05-30","1988-09-07","1988-10-10","1988-10-31","1988-11-15"],"category":"CANDIDATO_DIA_SEM_PREGAO_NAO_CLASSIFICADO","field":"data_pregao","status":"ABERTA","evidence":["COTAHIST_1988_AUDITORIA_CALENDARIO_V1.json"],"action":"Nao classificar como feriado/dia sem pregao sem fonte historica primaria."}],
"deduplication":{"prazot_control_bytes_are_same_47_records":True,"exceptions_are_not_double_counted":True,"unique_exception_classes":4},
"counts":{"prazot":47,"ohlc_premed":3,"ohlc_order":1,"calendar_candidates":13},
"governance":{"raw_immutable":True,"no_correction":True,"no_semantic_reinterpretation":True,"economic_release":False,"fail_closed":True},
"gates":{"all_known_exceptions_classified":True,"evidence_pointer_for_each_class":True,"unresolved_items_preserved":True,"release_to_phase_10":True},
"next_gate":"VALIDACAO_INDEPENDENTE_COTAHIST_1988"}
(Q/"COTAHIST_1988_CLASSIFICACAO_FINAL_EXCECOES_V1.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"
")
print("PHASE9_CLASSIFICATION_OK")
