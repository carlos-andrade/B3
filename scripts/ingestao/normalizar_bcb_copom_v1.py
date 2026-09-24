#!/usr/bin/env python3
"""Normalizador BCB/Copom V1.0: RAW JSON -> NORMALIZED JSON."""
from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = ("event_id","source","source_url","event_name","event_code","meeting_number","scheduled_date","timezone","status")

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def normalize(raw: dict, raw_path: Path) -> dict:
    if not isinstance(raw, dict): raise ValueError("RAW deve ser objeto JSON")
    events = raw.get("events", [])
    if not isinstance(events, list): raise ValueError("events deve ser lista")
    normalized = []
    for event in events:
        missing = [k for k in REQUIRED if k not in event]
        if missing: raise ValueError(f"evento {event.get('event_id')} sem campos: {missing}")
        e = dict(event)
        e.setdefault("scheduled_time", None)
        e.setdefault("event_time_status", "UNKNOWN")
        e["retrieved_at"] = datetime.now(timezone.utc).isoformat()
        e["source_hash"] = sha256_file(raw_path)
        e["evidence_path"] = str(raw_path)
        if e["event_time_status"] == "EXACT" and not e.get("scheduled_time"):
            raise ValueError(f"EXACT sem horário: {e['event_id']}")
        normalized.append(e)
    return {"schema_version":"1.0","source":"Banco Central do Brasil","normalized_at":datetime.now(timezone.utc).isoformat(),"events":normalized}

def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument("raw"); p.add_argument("output")
    a=p.parse_args()
    raw_path=Path(a.raw); output=Path(a.output)
    with raw_path.open("r",encoding="utf-8") as f: raw=json.load(f)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(normalize(raw,raw_path),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"OK: {output}")
    return 0

if __name__=="__main__": raise SystemExit(main())
