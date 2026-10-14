#!/usr/bin/env python3
"""Importação diária automática e retroativa do COTAHIST B3."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import tempfile
import urllib.error
import urllib.request
import zipfile
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from normalize_cotahist import PARSER_VERSION

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "dados/cotahist/raw/diario"
NORM_DIR = ROOT / "dados/cotahist/normalized/diario"
MAN_DIR = ROOT / "dados/cotahist/normalized/manifests/diario"
CONFLICT_DIR = ROOT / "dados/cotahist/quality/diario/conflitos"
RUN_DIR = ROOT / "dados/cotahist/quality/diario/execucoes"
BASE_URL = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist"
BACKFILL_DAYS = 7


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def import_day(ref_date: date) -> str:
    iso_date = ref_date.isoformat()
    date_ref = ref_date.strftime("%d%m%Y")
    name = f"COTAHIST_D{date_ref}"
    url = f"{BASE_URL}/{name}.ZIP"

    raw_out = RAW_DIR / f"{name}.ZIP"
    norm_out = NORM_DIR / f"{name}.csv"
    manifest_out = MAN_DIR / f"{name}_quality.json"

    with tempfile.NamedTemporaryFile(suffix=".ZIP", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "B3-repository-ingestion/1.1"})
        try:
            with urllib.request.urlopen(req, timeout=60) as response, tmp_path.open("wb") as dst:
                dst.write(response.read())
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 410):
                print(f"SEM_PREGAO_OU_ARQUIVO: {iso_date} HTTP={exc.code}")
                return "SKIPPED"
            raise

        if tmp_path.stat().st_size == 0:
            print(f"ARQUIVO_VAZIO: {iso_date}")
            return "SKIPPED"

        with zipfile.ZipFile(tmp_path) as zf:
            members = [n for n in zf.namelist() if not n.endswith("/")]
            if len(members) != 1:
                raise SystemExit(f"ZIP inesperado: {members}")
            if zf.getinfo(members[0]).file_size == 0:
                print(f"ZIP_SEM_CONTEUDO: {iso_date}")
                return "SKIPPED"

        tmp_sha = sha256(tmp_path)
        if raw_out.exists():
            existing_sha = sha256(raw_out)
            if existing_sha == tmp_sha and norm_out.exists() and manifest_out.exists():
                integrity_errors = []
                manifest_data = None
                try:
                    manifest_data = json.loads(manifest_out.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    integrity_errors.append("MANIFESTO_JSON_INVALIDO")
                normalized_sha = sha256(norm_out)
                if manifest_data is not None:
                    if manifest_data.get("status") != "VALIDADO":
                        integrity_errors.append("MANIFESTO_NAO_VALIDADO")
                    if manifest_data.get("raw_sha256") != existing_sha:
                        integrity_errors.append("RAW_SHA_DIVERGE_DO_MANIFESTO")
                    if manifest_data.get("normalized_sha256") != normalized_sha:
                        integrity_errors.append("NORMALIZED_SHA_DIVERGE_DO_MANIFESTO")
                    if manifest_data.get("campos") != 25:
                        integrity_errors.append("CONTAGEM_CAMPOS_DIVERGE")
                if not integrity_errors:
                    print(f"SEM_MUDANCA: {name} raw_sha256={tmp_sha} normalized_sha256={normalized_sha}")
                    return "UNCHANGED"

                CONFLICT_DIR.mkdir(parents=True, exist_ok=True)
                conflict = {
                    "schema_version": "1.0.0",
                    "tipo": "CONFLITO_INTEGRIDADE_COTAHIST_DIARIO",
                    "status": "NAO_PROMOVIDO",
                    "data_referencia": iso_date,
                    "source": "B3",
                    "url": url,
                    "raw_sha256_canonico": existing_sha,
                    "normalized_file": str(norm_out.relative_to(ROOT)).replace("\\\\", "/"),
                    "normalized_sha256_fisico": normalized_sha,
                    "normalized_sha256_manifesto": manifest_data.get("normalized_sha256") if manifest_data else None,
                    "manifest_file": str(manifest_out.relative_to(ROOT)).replace("\\\\", "/"),
                    "erros": integrity_errors,
                    "detectado_em_utc": datetime.now(timezone.utc).isoformat(),
                    "decisao": "Preservar os artefactos canónicos e exigir revisão; não reescrever dados automaticamente."
                }
                conflict_path = CONFLICT_DIR / f"{name}_INTEGRIDADE_{normalized_sha[:12]}.json"
                conflict_path.write_text(json.dumps(conflict, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
                print(f"CONFLITO_INTEGRIDADE_NAO_PROMOVIDO: {name} erros={integrity_errors}")
                return "CONFLICT"

            if existing_sha != tmp_sha:
                # Fail closed: uma correção da fonte não pode substituir silenciosamente o RAW já validado.
                CONFLICT_DIR.mkdir(parents=True, exist_ok=True)
                conflict = {
                    "schema_version": "1.0.0",
                    "tipo": "CONFLITO_HASH_FONTE_COTAHIST_DIARIO",
                    "status": "NAO_PROMOVIDO",
                    "data_referencia": iso_date,
                    "source": "B3",
                    "url": url,
                    "raw_canonico_preservado": str(raw_out.relative_to(ROOT)).replace("\\\\", "/"),
                    "raw_sha256_canonico": existing_sha,
                    "raw_sha256_recebido": tmp_sha,
                    "detectado_em_utc": datetime.now(timezone.utc).isoformat(),
                    "decisao": "Preservar versão canónica e exigir revisão formal antes de promover correção."
                }
                conflict_path = CONFLICT_DIR / f"{name}_{existing_sha[:12]}_{tmp_sha[:12]}.json"
                conflict_path.write_text(json.dumps(conflict, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                print(f"CONFLITO_FONTE_NAO_PROMOVIDO: {name} canonico={existing_sha} recebido={tmp_sha}")
                return "CONFLICT"

        tmp_path.replace(raw_out)

        subprocess.run(
            [
                "python",
                "scripts/ingestao/normalize_cotahist.py",
                "--zip",
                str(raw_out),
                "--output",
                str(norm_out),
            ],
            cwd=ROOT,
            check=True,
        )

        rows = 0
        first_date = None
        last_date = None
        with norm_out.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows += 1
                d = row["data_pregao"]
                first_date = d if first_date is None else min(first_date, d)
                last_date = d if last_date is None else max(last_date, d)

        manifest = {
            "schema_version": "1.0.0",
            "status": "VALIDADO",
            "tipo": "DIARIO",
            "data_referencia": iso_date,
            "parser_version": PARSER_VERSION,
            "source": "B3",
            "url": url,
            "raw_file": str(raw_out.relative_to(ROOT)).replace("\\", "/"),
            "raw_sha256": tmp_sha,
            "normalized_file": str(norm_out.relative_to(ROOT)).replace("\\", "/"),
            "normalized_sha256": sha256(norm_out),
            "linhas_normalized": rows,
            "campos": 25,
            "primeira_data": first_date,
            "ultima_data": last_date,
            "adquirido_em_utc": datetime.now(timezone.utc).isoformat(),
        }
        manifest_out.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"IMPORTADO: {name} linhas={rows} sha256={tmp_sha}")
        return "IMPORTED"
    finally:
        tmp_path.unlink(missing_ok=True)


def main() -> None:
    today = datetime.now(ZoneInfo("America/Sao_Paulo")).date()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    NORM_DIR.mkdir(parents=True, exist_ok=True)
    MAN_DIR.mkdir(parents=True, exist_ok=True)
    RUN_DIR.mkdir(parents=True, exist_ok=True)

    results = {}
    for offset in range(BACKFILL_DAYS):
        ref_date = today - timedelta(days=offset)
        results[ref_date.isoformat()] = import_day(ref_date)

    conflicts = [day for day, status in results.items() if status == "CONFLICT"]
    run_report = {
        "schema_version": "1.0.0",
        "tipo": "EXECUCAO_IMPORTACAO_COTAHIST_DIARIO",
        "executado_em_utc": datetime.now(timezone.utc).isoformat(),
        "data_referencia_local": today.isoformat(),
        "janela_backfill_dias": BACKFILL_DAYS,
        "resultados": results,
        "dias_com_conflito": conflicts,
        "status": "CONFLITO_FONTE_NAO_PROMOVIDO" if conflicts else "EXECUCAO_SEM_CONFLITOS",
        "regra": "Nenhum RAW canónico é substituído se o hash da fonte divergir; revisão formal necessária."
    }
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = RUN_DIR / f"COTAHIST_DIARIO_EXECUCAO_{stamp}.json"
    report_path.write_text(json.dumps(run_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("RESUMO_BACKFILL=" + json.dumps(results, ensure_ascii=False, sort_keys=True))
    print(f"RELATORIO_EXECUCAO={report_path.relative_to(ROOT)}")
    print(f"CONFLITOS_FONTE={len(conflicts)}")


if __name__ == "__main__":
    main()
