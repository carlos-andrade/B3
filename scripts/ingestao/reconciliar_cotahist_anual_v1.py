#!/usr/bin/env python3
"""Consolida COTAHIST 2026: snapshot anual B3 + incrementos diarios validados."""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YEAR = 2026
ANNUAL = ROOT / f"dados/cotahist/normalized/COTAHIST_A{YEAR}.csv"
MANIFEST = ROOT / f"dados/cotahist/normalized/manifests/COTAHIST_A{YEAR}_quality.json"
DAILY_DIR = ROOT / "dados/cotahist/normalized/diario"
DAILY_MAN_DIR = ROOT / "dados/cotahist/normalized/manifests/diario"
DATASET = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if not ANNUAL.exists():
        raise SystemExit(f"ANUAL_AUSENTE: {ANNUAL}")
    meta = json.loads(MANIFEST.read_text(encoding="utf-8"))
    annual_last = meta["ultima_data"]
    annual_rows = int(meta["linhas_normalized"])

    candidates = []
    increment_rows = 0
    first_increment = None
    last_increment = annual_last

    for manifest_path in sorted(DAILY_MAN_DIR.glob("COTAHIST_D*_quality.json")):
        m = json.loads(manifest_path.read_text(encoding="utf-8"))
        if m.get("status") != "VALIDADO":
            continue
        if m.get("ultima_data", "") <= annual_last:
            continue
        daily_path = ROOT / m["normalized_file"]
        if not daily_path.exists():
            raise SystemExit(f"NORMALIZED_DIARIO_AUSENTE: {daily_path}")
        candidates.append((daily_path, m))
        increment_rows += int(m["linhas_normalized"])
        first_increment = m["primeira_data"] if first_increment is None else min(first_increment, m["primeira_data"])
        last_increment = max(last_increment, m["ultima_data"])

    if not candidates:
        print(f"SEM_INCREMENTO_ANUAL: ultima_data={annual_last}")
        return

    tmp = ANNUAL.with_suffix(".csv.tmp")
    with ANNUAL.open("rb") as src, tmp.open("wb") as dst:
        shutil.copyfileobj(src, dst, length=1024 * 1024)
        for daily_path, _ in candidates:
            with daily_path.open("rb") as src_daily:
                src_daily.readline()  # remove header
                dst.write(src_daily.read())
    tmp.replace(ANNUAL)

    new_manifest = {
        "schema_version": "1.1.0",
        "status": "VALIDADO_CONSOLIDADO",
        "tipo": "ANUAL_CONSOLIDADO",
        "ano": YEAR,
        "source": "B3",
        "snapshot_anual": "dados/cotahist/raw/anual/COTAHIST_A2026.ZIP",
        "snapshot_ultima_data": annual_last,
        "incrementos_diarios_validados": [
            str((DAILY_MAN_DIR / f"COTAHIST_D{m['data_referencia'].replace('-', '')}_quality.json").relative_to(ROOT)).replace("\\", "/")
            for _, m in candidates
        ],
        "incrementos_linhas": increment_rows,
        "primeira_data": meta["primeira_data"],
        "ultima_data": last_increment,
        "linhas_normalized": annual_rows + increment_rows,
        "campos": meta["campos"],
        "normalized_sha256": sha256(ANNUAL),
        "consolidado_em_utc": datetime.now(timezone.utc).isoformat(),
        "regra": "RAW anual preservado; NORMALIZED consolidado por snapshot anual + diarios VALIDADO posteriores.",
    }
    MANIFEST.write_text(json.dumps(new_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    dataset = json.loads(DATASET.read_text(encoding="utf-8"))
    for record in dataset.get("records", []):
        if record.get("ano") == YEAR:
            record.update({
                "normalized_sha256": new_manifest["normalized_sha256"],
                "linhas_normalized": new_manifest["linhas_normalized"],
                "primeira_data": new_manifest["primeira_data"],
                "ultima_data": new_manifest["ultima_data"],
                "quality_manifest": str(MANIFEST.relative_to(ROOT)).replace("\\", "/"),
                "status_consolidacao": "CONSOLIDADO_ANUAL_PLUS_DIARIO",
                "incrementos_diarios_validados": new_manifest["incrementos_diarios_validados"],
            })
            break
    DATASET.write_text(json.dumps(dataset, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"CONSOLIDADO_ANUAL: antes={annual_last} depois={last_increment} incrementos={increment_rows}")


if __name__ == "__main__":
    main()
