#!/usr/bin/env python3
"""FASE 08C - Reconstrucao interna de padroes de negociacao em torno de dias ausentes."""
from __future__ import annotations
import json, zipfile
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
AUDIT = Path("dados/cotahist/quality/COTAHIST_1986_AUDITORIA_CALENDARIO_V1.json")
OUT = Path("dados/cotahist/quality/COTAHIST_1986_EVIDENCIA_PADROES_AUSENCIA_V1.json")
WINDOW = 3

def parse_date(s):
    return datetime.strptime(s, "%Y%m%d").date()

def read_rows():
    by_date = defaultdict(lambda: {"rows": 0, "codbdi": set(), "codneg": set(), "tpmerc": set()})
    with zipfile.ZipFile(RAW) as z:
        names = [n for n in z.namelist() if not n.endswith("/")]
        if not names:
            raise RuntimeError("Nenhum membro de dados encontrado no ZIP RAW")
        with z.open(names[0]) as fh:
            for raw in fh:
                if not raw.startswith(b"01"):
                    continue
                line = raw.decode("latin1").rstrip("\r\n")
                d = parse_date(line[2:10])
                k = d.isoformat()
                by_date[k]["rows"] += 1
                by_date[k]["codbdi"].add(line[10:12])
                by_date[k]["codneg"].add(line[12:24].strip())
                by_date[k]["tpmerc"].add(line[24:27])
    return by_date

def nearest_observed(by_date, target, direction):
    d = target + timedelta(days=direction)
    while d.isoformat() not in by_date:
        d += timedelta(days=direction)
    return d

def snapshot(by_date, d):
    x = by_date.get(d.isoformat())
    if not x:
        return {"date": d.isoformat(), "observed": False, "rows": 0, "codbdi": 0, "codneg": 0, "tpmerc": 0}
    return {"date": d.isoformat(), "observed": True, "rows": x["rows"],
            "codbdi": len(x["codbdi"]), "codneg": len(x["codneg"]), "tpmerc": len(x["tpmerc"])}

def main():
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    missing = []
    for gap in audit["long_gaps"]:
        for s in gap["missing_calendar_dates"]:
            d = date.fromisoformat(s)
            if d.weekday() < 5:
                missing.append(d)
    missing = sorted(set(missing))
    by_date = read_rows()
    out = []
    for d in missing:
        prev = nearest_observed(by_date, d, -1)
        nxt = nearest_observed(by_date, d, +1)
        days = [snapshot(by_date, d + timedelta(days=off)) for off in range(-WINDOW, WINDOW + 1)]
        nearby_obs = [x for x in days if x["observed"]]
        prev_s, next_s = snapshot(by_date, prev), snapshot(by_date, nxt)
        out.append({
            "missing_date": d.isoformat(),
            "weekday": d.strftime("%A"),
            "previous_observed": prev_s,
            "next_observed": next_s,
            "calendar_distance_prev_days": (d-prev).days,
            "calendar_distance_next_days": (nxt-d).days,
            "window_minus_plus_3_calendar_days": days,
            "local_pattern": {
                "observed_days_in_window": len(nearby_obs),
                "row_count_min_observed": min(x["rows"] for x in nearby_obs),
                "row_count_max_observed": max(x["rows"] for x in nearby_obs),
                "row_count_prev_next_mean": round((prev_s["rows"] + next_s["rows"]) / 2, 2),
                "broad_activity_before_after": prev_s["rows"] >= 100 and next_s["rows"] >= 100
            },
            "interpretation": "EVIDENCIA_COMPATIVEL_COM_CONTINUIDADE_DE_ATIVIDADE_AO_REDOR_DA_AUSENCIA",
            "session_status": "NAO_DETERMINADO_SEM_FONTE_HISTORICA_OFICIAL"
        })
    result = {
        "schema_version": "1.0.0",
        "status": "FASE08C_PADROES_NEGOCIACAO_AUSENCIAS_1986",
        "generated_at_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "source": {"raw_file": RAW.name, "audit_artifact": str(AUDIT), "window_calendar_days": WINDOW},
        "candidate_count": len(missing),
        "candidates": out,
        "governance": {
            "raw_unchanged": True,
            "normalized_unchanged": True,
            "no_historical_calendar_inference": True,
            "no_missing_session_assertion": True,
            "evidence_is_observational": True
        }
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
