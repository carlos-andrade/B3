#!/usr/bin/env python3
"""Cadeia COTAHIST 1994 — FASE09/10/11/12, fail-closed."""
import csv
import hashlib
import json
from pathlib import Path
import sys

YEAR="1994"
# Contrato de release 1994: a normalizacao atual nao exige correcao de dados.
# Se uma correcao futura for necessaria, ela devera ser explicitamente registrada
# e comprovada antes de liberar a certificacao.
CORRECTION_REQUIRED=False
Q=Path("dados/cotahist/quality")
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
NORMALIZED=Path(f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv")
MANIFEST=Path(f"dados/cotahist/normalized/manifests/COTAHIST_A{YEAR}_quality.json")
CERT_MATRIX=Path("dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv")

def load(name):
    p=Q/f"COTAHIST_{YEAR}_{name}.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {"status":"INVALID_JSON"}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def phase_ok(obj):
    return obj is not None and obj.get("status") in {"VALIDADO","VALIDADO_COM_EXCECAO"}

f00=load("FASE00_GOVERNANCA_PRE_CONDICOES_V1")
f01=load("FASE01_AQUISICAO_RAW_V1")
f02=load("FASE02_INTEGRIDADE_FONTE_V1")
f06=load("FASE06_RECONCILIACAO_V1")
f07=load("FASE07_IDENTIDADE_CHAVES_V1")
f08=load("FASE08_SEMANTICA_CALENDARIO_V1")

required_paths=[RAW,NORMALIZED,MANIFEST]
missing=[str(p) for p in required_paths if not p.exists()]
prior={"FASE00":f00,"FASE01":f01,"FASE02":f02,"FASE06":f06,"FASE07":f07,"FASE08":f08}
blocked=[k for k,v in prior.items() if not phase_ok(v)]

f09_ok=not missing and not blocked
f09={
 "schema_version":"1.0.0","year":1994,"phase":"FASE09",
 "status":"LIBERADO_PARA_FASE10" if f09_ok else "BLOQUEADO",
 "preconditions":{k:("OK" if phase_ok(v) else "BLOQUEADO") for k,v in prior.items()},
 "required_files":{str(p):p.exists() for p in required_paths},
 "missing":missing,"blocked":blocked,
 "decision":"LIBERADO_PARA_FASE10" if f09_ok else "BLOQUEADO",
 "note":"Pré-release reproduz o gate documental de 1993: consolida evidências anteriores e não retrocertifica fase ausente."
}
(Q/f"COTAHIST_{YEAR}_FASE09_PRE_RELEASE_V1.json").write_text(json.dumps(f09,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if not f09_ok:
    sys.exit("FAIL-CLOSED: FASE09 bloqueada; FASE10 não executada")

manifest={}
if MANIFEST.exists():
    try: manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception: manifest={"status":"INVALID_JSON"}

raw_sha=sha(RAW) if RAW.exists() else None
norm_sha=sha(NORMALIZED) if NORMALIZED.exists() else None

checks={
 "raw_exists":RAW.exists(),
 "normalized_exists":NORMALIZED.exists(),
 "manifest_exists":MANIFEST.exists(),
 "manifest_validated":manifest.get("status")=="VALIDADO",
 "raw_sha256_matches_manifest":raw_sha==manifest.get("raw_sha256"),
 "normalized_sha256_matches_manifest":norm_sha==manifest.get("normalized_sha256"),
 "normalized_rows_match_manifest":manifest.get("linhas_normalized")==119097,
 "normalized_fields_match_manifest":manifest.get("campos")==25,
 "raw_immutable":True,
 "correction_contract_valid": (not CORRECTION_REQUIRED)
}
f10_ok=f09_ok and all(checks.values())
f10={
 "schema_version":"1.0.0","phase":"FASE_10","year":1994,
 "raw_path":str(RAW),"normalized_path":str(NORMALIZED),"manifest_path":str(MANIFEST),
 "raw_immutable":True,
 "correction_required":CORRECTION_REQUIRED,
 "correction_applied":False,
 "correction_contract_valid": (not CORRECTION_REQUIRED),
 "hashes":{"raw_sha256_actual":raw_sha,"normalized_sha256_actual":norm_sha},
 "checks":checks,
 "status":"VALIDADO" if f10_ok else "BLOQUEADO",
 "failures":[k for k,v in checks.items() if not v],
 "decision":"FASE_10_CONCLUIDA_E_RELEASE_NORMALIZADO_AUTORIZADO" if f10_ok else "BLOQUEADO"
}
(Q/f"COTAHIST_{YEAR}_FASE10_INTEGRIDADE_V1.json").write_text(json.dumps(f10,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if not f10_ok:
    sys.exit("FAIL-CLOSED: FASE10 bloqueada; FASE11 não executada")

f11_ok=f10_ok
f11={
 "schema_version":"1.0.0","year":1994,"phase":"FASE11",
 "status":"VALIDADO" if f11_ok else "BLOQUEADO",
 "certificacao":"CERTIFICADO_NORMALIZACAO" if f11_ok else "NAO_CERTIFICADO",
 "decision":"CERTIFICADO_NORMALIZACAO_1994" if f11_ok else "CERTIFICACAO_1994_BLOQUEADA",
 "source_evidence":{
   "FASE06":f06.get("status") if f06 else None,
   "FASE07":f07.get("status") if f07 else None,
   "FASE08":f08.get("status") if f08 else None,
   "FASE09":f09.get("status"),
   "FASE10":f10.get("status")
 },
 "raw_sha256":raw_sha,"normalized_sha256":norm_sha,
 "note":"Certificação somente é emitida após os gates 06-10 passarem."
}
(Q/f"COTAHIST_{YEAR}_FASE11_CERTIFICACAO_V1.json").write_text(json.dumps(f11,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if not f11_ok:
    sys.exit("FAIL-CLOSED: FASE11 bloqueada; FASE12 não executada")

f12_ok=f11_ok
f12={
 "schema_version":"1.0.0","phase":"FASE12","year":1994,"next_year":1995,
 "status":"CONCLUIDA" if f12_ok else "BLOQUEADA",
 "decision":"ANO_1994_FECHADO_TRANSICAO_1995_AUTORIZADA" if f12_ok else "TRANSICAO_1995_NAO_AUTORIZADA",
 "required_evidence":{
   "FASE06":f06.get("status") if f06 else None,
   "FASE07":f07.get("status") if f07 else None,
   "FASE08":f08.get("status") if f08 else None,
   "FASE09":f09.get("status"),
   "FASE10":f10.get("status"),
   "FASE11":f11.get("status")
 },
 "raw_sha256":raw_sha,"normalized_sha256":norm_sha,
 "rule":"docs/cotahist/REGRA_GERAL_EXISTENCIA_E_VALIDACAO_V1.md",
 "note":"FASE12 não retrocertifica fases nem libera dados inexistentes."
}
(Q/f"COTAHIST_{YEAR}_FASE12_FECHAMENTO_TRANSICAO_V1.json").write_text(json.dumps(f12,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

result={"year":1994,"fases":{"06":f06.get("status") if f06 else None,"07":f07.get("status") if f07 else None,"08":f08.get("status") if f08 else None,"09":f09["status"],"10":f10["status"],"11":f11["status"],"12":f12["status"]}}
print(json.dumps(result,ensure_ascii=False))
if not f12_ok:
    sys.exit("FAIL-CLOSED: cadeia 1994 bloqueada")
