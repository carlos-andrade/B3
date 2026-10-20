#!/usr/bin/env python3
"""Captura diária de PTAX (EUR e USD) via API OData oficial do BCB, sob ODbL.

Preserva resposta JSON RAW e manifesto com URL, período, bytes e SHA-256.
Não promove os dados a NORMALIZED/CERTIFIED.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"
RAW_ROOT = ROOT / "dados/cambio/ptax/raw"
MANIFEST_ROOT = ROOT / "dados/cambio/ptax/manifests"
CURRENCIES = ("EUR", "USD")
REQUIRED_FIELDS = {"dataHoraCotacao", "cotacaoCompra", "cotacaoVenda"}
MAX_BYTES = 15 * 1024 * 1024


class PtaxError(RuntimeError):
    pass


def build_url(currency: str, start: date, end: date) -> str:
    if currency not in CURRENCIES:
        raise PtaxError(f"Moeda não permitida: {currency}")
    if end < start or (end - start).days > 45:
        raise PtaxError("Período inválido; intervalo máximo de 45 dias.")
    # OData PTAX documentado pelo BCB: datas no formato MM-DD-YYYY.
    start_text = start.strftime("%m-%d-%Y")
    end_text = end.strftime("%m-%d-%Y")
    query = urllib.parse.urlencode({
        "@moeda": f"'{currency}'",
        "@dataInicial": f"'{start_text}'",
        "@dataFinalCotacao": f"'{end_text}'",
        "$top": "10000",
        "$format": "json",
    })
    return (
        f"{BASE}/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,"
        f"dataFinalCotacao=@dataFinalCotacao)?{query}"
    )


def get_payload(url: str) -> tuple[bytes, dict]:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != "olinda.bcb.gov.br":
        raise PtaxError("Endpoint fora do domínio oficial OData BCB.")
    request = urllib.request.Request(
        url, headers={"User-Agent": "B3-PublicData-Ingestion/1.0", "Accept": "application/json"}
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read(MAX_BYTES + 1)
    except (urllib.error.URLError, TimeoutError) as exc:
        raise PtaxError(f"Falha de transporte na API PTAX: {exc}") from exc
    if not raw:
        raise PtaxError("Resposta PTAX vazia.")
    if len(raw) > MAX_BYTES:
        raise PtaxError("Resposta PTAX excedeu o limite de segurança de 15 MiB.")
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PtaxError("Resposta PTAX não é JSON UTF-8 válido.") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("value"), list):
        raise PtaxError("Resposta PTAX sem a lista 'value'.")
    rows = payload["value"]
    if not rows:
        raise PtaxError("Resposta PTAX sem observações para o período.")
    if not all(isinstance(row, dict) for row in rows):
        raise PtaxError("Resposta PTAX contém registos com formato inválido.")
    missing = REQUIRED_FIELDS - set(rows[0])
    if missing:
        raise PtaxError(f"Campos obrigatórios ausentes: {sorted(missing)}")
    return raw, payload


def ingest(currency: str, start: date, end: date) -> dict:
    url = build_url(currency, start, end)
    raw, payload = get_payload(url)
    digest = hashlib.sha256(raw).hexdigest()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    RAW_ROOT.mkdir(parents=True, exist_ok=True)
    MANIFEST_ROOT.mkdir(parents=True, exist_ok=True)
    raw_path = RAW_ROOT / f"PTAX_{currency}_{start.isoformat()}_{end.isoformat()}_{stamp}.json"
    raw_path.write_bytes(raw)
    manifest = {
        "schema_version": "1.0.0",
        "source": "BCB Dados Abertos / PTAX OData",
        "dataset_url": "https://dadosabertos.bcb.gov.br/dataset/taxas-de-cambio-todos-os-boletins-diarios",
        "endpoint": url,
        "license": "Open Data Commons Open Database License (ODbL)",
        "currency": currency,
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "observations": len(payload["value"]),
        "bytes": len(raw),
        "sha256": digest,
        "raw_path": str(raw_path.relative_to(ROOT)),
        "validation": {
            "official_https_endpoint": True,
            "json_schema_minimum": "PASS",
            "observations_nonempty": True,
            "normalized": False,
            "certified": False,
        },
    }
    manifest_path = MANIFEST_ROOT / f"PTAX_{currency}_{end.isoformat()}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "currency": currency,
        "observations": len(payload["value"]),
        "bytes": len(raw),
        "sha256": digest,
        "raw_path": str(raw_path.relative_to(ROOT)),
        "manifest_path": str(manifest_path.relative_to(ROOT)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--end-date", default=date.today().isoformat(), help="Data final YYYY-MM-DD")
    parser.add_argument("--lookback-days", type=int, default=30)
    args = parser.parse_args()
    try:
        end = date.fromisoformat(args.end_date)
        if not 1 <= args.lookback_days <= 45:
            raise PtaxError("--lookback-days deve estar entre 1 e 45.")
        start = end - timedelta(days=args.lookback_days - 1)
        results = [ingest(currency, start, end) for currency in CURRENCIES]
    except (ValueError, PtaxError, OSError) as exc:
        print(json.dumps({"status": "ERROR", "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps({"status": "CAPTURED", "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
