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

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "dados/cotahist/raw/diario"
NORM_DIR = ROOT / "dados/cotahist/normalized/diario"
MAN_DIR = ROOT / "dados/cotahist/normalized/manifests/diario"
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
        if raw_out.exists() and sha256(raw_out) == tmp_sha and norm_out.exists() and manifest_out.exists():
            print(f"SEM_MUDANCA: {name} sha256={tmp_sha}")
            return "UNCHANGED"

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
            "parser_version": "1.1.0",
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

    results = {}
    for offset in range(BACKFILL_DAYS):
        ref_date = today - timedelta(days=offset)
        results[ref_date.isoformat()] = import_day(ref_date)

    print("RESUMO_BACKFILL=" + json.dumps(results, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
