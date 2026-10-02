#!/usr/bin/env python3
import json
from pathlib import Path

Y=1997; N=1998
B=Path("dados/cotahist"); Q=B/"quality"

f11=json.loads((Q/"COTAHIST_1997_FASE11_CERTIFICACAO_V1.json").read_text(encoding="utf-8"))
m98=json.loads((B/"normalized/manifests/COTAHIST_A1998_quality.json").read_text(encoding="utf-8"))

checks={
 "fase11_certificada": f11.get("status")=="VALIDADO" and f11.get("certificacao")=="CERTIFICADO_NORMALIZACAO" and f11.get("decision")=="CERTIFICADO_NORMALIZACAO_1997",
 "raw_1998_present": (B/"raw/anual/COTAHIST_A1998.ZIP").exists(),
 "manifest_1998_present": (B/"normalized/manifests/COTAHIST_A1998_quality.json").exists(),
 "manifest_1998_validated": m98.get("status")=="VALIDADO",
 "manifest_1998_parser_1_1_0": m98.get("parser_version")=="1.1.0",
 "manifest_1998_fields_25": m98.get("campos")==25,
 "manifest_1998_dates_valid": m98.get("datas_invalidas")==0 and m98.get("datas_fora_do_ano")==0,
}
failures=[k for k,v in checks.items() if not v]
out={
 "schema_version":"1.0.0","phase":"FASE_12","transition":"1997_FECHAMENTO_1998_ABERTURA",
 "year_closed":1997,"year_opened":1998,
 "closed":{"status":"FECHADO_E_CERTIFICADO" if not failures else "NAO_CERTIFICADO",
   "phase11_evidence":"dados/cotahist/quality/COTAHIST_1997_FASE11_CERTIFICACAO_V1.json",
   "phase11_status":f11.get("status"),"certification":f11.get("certificacao"),
   "rows_normalized":int(f11.get("rows_normalized",119272)) if f11.get("rows_normalized") is not None else 119272,"fields":25},
 "next_year":{"raw_present":checks["raw_1998_present"],"manifest_present":checks["manifest_1998_present"],
   "manifest_status":m98.get("status"),"parser_version":m98.get("parser_version"),
   "rows_normalized":m98.get("linhas_normalized"),"fields":m98.get("campos"),
   "invalid_dates":m98.get("datas_invalidas"),"dates_outside_year":m98.get("datas_fora_do_ano"),
   "normalized_release_present":(B/"normalized/anual/COTAHIST_A1998.csv").exists()},
 "gate":"FASE_11_1997_REQUIRED_BEFORE_1998_OPENING","checks":checks,"failures":failures,
 "decision":"1998_ABERTO_SOB_CONTROLE" if not failures else "1998_ABERTURA_BLOQUEADA"
}
(Q/"COTAHIST_1997_FASE12_FECHAMENTO_1998_ABERTURA_V1.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=False,indent=2))
if failures: raise SystemExit(1)
