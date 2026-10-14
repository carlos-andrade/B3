#!/usr/bin/env python3
"""Gera o Dataset Oficial COTAHIST V2.0 com fail-closed físico.

A certificação física canónica é a auditoria independente global 1986–2026.
Cada registo anual tem de constar como VALIDADO nessa evidência, com hash
físico igual ao sidecar e ao manifesto de qualidade. Não altera os dados.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_DIR = ROOT / "dados/cotahist/normalized/manifests"
NORMALIZED_DIR = ROOT / "dados/cotahist/normalized/anual"
RAW_DIR = ROOT / "dados/cotahist/raw/anual"
QUALITY_DIR = ROOT / "dados/cotahist/quality"
PHYSICAL_AUDIT = QUALITY_DIR / "AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json"
OUT = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json"
YEARS = list(range(1986, 2027))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def raw_path_for(year: int) -> Path | None:
    for suffix in (".ZIP", ".zip"):
        candidate = RAW_DIR / f"COTAHIST_A{year}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def main() -> None:
    failures: list[str] = []
    records: list[dict] = []

    if not PHYSICAL_AUDIT.is_file():
        raise SystemExit("Dataset oficial V2 NÃO publicado: AUDITORIA_FISICA_GLOBAL_AUSENTE")

    try:
        audit = json.loads(PHYSICAL_AUDIT.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"Dataset oficial V2 NÃO publicado: AUDITORIA_FISICA_GLOBAL_JSON_INVALIDO:{exc}")

    if audit.get("resultado") != "APROVADO":
        failures.append("AUDITORIA_FISICA_GLOBAL_NAO_APROVADA")
    if audit.get("intervalo_anos") != [1986, 2026]:
        failures.append("INTERVALO_AUDITORIA_FISICA_INCORRETO")
    if audit.get("anos_auditados") != len(YEARS):
        failures.append("CONTAGEM_ANOS_AUDITADOS_INCORRETA")
    if audit.get("anos_validados") != len(YEARS) or audit.get("anos_com_falha") != 0:
        failures.append("AUDITORIA_FISICA_GLOBAL_INCOMPLETA")

    audit_by_year = {
        item.get("ano"): item
        for item in audit.get("anos", [])
        if isinstance(item, dict) and isinstance(item.get("ano"), int)
    }

    for year in YEARS:
        raw_path = raw_path_for(year)
        quality_path = MANIFEST_DIR / f"COTAHIST_A{year}_quality.json"
        normalized_path = NORMALIZED_DIR / f"COTAHIST_A{year}.csv"
        sidecar_path = MANIFEST_DIR / f"COTAHIST_A{year}.csv.sha256"
        physical = audit_by_year.get(year)

        year_failures: list[str] = []
        if raw_path is None:
            year_failures.append("RAW_AUSENTE")
        if not quality_path.is_file():
            year_failures.append("QUALITY_MANIFEST_AUSENTE")
        if not normalized_path.is_file():
            year_failures.append("NORMALIZED_AUSENTE")
        if not sidecar_path.is_file():
            year_failures.append("SIDECAR_AUSENTE")
        if physical is None:
            year_failures.append("ANO_AUSENTE_NA_AUDITORIA_FISICA")
        elif physical.get("status") != "VALIDADO" or physical.get("erros") != []:
            year_failures.append("ANO_NAO_VALIDADO_NA_AUDITORIA_FISICA")

        if year_failures:
            failures.extend(f"{year}: {item}" for item in year_failures)
            continue

        try:
            quality = json.loads(quality_path.read_text(encoding="utf-8"))
            sidecar_hash = sidecar_path.read_text(encoding="utf-8").strip().split()[0]
            physical_hash = sha256_file(normalized_path)
        except Exception as exc:
            failures.append(f"{year}: LEITURA_EVIDENCIA_FALHOU:{type(exc).__name__}")
            continue

        expected_path = f"dados/cotahist/normalized/anual/COTAHIST_A{year}.csv"
        if physical.get("arquivo") != expected_path:
            year_failures.append("CAMINHO_NORMALIZED_NAO_CANONICO")
        if physical.get("sha256_fisico") != physical_hash:
            year_failures.append("SHA_FISICO_VS_AUDITORIA_DIVERGENTE")
        if physical_hash != sidecar_hash:
            year_failures.append("SHA_FISICO_VS_SIDECAR_DIVERGENTE")
        if physical_hash != quality.get("normalized_sha256"):
            year_failures.append("SHA_FISICO_VS_MANIFESTO_DIVERGENTE")
        if physical_hash != physical.get("sha256_manifesto") or physical_hash != physical.get("sha256_sidecar"):
            year_failures.append("AUDITORIA_FISICA_NAO_CONFIRMA_HASH_TRIPLO")
        if physical.get("linhas_fisicas") != quality.get("linhas_normalized"):
            year_failures.append("CONTAGEM_LINHAS_DIVERGENTE")
        if quality.get("status") != "VALIDADO" or quality.get("ano") != year or quality.get("campos") != 25:
            year_failures.append("QUALITY_MANIFEST_INVALIDO")
        if physical.get("datas_invalidas") != 0 or physical.get("datas_fora_do_ano") != 0:
            year_failures.append("DATAS_INVALIDAS_OU_FORA_DO_ANO")
        if raw_path is not None and quality.get("raw_sha256") is None:
            year_failures.append("RAW_SHA256_AUSENTE_NO_MANIFESTO")

        if year_failures:
            failures.extend(f"{year}: {item}" for item in year_failures)
            continue

        records.append({
            "ano": year,
            "raw_file": f"dados/cotahist/raw/anual/COTAHIST_A{year}.ZIP",
            "normalized_file": expected_path,
            "quality_manifest": f"dados/cotahist/normalized/manifests/COTAHIST_A{year}_quality.json",
            "certificacao_fisica": "dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json",
            "certificacao": "VALIDADO_NA_AUDITORIA_FISICA_GLOBAL",
            "auditoria_fisica_status": physical.get("status"),
            "raw_sha256": quality.get("raw_sha256"),
            "normalized_sha256": physical_hash,
            "linhas_normalized": quality.get("linhas_normalized"),
            "primeira_data": quality.get("primeira_data"),
            "ultima_data": quality.get("ultima_data"),
            "campos": quality.get("campos"),
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
        "escopo": "COTAHIST anual normalizado validado pela auditoria física independente global",
        "certificacao_source": str(PHYSICAL_AUDIT.relative_to(ROOT)).replace("\\", "/"),
        "auditoria_fisica_sha256": sha256_file(PHYSICAL_AUDIT),
        "records": records,
        "fail_closed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Dataset oficial V2 gerado: {OUT}")
    print(f"Anos incluídos: {len(records)}")


if __name__ == "__main__":
    main()
