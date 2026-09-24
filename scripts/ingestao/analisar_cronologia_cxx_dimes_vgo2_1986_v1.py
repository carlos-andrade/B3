#!/usr/bin/env python3
import csv, hashlib, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT = Path("dados/cotahist/quality/COTAHIST_1986_FASE08E_CRONOLOGIA_V1.json")

def s(line, a, b):
    return line[a-1:b]

rows = []
with zipfile.ZipFile(RAW) as z:
    name = [n for n in z.namelist() if not n.endswith("/")][0]
    with z.open(name) as f:
        for n, raw in enumerate(f, 1):
            line = raw.decode("latin-1").rstrip("\r\n")
            if len(line) != 245 or line[:2] != "01":
                continue
            rows.append({
                "source_line": n,
                "date": s(line,3,10),
                "codbdi": s(line,11,12),
                "codneg": s(line,13,24).strip(),
                "tpmerc": s(line,25,27),
                "nomres": s(line,28,39).strip(),
                "especi": s(line,40,49).strip(),
                "prazot": s(line,50,52).strip(),
                "codisi": s(line,231,242).strip(),
                "dimes": s(line,243,245).strip(),
            })

vgo = [r for r in rows if r["codneg"] == "VGO 2"]
vgor = [r for r in rows if r["codisi"] == "VGORACPP"]

def dates_for(records, predicate=None):
    vals = sorted({r["date"] for r in records if predicate is None or predicate(r)})
    return {"count_dates": len(vals), "first": vals[0] if vals else None, "last": vals[-1] if vals else None}

def date_hist(records, field):
    d = defaultdict(Counter)
    for r in records:
        d[r["date"]][r[field]] += 1
    return {k: dict(sorted(v.items())) for k,v in sorted(d.items())}

def transitions(records, field):
    hist = date_hist(records, field)
    dates = list(hist)
    out = []
    for a,b in zip(dates, dates[1:]):
        if set(hist[a]) != set(hist[b]):
            out.append({"from":a,"to":b,"from_values":hist[a],"to_values":hist[b]})
    return out

def interval_rows(records, fields):
    return [
        {**{f:r[f] for f in fields}, "date":r["date"], "source_line":r["source_line"]}
        for r in sorted(records, key=lambda x:(x["date"],x["source_line"]))
    ]

especi_groups = defaultdict(list)
for r in vgor:
    especi_groups[r["especi"]].append(r)

dimes_groups = defaultdict(list)
for r in vgor:
    dimes_groups[r["dimes"]].append(r)

vgo_by_date = defaultdict(list)
for r in vgo:
    vgo_by_date[r["date"]].append(r)

# Focus window around the anomaly.
window = [r for r in vgo if "19861001" <= r["date"] <= "19861017"]

# Detect whether C05 existed under other CODNEG values and whether VGO 2 had Cxx other than C05.
c05_other_codneg = [r for r in rows if "C05" in r["especi"] and r["codneg"] != "VGO 2"]
vgo_other_cxx = [r for r in vgo if "C" in r["especi"] and "C05" not in r["especi"]]

# Compact per-day state for VGO 2.
daily = []
for date, rs in sorted(vgo_by_date.items()):
    daily.append({
        "date": date,
        "rows": len(rs),
        "especi": sorted(set(r["especi"] for r in rs)),
        "dimes": sorted(set(r["dimes"] for r in rs)),
        "markets": sorted(set(f"{r['codbdi']}|{r['tpmerc']}|{r['prazot']}" for r in rs)),
        "codisi": sorted(set(r["codisi"] for r in rs))
    })

result = {
    "schema_version":"1.0.0",
    "status":"FASE_08E_CRONOLOGIA_CXX_DIMES_VGO2_1986",
    "raw_file":RAW.name,
    "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
    "records_type01":len(rows),
    "vgo2_count":len(vgo),
    "vgoracpp_count":len(vgor),
    "vgo2_especi_distribution":dict(sorted(Counter(r["especi"] for r in vgo).items())),
    "vgo2_dimes_distribution":dict(sorted(Counter(r["dimes"] for r in vgo).items())),
    "vgoracpp_especi_distribution":dict(sorted(Counter(r["especi"] for r in vgor).items())),
    "vgoracpp_dimes_distribution":dict(sorted(Counter(r["dimes"] for r in vgor).items())),
    "vgo2_especi_intervals":{k:dates_for(v) for k,v in sorted(especi_groups.items())},
    "vgoracpp_especi_intervals":{k:dates_for(v) for k,v in sorted(especi_groups.items())},
    "vgo2_dimes_intervals":{k:dates_for(vgo, lambda r,k=k:r["dimes"]==k) for k in sorted(set(r["dimes"] for r in vgo))},
    "vgo2_especi_transitions":transitions(vgo,"especi"),
    "vgo2_dimes_transitions":transitions(vgo,"dimes"),
    "vgo2_market_transitions":transitions(vgo,"codbdi"),
    "vgo2_daily":daily,
    "window_19861001_19861017":window,
    "c05_other_codneg_count":len(c05_other_codneg),
    "c05_other_codneg_sample":c05_other_codneg[:20],
    "vgo2_other_cxx_count":len(vgo_other_cxx),
    "vgo2_other_cxx_sample":vgo_other_cxx[:20],
    "interpretation": {
        "fact": [
            "VGO 2 has a measurable chronological sequence of ESPECI and DIMES states in the preserved RAW.",
            "The 10/10/1986 anomaly occurs after VGO 2 is already observed with PP *C05 on 09/10/1986.",
            "The same PP *C05 and DIMES 104 context continues after 10/10/1986."
        ],
        "pattern": [
            "The anomaly is not coincident with the first appearance of PP *C05.",
            "The anomaly is not coincident with the first observed use of DIMES 104.",
            "The same VGO 2 identification continues across the anomaly window."
        ],
        "hypothesis": [
            "The two K4-identical term rows are unlikely to be explained solely by a C03-to-C05 transition occurring on 10/10/1986.",
            "The evidence remains insufficient to determine whether the duplicate rows represent aggregation, publication, or another historical record class."
        ],
        "not_determined": [
            "Exact meaning of C05.",
            "Exact historical meaning of DIMES 104.",
            "Reason for two distinct trade aggregates under the same K4."
        ]
    }
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status":"OK","records_type01":len(rows),"vgo2_count":len(vgo),"vgoracpp_count":len(vgor),"c05_other_codneg_count":len(c05_other_codneg),"vgo2_other_cxx_count":len(vgo_other_cxx)}))
