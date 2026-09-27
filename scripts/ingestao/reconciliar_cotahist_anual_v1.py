#!/usr/bin/env python3
"""Atualiza o índice oficial corrente do COTAHIST sem alterar snapshots anuais."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YEAR = 2026
ANNUAL_MANIFEST = ROOT / f"dados/cotahist/normalized/manifests/COTAHIST_A{YEAR}_quality.json"
DAILY_MAN_DIR = ROOT / "dados/cotahist/normalized/manifests/diario"
OUT = ROOT / "dados/cotahist/oficial/COTAHIST_DATASET_ATUAL_V1.1.json"


def main() -> None:
    annual = json.loads(ANNUAL_MANIFEST.read_text(encoding="utf-8"))
    last = annual["ultima_data"]
    daily = []

    for path in sorted(DAILY_MAN_DIR.glob("COTAHIST_D*_quality.json")):
        m = json.loads(path.read_text(encoding="utf-8"))
        if m.get("status") == "VALIDADO" and m.get("ultima_data", "") > last:
            daily.append({
                "data_referencia": m["data_referencia"],
                "primeira_data": m["primeira_data"],
                "ultima_data": m["ultima_data"],
                "linhas_normalized": m["linhas_normalized"],
                "raw_file": m["raw_file"],
                "normalized_file": m["normalized_file"],
                "raw_sha256": m["raw_sha256"],
                "normalized_sha256": m["normalized_sha256"],
                "quality_manifest": str(path.relative_to(ROOT)).replace("\\", "/"),
            })

    current_last = max([last] + [x["ultima_data"] for x in daily])
    payload = {
        "schema_version": "1.1.0",
        "dataset_id": "COTAHIST_OFICIAL_ATUAL",
        "status": "VIGENTE",
        "status_frescor": "VALIDADO",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "B3",
        "ano_corrente": YEAR,
        "ultima_data": current_last,
        "composicao": {
            "snapshot_anual": {
                "normalized_file": annual["normalized_file"],
                "quality_manifest": str(ANNUAL_MANIFEST.relative_to(ROOT)).replace("\\", "/"),
                "ultima_data": last,
                "linhas_normalized": annual["linhas_normalized"],
                "normalized_sha256": annual["normalized_sha256"],
            },
            "incrementos_diarios": daily,
        },
        "regra": "Dataset corrente = snapshot anual B3 + todos os manifests diarios VALIDADO posteriores ao snapshot. O RAW anual permanece imutavel.",
        "fail_closed": True,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"INDICE_OFICIAL_ATUALIZADO: ultima_data={current_last} incrementos={len(daily)}")


if __name__ == "__main__":
    main()
