#!/usr/bin/env python3
"""Auditoria estrutural do calendario COTAHIST 1987."""
from pathlib import Path
import csv, datetime, json
ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "dados/cotahist/normalized/anual/COTAHIST_A1987.csv"
OUT = ROOT / "dados/cotahist/quality/COTAHIST_1987_AUDITORIA_CALENDARIO_V1.json"
dates=[]
with CSV_PATH.open("r",encoding="utf-8",newline="") as f:
    for row in csv.DictReader(f): dates.append(row["data_pregao"])
valid=[]; invalid=[]
for s in dates:
    try:
        d=datetime.datetime.strptime(s,"%Y-%m-%d").date(); valid.append(d)
        if d.weekday()>=5: invalid.append(s)
    except ValueError: invalid.append(s)
unique=sorted(set(valid)); us=set(unique); gaps=[]
if unique:
    cur=unique[0]
    while cur<=unique[-1]:
        if cur.weekday()<5 and cur not in us: gaps.append(cur.isoformat())
        cur+=datetime.timedelta(days=1)
out_of_order=sum(1 for a,b in zip(dates,dates[1:]) if b<a)
result={
 "schema_version":"1.0.0","status":"AUDITORIA_CALENDARIO_1987",
 "records":len(dates),"first_date":min(dates) if dates else None,
 "last_date":max(dates) if dates else None,"valid_date_count":len(valid),
 "invalid_or_weekend_dates":len(invalid),"distinct_trading_dates":len(unique),
 "weekday_gaps_candidate_non_trading_days":gaps,"out_of_order_records":out_of_order,
 "gates":{"records_positive":len(dates)>0,"all_dates_valid":len(valid)==len(dates),
 "no_weekend_dates":len(invalid)==0,"chronological_bounds":bool(unique) and unique[0].isoformat()==min(dates) and unique[-1].isoformat()==max(dates),
 "records_chronological":out_of_order==0,"distinct_dates_positive":len(unique)>0},
 "fail_closed":False,
 "note":"Datas repetidas entre ativos sao esperadas. Lacunas em dias uteis sao apenas candidatos a dias sem pregao; nao sao classificadas como feriados sem fonte historica primaria."
}
result["fail_closed"]=all(result["gates"].values())
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
if not result["fail_closed"]: raise SystemExit(1)
