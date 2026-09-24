#!/usr/bin/env python3
"""Auditoria estrutural reutilizável de COTAHIST normalizado.

Uso:
  python scripts/ingestao/auditar_cotahist_v1.py arquivo.csv
"""

import sys
import pandas as pd

REQUIRED = [
    "data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot",
    "modref","preabe","premax","premin","premed","preult","preofc","preofv",
    "totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe",
    "codisi","dismes"
]

def main(path: str) -> int:
    df = pd.read_csv(path, low_memory=False)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        print("FAIL: campos ausentes:", ",".join(missing))
        return 1

    dates = pd.to_datetime(df["data_pregao"], errors="coerce")
    year = int(dates.dropna().dt.year.mode().iloc[0]) if dates.notna().any() else None

    key = ["data_pregao","codneg","tpmerc","codbdi"]
    ohlc_bad = (
        (df["premax"] < df[["preabe","premin","preult"]].max(axis=1)) |
        (df["premin"] > df[["preabe","premax","preult"]].min(axis=1))
    ).sum()

    result = {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "year_mode": year,
        "invalid_dates": int(dates.isna().sum()),
        "dates_monotonic": bool(dates.is_monotonic_increasing),
        "distinct_dates": int(df["data_pregao"].nunique()),
        "duplicate_diagnostic_key_rows": int(df.duplicated(key).sum()),
        "ohlc_rule_exceptions": int(ohlc_bad),
        "null_total": int(df.isna().sum().sum()),
        "negative_prices": int((df[["preabe","premax","premin","premed","preult"]] < 0).sum().sum()),
        "negative_totneg": int((df["totneg"] < 0).sum()),
        "negative_quatot": int((df["quatot"] < 0).sum()),
        "negative_voltot": int((df["voltot"] < 0).sum()),
    }
    for k, v in result.items():
        print(f"{k}={v}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
