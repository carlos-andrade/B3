#!/usr/bin/env python3
"""Gera a matriz canônica provisória de calendário COTAHIST 1986 sem inferir pregões históricos."""

import argparse, json
from datetime import date, timedelta

def daterange(a,b):
    d=a
    while d<=b:
        yield d
        d += timedelta(days=1)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audit",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    with open(args.audit,encoding="utf-8") as f:
        audit=json.load(f)

    observed=set()
    # O artefato de auditoria traz a contagem por data; não precisamos reabrir o RAW.
    for ds in audit["date_record_counts"]:
        observed.add(ds)

    first=date.fromisoformat(audit["first_trading_date_observed"])
    last=date.fromisoformat(audit["last_trading_date_observed"])
    rows=[]
    for d in daterange(first,last):
        ds=d.isoformat()
        if ds in observed:
            status="OBSERVADA_COTAHIST"
            reason="Há registro tipo 01 no RAW."
        elif d.weekday()>=5:
            status="NAO_SESSAO_FIM_DE_SEMANA"
            reason="Sábado/domingo; não é inferido como pregão."
        else:
            status="PENDENTE_FONTE_HISTORICA"
            reason="Dia útil sem observação; requer calendário histórico aplicável à Bovespa em 1986."
        rows.append({"data":ds,"dia_semana":d.strftime("%A"),"status":status,"observado_cotahist":ds in observed,"justificativa":reason})

    summary={}
    for r in rows:
        summary[r["status"]]=summary.get(r["status"],0)+1

    out={
      "schema_version":"1.0.0",
      "status":"MATRIZ_CALENDARIO_CANONICO_PROVISORIA_1986",
      "scope":{"first":first.isoformat(),"last":last.isoformat()},
      "source_audit":args.audit,
      "governance":{
        "raw_unchanged":True,
        "no_historical_session_inference":True,
        "weekday_missing_requires_primary_or_institutional_source":True,
        "weekend_observation_is_preserved_as_anomaly":True
      },
      "summary":summary,
      "rows":rows,
      "unresolved_weekdays":[r["data"] for r in rows if r["status"]=="PENDENTE_FONTE_HISTORICA"]
    }
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(out,f,ensure_ascii=False,indent=2)
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
