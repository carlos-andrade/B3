#!/usr/bin/env python3
"""
Esqueleto auditável para ingestão da Pesquisa por Pregão da B3.

ATENÇÃO:
A página pública usa controles dinâmicos para gerar os downloads.
Este módulo NÃO inventa URLs de download. A implementação do endpoint
deve ser preenchida somente após identificar o mecanismo oficial de
download da página.

Fluxo:
1. identificar arquivo e data;
2. obter o download oficial;
3. preservar bytes brutos;
4. SHA-256;
5. validar;
6. gerar manifesto;
7. publicar no repositório.

Uso futuro:
  python ferramentas/importar_pesquisa_pregao.py --arquivo BVBG.086.01 --date 2026-09-22
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "dados" / "market_data" / "raw"
MANIFESTS = ROOT / "dados" / "market_data" / "manifests"

PRIORITARIOS = {
    "BVBG.028.02": "Cadastro de instrumentos",
    "BVBG.029.02": "Cadastro de instrumentos indicadores",
    "BVBG.086.01": "PriceReport",
    "BVBG.087.01": "IndexReport",
    "BVBG.186.01": "Simplified Price Report - Equities",
    "BVBG.187.01": "Simplified Price Report - Derivatives",
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo", required=True)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()

    if args.arquivo not in PRIORITARIOS:
        raise SystemExit(
            f"Arquivo não catalogado como prioritário: {args.arquivo}"
        )

    target = RAW / args.arquivo / args.date
    manifest = MANIFESTS / args.arquivo
    target.mkdir(parents=True, exist_ok=True)
    manifest.mkdir(parents=True, exist_ok=True)

    raise SystemExit(
        "Download endpoint ainda não configurado. "
        "Não foram inventados links nem dados."
    )

if __name__ == "__main__":
    main()
