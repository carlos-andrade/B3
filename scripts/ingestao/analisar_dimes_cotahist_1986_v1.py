#!/usr/bin/env python3
"""FASE 07E — DIMES no COTAHIST 1986.

Analisa o campo DIMES sem alterar RAW/NORMALIZED.
DIMES ocupa as posições 243-245 no registro tipo 01.
"""
from __future__ import annotations
import argparse
import json
import zipfile
from collections import Counter, defaultdict
from datetime import datetime

def parse(raw: bytes):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None

    def s(a: int, z: int) -> str:
        return b[a - 1:z].decode("latin-1", errors="replace").strip()

    return {
        "data_pregao": s(3, 10),
        "codbdi": s(11, 12),
        "codneg": s(13, 24),
        "tpmerc": s(25, 27),
        "codisi": s(231, 242),
        "dimes_raw": b[242:245].decode("latin-1", errors="replace"),
        "dimes": s(243, 245),
        "especi": s(39, 48),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--output", required=True)
    a = ap.parse_args()

    rows = 0
    blank_rows = 0
    counts = Counter()
    raw_counts = Counter()
    dates = defaultdict(set)
    codneg = defaultdict(set)
    codisi = defaultdict(set)
    especi = defaultdict(set)
    tpmerc = defaultdict(Counter)
    dimes_by_codneg = defaultdict(set)
    dimes_by_codisi = defaultdict(set)
    raw_length = Counter()

    with zipfile.ZipFile(a.zip) as z:
        members = [x for x in z.namelist() if not x.endswith("/")]
        if len(members) != 1:
            raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                r = parse(raw)
                if not r:
                    continue
                rows += 1
                d = r["dimes"]
                counts[d] += 1
                raw_counts[r["dimes_raw"]] += 1
                raw_length[len(r["dimes_raw"])] += 1
                dates[d].add(r["data_pregao"])
                codneg[d].add(r["codneg"])
                codisi[d].add(r["codisi"])
                especi[d].add(r["especi"])
                tpmerc[d][r["tpmerc"]] += 1
                dimes_by_codneg[r["codneg"]].add(d)
                if r["codisi"]:
                    dimes_by_codisi[r["codisi"]].add(d)
                if not d:
                    blank_rows += 1

    changing_codneg = {
        k: sorted(v) for k, v in dimes_by_codneg.items() if len(v) > 1
    }
    changing_codisi = {
        k: sorted(v) for k, v in dimes_by_codisi.items() if len(v) > 1
    }

    result = {
        "schema_version": "1.0.0",
        "status": "FASE_07E_DIMES_1986_ANALISE",
        "generated_at_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "raw_file": "COTAHIST_A1986.ZIP",
        "rows": rows,
        "source_document": {
            "institution": "B3",
            "document": "LAYOUT DO ARQUIVO – COTAÇÕES HISTÓRICAS",
            "revision": "02",
            "date": "05/10/2020",
            "field": "DIMES",
            "positions": "243-245",
            "type": "9(03)",
            "source_url": "https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf"
        },
        "documentary_semantics": {
            "official_text": "NÚMERO DE DISTRIBUIÇÃO DO PAPEL",
            "historical_note": "NÚMERO DE SEQÜÊNCIA DO PAPEL CORRESPONDENTE AO ESTADO DE DIREITO VIGENTE",
            "interpretation_rule": "DIMES é tratado como atributo histórico de distribuição/estado de direito; não é convertido em identificador econômico moderno."
        },
        "observed": {
            "distinct_dimes": len(counts),
            "blank_rows": blank_rows,
            "nonblank_rows": rows - blank_rows,
            "raw_field_length_distribution": dict(sorted(raw_length.items())),
            "dimes_frequency": dict(sorted(counts.items(), key=lambda x: (-x[1], x[0]))),
            "dimes_trading_dates": {k: len(v) for k, v in sorted(dates.items())},
            "dimes_distinct_codneg": {k: len(v) for k, v in sorted(codneg.items())},
            "dimes_distinct_codisi": {k: len(v) for k, v in sorted(codisi.items())},
            "dimes_distinct_especi": {k: len(v) for k, v in sorted(especi.items())},
            "dimes_tpmerc_distribution": {
                k: dict(sorted(v.items())) for k, v in sorted(tpmerc.items())
            }
        },
        "reuse_analysis": {
            "codneg_with_multiple_dimes": len(changing_codneg),
            "codisi_nonblank_with_multiple_dimes": len(changing_codisi),
            "codneg_dimes": changing_codneg,
            "codisi_dimes": changing_codisi
        },
        "governance": {
            "raw_unchanged": True,
            "normalized_unchanged": True,
            "dimes_not_treated_as_economic_identity": True,
            "dimes_not_converted_to_modern_identifier": True,
            "historical_semantics_requires_temporal_context": True
        }
    }

    with open(a.output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

if __name__ == "__main__":
    main()

# Trigger de execucao auditavel FASE 07
