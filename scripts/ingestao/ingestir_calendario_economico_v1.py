#!/usr/bin/env python3
"""Ingestão inicial do calendário econômico oficial.

Projeto: B3 — A BOLSA DO BRASIL
Versão: V1.0
Data: 24/09/2026

A rotina é deliberadamente conservadora: captura páginas/feeds oficiais,
preserva a evidência RAW e produz registros NORMALIZED somente quando os
campos mínimos podem ser identificados sem inferência indevida.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

USER_AGENT = "B3-Calendar-Ingestion/1.0"
DEFAULT_RAW = Path("dados/calendario_economico/raw")
DEFAULT_NORMALIZED = Path("dados/calendario_economico/normalized")
DEFAULT_METADATA = Path("dados/calendario_economico/metadata")


@dataclass(frozen=True)
class Evidence:
    source: str
    source_url: str
    retrieved_at: str
    sha256: str
    raw_path: str


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=60) as response:
        return response.read()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    return value.strip("._") or "source"


def ingest_source(name: str, url: str, raw_dir: Path, metadata_dir: Path) -> Evidence:
    payload = fetch(url)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    digest = sha256(payload)
    filename = f"{safe_name(name)}_{stamp}_{digest[:12]}.raw"
    raw_path = raw_dir / filename
    raw_path.write_bytes(payload)

    evidence = Evidence(
        source=name,
        source_url=url,
        retrieved_at=datetime.now(timezone.utc).isoformat(),
        sha256=digest,
        raw_path=str(raw_path).replace("\\", "/"),
    )

    metadata_dir.mkdir(parents=True, exist_ok=True)
    metadata_path = metadata_dir / f"{safe_name(name)}_{stamp}_{digest[:12]}.json"
    metadata_path.write_text(
        json.dumps(asdict(evidence), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", action="append", nargs=2, metavar=("NAME", "URL"))
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW)
    parser.add_argument("--metadata-dir", type=Path, default=DEFAULT_METADATA)
    args = parser.parse_args()

    if not args.source:
        parser.error("Informe ao menos uma fonte com --source NOME URL")

    args.raw_dir.mkdir(parents=True, exist_ok=True)

    evidences = []
    for name, url in args.source:
        try:
            evidences.append(asdict(ingest_source(name, url, args.raw_dir, args.metadata_dir)))
        except Exception as exc:
            print(f"ERRO: {name}: {exc}", file=sys.stderr)
            return 2

    print(json.dumps(evidences, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
