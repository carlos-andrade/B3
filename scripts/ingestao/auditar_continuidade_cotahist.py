#!/usr/bin/env python3
"""Auditoria estrutural e de continuidade do COTAHIST anual B3.

Audita, por ano:
- presença e integridade do ZIP;
- comprimento dos registros e quantidade de registros tipo 01;
- cobertura temporal e candidatos a intervalos longos;
- duplicidade da chave candidata (data,codbdi,codneg,tpmerc,dismes);
- relações codneg <-> codisi e mudanças de nome;
- consistência OHLC básica;
- hashes SHA-256 do arquivo bruto.

Importante: intervalos de calendário não são classificados como pregões
ausentes, pois feriados e suspensões não são inferidos sem um calendário
oficial independente. Eles são reportados como "candidatos a intervalo".
"""

import argparse
import csv
import hashlib
import json
import os
import sys
import zipfile
from collections import defaultdict
from datetime import date

FIELDS = [
    "data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
    "preabe","premax","premin","premed","preult","preofc","preofv","totneg",
    "quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"
]
KEY_IDX = (0, 1, 2, 3, 24)
MAX_GAP_DAYS = 4

def parse(raw):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    def s(a, z):
        return b[a-1:z].decode("latin-1", errors="replace").strip()
    def n(a, z, scale=0):
        x = s(a, z)
        if not x:
            return None
        v = int(x)
        return v / (10 ** scale) if scale else v
    return [
        s(3,10), s(11,12), s(13,24), s(25,27), s(28,39), s(40,49),
        s(50,52), s(53,56), n(57,69,2), n(70,82,2), n(83,95,2),
        n(96,108,2), n(109,121,2), n(122,134,2), n(135,147,2),
        n(148,152), n(153,170), n(171,188,2), n(189,201,2), s(202,202),
        s(203,210), n(211,217), n(218,230,6), s(231,242), s(243,245)
    ]

def audit_year(path, year):
    sha = hashlib.sha256()
    dates = set()
    key_seen = set()
    duplicate_groups = 0
    duplicate_excess = 0
    duplicate_examples = []
    isin_to_tickers = defaultdict(set)
    ticker_to_isins = defaultdict(set)
    ticker_to_names = defaultdict(set)
    total_lines = valid_records = invalid_length = non_type01 = 0
    price_violations = 0
    price_examples = []

    with open(path, "rb") as raw_file:
        for raw in raw_file:
            sha.update(raw)
            total_lines += 1
            body = raw.rstrip(b"\r\n")
            if len(body) != 245:
                invalid_length += 1
                continue
            if body[:2] != b"01":
                non_type01 += 1
                continue
            row = parse(raw)
            if row is None:
                continue
            valid_records += 1
            d = row[0]
            if len(d) == 8 and d.isdigit():
                try:
                    dt = date(int(d[:4]), int(d[4:6]), int(d[6:8]))
                    dates.add(dt)
                except ValueError:
                    pass
            key = tuple(row[i] for i in KEY_IDX)
            if key in key_seen:
                duplicate_excess += 1
                if not any(tuple(x["key"]) == key for x in duplicate_examples):
                    duplicate_groups += 1
                    if len(duplicate_examples) < 20:
                        duplicate_examples.append({"key": list(key), "occurrences_seen": 2})
            else:
                key_seen.add(key)

            codneg, codisi, nomres = row[2], row[23], row[4]
            if codneg and codisi:
                isin_to_tickers[codisi].add(codneg)
                ticker_to_isins[codneg].add(codisi)
            if codneg and nomres:
                ticker_to_names[codneg].add(nomres)

            hi, lo, op, cl = row[9], row[10], row[8], row[12]
            if None not in (hi, lo) and hi < lo:
                price_violations += 1
                if len(price_examples) < 10:
                    price_examples.append({"codneg": codneg, "data": d, "premax": hi, "premin": lo, "tipo": "premax<premin"})
            if None not in (hi, op, cl, lo) and hi >= lo:
                bad = op > hi or op < lo or cl > hi or cl < lo
                if bad:
                    price_violations += 1
                    if len(price_examples) < 10:
                        price_examples.append({"codneg": codneg, "data": d, "preabe": op, "premax": hi, "premin": lo, "preult": cl, "tipo": "OHLC_fora_do_range"})

    ordered = sorted(dates)
    gaps = []
    for a, b in zip(ordered, ordered[1:]):
        delta = (b - a).days
        if delta > MAX_GAP_DAYS:
            gaps.append({"from": a.isoformat(), "to": b.isoformat(), "calendar_days": delta, "intervening_calendar_days": delta - 1})

    multi_ticker_isin = {k: sorted(v) for k, v in isin_to_tickers.items() if len(v) > 1}
    multi_isin_ticker = {k: sorted(v) for k, v in ticker_to_isins.items() if len(v) > 1}
    renamed = {k: sorted(v) for k, v in ticker_to_names.items() if len(v) > 1}

    return {
        "ano": year,
        "raw_file": os.path.basename(path),
        "raw_sha256": sha.hexdigest(),
        "linhas_totais": total_lines,
        "registros_tipo_01_validos": valid_records,
        "linhas_comprimento_diferente_245": invalid_length,
        "linhas_nao_tipo_01": non_type01,
        "datas_unicas": len(ordered),
        "primeira_data": ordered[0].isoformat() if ordered else None,
        "ultima_data": ordered[-1].isoformat() if ordered else None,
        "candidatos_intervalo_longo": gaps[:100],
        "candidatos_intervalo_longo_total": len(gaps),
        "duplicidade_chave_grupos": duplicate_groups,
        "duplicidade_chave_excesso_linhas": duplicate_excess,
        "duplicidade_exemplos": duplicate_examples,
        "isin_com_multiplos_codneg": multi_ticker_isin,
        "codneg_com_multiplos_isin": multi_isin_ticker,
        "codneg_com_multiplos_nomres": renamed,
        "inconsistencias_ohlc": price_violations,
        "exemplos_inconsistencia_ohlc": price_examples,
    }

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
        years.append((year, path))

    reports = []
    for year, zip_path in years:
        with zipfile.ZipFile(zip_path) as z:
            members = z.namelist()
            if len(members) != 1:
                raise SystemExit(f"{zip_path}: ZIP deve conter exatamente 1 membro: {members}")
            z.extract(members[0], "/tmp/cotahist-audit")
            extracted = os.path.join("/tmp/cotahist-audit", members[0])
            try:
                reports.append(audit_year(extracted, year))
            finally:
                try:
                    os.remove(extracted)
                except OSError:
                    pass

    # O ano corrente pode ser parcial; portanto a auditoria não exige fechamento anual.
    all_first = [r["primeira_data"] for r in reports if r["primeira_data"]]
    all_last = [r["ultima_data"] for r in reports if r["ultima_data"]]
    out = {
        "schema_version": "1.0.0",
        "status": "AUDITORIA_CONTINUIDADE_CONCLUIDA",
        "escopo": {"inicio": args.start_year, "fim": args.end_year},
        "criterio_intervalo_longo_dias": MAX_GAP_DAYS,
        "criterio_intervalo_longo_nota": "Não classifica feriados como falhas; são candidatos que exigem calendário oficial independente.",
        "anos_processados": len(reports),
        "anos_com_erro_estrutural": [
            r["ano"] for r in reports
            if r["linhas_comprimento_diferente_245"] or r["linhas_nao_tipo_01"]
        ],
        "anos_com_duplicidade": [
            r["ano"] for r in reports if r["duplicidade_chave_excesso_linhas"]
        ],
        "anos_com_inconsistencia_ohlc": [
            r["ano"] for r in reports if r["inconsistencias_ohlc"]
        ],
        "primeira_data_global": min(all_first) if all_first else None,
        "ultima_data_global": max(all_last) if all_last else None,
        "por_ano": reports,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps({
        "status": out["status"],
        "anos_processados": out["anos_processados"],
        "anos_com_erro_estrutural": out["anos_com_erro_estrutural"],
        "anos_com_duplicidade": out["anos_com_duplicidade"],
        "anos_com_inconsistencia_ohlc": out["anos_com_inconsistencia_ohlc"],
        "primeira_data_global": out["primeira_data_global"],
        "ultima_data_global": out["ultima_data_global"],
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
