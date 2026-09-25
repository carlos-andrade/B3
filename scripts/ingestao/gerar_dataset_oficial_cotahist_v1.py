#!/usr/bin/env python3
"""Gera o manifesto oficial do dataset COTAHIST a partir da certificação anual."""

from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv"
MANIFESTS = ROOT / "dados/cotahist/normalized/manifests"
OUT = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json"

EXPECTED_YEARS = list(range(1986, 2027))
ALLOWED_CERTIFICATIONS = {
    "CERTIFICADO_NORMALIZACAO",
    "CERTIFICADO_NORMALIZACAO_COM_EXCECAO_SEMANTICA",
}

def main() -> None:
    rows = list(csv.DictReader(CERT.open(encoding="utf-8", newline="")))
    by_year = {int(row["ano"]): row for row in rows}
    failures = []

    records = []
    for year in EXPECTED_YEARS:
        row = by_year.get(year)
        manifest_path = MANIFESTS / f"COTAHIST_A{year}_quality.json"

        if row is None or not manifest_path.is_file():
            failures.append(f"{year}: certificação ou quality manifest ausente")
            continue

        cert = row["certificacao"]
        if cert not in ALLOWED_CERTIFICATIONS:
            failures.append(f"{year}: certificação não permitida: {cert}")
            continue

        quality = json.loads(manifest_path.read_text(encoding="utf-8"))
        if quality.get("status") != "VALIDADO":
            failures.append(f"{year}: quality status inválido")
            continue

        if quality.get("parser_version") != "1.1.0":
            failures.append(f"{year}: parser incompatível")
            continue

        if quality.get("campos") != 25 or quality.get("datas_invalidas") != 0 or quality.get("datas_fora_do_ano") != 0:
            failures.append(f"{year}: critérios estruturais inválidos")
            continue

        records.append({
            "ano": year,
            "certificacao": cert,
            "escopo_semantico": row["escopo_semantico"],
            "raw_file": f"dados/cotahist/raw/anual/COTAHIST_A{year}.ZIP",
            "normalized_file": f"dados/cotahist/normalized/COTAHIST_A{year}.csv",
            "quality_manifest": f"dados/cotahist/normalized/manifests/COTAHIST_A{year}_quality.json",
            "raw_sha256": quality.get("raw_sha256"),
            "normalized_sha256": quality.get("normalized_sha256"),
            "linhas_normalized": quality.get("linhas_normalized"),
            "primeira_data": quality.get("primeira_data"),
            "ultima_data": quality.get("ultima_data"),
            "campos": quality.get("campos"),
            "excecao": row["excecao"],
        })

    if failures or len(records) != len(EXPECTED_YEARS):
        raise SystemExit("Dataset oficial NÃO publicado. Falhas: " + repr(failures))

    payload = {
        "schema_version": "1.0.0",
        "dataset_id": "COTAHIST_OFICIAL",
        "dataset_version": "1.0.0",
        "status": "VIGENTE",
        "generated_at": date.today().isoformat(),
        "source": "B3",
        "periodo": {"inicio": 1986, "fim": 2026},
        "escopo": "COTAHIST anual normalizado e certificado estruturalmente",
        "certificacao_source": "dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv",
        "records": records,
        "fail_closed": True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Dataset oficial gerado: {OUT}")
    print(f"Anos incluídos: {len(records)}")

if __name__ == "__main__":
    main()
