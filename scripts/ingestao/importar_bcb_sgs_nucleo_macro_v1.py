#!/usr/bin/env python3
"""Ingestão auditável de séries BCB/SGS.

- Consulta a API oficial BCData/SGS em janelas inferiores a 10 anos.
- Persiste cada resposta RAW antes da normalização.
- Consolida NORMALIZED CSV por série.
- Gera manifesto com hashes, contagens, datas e testes de qualidade.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import time
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

BASE_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"
ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = ROOT / "dados" / "bcb_sgs" / "raw"
NORM_ROOT = ROOT / "dados" / "bcb_sgs" / "normalized"
MANIFEST_ROOT = ROOT / "dados" / "bcb_sgs" / "manifests"

SERIES = {
    432: {"nome": "Meta Selic definida pelo Copom", "inicio": "1999-03-05", "frequencia": "D", "allow_future": True},
    11: {"nome": "Taxa Selic efetiva", "inicio": "1986-06-04", "frequencia": "D", "allow_future": False},
    12: {"nome": "CDI", "inicio": "1986-03-06", "frequencia": "D", "allow_future": False},
    1: {"nome": "Dólar americano venda", "inicio": "1984-11-28", "frequencia": "D", "allow_future": False},
    433: {"nome": "IPCA", "inicio": "1980-01-01", "frequencia": "M", "allow_future": False},
}

CHUNK_DAYS = 365 * 9 + 364
TIMEOUT = 90


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def parse_date_br(value: str) -> date:
    return datetime.strptime(value, "%d/%m/%Y").date()


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "B3-BancoCentral-Ingestao/1.0"})
    last_error = None
    for attempt in range(4):
        try:
            with urlopen(req, timeout=TIMEOUT) as response:
                return response.read()
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < 3:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Falha API BCB após 4 tentativas: {last_error}")


def chunks(start: date, end: date):
    current = start
    while current <= end:
        chunk_end = min(current + timedelta(days=CHUNK_DAYS), end)
        yield current, chunk_end
        current = chunk_end + timedelta(days=1)


def validate_records(records: list[dict], code: int, allow_future: bool, capture_date: date):
    seen = set()
    invalid_dates = 0
    invalid_values = 0
    duplicates = 0
    future = 0
    normalized = []

    for row in records:
        raw_date = str(row.get("data", "")).strip()
        raw_value = str(row.get("valor", "")).strip()
        try:
            d = parse_date_br(raw_date)
            iso = d.isoformat()
        except Exception:
            invalid_dates += 1
            continue

        try:
            if raw_value.upper() in {"", "NULL", "NA", "N/A"}:
                value = None
            else:
                value = str(Decimal(raw_value.replace(",", ".")))
        except InvalidOperation:
            invalid_values += 1
            continue

        key = iso
        if key in seen:
            duplicates += 1
        seen.add(key)

        if d > capture_date:
            future += 1
            if not allow_future:
                # Future observations are retained for forensic evidence but flagged.
                pass

        normalized.append((iso, value))

    normalized.sort(key=lambda x: x[0])
    return normalized, {
        "datas_invalidas": invalid_dates,
        "valores_invalidos": invalid_values,
        "duplicidades": duplicates,
        "datas_futuras": future,
    }


def main():
    capture_dt = datetime.now(ZoneInfo("America/Sao_Paulo"))
    capture_date = capture_dt.date()
    stamp = capture_dt.strftime("%Y%m%dT%H%M%S%z")
    run_manifests = []

    for code, meta in SERIES.items():
        raw_dir = RAW_ROOT / str(code)
        norm_dir = NORM_ROOT
        manifest_dir = MANIFEST_ROOT
        raw_dir.mkdir(parents=True, exist_ok=True)
        norm_dir.mkdir(parents=True, exist_ok=True)
        manifest_dir.mkdir(parents=True, exist_ok=True)

        start = date.fromisoformat(meta["inicio"])
        end = capture_date
        all_records = []
        chunks_meta = []

        for idx, (chunk_start, chunk_end) in enumerate(chunks(start, end), start=1):
            params = urlencode({
                "formato": "json",
                "dataInicial": chunk_start.strftime("%d/%m/%Y"),
                "dataFinal": chunk_end.strftime("%d/%m/%Y"),
            })
            url = BASE_URL.format(codigo=code) + "?" + params
            payload = fetch(url)

            raw_path = raw_dir / f"SGS_{code}_{chunk_start.isoformat()}_{chunk_end.isoformat()}.json"
            raw_path.write_bytes(payload)

            parsed = json.loads(payload.decode("utf-8"))
            if not isinstance(parsed, list):
                raise RuntimeError(f"Resposta inesperada para SGS {code}: não é lista")

            all_records.extend(parsed)
            chunks_meta.append({
                "chunk": idx,
                "data_inicial": chunk_start.isoformat(),
                "data_final": chunk_end.isoformat(),
                "raw_file": str(raw_path.relative_to(ROOT)),
                "raw_sha256": sha256_file(raw_path),
                "raw_bytes": raw_path.stat().st_size,
                "records_api": len(parsed),
            })

        normalized, quality = validate_records(
            all_records, code, meta["allow_future"], capture_date
        )

        # Regra fail-closed: datas futuras são rejeitadas para séries sem calendário futuro autorizado.
        if quality["datas_futuras"] > 0 and not meta["allow_future"]:
            quality["future_rejected"] = True
        else:
            quality["future_rejected"] = False

        norm_path = norm_dir / f"SGS_{code}.csv"
        with norm_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["codigo_sgs", "data", "valor"])
            for d, value in normalized:
                writer.writerow([code, d, "" if value is None else value])

        dates = [x[0] for x in normalized]
        manifest = {
            "schema_version": "1.0.0",
            "status": "VALIDADO" if quality["datas_invalidas"] == 0 and quality["valores_invalidos"] == 0 and quality["duplicidades"] == 0 and not quality["future_rejected"] else "REJEITADO",
            "source": "Banco Central do Brasil - BCData/SGS",
            "codigo_sgs": code,
            "nome": meta["nome"],
            "frequencia": meta["frequencia"],
            "captured_at": capture_dt.isoformat(),
            "capture_timezone": "America/Sao_Paulo",
            "source_api": BASE_URL.format(codigo=code),
            "normalized_file": str(norm_path.relative_to(ROOT)),
            "normalized_sha256": sha256_file(norm_path),
            "linhas_normalized": len(normalized),
            "primeira_data": dates[0] if dates else None,
            "ultima_data": dates[-1] if dates else None,
            "datas_invalidas": quality["datas_invalidas"],
            "valores_invalidos": quality["valores_invalidos"],
            "duplicidades": quality["duplicidades"],
            "datas_futuras": quality["datas_futuras"],
            "future_rejected": quality["future_rejected"],
            "future_policy": "ACEITA_CALENDARIO_COPOM" if meta["allow_future"] else "REJEITA_FAIL_CLOSED",
            "chunks": chunks_meta,
            "fail_closed": True,
        }

        manifest_path = manifest_dir / f"SGS_{code}_quality.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        run_manifests.append(manifest)

        print(
            f"SGS={code} STATUS={manifest['status']} "
            f"LINHAS={manifest['linhas_normalized']} "
            f"INICIO={manifest['primeira_data']} FIM={manifest['ultima_data']} "
            f"DUP={manifest['duplicidades']} INVALID={manifest['datas_invalidas'] + manifest['valores_invalidos']}"
        )

    summary = {
        "schema_version": "1.0.0",
        "generated_at": capture_dt.isoformat(),
        "status": "VALIDADO" if all(m["status"] == "VALIDADO" for m in run_manifests) else "REJEITADO",
        "series": [
            {
                "codigo_sgs": m["codigo_sgs"],
                "status": m["status"],
                "ultima_data": m["ultima_data"],
                "linhas": m["linhas_normalized"],
                "manifest": str((MANIFEST_ROOT / f"SGS_{m['codigo_sgs']}_quality.json").relative_to(ROOT)),
            }
            for m in run_manifests
        ],
        "fail_closed": True,
    }
    summary_path = MANIFEST_ROOT / "BCB_SGS_NUCLEO_MACRO_quality.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"RESUMO_BCB_SGS={summary['status']}")


if __name__ == "__main__":
    main()
