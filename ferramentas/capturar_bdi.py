#!/usr/bin/env python3
"""Captura bruta de uma tabela BDI via API POST.

Suporta data explícita ou --date auto, que procura a última data disponível
até sete dias de calendário para trás. Não grava dados antes de validar a resposta.

Uso:
  python ferramentas/capturar_bdi.py --endpoint DailyAverageStocks --date auto
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "dados" / "bdi" / "raw"
MANIFESTS = ROOT / "dados" / "bdi" / "manifests"
BASE = "https://arquivos.b3.com.br/bdi/table"
PAGE_SIZE = 1000


def candidate_dates(requested: str, today: dt.date | None = None) -> list[dt.date]:
    if requested.strip().lower() == "auto":
        today = today or dt.datetime.now(ZoneInfo("America/Sao_Paulo")).date()
        return [today - dt.timedelta(days=offset) for offset in range(1, 8)]
    try:
        return [dt.date.fromisoformat(requested)]
    except ValueError as exc:
        raise ValueError("A data deve estar em YYYY-MM-DD ou ser 'auto'.") from exc


def download(url: str) -> bytes:
    req = Request(
        url,
        data=b"{}",
        method="POST",
        headers={
            "User-Agent": "B3-Dados/1.0",
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    try:
        with urlopen(req, timeout=120) as response:
            return response.read()
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"BDI HTTP {exc.code}: {body[:1000]}") from exc


def parse_response(data: bytes) -> tuple[dict, list, list]:
    if not data:
        raise RuntimeError("Resposta BDI vazia.")
    try:
        payload = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("Resposta BDI não é JSON válido.") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("Resposta BDI não é um objeto JSON.")
    table = payload.get("table") or {}
    if not isinstance(table, dict):
        raise RuntimeError("Resposta BDI sem objeto table.")
    columns = table.get("columns") or []
    values = table.get("values") or []
    if not isinstance(columns, list) or not isinstance(values, list):
        raise RuntimeError("Colunas ou valores BDI têm formato inválido.")
    if not columns or not values:
        raise RuntimeError("A resposta BDI não contém colunas e registos utilizáveis.")
    return payload, columns, values


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", required=True)
    ap.add_argument("--date", required=True, help="YYYY-MM-DD ou auto")
    ap.add_argument("--page", type=int, default=1)
    args = ap.parse_args()
    if args.page < 1:
        raise ValueError("--page deve ser >= 1.")

    dates = candidate_dates(args.date)
    selected_date = None
    data = None
    columns = []
    values = []
    failures = []
    for candidate in dates:
        date_text = candidate.isoformat()
        url = f"{BASE}/{args.endpoint}/{date_text}/{date_text}/{args.page}/{PAGE_SIZE}"
        print(f"BDI_REQUEST={url}")
        try:
            candidate_data = download(url)
            _, candidate_columns, candidate_values = parse_response(candidate_data)
        except (RuntimeError, URLError, TimeoutError, OSError) as exc:
            failures.append(f"{date_text}: {exc.__class__.__name__}")
            print(f"BDI_DATA_UNAVAILABLE={date_text} ({exc.__class__.__name__})")
            if args.date.strip().lower() != "auto":
                raise
            continue
        selected_date = candidate
        data = candidate_data
        columns = candidate_columns
        values = candidate_values
        break

    if selected_date is None or data is None:
        raise RuntimeError("Não foi encontrada uma data BDI válida nos últimos sete dias. " + "; ".join(failures))

    date_text = selected_date.isoformat()
    target = RAW / args.endpoint / date_text
    target.mkdir(parents=True, exist_ok=True)
    path = target / f"page_{args.page:04d}.json"
    path.write_bytes(data)

    url = f"{BASE}/{args.endpoint}/{date_text}/{date_text}/{args.page}/{PAGE_SIZE}"
    manifest = {
        "date": date_text,
        "endpoint": args.endpoint,
        "page": args.page,
        "page_size": PAGE_SIZE,
        "source": "B3 BDI",
        "url": url,
        "file": str(path.relative_to(ROOT)),
        "size_bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "columns": len(columns),
        "records": len(values),
        "captured_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }

    mdir = MANIFESTS / args.endpoint
    mdir.mkdir(parents=True, exist_ok=True)
    (mdir / f"{date_text}_page_{args.page:04d}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
