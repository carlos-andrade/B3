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
AUDIT_YEARS = list(range(1986, 2027))
# V2.0.0 publica apenas anos encerrados; 2026 continua bloqueado para publicação.
YEARS = list(range(1986, 2026))
AUTH_REGISTRY = ROOT / "docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json"
QUALITY_2026 = MANIFEST_DIR / "COTAHIST_A2026_quality.json"


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



def policy_exclusion_for_2026(quality: dict, endpoint: dict | None) -> dict:
    """Exclui 2026 da V2.0.0 sem confundir integridade física com licença de publicação."""
    publication_authorized = bool(
        endpoint
        and endpoint.get("publication_authorized") is True
        and endpoint.get("storage_and_redistribution") in {
            "AUTHORIZED", "AUTHORIZED_WITH_CONDITIONS", "LICENSED"
        }
    )
    if publication_authorized:
        status = "EXCLUDED_BY_VERSION_SCOPE"
        reason = (
            "A V2.0.0 está limitada explicitamente a 1986–2025; incluir 2026 exige revisão "
            "versionada do dataset e dos critérios de aceitação."
        )
    else:
        status = "BLOQUEADO_AUTORIZACAO_FONTE"
        reason = (
            "A autorização de publicação/redistribuição de COTAHIST 2026 não está demonstrada; "
            "a validação física não concede direitos de publicação."
        )
    return {
        "status": status,
        "reason": reason,
        "endpoint_id": "B3_COTAHIST_DAILY",
        "authorization_status": endpoint.get("authorization_status", "NOT_REGISTERED") if endpoint else "NOT_REGISTERED",
        "publication_authorized": publication_authorized,
        "quality_manifest_status": quality.get("status", "MISSING"),
        "quality_manifest": str(QUALITY_2026.relative_to(ROOT)).replace("\\", "/"),
        "authorization_registry": str(AUTH_REGISTRY.relative_to(ROOT)).replace("\\", "/"),
    }


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
    if audit.get("anos_auditados") != len(AUDIT_YEARS):
        failures.append("CONTAGEM_ANOS_AUDITADOS_INCORRETA")
    if audit.get("anos_validados") != len(AUDIT_YEARS) or audit.get("anos_com_falha") != 0:
        failures.append("AUDITORIA_FISICA_GLOBAL_INCOMPLETA")

    quality_2026 = {}
    if QUALITY_2026.is_file():
        try:
            quality_2026 = json.loads(QUALITY_2026.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"2026: QUALITY_MANIFEST_LEITURA_FALHOU:{type(exc).__name__}")
    registry = {}
    if AUTH_REGISTRY.is_file():
        try:
            registry = json.loads(AUTH_REGISTRY.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"2026: AUTH_REGISTRY_JSON_INVALIDO:{type(exc).__name__}")
    endpoint_2026 = next((
        row for row in registry.get("endpoints", [])
        if isinstance(row, dict) and row.get("id") == "B3_COTAHIST_DAILY"
    ), None)
    exclusion_2026 = policy_exclusion_for_2026(quality_2026, endpoint_2026)

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
        "periodo": {"inicio": YEARS[0], "fim": YEARS[-1]},
        "escopo": "Arquivo COTAHIST anual de consulta, com integridade física validada, limitado a 1986–2025; 2026 excluído por gate explícito de publicação.",
        "certificacao_source": str(PHYSICAL_AUDIT.relative_to(ROOT)).replace("\\", "/"),
        "auditoria_fisica_sha256": sha256_file(PHYSICAL_AUDIT),
        "records": records,
        "policy_exclusions": {"2026": exclusion_2026},
        "fail_closed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Dataset oficial V2 gerado: {OUT}")
    print(f"Anos incluídos: {len(records)}")


if __name__ == "__main__":
    main()
