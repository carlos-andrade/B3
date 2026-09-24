#!/usr/bin/env python3
"""Reconcilia gaps de datas do COTAHIST com regras de calendário verificáveis."""

import argparse, json, os, zipfile
from datetime import date, timedelta

# Datas de suspensão da negociação do segmento Listado B3, fonte oficial B3.
# Nesta V1 somente 2026 está cadastrado com granularidade diária oficial.
HOLIDAYS = {
    2026: {
        "2026-01-01": "Confraternização Universal",
        "2026-02-16": "Carnaval",
        "2026-02-17": "Carnaval",
        "2026-04-03": "Sexta-feira Santa",
        "2026-04-21": "Tiradentes",
        "2026-05-01": "Dia do Trabalho",
        "2026-06-04": "Corpus Christi",
        "2026-09-07": "Independência do Brasil",
        "2026-10-12": "Nossa Senhora Aparecida",
        "2026-11-02": "Finados",
        "2026-11-20": "Dia Nacional de Zumbi e Consciência Negra",
        "2026-12-24": "Véspera de Natal",
        "2026-12-25": "Natal",
        "2026-12-31": "Véspera de Ano Novo",
    }
}

def dates_from_zip(path):
    with zipfile.ZipFile(path) as z:
        members = z.namelist()
        if len(members) != 1:
            raise SystemExit(f"{path}: ZIP deve conter exatamente 1 membro")
        with z.open(members[0]) as f:
            dates = set()
            for raw in f:
                body = raw.rstrip(b"\r\n")
                if len(body) == 245 and body[:2] == b"01":
                    s = body[2:10].decode("ascii", errors="ignore")
                    if len(s) == 8 and s.isdigit():
                        try:
                            dates.add(date(int(s[:4]), int(s[4:6]), int(s[6:8])))
                        except ValueError:
                            pass
            return sorted(dates)

def classify_gap(a, b, year):
    missing = []
    d = a + timedelta(days=1)
    while d < b:
        ds = d.isoformat()
        if d.weekday() >= 5:
            cls = "FIM_DE_SEMANA"
        elif ds in HOLIDAYS.get(year, {}):
            cls = "FERIADO_B3"
        elif year in HOLIDAYS:
            cls = "DIA_UTIL_NAO_EXPLICADO"
        else:
            cls = "SEM_CALENDARIO_DIARIO_OFICIAL"
        missing.append({"data": ds, "classificacao": cls, "evento": HOLIDAYS.get(year, {}).get(ds)})
        d += timedelta(days=1)
    classes = {x["classificacao"] for x in missing}
    if classes <= {"FIM_DE_SEMANA"}:
        status = "EXPLICADO_FIM_DE_SEMANA"
    elif "DIA_UTIL_NAO_EXPLICADO" in classes:
        status = "REQUER_INVESTIGACAO"
    elif "FERIADO_B3" in classes and classes <= {"FIM_DE_SEMANA", "FERIADO_B3"}:
        status = "EXPLICADO_CALENDARIO_B3"
    else:
        status = "SEM_CALENDARIO_DIARIO_OFICIAL"
    return status, missing

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--start-year", type=int, default=1986)
    ap.add_argument("--end-year", type=int, default=2026)
    args = ap.parse_args()
    years = []
    for year in range(args.start_year, args.end_year + 1):
        path = os.path.join(args.raw_dir, f"COTAHIST_A{year}.ZIP")
        if not os.path.isfile(path):
            raise SystemExit(f"Arquivo ausente: {path}")
        ds = dates_from_zip(path)
        gaps = []
        for a, b in zip(ds, ds[1:]):
            delta = (b-a).days
            if delta > 4:
                status, missing = classify_gap(a, b, year)
                gaps.append({"de": a.isoformat(), "para": b.isoformat(), "dias_corridos": delta,
                             "status": status, "datas_intermediarias": missing})
        years.append({"ano": year, "gaps": gaps, "total_gaps": len(gaps)})
    flat = [g for y in years for g in y["gaps"]]
    out = {
        "schema_version": "1.0.0",
        "status": "RECONCILIACAO_CALENDARIO_V1",
        "escopo": {"inicio": args.start_year, "fim": args.end_year},
        "fonte_calendario": "B3 - Calendário de Negociação",
        "regra": "Gap > 4 dias corridos é candidato; fins de semana são explicados automaticamente; 2026 usa feriados B3 cadastrados; demais anos permanecem pendentes de calendário diário oficial.",
        "resumo": {
            "gaps_total": len(flat),
            "explicado_fim_de_semana": sum(g["status"] == "EXPLICADO_FIM_DE_SEMANA" for g in flat),
            "explicado_calendario_b3": sum(g["status"] == "EXPLICADO_CALENDARIO_B3" for g in flat),
            "requer_investigacao": sum(g["status"] == "REQUER_INVESTIGACAO" for g in flat),
            "sem_calendario_diario_oficial": sum(g["status"] == "SEM_CALENDARIO_DIARIO_OFICIAL" for g in flat),
        },
        "por_ano": years,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out["resumo"], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
