#!/usr/bin/env python3
"""Captura bruta de uma tabela BDI via API POST.

Uso:
  python ferramentas/capturar_bdi.py --endpoint DailyAverageStocks --date 2026-09-22
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "dados" / "bdi" / "raw"
MANIFESTS = ROOT / "dados" / "bdi" / "manifests"
BASE = "https://arquivos.b3.com.br/bdi/table"
PAGE_SIZE = 1000


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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", required=True)
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--page", type=int, default=1)
    args = ap.parse_args()

    url = (
        f"{BASE}/{args.endpoint}/{args.date}/{args.date}/"
        f"{args.page}/{PAGE_SIZE}"
    )
    data = download(url)
    if not data:
        raise RuntimeError("Resposta BDI vazia.")

    target = RAW / args.endpoint / args.date
    target.mkdir(parents=True, exist_ok=True)
    path = target / f"page_{args.page:04d}.json"
    path.write_bytes(data)

    payload = json.loads(data.decode("utf-8"))
    table = payload.get("table") or {}
    columns = table.get("columns") or []
    values = table.get("values") or []

    manifest = {
        "date": args.date,
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
    }

    mdir = MANIFESTS / args.endpoint
    mdir.mkdir(parents=True, exist_ok=True)
    (mdir / f"{args.date}_page_{args.page:04d}.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
