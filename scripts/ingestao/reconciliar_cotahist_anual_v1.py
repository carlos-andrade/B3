#!/usr/bin/env python3
"""Reconcilia COTAHIST anual 2026 com pregões diários validados, em streaming."""

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


def annual_last_date() -> tuple[list[str], str, int]:
    with ANNUAL.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        if not fields or "data_pregao" not in fields:
            raise SystemExit("SCHEMA_ANUAL_INVALIDO")
        last = ""
        rows = 0
        for row in reader:
            rows += 1
            if row["data_pregao"] > last:
                last = row["data_pregao"]
        return fields, last, rows


def main() -> None:
    if not ANNUAL.exists():
        raise SystemExit(f"ANUAL_AUSENTE: {ANNUAL}")

    fields, annual_last, annual_rows = annual_last_date()
    daily_inputs = []
    increment_rows = 0
    used_manifests = []

    for path in sorted(DAILY_DIR.glob("COTAHIST_D*.csv")):
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != fields:
                raise SystemExit(f"SCHEMA_DIARIO_INCOMPATIVEL: {path}")
            rows = list(reader)
        if not rows:
            continue
        last = max(r["data_pregao"] for r in rows)
        if last <= annual_last:
            continue
        manifest = DAILY_MAN_DIR / f"{path.stem}_quality.json"
        if not manifest.exists():
            raise SystemExit(f"MANIFEST_DIARIO_AUSENTE: {manifest}")
        meta = json.loads(manifest.read_text(encoding="utf-8"))
        if meta.get("status") != "VALIDADO":
            raise SystemExit(f"MANIFEST_DIARIO_NAO_VALIDADO: {manifest}")
        daily_inputs.append((path, rows))
        increment_rows += sum(1 for r in rows if r["data_pregao"] > annual_last)
        used_manifests.append(str(manifest.relative_to(ROOT)).replace("\\", "/"))

    if not daily_inputs:
        print(f"SEM_INCREMENTO_ANUAL: ultima_data={annual_last}")
        return

    tmp = ANNUAL.with_suffix(".csv.tmp")
    total = 0
    first = None
    last = None
    with ANNUAL.open(encoding="utf-8", newline="") as src, tmp.open("w", encoding="utf-8", newline="") as dst:
        reader = csv.DictReader(src)
        writer = csv.DictWriter(dst, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in reader:
            writer.writerow(row)
            total += 1
            d = row["data_pregao"]
            first = d if first is None else min(first, d)
            last = d if last is None else max(last, d)
        for path, rows in daily_inputs:
            for row in rows:
                if row["data_pregao"] > annual_last:
                    writer.writerow(row)
                    total += 1
                    d = row["data_pregao"]
                    first = d if first is None else min(first, d)
                    last = d if last is None else max(last, d)
    tmp.replace(ANNUAL)

    manifest = {
        "schema_version": "1.1.0",
        "status": "VALIDADO_CONSOLIDADO",
        "tipo": "ANUAL_CONSOLIDADO",
        "ano": YEAR,
        "source": "B3",
        "snapshot_anual": "dados/cotahist/raw/anual/COTAHIST_A2026.ZIP",
        "snapshot_ultima_data": annual_last,
        "incrementos_diarios_validados": used_manifests,
        "incrementos_linhas": increment_rows,
        "primeira_data": first,
        "ultima_data": last,
        "linhas_normalized": total,
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
    print(f"CONSOLIDADO_ANUAL: antes={annual_last} depois={last} incrementos={increment_rows}")


if __name__ == "__main__":
    main()
