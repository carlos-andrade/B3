#!/usr/bin/env python3
"""Certificação física NORMALIZED COTAHIST V2.0.

Valida um ano contra RAW, quality manifest e CSV NORMALIZED canônico.
Nenhuma correção, deduplicação ou alteração de dados é executada.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "dados/cotahist/raw/anual"
NORMALIZED_DIR = ROOT / "dados/cotahist/normalized/anual"
MANIFEST_DIR = ROOT / "dados/cotahist/normalized/manifests"
OUT_DIR = ROOT / "dados/cotahist/certificacao/v2"
PARSER_VERSION = "1.1.0"
FIELDS = 25


def raw_path(year: int) -> Path:
    upper = RAW_DIR / f"COTAHIST_A{year}.ZIP"
    lower = RAW_DIR / f"COTAHIST_A{year}.zip"
    return upper if upper.is_file() else lower


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_csv(path: Path, year: int) -> tuple[int, str, str]:
    rows = 0
    first_date = None
    last_date = None
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader, None)
        if header is None or len(header) != FIELDS:
            raise ValueError(f"schema inválido: cabeçalho possui {0 if header is None else len(header)} campos")
        for line_no, row in enumerate(reader, start=2):
            if len(row) != FIELDS:
                raise ValueError(f"schema inválido na linha {line_no}: {len(row)} campos")
            value = row[0]
            try:
                parsed = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError as exc:
                raise ValueError(f"data inválida na linha {line_no}: {value!r}") from exc
            if parsed.year != year:
                raise ValueError(f"data fora do ano {year} na linha {line_no}: {value}")
            if first_date is None:
                first_date = value
            last_date = value
            rows += 1
    if rows == 0:
        raise ValueError("NORMALIZED sem registros")
    return rows, first_date, last_date


def certify(year: int) -> dict:
    raw = raw_path(year)
    manifest_path = MANIFEST_DIR / f"COTAHIST_A{year}_quality.json"
    normalized = NORMALIZED_DIR / f"COTAHIST_A{year}.csv"

    failures = []
    if not raw.is_file():
        failures.append("RAW_AUSENTE")
    if not manifest_path.is_file():
        failures.append("QUALITY_MANIFEST_AUSENTE")
    if not normalized.is_file():
        failures.append("NORMALIZED_AUSENTE")

    manifest = {}
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("status") != "VALIDADO":
            failures.append("QUALITY_STATUS_INVALIDO")
        if manifest.get("ano") != year:
            failures.append("QUALITY_ANO_INCOMPATIVEL")
        if manifest.get("parser_version") != PARSER_VERSION:
            failures.append("PARSER_INCOMPATIVEL")
        if manifest.get("campos") != FIELDS:
            failures.append("QUALITY_CAMPOS_INCOMPATIVEL")
        if manifest.get("datas_invalidas") != 0 or manifest.get("datas_fora_do_ano") != 0:
            failures.append("QUALITY_DATAS_INVALIDAS")

    normalized_sha = None
    normalized_rows = None
    first_date = None
    last_date = None
    normalized_bytes = None

    if normalized.is_file():
        normalized_bytes = normalized.stat().st_size
        normalized_sha = sha256_file(normalized)
        try:
            normalized_rows, first_date, last_date = inspect_csv(normalized, year)
        except ValueError as exc:
            failures.append(f"NORMALIZED_INVALIDO:{exc}")

        if manifest:
            if normalized_sha != manifest.get("normalized_sha256"):
                failures.append("SHA_NORMALIZED_DIVERGENTE")
            if normalized_rows != manifest.get("linhas_normalized"):
                failures.append("CONTAGEM_NORMALIZED_DIVERGENTE")
            if first_date != manifest.get("primeira_data"):
                failures.append("PRIMEIRA_DATA_DIVERGENTE")
            if last_date != manifest.get("ultima_data"):
                failures.append("ULTIMA_DATA_DIVERGENTE")

    if failures:
        status = "NAO_CERTIFICADO"
        certification = "NORMALIZED_FISICO_INVALIDO"
    else:
        status = "CERTIFICADO"
        certification = (
            "CERTIFICADO_NORMALIZACAO_FISICO_COM_EXCECAO_SEMANTICA"
            if year == 1986
            else "CERTIFICADO_NORMALIZACAO_FISICO"
        )

    result = {
        "schema_version": "2.0.0",
        "certificacao": certification,
        "status": status,
        "ano": year,
        "source": "B3",
        "parser_version": PARSER_VERSION,
        "raw_file": str(raw.relative_to(ROOT)) if raw.is_file() else f"dados/cotahist/raw/anual/COTAHIST_A{year}.ZIP",
        "normalized_file": str(normalized.relative_to(ROOT)),
        "quality_manifest": str(manifest_path.relative_to(ROOT)),
        "raw_sha256": manifest.get("raw_sha256"),
        "normalized_sha256_manifest": manifest.get("normalized_sha256"),
        "normalized_sha256_fisico": normalized_sha,
        "linhas_normalized_manifest": manifest.get("linhas_normalized"),
        "linhas_normalized_fisico": normalized_rows,
        "campos": FIELDS,
        "primeira_data_manifest": manifest.get("primeira_data"),
        "primeira_data_fisico": first_date,
        "ultima_data_manifest": manifest.get("ultima_data"),
        "ultima_data_fisico": last_date,
        "normalized_bytes": normalized_bytes,
        "failures": failures,
        "fail_closed": True,
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True, choices=range(1986, 2027))
    args = parser.parse_args()

    result = certify(args.year)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"COTAHIST_A{args.year}_CERTIFICACAO_FISICA_V2.0.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"Evidência: {out}")
    if result["status"] != "CERTIFICADO":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
