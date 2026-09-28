#!/usr/bin/env python3
"""Auditoria estrutural do calendario COTAHIST 1987.

Nao certifica feriados historicos por inferencia: verifica datas validas,
ordem, duplicidade e presenca em fim de semana. Falha se houver quebra
estrutural nos registros.
"""
from pathlib import Path
import csv, datetime, json

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "dados/cotahist/normalized/anual/COTAHIST_A1987.csv"
OUT = ROOT / "dados/cotahist/quality/COTAHIST_1987_AUDITORIA_CALENDARIO_V1.json"

dates = []
with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        dates.append(row["data_pregao"])

valid = []
invalid = []
for s in dates:
    try:
        d = datetime.datetime.strptime(s, "%Y-%m-%d").date()
        valid.append(d)
        if d.weekday() >= 5:
            invalid.append(s)
    except ValueError:
        invalid.append(s)

unique = sorted(set(valid))
duplicate_dates = len(valid) - len(unique)
gaps = []
if unique:
    cur = unique[0]
    while cur <= unique[-1]:
        if cur.weekday() < 5 and cur not in set(unique):
            gaps.append(cur.isoformat())
        cur += datetime.timedelta(days=1)

result = {
    "schema_version": "1.0.0",
    "status": "AUDITORIA_CALENDARIO_1987",
    "records": len(dates),
    "first_date": min(dates) if dates else None,
    "last_date": max(dates) if dates else None,
    "valid_date_count": len(valid),
    "invalid_or_weekend_dates": len(invalid),
    "duplicate_date_records": duplicate_dates,
    "distinct_trading_dates": len(unique),
    "weekday_gaps": gaps,
    "gates": {
        "records_positive": len(dates) > 0,
        "all_dates_valid": len(valid) == len(dates),
        "no_weekend_dates": len(invalid) == 0,
        "no_duplicate_dates": duplicate_dates == 0,
        "chronological_bounds": bool(unique) and unique[0].isoformat() == min(dates) and unique[-1].isoformat() == max(dates),
        "no_weekday_gaps": len(gaps) == 0,
    },
    "note": "Auditoria estrutural. A ausencia de um dia util nao e tratada como feriado confirmado sem fonte historica primaria."
}
result["fail_closed"] = all(result["gates"].values())
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
if not result["fail_closed"]:
    raise SystemExit(1)
