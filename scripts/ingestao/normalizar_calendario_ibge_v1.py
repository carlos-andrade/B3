#!/usr/bin/env python3
"""Normalizador V1 do calendário conjuntural IBGE.

Entrada: snapshot estruturado/raw produzido pela captura.
Saída: JSON NORMALIZED com IDs determinísticos e campos de auditoria.
"""

from __future__ import annotations
import hashlib
import json
from pathlib import Path

REQUIRED = {
    "event_id", "event_name", "event_code", "country", "reference_period",
    "scheduled_date", "scheduled_time", "event_time_status", "status", "importance"
}

def deterministic_id(event: dict) -> str:
    basis = "|".join(str(event.get(k, "")) for k in (
        "source", "event_name", "reference_period", "scheduled_date"
    ))
    return hashlib.sha256(basis.encode("utf-8")).hexdigest()[:24]

def normalize(input_path: Path, output_path: Path) -> None:
    data = json.loads(input_path.read_text(encoding="utf-8"))
    source = data["source"]
    events = []

    for raw in data["events"]:
        event = dict(raw)
        event["source"] = source
        event["source_url"] = data["source_url"]
        event["timezone"] = data.get("timezone", "America/Sao_Paulo")
        event["event_id"] = deterministic_id(event)
        missing = REQUIRED - event.keys()
        if missing:
            raise ValueError(f"Campos obrigatórios ausentes: {sorted(missing)}")
        events.append(event)

    output = {
        "schema_version": "1.0",
        "source": source,
        "source_url": data["source_url"],
        "timezone": data.get("timezone", "America/Sao_Paulo"),
        "retrieved_at": data["retrieved_at"],
        "event_count": len(events),
        "events": events,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    args = p.parse_args()
    normalize(args.input, args.output)
