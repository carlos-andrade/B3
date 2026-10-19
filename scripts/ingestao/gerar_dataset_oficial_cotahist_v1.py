#!/usr/bin/env python3
"""Mantém o arquivo histórico COTAHIST 1986–2025 apenas para consulta; exclui 2026 bloqueado."""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv"
OUT = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json"

EXPECTED_YEARS = list(range(1986, 2026))
ALLOWED_CERTIFICATIONS = {
    "CERTIFICADO_NORMALIZACAO",
    "CERTIFICADO_NORMALIZACAO_COM_EXCECAO_SEMANTICA",
}


def main() -> None:
    with CERT.open(encoding="utf-8", newline="") as handle:
        by_year = {int(row["ano"]): row for row in csv.DictReader(handle)}

    if not OUT.is_file():
        raise SystemExit(
            "Dataset histórico ausente: não reconstruir anos encerrados automaticamente; "
            "reabertura formal necessária."
        )

    existing_payload = json.loads(OUT.read_text(encoding="utf-8"))
    existing_records = {
        int(item["ano"]): item for item in existing_payload.get("records", [])
        if "ano" in item
    }
    missing_historical = [year for year in EXPECTED_YEARS if year not in existing_records]
    if missing_historical:
        raise SystemExit(
            f"Registos históricos ausentes no Dataset Oficial V1: {missing_historical}; "
            "reabertura formal necessária."
        )

    invalid_certifications = [
        year for year in EXPECTED_YEARS
        if year not in by_year or by_year[year].get("certificacao") not in ALLOWED_CERTIFICATIONS
    ]
    if invalid_certifications:
        raise SystemExit(
            f"Certificação histórica ausente ou inválida: {invalid_certifications}; "
            "dataset não será promovido."
        )

    # O arquivo histórico é imutável nesta rotina; 2026 fica excluído por bloqueio de autorização.
    records = [existing_records[year] for year in EXPECTED_YEARS]
    payload = {
        "schema_version": "1.0.0",
        "dataset_id": "COTAHIST_ARQUIVO_CONSULTA",
        "dataset_version": "1.1.0",
        "status": "CONSULTA_HISTORICA",
        "generated_at": date.today().isoformat(),
        "source": "B3",
        "periodo": {"inicio": 1986, "fim": 2025},
        "escopo": (
            "Arquivo histórico existente para consulta; sem nova captura automatizada. "
            "A publicação/redistribuição dos dados permanece sujeita ao registo de autorizações."
        ),
        "certificacao_source": "dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv",
        "records": records,
        "fail_closed": True,
        "policy_exclusions": {
            "2026": "BLOQUEADO_AUTORIZACAO_FONTE",
            "reason": "Não promover nem publicar automaticamente dados de preço sem direitos compatíveis demonstrados.",
        },
    }

    stable_existing = dict(existing_payload)
    stable_payload = dict(payload)
    stable_existing.pop("generated_at", None)
    stable_payload.pop("generated_at", None)
    if stable_existing == stable_payload:
        print(f"Arquivo histórico sem alteração material: {OUT}")
        print(f"Anos incluídos para consulta: {len(records)} (1986–2025)")
        print("2026 excluído: BLOQUEADO_AUTORIZACAO_FONTE")
        return

    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Arquivo histórico atualizado: {OUT}")
    print(f"Anos incluídos para consulta: {len(records)} (1986–2025)")
    print("2026 excluído: BLOQUEADO_AUTORIZACAO_FONTE")


if __name__ == "__main__":
    main()
