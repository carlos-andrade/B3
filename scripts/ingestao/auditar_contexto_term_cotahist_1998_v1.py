#!/usr/bin/env python3
import csv, hashlib, json
from collections import Counter
from decimal import Decimal
from pathlib import Path

CSV_PATH = Path("dados/cotahist/normalized/anual/COTAHIST_A1998.csv")
OUT = Path("dados/cotahist/quality/COTAHIST_1998_FASE06B_CONTEXT_TERM_V1.json")

def dec(v):
    return Decimal(v) if v else None

def main():
    if not CSV_PATH.exists():
        raise SystemExit("FAIL-CLOSED: NORMALIZED ausente")
    sha = hashlib.sha256(CSV_PATH.read_bytes()).hexdigest()
    total_term = 0
    anomalies = []
    counters = Counter()
    by_codbdi = Counter()
    by_month = Counter()

    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        for rownum, row in enumerate(csv.DictReader(f), start=2):
            if row.get("tpmerc", "").strip() != "030":
                continue
            total_term += 1
            by_codbdi[row.get("codbdi", "").strip()] += 1
            date = row.get("data_pregao", "").strip()
            if len(date) >= 7:
                by_month[date[:7]] += 1

            preabe, premax, premin, premed, preult = map(
                dec, [row.get("preabe",""), row.get("premax",""),
                      row.get("premin",""), row.get("premed",""), row.get("preult","")]
            )
            flags = {
                "preult_lt_premin": all(x is not None for x in (preult, premin)) and preult < premin,
                "preult_gt_premax": all(x is not None for x in (preult, premax)) and preult > premax,
                "premed_outside": all(x is not None for x in (premed, premin, premax)) and not (premin <= premed <= premax),
                "preabe_outside": all(x is not None for x in (preabe, premin, premax)) and not (premin <= preabe <= premax),
            }
            if any(flags.values()):
                counters.update(k for k,v in flags.items() if v)
                anomalies.append({
                    "row": rownum,
                    "date": date,
                    "codneg": row.get("codneg","").strip(),
                    "codbdi": row.get("codbdi","").strip(),
                    "tpmerc": row.get("tpmerc","").strip(),
                    "prazot": row.get("prazot","").strip(),
                    "datven": row.get("datven","").strip(),
                    "preabe": row.get("preabe","").strip(),
                    "premax": row.get("premax","").strip(),
                    "premin": row.get("premin","").strip(),
                    "premed": row.get("premed","").strip(),
                    "preult": row.get("preult","").strip(),
                    "flags": flags,
                })

    out = {
        "schema_version": "1.0.0",
        "year": 1998,
        "phase": "FASE06B_CONTEXT_TERM",
        "status": "VALIDADO",
        "decision": "INVESTIGACAO_CONTEXTUAL_CONCLUIDA_SEM_LIBERACAO",
        "purpose": "Medir a recorrencia das anomalias OHLC dentro de todo o universo TPMERC=030 antes da FASE07.",
        "normalized_path": str(CSV_PATH),
        "normalized_sha256": sha,
        "term_records": total_term,
        "anomaly_records": len(anomalies),
        "anomaly_counts": dict(counters),
        "codbdi_distribution": dict(by_codbdi),
        "monthly_term_distribution": dict(sorted(by_month.items())),
        "anomalies": anomalies,
        "rule_under_test": "PREMIN <= PREMED <= PREMAX e PREMIN <= PREULT <= PREMAX",
        "interpretation_policy": "Fato estatistico apenas; nenhuma anomalia e reinterpretada ou corrigida.",
        "next_gate": "FASE07 permanece bloqueada ate explicar as anomalias ou estabelecer regra documental de excecao.",
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "term_records": total_term,
        "anomaly_records": len(anomalies),
        "anomaly_counts": dict(counters),
        "output": str(OUT)
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
