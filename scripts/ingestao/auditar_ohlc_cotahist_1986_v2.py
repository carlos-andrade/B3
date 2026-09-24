#!/usr/bin/env python3
"""Auditoria OHLC COTAHIST 1986: classifica anomalias e preserva evidência RAW."""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from collections import Counter
from pathlib import Path
from decimal import Decimal

FIELDS = ["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
          "preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot",
          "voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]

def parse(raw: bytes):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    def s(a,z): return b[a-1:z].decode("latin-1", errors="replace").strip()
    vals=[s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56)]
    for a,z in [(57,69),(70,82),(83,95),(96,108),(109,121),(122,134),(135,147)]:
        x=s(a,z); vals.append(Decimal(x)/100 if x else None)
    vals += [int(s(148,152)) if s(148,152) else None,
             int(s(153,170)) if s(153,170) else None,
             Decimal(s(171,188))/100 if s(171,188) else None,
             Decimal(s(189,201))/100 if s(189,201) else None,
             s(202,202),s(203,210),int(s(211,217)) if s(211,217) else None,
             Decimal(s(218,230))/Decimal(10**6) if s(218,230) else None,
             s(231,242),s(243,245)]
    return dict(zip(FIELDS, vals))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--output", required=True)
    args=ap.parse_args()
    anomalies=[]; classes=Counter(); groups=Counter(); total=0
    with zipfile.ZipFile(args.zip) as z:
        members=[x for x in z.namelist() if not x.endswith("/")]
        if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for line_no, raw in enumerate(f, 1):
                r=parse(raw)
                if not r: continue
                total += 1
                vals=[r[k] for k in ("preabe","premax","premin","preult")]
                labels=[]
                if any(v == 0 for v in vals if v is not None):
                    labels.append("ZERO_OHLC")
                if any(v is None for v in vals):
                    labels.append("MISSING_OHLC")
                o,h,l,c=vals
                if None not in vals:
                    if h < l: labels.append("HIGH_LT_LOW")
                    if o > h or o < l: labels.append("OPEN_OUTSIDE_RANGE")
                    if c > h or c < l: labels.append("CLOSE_OUTSIDE_RANGE")
                if labels:
                    for x in labels: classes[x]+=1
                    groups[(r["tpmerc"],r["codbdi"])]+=1
                    anomalies.append({
                        "line_number": line_no,
                        "raw_sha256": hashlib.sha256(raw.rstrip(b"\r\n")).hexdigest(),
                        "classifications": labels,
                        "data_pregao": r["data_pregao"], "codbdi": r["codbdi"],
                        "codneg": r["codneg"], "tpmerc": r["tpmerc"],
                        "nomres": r["nomres"], "especi": r["especi"],
                        "preabe": str(o) if o is not None else None,
                        "premax": str(h) if h is not None else None,
                        "premin": str(l) if l is not None else None,
                        "preult": str(c) if c is not None else None,
                        "totneg": r["totneg"], "quatot": r["quatot"],
                        "voltot": str(r["voltot"]) if r["voltot"] is not None else None,
                        "codisi": r["codisi"], "dismes": r["dismes"]
                    })
    out={"schema_version":"2.0.0","status":"AUDITORIA_OHLC_1986","raw_file":Path(args.zip).name,
         "type01_records":total,"anomaly_count":len(anomalies),
         "classification_counts":dict(sorted(classes.items())),
         "tpmerc_codbdi_anomaly_counts":[{"tpmerc":a,"codbdi":b,"rows":n} for (a,b),n in sorted(groups.items())],
         "anomalies":anomalies,
         "interpretation":"Anomalia estrutural não implica erro do RAW. ZERO_OHLC e MISSING_OHLC exigem interpretação econômica; relações HIGH/LOW e OPEN/CLOSE fora da faixa são inconsistências geométricas."}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":out["status"],"records":total,"anomalies":len(anomalies),"classes":out["classification_counts"]},ensure_ascii=False))

if __name__=="__main__":
    main()
