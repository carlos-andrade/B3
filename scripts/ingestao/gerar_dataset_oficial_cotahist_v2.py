#!/usr/bin/env python3
"""Gera o Dataset Oficial COTAHIST V2.0 com fail-closed físico.

Somente publica quando os 41 anos possuem RAW, NORMALIZED canônico,
quality manifest coerente e certificação física V2.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT_DIR = ROOT / "dados/cotahist/certificacao/v2"
MANIFEST_DIR = ROOT / "dados/cotahist/normalized/manifests"
NORMALIZED_DIR = ROOT / "dados/cotahist/normalized/anual"
RAW_DIR = ROOT / "dados/cotahist/raw/anual"
OUT = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json"
YEARS = list(range(1986, 2027))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def raw_exists(year: int) -> bool:
    return (RAW_DIR / f"COTAHIST_A{year}.ZIP").is_file() or (RAW_DIR / f"COTAHIST_A{year}.zip").is_file()


def main() -> None:
    failures = []
    records = []

    for year in YEARS:
        manifest_path = MANIFEST_DIR / f"COTAHIST_A{year}_quality.json"
        normalized_path = NORMALIZED_DIR / f"COTAHIST_A{year}.csv"
        cert_path = CERT_DIR / f"COTAHIST_A{year}_CERTIFICACAO_FISICA_V2.0.json"

        if not raw_exists(year):
            failures.append(f"{year}: RAW_AUSENTE")
        if not manifest_path.is_file():
            failures.append(f"{year}: QUALITY_MANIFEST_AUSENTE")
        if not normalized_path.is_file():
            failures.append(f"{year}: NORMALIZED_AUSENTE")
        if not cert_path.is_file():
            failures.append(f"{year}: CERTIFICACAO_FISICA_AUSENTE")
            continue

        try:
            quality = json.loads(manifest_path.read_text(encoding="utf-8"))
            cert = json.loads(cert_path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"{year}: JSON_INVALIDO:{exc}")
            continue

        if cert.get("status") != "CERTIFICADO":
            failures.append(f"{year}: CERTIFICACAO_FISICA_NAO_CERTIFICADA")
            continue

        if cert.get("normalized_file") != f"dados/cotahist/normalized/anual/COTAHIST_A{year}.csv":
            failures.append(f"{year}: CAMINHO_NORMALIZED_NAO_CANONICO")
        if cert.get("normalized_sha256_fisico") != quality.get("normalized_sha256"):
            failures.append(f"{year}: SHA_CERT_VS_MANIFEST_DIVERGENTE")
        if normalized_path.is_file():
            physical_sha = sha256_file(normalized_path)
            if physical_sha != quality.get("normalized_sha256"):
                failures.append(f"{year}: SHA_FISICO_VS_MANIFEST_DIVERGENTE")

        if quality.get("status") != "VALIDADO" or quality.get("campos") != 25:
            failures.append(f"{year}: QUALITY_INVALIDA")

        if not failures or not any(item.startswith(f"{year}:") for item in failures):
            records.append({
                "ano": year,
                "raw_file": f"dados/cotahist/raw/anual/COTAHIST_A{year}.ZIP",
                "normalized_file": f"dados/cotahist/normalized/anual/COTAHIST_A{year}.csv",
                "quality_manifest": f"dados/cotahist/normalized/manifests/COTAHIST_A{year}_quality.json",
                "certificacao_fisica": f"dados/cotahist/certificacao/v2/COTAHIST_A{year}_CERTIFICACAO_FISICA_V2.0.json",
                "raw_sha256": quality.get("raw_sha256"),
                "normalized_sha256": quality.get("normalized_sha256"),
                "linhas_normalized": quality.get("linhas_normalized"),
                "primeira_data": quality.get("primeira_data"),
                "ultima_data": quality.get("ultima_data"),
                "campos": quality.get("campos"),
                "certificacao": cert.get("certificacao"),
                "escopo_semantico": "EXCECAO_HISTORICA_CONTROLADA" if year == 1986 else "NORMALIZACAO_ESTRUTURAL",
            })

    if failures or len(records) != len(YEARS):
        print("Dataset oficial V2 NÃO publicado.")
        print("Falhas:")
        for failure in failures:
            print(f" - {failure}")
        raise SystemExit(1)

    payload = {
        "schema_version": "2.0.0",
        "dataset_id": "COTAHIST_OFICIAL",
        "dataset_version": "2.0.0",
        "status": "VIGENTE",
        "generated_at": date.today().isoformat(),
        "source": "B3",
        "periodo": {"inicio": 1986, "fim": 2026},
        "escopo": "COTAHIST anual normalizado fisicamente persistido e certificado",
        "certificacao_source": "dados/cotahist/certificacao/v2/",
        "records": records,
        "fail_closed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Dataset oficial V2 gerado: {OUT}")
    print(f"Anos incluídos: {len(records)}")


if __name__ == "__main__":
    main()
