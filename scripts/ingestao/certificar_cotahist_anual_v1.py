#!/usr/bin/env python3
"""Preserva as linhas históricas e recalcula a certificação de 2026."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "dados" / "cotahist" / "raw" / "anual"
MANIFESTS = ROOT / "dados" / "cotahist" / "normalized" / "manifests"
OUT = ROOT / "dados" / "cotahist" / "certificacao" / "COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv"

YEARS = range(1986, 2027)
# Versoes explicitamente reconhecidas apos validacao dos manifestos historicos.
SUPPORTED_PARSER_VERSIONS = {"1.1.0", "1.1.1", "1.1.2"}

FIELDS = [
    "ano", "raw_present", "quality_manifest_present", "quality_status",
    "parser_version", "linhas_normalized", "campos", "datas_invalidas",
    "datas_fora_do_ano", "escopo_semantico", "certificacao", "excecao",
]


def raw_exists(year: int) -> bool:
    return (RAW / f"COTAHIST_A{year}.ZIP").is_file() or (RAW / f"COTAHIST_A{year}.zip").is_file()


def main() -> None:
    if not OUT.is_file():
        raise SystemExit(
            "Matriz histórica ausente: não reconstruir anos encerrados automaticamente; "
            "reabertura formal necessária."
        )
    with OUT.open(encoding="utf-8", newline="") as handle:
        existing_rows = {int(row["ano"]): row for row in csv.DictReader(handle)}
    missing_historical = [year for year in range(1986, 2026) if year not in existing_rows]
    if missing_historical:
        raise SystemExit(
            f"Linhas históricas ausentes na matriz: {missing_historical}; "
            "histórico congelado, sem reconstrução automática."
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = []

    for year in YEARS:
        if year < 2026:
            # Congelar as linhas históricas: não reavaliar nem reescrever 1986–2025 na rotina.
            rows.append(existing_rows[year])
            continue

        manifest_path = MANIFESTS / f"COTAHIST_A{year}_quality.json"
        present = manifest_path.is_file()
        raw = raw_exists(year)
        data = json.loads(manifest_path.read_text(encoding="utf-8")) if present else {}

        status = data.get("status", "AUSENTE")
        parser = data.get("parser_version", "")
        lines = data.get("linhas_normalized", "")
        fields = data.get("campos", "")
        invalid = data.get("datas_invalidas", "")
        outside = data.get("datas_fora_do_ano", "")

        structural_ok = (
            raw and present and status == "VALIDADO" and parser in SUPPORTED_PARSER_VERSIONS
            and fields == 25 and invalid == 0 and outside == 0
        )

        if year == 1986:
            semantic_scope = "EXCEÇÃO_HISTÓRICA_CONTROLADA"
            certification = (
                "CERTIFICADO_NORMALIZACAO_COM_EXCECAO_SEMANTICA"
                if structural_ok else "NAO_CERTIFICADO"
            )
            exception = "Investigação semântica histórica mantida como exceção controlada."
        else:
            semantic_scope = "NORMALIZACAO_ESTRUTURAL"
            certification = "CERTIFICADO_NORMALIZACAO" if structural_ok else "NAO_CERTIFICADO"
            exception = ""

        if not structural_ok:
            failures.append(year)

        rows.append({
            "ano": year,
            "raw_present": "SIM" if raw else "NAO",
            "quality_manifest_present": "SIM" if present else "NAO",
            "quality_status": status,
            "parser_version": parser,
            "linhas_normalized": lines,
            "campos": fields,
            "datas_invalidas": invalid,
            "datas_fora_do_ano": outside,
            "escopo_semantico": semantic_scope,
            "certificacao": certification,
            "excecao": exception,
        })

    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Matriz gerada: {OUT}")
    print(f"Anos avaliados: {len(rows)}")
    print(f"Anos certificados: {sum(r['certificacao'].startswith('CERTIFICADO_') for r in rows)}")
    print(f"Falhas de certificação estrutural: {failures}")

    if failures:
        raise SystemExit(f"Certificação falhou para os anos: {failures}")


if __name__ == "__main__":
    main()

# Retrigger: evidencia FASE10 1991 materializada no main.

# Retrigger auditável: sincronização do manifesto canónico COTAHIST 2026 em 2026-10-14.
