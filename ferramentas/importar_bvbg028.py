#!/usr/bin/env python3
"""
Importador auditável do Cadastro de Instrumentos (Listado) da B3.

Fonte B3:
  https://arquivos.b3.com.br/api/download/requestname
  fileName=InstrumentsConsolidated
  date=YYYY-MM-DD

Fluxo:
1. Solicita o token de download.
2. Baixa o CSV completo.
3. Preserva o bruto.
4. Detecta cabeçalho e separador.
5. Gera inventário normalizado.
6. Gera diretórios individuais por TckrSymb, sem alterar o bruto.

Uso:
  python ferramentas/importar_bvbg028.py --date 2026-09-21
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://arquivos.b3.com.br/api/download/"
REQUESTNAME = "https://arquivos.b3.com.br/api/download/requestname"

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "ativos" / "catalogo" / "fontes" / "bruto"
CATALOG = ROOT / "ativos" / "catalogo" / "inventario"
ASSET_ROOT = ROOT / "ativos" / "instrumentos"


def get_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "B3-Catalogo/1.0"})
    with urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def get_bytes(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "B3-Catalogo/1.0"})
    with urlopen(req, timeout=120) as r:
        return r.read()


def safe_name(value: str) -> str:
    value = value.strip().upper()
    value = re.sub(r"[^A-Z0-9._-]+", "_", value)
    return value[:120] or "SEM_CODIGO"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def find_header(lines: list[str]) -> int:
    for i, line in enumerate(lines):
        if "TckrSymb" in line or "Tckr" in line:
            return i
    raise RuntimeError("Cabeçalho do cadastro não localizado.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Data YYYY-MM-DD")
    args = ap.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    CATALOG.mkdir(parents=True, exist_ok=True)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)

    params = urlencode({"fileName": "InstrumentsConsolidated", "date": args.date})
    request_info = get_json(f"{REQUESTNAME}?{params}")

    token = request_info.get("token")
    if not token:
        raise RuntimeError(f"Token não retornado pela B3: {request_info}")

    data = get_bytes(f"{BASE}?token={token}")
    digest = sha256(data)

    raw_path = RAW / f"InstrumentsConsolidated_{args.date}.csv"
    raw_path.write_bytes(data)

    text = data.decode("latin-1")
    lines = text.splitlines()
    header_idx = find_header(lines)
    delimiter = ";" if ";" in lines[header_idx] else ","

    rows = list(csv.DictReader(lines[header_idx:], delimiter=delimiter))
    inventory_path = CATALOG / f"INVENTARIO_B3_{args.date}.csv"

    if rows:
        fields = list(rows[0].keys())
        with inventory_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=";", extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    manifest = {
        "date": args.date,
        "source": "B3 BVBG.028.02 / InstrumentsConsolidated",
        "rows": len(rows),
        "sha256": digest,
        "raw_file": str(raw_path.relative_to(ROOT)),
        "inventory_file": str(inventory_path.relative_to(ROOT)),
    }
    (CATALOG / f"MANIFEST_{args.date}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    created = 0
    for row in rows:
        ticker = row.get("TckrSymb") or row.get("Ticker") or ""
        if not ticker.strip():
            continue
        folder = ASSET_ROOT / safe_name(ticker)
        folder.mkdir(parents=True, exist_ok=True)
        readme = folder / "README.md"
        if not readme.exists():
            readme.write_text(
                "# " + ticker.strip() + "\n\n"
                f"**Data de referência:** {args.date}\n"
                "**Fonte:** B3 — Cadastro de Instrumentos (Listado), BVBG.028.02\n\n"
                "Este diretório foi gerado automaticamente a partir do cadastro oficial. "
                "Os campos completos permanecem no inventário consolidado.\n",
                encoding="utf-8",
            )
            created += 1

    print(json.dumps({
        "date": args.date,
        "rows": len(rows),
        "directories_created": created,
        "sha256": digest,
        "raw": str(raw_path),
        "inventory": str(inventory_path),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
