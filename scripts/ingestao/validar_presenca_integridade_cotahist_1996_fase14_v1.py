#!/usr/bin/env python3
import hashlib
import json
import zipfile
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1996.ZIP")
MANIFEST = Path("dados/cotahist/manifests/COTAHIST_A1996.json")
CHECKSUM = Path("dados/cotahist/checksums/COTAHIST_A1996.ZIP.sha256")
EVIDENCE = Path("dados/cotahist/quality/COTAHIST_1996_FASE14_PRESENCA_INTEGRIDADE_V1.json")

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    for p in (RAW, MANIFEST, CHECKSUM):
        if not p.exists():
            raise SystemExit(f"FASE14 BLOQUEADA: arquivo ausente: {p}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = manifest["sha256"]
    actual = sha256(RAW)
    if expected != actual:
        raise SystemExit("FASE14 BLOQUEADA: SHA-256 divergente")

    with zipfile.ZipFile(RAW) as z:
        names = z.namelist()
        if len(names) != 1:
            raise SystemExit(f"FASE14 BLOQUEADA: esperado 1 membro ZIP, encontrado {len(names)}")
        member = names[0]
        payload = z.read(member)

    lines = payload.splitlines()
    if not lines:
        raise SystemExit("FASE14 BLOQUEADA: ZIP sem registros")
    bad = [len(line) for line in lines if len(line) != 245]
    if bad:
        raise SystemExit(f"FASE14 BLOQUEADA: {len(bad)} registros fora de 245 bytes")

    types = sorted({line[:2].decode("latin-1") for line in lines if len(line) == 245})
    required = {"00", "01", "99"}
    if not required.issubset(types):
        raise SystemExit(f"FASE14 BLOQUEADA: tipos estruturais ausentes; observados={types}")

    evidence = {
        "versao": "1.0",
        "fase": "FASE14",
        "ano": 1996,
        "status": "VALIDADO",
        "presenca_raw": True,
        "manifesto_presente": True,
        "checksum_presente": True,
        "sha256_manifesto": expected,
        "sha256_calculado": actual,
        "sha256_coerente": True,
        "zip_membros": len(names),
        "zip_membro": member,
        "bytes_membro": len(payload),
        "registros_245_bytes": len(lines),
        "tipos_registro_observados": types,
        "correction_required": False,
        "correction_applied": False,
        "correction_contract_valid": True,
        "decisao": "LIBERADO_PARA_FASE03_05",
        "regra": "RAW existente; nenhuma nova aquisicao realizada."
    }
    EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
