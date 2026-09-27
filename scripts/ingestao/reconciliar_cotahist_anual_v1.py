#!/usr/bin/env python3
"""Reconcilia o COTAHIST anual de 2026 com os pregões diários validados.

A camada RAW anual permanece imutável como snapshot da fonte B3. A camada
NORMALIZED anual passa a representar o dataset consolidado: anual B3 +
incrementos diários validados posteriores ao último pregão do snapshot.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YEAR = 2026
ANNUAL = ROOT / f"dados/cotahist/normalized/COTAHIST_A{YEAR}.csv"
ANNUAL_MANIFEST = ROOT / f"dados/cotahist/normalized/manifests/COTAHIST_A{YEAR}_quality.json"
DAILY_DIR = ROOT / "dados/cotahist/normalized/diario"
DAILY_MAN_DIR = ROOT / "dados/cotahist/normalized/manifests/diario"
SOURCE_DATASET = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv(path: Path):
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def main() -> None:
    if not ANNUAL.exists():
        raise SystemExit(f"ANUAL_AUSENTE: {ANNUAL}")
    fields, annual_rows = read_csv(ANNUAL)
    if not fields or "data_pregao" not in fields:
        raise SystemExit("SCHEMA_ANUAL_INVALIDO")

    annual_last = max(r["data_pregao"] for r in annual_rows)
    daily_files = sorted(DAILY_DIR.glob("COTAHIST_D*.csv"))
    increments = []
    used_manifests = []

    for path in daily_files:
        _, rows = read_csv(path)
        if not rows:
            continue
        first = min(r["data_pregao"] for r in rows)
        last = max(r["data_pregao"] for r in rows)
        if last <= annual_last:
            continue

        manifest = DAILY_MAN_DIR / f"{path.stem}_quality.json"
        if not manifest.exists():
            raise SystemExit(f"MANIFEST_DIARIO_AUSENTE: {manifest}")
        meta = json.loads(manifest.read_text(encoding="utf-8"))
        if meta.get("status") != "VALIDADO":
            raise SystemExit(f"MANIFEST_DIARIO_NAO_VALIDADO: {manifest}")

        for row in rows:
            if row["data_pregao"] > annual_last:
                increments.append(row)
        used_manifests.append(str(manifest.relative_to(ROOT)).replace("\\", "/"))

    if not increments:
        print(f"SEM_INCREMENTO_ANUAL: ultima_data={annual_last}")
        return

    # Evita duplicidade por chave completa e ordena cronologicamente.
    seen = {tuple(r.get(k, "") for k in fields) for r in annual_rows}
    new_rows = []
    for row in increments:
        key = tuple(row.get(k, "") for k in fields)
        if key not in seen:
            seen.add(key)
            new_rows.append(row)

    all_rows = annual_rows + new_rows
    all_rows.sort(key=lambda r: tuple(r.get(k, "") for k in ("data_pregao", "codneg", "tpmerc", "codbdi")))

    tmp = ANNUAL.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(all_rows)
    tmp.replace(ANNUAL)

    new_last = max(r["data_pregao"] for r in all_rows)
    manifest = {
        "schema_version": "1.1.0",
        "status": "VALIDADO_CONSOLIDADO",
        "tipo": "ANUAL_CONSOLIDADO",
        "ano": YEAR,
        "source": "B3",
        "snapshot_anual": "dados/cotahist/raw/anual/COTAHIST_A2026.ZIP",
        "snapshot_ultima_data": annual_last,
        "incrementos_diarios_validados": used_manifests,
        "incrementos_linhas": len(new_rows),
        "primeira_data": min(r["data_pregao"] for r in all_rows),
        "ultima_data": new_last,
        "linhas_normalized": len(all_rows),
        "campos": len(fields),
        "normalized_sha256": sha256(ANNUAL),
        "consolidado_em_utc": datetime.now(timezone.utc).isoformat(),
        "regra": "RAW anual preservado; NORMALIZED consolidado por snapshot anual + diarios VALIDADO posteriores.",
    }
    ANNUAL_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    dataset = json.loads(SOURCE_DATASET.read_text(encoding="utf-8"))
    for record in dataset.get("records", []):
        if record.get("ano") == YEAR:
            record["normalized_sha256"] = manifest["normalized_sha256"]
            record["linhas_normalized"] = manifest["linhas_normalized"]
            record["primeira_data"] = manifest["primeira_data"]
            record["ultima_data"] = manifest["ultima_data"]
            record["quality_manifest"] = str(ANNUAL_MANIFEST.relative_to(ROOT)).replace("\\", "/")
            record["status_consolidacao"] = "CONSOLIDADO_ANUAL_PLUS_DIARIO"
            record["incrementos_diarios_validados"] = used_manifests
            break
    SOURCE_DATASET.write_text(json.dumps(dataset, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"CONSOLIDADO_ANUAL: antes={annual_last} depois={new_last} incrementos={len(new_rows)}")


if __name__ == "__main__":
    main()
