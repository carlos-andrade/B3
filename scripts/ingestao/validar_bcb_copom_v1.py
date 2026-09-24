#!/usr/bin/env python3
"""Valida dataset normalizado BCB/Copom."""

import json
import sys
from datetime import date

ALLOWED_STATUS = {"SCHEDULED", "RELEASED", "CANCELLED", "REVISED"}
ALLOWED_TIME_STATUS = {"EXACT", "APPROXIMATE", "UNKNOWN"}
REQUIRED = {"event_id", "event_name", "event_code", "scheduled_date", "event_time_status", "status"}

def main(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    errors = []
    events = data.get("events", [])
    ids = set()

    for i, e in enumerate(events, 1):
        missing = REQUIRED - e.keys()
        if missing:
            errors.append(f"evento {i}: campos ausentes {sorted(missing)}")
        if e.get("event_id") in ids:
            errors.append(f"evento {i}: event_id duplicado {e.get('event_id')}")
        ids.add(e.get("event_id"))
        try:
            date.fromisoformat(e["scheduled_date"])
        except Exception:
            errors.append(f"evento {i}: scheduled_date inválida")
        if e.get("status") not in ALLOWED_STATUS:
            errors.append(f"evento {i}: status inválido")
        if e.get("event_time_status") not in ALLOWED_TIME_STATUS:
            errors.append(f"evento {i}: event_time_status inválido")
        if e.get("event_time_status") == "EXACT" and not e.get("scheduled_time"):
            errors.append(f"evento {i}: EXACT sem scheduled_time")

    if data.get("event_count") not in (None, len(events)):
        errors.append("event_count não corresponde ao número de eventos")

    if errors:
        for err in errors:
            print("ERROR:", err)
        return 1

    print(f"OK: {len(events)} eventos BCB/Copom validados")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
