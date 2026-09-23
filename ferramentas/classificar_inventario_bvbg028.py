#!/usr/bin/env python3
"""Classificação estrutural auditável do inventário BVBG.028.02."""

import csv
import re
from collections import Counter

INPUT = "ativos/catalogo/INVENTARIO_B3_2026-09-22.csv"
OUTPUT = "ativos/catalogo/classificacao/CLASSIFICACAO_ESTRUTURAL_B3_2026-09-22.csv"
STATS = "ativos/catalogo/classificacao/ESTATISTICAS_CLASSIFICACAO_B3_2026-09-22.md"

FIELDS = [
    "Id","TckrSymb","Asst","AsstDesc","SctyCtgy","CFICd",
    "CategoriaEstrutural","NivelConfianca","RegraAplicada","Evidencia"
]

def norm(*values):
    return " ".join(str(v or "") for v in values).upper()

def classify(row):
    text = norm(row.get("AsstDesc"), row.get("Desc"), row.get("Asst"))
    cfi = (row.get("CFICd") or "").upper()
    optn = (row.get("OptnTp") or "").upper()
    xpr = row.get("XprtnDt") or ""
    underlying = row.get("Undrlyg") or ""

    # Descrição explícita tem precedência sobre padrões de ticker.
    if any(x in text for x in ("OPÇÃO", "OPTION")) or optn:
        return "OPCOES", "ESTRUTURAL", "descricao/opcao", "descrição ou OptnTp identifica opção"
    if any(x in text for x in ("FUTURO", "FUTURE", "MINICONTRATO", "MINI CONTRATO")):
        return "FUTUROS", "ESTRUTURAL", "descricao/futuro", "descrição identifica futuro"
    if any(x in text for x in ("ETF", "EXCHANGE TRADED FUND")):
        return "ETF", "ESTRUTURAL", "descricao/ETF", "descrição identifica ETF"
    if any(x in text for x in ("BDR", "BRAZILIAN DEPOSITARY")):
        return "BDR", "ESTRUTURAL", "descricao/BDR", "descrição identifica BDR"
    if any(x in text for x in ("FIC", "FUNDO", "FUND", "FII")):
        return "FUNDOS", "ESTRUTURAL", "descricao/fundo", "descrição identifica fundo"
    if any(x in text for x in ("ÍNDICE", "INDICE", "INDEX")):
        return "INDICES", "ESTRUTURAL", "descricao/indice", "descrição identifica índice"
    if any(x in text for x in ("DÓLAR", "DOLAR", "EURO", "IENE", "LIBRA", "FX", "CAMBIAL", "CÂMBIO", "CAMBIO")):
        return "MOEDAS_FX", "ESTRUTURAL", "descricao/fx", "descrição identifica moeda/FX"
    if any(x in text for x in ("DI1", "DI ", "FRA", "CUPOM", "DV01", "TAXA", "JUROS")):
        return "JUROS_TAXAS", "ESTRUTURAL", "descricao/juros", "descrição identifica juros/taxa"
    if any(x in text for x in ("BOI", "MILHO", "CAFÉ", "CAFE", "SOJA", "OURO", "ETANOL", "PETRÓLEO", "PETROLEO")):
        return "COMMODITIES", "ESTRUTURAL", "descricao/commodity", "descrição identifica commodity"
    if any(x in text for x in ("DEBÊNTURE", "DEBENTURE", "TESOURO", "BOND", "LETRA", "CDB", "CRI", "CRA")):
        return "RENDA_FIXA", "ESTRUTURAL", "descricao/renda_fixa", "descrição identifica renda fixa"
    if cfi.startswith("E"):
        return "PARTICIPACOES_EQUITY", "ESTRUTURAL", "CFICd/E", "CFI inicia por E; confirmar subcategoria"
    if xpr or underlying:
        return "OUTROS_DERIVATIVOS", "HIPOTESE", "atributos_derivativos", "vencimento ou subjacente presentes sem descrição suficiente"
    return "NAO_CLASSIFICADO", "NAO_CLASSIFICADO", "sem_evidencia_suficiente", "não há evidência textual/estrutural suficiente"

def main():
    counts = Counter()
    confidence = Counter()
    rows = 0
    with open(INPUT, newline="", encoding="utf-8") as f, open(OUTPUT, "w", newline="", encoding="utf-8") as out:
        reader = csv.DictReader(f, delimiter=";")
        writer = csv.DictWriter(out, fieldnames=FIELDS, delimiter=";", extrasaction="ignore")
        writer.writeheader()
        for row in reader:
            cat, level, rule, evidence = classify(row)
            counts[cat] += 1
            confidence[level] += 1
            rows += 1
            writer.writerow({
                **row,
                "CategoriaEstrutural": cat,
                "NivelConfianca": level,
                "RegraAplicada": rule,
                "Evidencia": evidence,
            })

    with open(STATS, "w", encoding="utf-8") as f:
        f.write("# ESTATÍSTICAS — CLASSIFICAÇÃO ESTRUTURAL B3 2026-09-22\n\n")
        f.write(f"Registros processados: **{rows:,}**\n\n".replace(",", "."))
        f.write("## Distribuição por categoria\n\n| Categoria | Registros |\n|---|---:|\n")
        for k, v in counts.most_common():
            f.write(f"| {k} | {v:,} |\n".replace(",", "."))
        f.write("\n## Nível de confiança\n\n| Nível | Registros |\n|---|---:|\n")
        for k, v in confidence.most_common():
            f.write(f"| {k} | {v:,} |\n".replace(",", "."))

if __name__ == "__main__":
    main()
