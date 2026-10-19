#!/usr/bin/env python3
"""Preserva certificações históricas e classifica 2026 como bloqueado por política de fonte."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "dados" / "cotahist" / "raw" / "anual"
MANIFESTS = ROOT / "dados" / "cotahist" / "normalized" / "manifests"
OUT = ROOT / "dados" / "cotahist" / "certificacao" / "COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv"

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

    # Anos encerrados: preservar literalmente as linhas já certificadas.
    rows = [existing_rows[year] for year in range(1986, 2026)]

    # 2026: registar o bloqueio de autorização sem confundi-lo com defeito estrutural.
    year = 2026
    manifest_path = MANIFESTS / f"COTAHIST_A{year}_quality.json"
    present = manifest_path.is_file()
    raw = raw_exists(year)
    data = json.loads(manifest_path.read_text(encoding="utf-8")) if present else {}
    rows.append({
        "ano": year,
        "raw_present": "SIM" if raw else "NAO",
        "quality_manifest_present": "SIM" if present else "NAO",
        "quality_status": data.get("status", "AUSENTE"),
        "parser_version": data.get("parser_version", ""),
        "linhas_normalized": data.get("linhas_normalized", ""),
        "campos": data.get("campos", ""),
        "datas_invalidas": data.get("datas_invalidas", ""),
        "datas_fora_do_ano": data.get("datas_fora_do_ano", ""),
        "escopo_semantico": "FORA_DO_ESCOPO_PUBLICACAO",
        "certificacao": "BLOQUEADO_AUTORIZACAO_FONTE",
        "excecao": (
            "Não promover nem publicar automaticamente 2026: autorização compatível da fonte "
            "não demonstrada. A presença de RAW/NORMALIZED não equivale a autorização."
        ),
    })

    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    certified_historical = sum(
        row["certificacao"].startswith("CERTIFICADO_")
        for row in rows if int(row["ano"]) < 2026
    )
    print(f"Matriz gerada: {OUT}")
    print("Anos históricos preservados: 40 (1986–2025; sem reavaliação automática)")
    print(f"Anos históricos certificados na matriz: {certified_historical}")
    print("Ano 2026: BLOQUEADO_AUTORIZACAO_FONTE; não contado como certificado.")
    print("Política: nenhuma nova captura foi efetuada; esta rotina só classifica artefactos locais existentes.")
    print("Nenhum ano histórico foi recalculado ou reescrito semanticamente.")


if __name__ == "__main__":
    main()
