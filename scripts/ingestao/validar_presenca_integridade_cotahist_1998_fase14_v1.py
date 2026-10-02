#!/usr/bin/env python3
import hashlib, json, zipfile
from pathlib import Path
RAW=Path("dados/cotahist/raw/anual/COTAHIST_A1998.ZIP")
MANIFEST=Path("dados/cotahist/manifests/COTAHIST_A1998.json")
CHECKSUM=Path("dados/cotahist/checksums/COTAHIST_A1998.ZIP.sha256")
EVIDENCE=Path("dados/cotahist/quality/COTAHIST_1998_FASE14_PRESENCA_INTEGRIDADE_V1.json")
def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()
def main():
    for p in (RAW,MANIFEST,CHECKSUM):
        if not p.exists(): raise SystemExit(f"FASE14 BLOQUEADA: ausente {p}")
    m=json.loads(MANIFEST.read_text(encoding="utf-8"))
    actual=sha256(RAW)
    if actual!=m.get("sha256"): raise SystemExit("FASE14 BLOQUEADA: SHA-256 divergente")
    with zipfile.ZipFile(RAW) as z:
        names=z.namelist()
        if len(names)!=1: raise SystemExit(f"FASE14 BLOQUEADA: {len(names)} membros ZIP")
        payload=z.read(names[0])
    lines=payload.splitlines()
    if not lines: raise SystemExit("FASE14 BLOQUEADA: ZIP vazio")
    bad=[len(x) for x in lines if len(x)!=245]
    if bad: raise SystemExit(f"FASE14 BLOQUEADA: {len(bad)} registros fora de 245 bytes")
    types=sorted({x[:2].decode("latin-1") for x in lines})
    if not {"00","01","99"}.issubset(types): raise SystemExit(f"FASE14 BLOQUEADA: tipos incompletos {types}")
    out={"versao":"1.0","fase":"FASE14","ano":1998,"status":"VALIDADO",
      "presenca_raw":True,"manifesto_presente":True,"checksum_presente":True,
      "sha256_manifesto":m["sha256"],"sha256_calculado":actual,"sha256_coerente":True,
      "zip_membros":len(names),"zip_membro":names[0],"bytes_membro":len(payload),
      "registros_245_bytes":len(lines),"tipos_registro_observados":types,
      "correction_required":False,"correction_applied":False,"correction_contract_valid":True,
      "decisao":"LIBERADO_PARA_FASE03_05","regra":"RAW existente; nenhuma nova aquisicao realizada."}
    EVIDENCE.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
