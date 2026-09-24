#!/usr/bin/env python3
"""Auditoria de calendario observável no COTAHIST 1986; somente leitura do RAW."""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

def parse_date(raw: bytes) -> date | None:
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    s = b[2:10].decode("latin-1", errors="replace").strip()
    if len(s) != 8 or not s.isdigit():
        return None
    try:
        return date(int(s[:4]), int(s[4:6]), int(s[6:8]))
    except ValueError:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()

    counts = Counter()
    raw_sha = hashlib.sha256()
    total_lines = valid_type01 = invalid_dates = 0

    with zipfile.ZipFile(a.zip) as z:
        members = [x for x in z.namelist() if not x.endswith("/")]
        if len(members) != 1:
            raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                total_lines += 1
                raw_sha.update(raw)
                d = parse_date(raw)
                if d is None:
                    continue
                valid_type01 += 1
                counts[d] += 1

    dates = sorted(counts)
    gaps = []
    for prev, nxt in zip(dates, dates[1:]):
        delta = (nxt - prev).days
        if delta > 4:
            missing = [(prev + timedelta(days=i)).isoformat() for i in range(1, delta)]
            gaps.append({
                "from": prev.isoformat(),
                "to": nxt.isoformat(),
                "calendar_days_between": delta,
                "missing_calendar_dates": missing,
            })

    weekday_counts = Counter(d.strftime("%A") for d in dates)
    weekend_observed = [d.isoformat() for d in dates if d.weekday() >= 5]

    out = {
        "schema_version": "1.0.0",
        "status": "AUDITORIA_CALENDARIO_OBSERVAVEL_COTAHIST_1986",
        "raw_file": Path(a.zip).name,
        "raw_sha256_stream": raw_sha.hexdigest(),
        "total_lines": total_lines,
        "valid_type_01_rows": valid_type01,
        "unique_trading_dates": len(dates),
        "first_trading_date_observed": dates[0].isoformat() if dates else None,
        "last_trading_date_observed": dates[-1].isoformat() if dates else None,
        "weekday_counts": dict(sorted(weekday_counts.items())),
        "weekend_dates_observed": weekend_observed,
        "long_gaps_threshold_days_exclusive": 4,
        "long_gaps_count": len(gaps),
        "long_gaps": gaps,
        "records_per_date_min": min(counts.values(), default=0),
        "records_per_date_max": max(counts.values(), default=0),
        "records_per_date_total": sum(counts.values()),
        "date_record_counts": {d.isoformat(): counts[d] for d in dates},
    }

    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    Path(a.output).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": out["status"],
        "unique_trading_dates": out["unique_trading_dates"],
        "first_trading_date_observed": out["first_trading_date_observed"],
        "last_trading_date_observed": out["last_trading_date_observed"],
        "weekend_dates_observed": out["weekend_dates_observed"],
        "long_gaps_count": out["long_gaps_count"],
        "long_gaps": out["long_gaps"],
        "records_per_date_min": out["records_per_date_min"],
        "records_per_date_max": out["records_per_date_max"],
        "records_per_date_total": out["records_per_date_total"],
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
