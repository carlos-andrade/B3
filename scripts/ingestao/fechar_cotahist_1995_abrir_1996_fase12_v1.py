#!/usr/bin/env python3
import json
from pathlib import Path

Y=1995; N=1996
B=Path("dados/cotahist"); Q=B/"quality"
def load(p): return json.loads((Q/p).read_text(encoding="utf-8"))
f11=load("COTAHIST_1995_FASE11_CERTIFICACAO_V1.json")
m96=json.loads((B/"normalized/manifests/COTAHIST_A1996_quality.json").read_text(encoding="utf-8"))
checks={
 "fase11_certificada": f11.get("status")=="VALIDADO" and f11.get("certificacao")=="CERTIFICADO_NORMALIZACAO" and f11.get("decision")=="CERTIFICADO_NORMALIZACAO_1995",
 "raw_1996_present": (B/"raw/anual/COTAHIST_A1996.ZIP").exists(),
 "manifest_1996_present": (B/"normalized/manifests/COTAHIST_A1996_quality.json").exists(),
 "manifest_1996_validated": m96.get("status")=="VALIDADO",
 "manifest_1996_parser_1_1_0": m96.get("parser_version")=="1.1.0",
 "manifest_1996_fields_25": m96.get("campos")==25,
 "manifest_1996_dates_valid": m96.get("datas_invalidas")==0 and m96.get("datas_fora_do_ano")==0,
}
failures=[k for k,v in checks.items() if not v]
status="VALIDADO" if not failures else "BLOQUEADO"
out={"schema_version":"1.0.0","phase":"FASE_12","transition":"1995_FECHAMENTO_1996_ABERTURA","year_closed":1995,"year_opened":1996,
"closed":{"status":"FECHADO_E_CERTIFICADO" if not failures else "NAO_CERTIFICADO","phase11_evidence":"dados/cotahist/quality/COTAHIST_1995_FASE11_CERTIFICACAO_V1.json","phase11_status":f11.get("status"),"certification":f11.get("certificacao"),"rows_normalized":104791,"fields":25},
"next_year":{"raw_present":checks["raw_1996_present"],"manifest_present":checks["manifest_1996_present"],"manifest_status":m96.get("status"),"parser_version":m96.get("parser_version"),"rows_normalized":m96.get("linhas_normalized"),"fields":m96.get("campos"),"invalid_dates":m96.get("datas_invalidas"),"dates_outside_year":m96.get("datas_fora_do_ano"),"normalized_release_present":(B/"normalized/anual/COTAHIST_A1996.csv").exists()},
"gate":"FASE_11_1995_REQUIRED_BEFORE_1996_OPENING","checks":checks,"failures":failures,"decision":"1996_ABERTO_SOB_CONTROLE" if not failures else "1996_ABERTURA_BLOQUEADA"}
(Q/"COTAHIST_1995_FASE12_FECHAMENTO_1996_ABERTURA_V1.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=False,indent=2))
if failures: raise SystemExit(1)
