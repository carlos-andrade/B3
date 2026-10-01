#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

YEAR=1995
BASE=Path("dados/cotahist")
Q=BASE/"quality"
RAW=BASE/"raw/anual/COTAHIST_A1995.ZIP"
NORM=BASE/"normalized/anual/COTAHIST_A1995.csv"
OUT=Q/"COTAHIST_1995_FASE11_CERTIFICACAO_V1.json"

def load(name):
    p=Q/name
    if not p.exists(): raise FileNotFoundError(p)
    return json.loads(p.read_text(encoding="utf-8"))

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

f06=load("COTAHIST_1995_FASE06_SEMANTICA_V1.json")
f07=load("COTAHIST_1995_FASE07_IDENTIDADE_HISTORICA_V1.json")
f08=load("COTAHIST_1995_FASE08_SEMANTICA_K4_V1.json")
f09=load("COTAHIST_1995_FASE09_PRE_RELEASE_V1.json")
f10=load("COTAHIST_1995_FASE10_INTEGRIDADE_V1.json")
manifest=json.loads((BASE/"normalized/manifests/COTAHIST_A1995_quality.json").read_text(encoding="utf-8"))

raw_sha=sha256(RAW); norm_sha=sha256(NORM)
checks={
 "FASE06_validada": f06.get("status")=="VALIDADO" and f06.get("decision")=="LIBERADO_PARA_FASE07",
 "FASE07_analise_concluida": f07.get("status") in {"VALIDADO","FASE_07_IDENTIDADE_HISTORICA_1995_ANALISE"},
 "FASE08_validada": f08.get("status")=="VALIDADO" and f08.get("decision")=="LIBERADO_PARA_FASE09",
 "FASE09_liberada": f09.get("status")=="LIBERADO_PARA_FASE10" and f09.get("decision")=="LIBERADO_PARA_FASE10" and not f09.get("missing") and not f09.get("blocked"),
 "FASE10_validada": f10.get("status")=="VALIDADO" and f10.get("decision")=="FASE_10_CONCLUIDA_E_RELEASE_NORMALIZADO_AUTORIZADO" and not f10.get("failures"),
 "raw_hash_consistente_F10": raw_sha==f10["hashes"]["raw_sha256_actual"]==f10["hashes"]["raw_sha256_manifest"],
 "normalized_hash_consistente_F10": norm_sha==f10["hashes"]["normalized_sha256_actual"]==f10["hashes"]["normalized_sha256_manifest"],
 "manifest_validado": manifest.get("status")=="VALIDADO",
}
failures=[k for k,v in checks.items() if not v]
status="VALIDADO" if not failures else "INVALIDADO"
out={
 "schema_version":"1.0.0","year":YEAR,"phase":"FASE11","status":status,
 "certificacao":"CERTIFICADO_NORMALIZACAO" if not failures else "CERTIFICACAO_BLOQUEADA",
 "decision":f"CERTIFICADO_NORMALIZACAO_{YEAR}" if not failures else f"FASE11_BLOQUEADA_{YEAR}",
 "source_evidence":{
  "FASE06":f06.get("status"),"FASE07":f07.get("status"),
  "FASE08":f08.get("status"),"FASE09":f09.get("status"),"FASE10":f10.get("status")
 },
 "raw_sha256":raw_sha,"normalized_sha256":norm_sha,
 "checks":checks,"failures":failures,
 "note":"Certificação emitida somente após os gates 06-10 passarem. FASE07 é aceita como análise concluída porque seu artefato histórico usa status analítico, enquanto FASE09 registra explicitamente esse tratamento."
}
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,ensure_ascii=False,indent=2))
if failures: raise SystemExit(1)
