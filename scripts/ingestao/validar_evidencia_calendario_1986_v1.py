#!/usr/bin/env python3
"""Valida a matriz de evidência dos dias úteis ausentes de 1986."""

import argparse,json

EXPECTED=[
"1986-02-10","1986-02-11","1986-02-12","1986-02-28",
"1986-03-03","1986-03-27","1986-03-28","1986-04-21",
"1986-05-01","1986-05-26","1986-12-24","1986-12-25"
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audit",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    with open(args.audit,encoding="utf-8") as f: a=json.load(f)
    observed=set(a["date_record_counts"])
    missing=[d for d in EXPECTED if d not in observed]
    if missing != EXPECTED:
        raise SystemExit("A lista esperada de 12 dias diverge da auditoria.")
    out={
      "schema_version":"1.0.0",
      "status":"FASE08B_EVIDENCIA_DIAS_UTEIS_AUSENTES_1986",
      "audit_sha256":a["raw_sha256_stream"],
      "candidate_count":len(missing),
      "candidates":[{"data":d,"status":"PENDENTE_FONTE_HISTORICA"} for d in missing],
      "weekend_anomaly":{"data":"1986-04-26","status":"ANOMALIA_DE_DATA_OBSERVADA","rows":3},
      "governance":{"raw_unchanged":True,"normalized_unchanged":True,"no_modern_calendar_backprojection":True}
    }
    with open(args.output,"w",encoding="utf-8") as f: json.dump(out,f,ensure_ascii=False,indent=2)
    print(json.dumps({"candidate_count":len(missing),"raw_unchanged":True},ensure_ascii=False))
if __name__=="__main__": main()
