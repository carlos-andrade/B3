#!/usr/bin/env python3
"""Auditoria física independente dos CSV COTAHIST NORMALIZED (1986–2026).

Leitura somente: não altera dados, manifestos, checksums nem artefactos históricos.
Valida o conteúdo materializado após checkout Git LFS contra o manifesto e sidecar.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "dados/cotahist/normalized/anual"
MANIFEST_DIR = ROOT / "dados/cotahist/normalized/manifests"
DEFAULT_OUTPUT = ROOT / "dados/cotahist/quality/AUDITORIA_FISICA_COTAHIST_1986_2026_V1.json"
LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def audit_year(year: int) -> dict:
    name = f"COTAHIST_A{year}"
    csv_path = DATA_DIR / f"{name}.csv"
    manifest_path = MANIFEST_DIR / f"{name}_quality.json"
    checksum_path = MANIFEST_DIR / f"{name}.csv.sha256"
    result = {
        "ano": year,
        "arquivo": str(csv_path.relative_to(ROOT)).replace("\\", "/"),
        "status": "FALHA",
        "erros": [],
    }

    for path in (csv_path, manifest_path, checksum_path):
        if not path.is_file() or path.stat().st_size == 0:
            result["erros"].append(f"ARQUIVO_AUSENTE_OU_VAZIO:{path.name}")
    if result["erros"]:
        return result

    with csv_path.open("rb") as handle:
        prefix = handle.read(100)
    if prefix.startswith(LFS_POINTER_PREFIX):
        result["erros"].append("GIT_LFS_POINTER_NAO_MATERIALIZADO")
        return result

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        result["erros"].append(f"MANIFESTO_JSON_INVALIDO:{type(exc).__name__}")
        return result

    actual_sha = sha256(csv_path)
    sidecar = checksum_path.read_text(encoding="utf-8").strip().split()
    expected_sidecar_sha = sidecar[0] if sidecar else ""
    expected_manifest_sha = manifest.get("normalized_sha256")
    result.update({
        "sha256_fisico": actual_sha,
        "sha256_sidecar": expected_sidecar_sha,
        "sha256_manifesto": expected_manifest_sha,
        "linhas_manifesto": manifest.get("linhas_normalized"),
        "campos_manifesto": manifest.get("campos"),
        "parser_version": manifest.get("parser_version"),
        "status_manifesto": manifest.get("status"),
    })

    if actual_sha != expected_sidecar_sha:
        result["erros"].append("SHA256_DIVERGE_DO_SIDECAR")
    if actual_sha != expected_manifest_sha:
        result["erros"].append("SHA256_DIVERGE_DO_MANIFESTO")
    if manifest.get("ano") != year:
        result["erros"].append("ANO_DO_MANIFESTO_INCORRETO")
    if manifest.get("status") != "VALIDADO":
        result["erros"].append("MANIFESTO_NAO_VALIDADO")

    rows = 0
    invalid_dates = 0
    out_of_year = 0
    min_date = None
    max_date = None
    field_counts = set()
    try:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            header = next(reader, None)
            if header is None:
                result["erros"].append("CSV_SEM_CABECALHO")
                return result
            if len(header) != 25:
                result["erros"].append(f"CABECALHO_COM_{len(header)}_CAMPOS")
            for line_number, row in enumerate(reader, start=2):
                if not row or (len(row) == 1 and not row[0].strip()):
                    result["erros"].append(f"LINHA_VAZIA:{line_number}")
                    continue
                rows += 1
                field_counts.add(len(row))
                if len(row) != 25:
                    result["erros"].append(f"CONTAGEM_CAMPOS_INVALIDA:{line_number}:{len(row)}")
                    continue
                try:
                    value = date.fromisoformat(row[0].strip())
                    min_date = value if min_date is None or value < min_date else min_date
                    max_date = value if max_date is None or value > max_date else max_date
                    if value.year != year:
                        out_of_year += 1
                except (ValueError, TypeError):
                    invalid_dates += 1
    except (UnicodeDecodeError, csv.Error, OSError) as exc:
        result["erros"].append(f"LEITURA_CSV_FALHOU:{type(exc).__name__}")
        return result

    result.update({
        "linhas_fisicas": rows,
        "campos_observados": sorted(field_counts),
        "datas_invalidas": invalid_dates,
        "datas_fora_do_ano": out_of_year,
        "primeira_data_observada": min_date.isoformat() if min_date else None,
        "ultima_data_observada": max_date.isoformat() if max_date else None,
    })
    if rows != manifest.get("linhas_normalized"):
        result["erros"].append("CONTAGEM_LINHAS_DIVERGE_DO_MANIFESTO")
    if manifest.get("campos") != 25 or field_counts != {25}:
        result["erros"].append("ESTRUTURA_25_CAMPOS_NAO_CONFIRMADA")
    if invalid_dates != manifest.get("datas_invalidas", 0):
        result["erros"].append("DATAS_INVALIDAS_DIVERGEM_DO_MANIFESTO")
    if invalid_dates != 0:
        result["erros"].append("DATAS_INVALIDAS_DETETADAS")
    if out_of_year != manifest.get("datas_fora_do_ano", 0):
        result["erros"].append("DATAS_FORA_DO_ANO_DIVERGEM_DO_MANIFESTO")
    if out_of_year != 0:
        result["erros"].append("DATAS_FORA_DO_ANO_DETETADAS")
    if min_date and manifest.get("primeira_data") != min_date.isoformat():
        result["erros"].append("PRIMEIRA_DATA_DIVERGE_DO_MANIFESTO")
    if max_date and manifest.get("ultima_data") != max_date.isoformat():
        result["erros"].append("ULTIMA_DATA_DIVERGE_DO_MANIFESTO")

    result["status"] = "VALIDADO" if not result["erros"] else "FALHA"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=1986)
    parser.add_argument("--end-year", type=int, default=2026)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.start_year < 1986 or args.end_year > 2026 or args.start_year > args.end_year:
        parser.error("intervalo permitido: 1986–2026")

    years = [audit_year(year) for year in range(args.start_year, args.end_year + 1)]
    failures = [item for item in years if item["status"] != "VALIDADO"]
    report = {
        "schema_version": "1.0.0",
        "tipo": "AUDITORIA_FISICA_INDEPENDENTE_COTAHIST_NORMALIZED",
        "intervalo_anos": [args.start_year, args.end_year],
        "anos_auditados": len(years),
        "anos_validados": len(years) - len(failures),
        "anos_com_falha": len(failures),
        "resultado": "APROVADO" if not failures else "REPROVADO",
        "somente_leitura": True,
        "criterios": [
            "arquivo físico materializado, sem ponteiro Git LFS",
            "SHA-256 físico igual ao sidecar e ao manifesto",
            "contagem de registos físicos igual ao manifesto",
            "25 campos em cabeçalho e em todas as linhas",
            "datas válidas e pertencentes ao ano",
            "datas mínima e máxima coerentes com o manifesto",
        ],
        "anos": years,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("intervalo_anos", "anos_auditados", "anos_validados", "anos_com_falha", "resultado")}, ensure_ascii=False))
    for item in failures:
        print(json.dumps({"ano": item["ano"], "erros": item["erros"]}, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
