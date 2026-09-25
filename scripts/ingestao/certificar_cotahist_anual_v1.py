#!/usr/bin/env python3
"""Regenera a matriz oficial de certificação anual do COTAHIST."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "dados" / "cotahist" / "raw" / "anual"
MANIFESTS = ROOT / "dados" / "cotahist" / "normalized" / "manifests"
OUT = ROOT / "dados" / "cotahist" / "certificacao" / "COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv"

YEARS = range(1986, 2027)
PARSER_VERSION = "1.1.0"

FIELDS = [
    "ano", "raw_present", "quality_manifest_present", "quality_status",
    "parser_version", "linhas_normalized", "campos", "datas_invalidas",
    "datas_fora_do_ano", "escopo_semantico", "certificacao", "excecao",
]


def raw_exists(year: int) -> bool:
    return (RAW / f"COTAHIST_A{year}.ZIP").is_file() or (RAW / f"COTAHIST_A{year}.zip").is_file()


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = []

    for year in YEARS:
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
            raw and present and status == "VALIDADO" and parser == PARSER_VERSION
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
