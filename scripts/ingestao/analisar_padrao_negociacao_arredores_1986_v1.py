#!/usr/bin/env python3
"""Reconstrói evidência interna em torno dos dias úteis ausentes do COTAHIST 1986.

Não classifica feriados/pregões. Mede apenas continuidade observável antes/depois.
"""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

CANDIDATES = [
    "1986-02-10","1986-02-11","1986-02-12","1986-02-28",
    "1986-03-03","1986-03-27","1986-03-28","1986-04-21",
    "1986-05-01","1986-05-26","1986-12-24","1986-12-25"
]

def field(b, a, z):
    return b[a-1:z].decode("latin-1", errors="replace").strip()

def parse_row(raw):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    ds = b[2:10].decode("latin-1", errors="replace").strip()
    try:
        d = date.fromisoformat(f"{ds[:4]}-{ds[4:6]}-{ds[6:8]}")
    except Exception:
        return None
    return {
        "date": d.isoformat(),
        "codbdi": field(b,11,12),
        "codneg": field(b,13,24),
        "tpmerc": field(b,25,27),
        "raw_sha256": hashlib.sha256(b).hexdigest(),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    per_date = defaultdict(lambda: {"rows":0,"codbdi":set(),"tpmerc":set(),"codneg":set()})
    raw_sha = hashlib.sha256()
    with zipfile.ZipFile(args.zip) as z:
        members = [x for x in z.namelist() if not x.endswith("/")]
        if len(members) != 1:
            raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                raw_sha.update(raw)
                r = parse_row(raw)
                if not r:
                    continue
                x = per_date[r["date"]]
                x["rows"] += 1
                x["codbdi"].add(r["codbdi"])
                x["tpmerc"].add(r["tpmerc"])
                x["codneg"].add(r["codneg"])

    dates = sorted(per_date)
    idx = {d:i for i,d in enumerate(dates)}

    def snap(ds):
        x = per_date.get(ds)
        if not x:
            return {"data":ds,"observed":False,"records":0,"distinct_codbdi":0,"distinct_tpmerc":0,"distinct_codneg":0}
        return {"data":ds,"observed":True,"records":x["rows"],
                "distinct_codbdi":len(x["codbdi"]),"distinct_tpmerc":len(x["tpmerc"]),
                "distinct_codneg":len(x["codneg"])}

    rows=[]
    for target in CANDIDATES:
        d=date.fromisoformat(target)
        prev_dates=[x for x in dates if x < target]
        next_dates=[x for x in dates if x > target]
        prev=prev_dates[-1] if prev_dates else None
        nxt=next_dates[0] if next_dates else None
        pi=idx.get(prev,-1); ni=idx.get(nxt,-1)
        before=[snap(x) for x in dates[max(0,pi-2):pi+1]] if pi>=0 else []
        after=[snap(x) for x in dates[ni:min(len(dates),ni+3)]] if ni>=0 else []
        before_rows=[x["records"] for x in before]
        after_rows=[x["records"] for x in after]
        prev_x=per_date.get(prev,{})
        next_x=per_date.get(nxt,{})
        gap_days=(date.fromisoformat(nxt)-date.fromisoformat(prev)).days if prev and nxt else None
        row={
            "data":target,
            "weekday":d.strftime("%A"),
            "observed":False,
            "previous_observed_date":prev,
            "next_observed_date":nxt,
            "calendar_gap_between_observed_neighbors":gap_days,
            "days_from_previous_to_candidate":(d-date.fromisoformat(prev)).days if prev else None,
            "days_from_candidate_to_next":(date.fromisoformat(nxt)-d).days if nxt else None,
            "previous_observed":snap(prev) if prev else None,
            "next_observed":snap(nxt) if nxt else None,
            "window_before":before,
            "window_after":after,
            "continuity_metrics":{
                "previous_and_next_both_observed": bool(prev and nxt),
                "records_previous": before_rows[-1] if before_rows else 0,
                "records_next": after_rows[0] if after_rows else 0,
                "neighbor_record_ratio_next_over_previous": (
                    round(after_rows[0]/before_rows[-1],6) if before_rows and after_rows and before_rows[-1] else None
                ),
                "broad_activity_before": bool(before_rows and before_rows[-1] >= 500),
                "broad_activity_after": bool(after_rows and after_rows[0] >= 500),
                "distinct_codbdi_previous": len(prev_x.get("codbdi",set())),
                "distinct_codbdi_next": len(next_x.get("codbdi",set())),
                "distinct_tpmerc_previous": len(prev_x.get("tpmerc",set())),
                "distinct_tpmerc_next": len(next_x.get("tpmerc",set())),
                "distinct_codneg_previous": len(prev_x.get("codneg",set())),
                "distinct_codneg_next": len(next_x.get("codneg",set())),
            },
            "interpretation":"EVIDENCIA_COMPATIVEL_COM_CONTINUIDADE_DE_ATIVIDADE_AO_REDOR_DA_DATA" if prev and nxt else "EVIDENCIA_INSUFICIENTE",
            "classification_authority":"NAO_CLASSIFICA_SESSAO; requer fonte historica externa"
        }
        rows.append(row)

    out={
      "schema_version":"1.0.0",
      "status":"FASE08C_PADRAO_NEGOCIACAO_ARREDORES_1986",
      "raw_file":Path(args.zip).name,
      "raw_sha256_stream":raw_sha.hexdigest(),
      "evidence_input":args.evidence,
      "candidate_count":len(rows),
      "candidates":rows,
      "governance":{
        "raw_unchanged":True,
        "normalized_unchanged":True,
        "no_session_inference":True,
        "no_holiday_inference":True,
        "internal_pattern_is_supporting_evidence_only":True
      }
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":out["status"],"candidate_count":len(rows),"raw_sha256_stream":out["raw_sha256_stream"]},ensure_ascii=False))

if __name__=="__main__":
    main()
