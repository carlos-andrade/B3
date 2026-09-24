#!/usr/bin/env python3
import hashlib
import json
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

RAW_DIR = Path("dados/cotahist/raw/anual")
OUT = Path("dados/cotahist/quality/COTAHIST_FASE08H_RECORRENCIA_K4_MULTIANOS_V1.json")

K4_FIELDS = (
    "data_pregao", "codbdi", "codneg", "tpmerc", "codisi", "dimes",
    "especi", "prazot", "datven", "preexe", "indopc", "ptoexe"
)
STAT_FIELDS = ("preab", "premax", "premin", "premed", "preult", "totneg", "quatot", "voltot", "fatcot")

def s(line, a, b):
    return line[a-1:b]

def parse_zip(path):
    rows = []
    with zipfile.ZipFile(path) as z:
        members = [n for n in z.namelist() if not n.endswith("/")]
        if not members:
            raise ValueError(f"ZIP sem arquivo: {path}")
        name = members[0]
        with z.open(name) as f:
            for source_line, raw in enumerate(f, 1):
                line = raw.decode("latin-1").rstrip("\r\n")
                if len(line) != 245 or line[:2] != "01":
                    continue
                def integer(a, b):
                    v = s(line, a, b).strip()
                    return int(v) if v else 0
                rows.append({
                    "source_line": source_line,
                    "data_pregao": s(line,3,10),
                    "codbdi": s(line,11,12),
                    "codneg": s(line,13,24).strip(),
                    "tpmerc": s(line,25,27),
                    "especi": s(line,40,49).strip(),
                    "prazot": s(line,50,52).strip(),
                    "preab": s(line,57,69),
                    "premax": s(line,70,82),
                    "premin": s(line,83,95),
                    "premed": s(line,96,108),
                    "preult": s(line,109,121),
                    "totneg": integer(148,152),
                    "quatot": integer(153,170),
                    "voltot": integer(171,188),
                    "preexe": integer(189,201),
                    "indopc": s(line,202,202),
                    "datven": s(line,203,210),
                    "fatcot": integer(211,217),
                    "ptoexe": integer(218,230),
                    "codisi": s(line,231,242).strip(),
                    "dimes": s(line,243,245).strip(),
                })
    return rows

def k4(r):
    return tuple(str(r[x]) for x in K4_FIELDS)

def stat_profile(r):
    return tuple(str(r[x]) for x in STAT_FIELDS)

def context(r):
    return {
        "source_line": r["source_line"],
        "data_pregao": r["data_pregao"],
        "codbdi": r["codbdi"],
        "codneg": r["codneg"],
        "tpmerc": r["tpmerc"],
        "especi": r["especi"],
        "prazot": r["prazot"],
        "datven": r["datven"],
        "codisi": r["codisi"],
        "dimes": r["dimes"],
        "preab": r["preab"],
        "premax": r["premax"],
        "premin": r["premin"],
        "premed": r["premed"],
        "preult": r["preult"],
        "totneg": r["totneg"],
        "quatot": r["quatot"],
        "voltot": r["voltot"],
        "fatcot": r["fatcot"],
    }

def analyze_year(path):
    year = path.stem[-4:]
    raw_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    rows = parse_zip(path)
    groups = defaultdict(list)
    for r in rows:
        groups[k4(r)].append(r)
    dups = [g for g in groups.values() if len(g) > 1]

    differing_stat_groups = 0
    byte_identical_groups = 0
    differing_field_counter = Counter()
    examples = []

    for g in dups:
        raw_rows = []
        for r in g:
            # Statistical comparison only; K4 fields are already equal by construction.
            raw_rows.append(stat_profile(r))
        if len(set(raw_rows)) == 1:
            byte_identical_groups += 1
        else:
            differing_stat_groups += 1
            diff = tuple(f for f in STAT_FIELDS if len({str(r[f]) for r in g}) > 1)
            differing_field_counter[diff] += 1
            if len(examples) < 20:
                examples.append({
                    "k4": list(k4(g[0])),
                    "group_size": len(g),
                    "differing_stat_fields": list(diff),
                    "rows": [context(r) for r in g]
                })

    return {
        "year": year,
        "raw_file": path.name,
        "raw_sha256": raw_sha,
        "records_type01": len(rows),
        "k4_groups_total": len(groups),
        "duplicate_k4_groups_total": len(dups),
        "duplicate_k4_rows_total": sum(len(g) for g in dups),
        "duplicate_k4_groups_with_statistical_difference": differing_stat_groups,
        "duplicate_k4_groups_statistically_identical": byte_identical_groups,
        "duplicate_k4_group_size_distribution": dict(sorted(Counter(map(len, dups)).items())),
        "duplicate_k4_groups_by_market": {
            f"{g[0]['codbdi']}|{g[0]['tpmerc']}": n
            for (g, n) in sorted(
                Counter((g[0]["codbdi"], g[0]["tpmerc"]) for g in dups).items(),
                key=lambda x: (-x[1], x[0])
            )
        },
        "duplicate_k4_groups_by_differing_stat_fields": {
            "|".join(k) if k else "NONE": v
            for k, v in sorted(differing_field_counter.items(), key=lambda x: (-x[1], x[0]))
        },
        "examples_first_20_statistically_different": examples,
    }

def main():
    zips = sorted(RAW_DIR.glob("COTAHIST_A*.ZIP"))
    if not zips:
        raise SystemExit("Nenhum COTAHIST_A*.ZIP encontrado.")
    years = []
    totals = Counter()
    collision_years = []
    all_examples = []
    raw_inventory = []

    for path in zips:
        result = analyze_year(path)
        years.append(result)
        raw_inventory.append({
            "year": result["year"],
            "file": result["raw_file"],
            "sha256": result["raw_sha256"],
            "size_bytes": path.stat().st_size
        })
        for key in (
            "records_type01", "k4_groups_total", "duplicate_k4_groups_total",
            "duplicate_k4_rows_total", "duplicate_k4_groups_with_statistical_difference",
            "duplicate_k4_groups_statistically_identical"
        ):
            totals[key] += result[key]
        if result["duplicate_k4_groups_with_statistical_difference"] > 0:
            collision_years.append(result["year"])
            for ex in result["examples_first_20_statistically_different"]:
                if len(all_examples) < 100:
                    ex["year"] = result["year"]
                    all_examples.append(ex)

    years_with_duplicates = [r["year"] for r in years if r["duplicate_k4_groups_total"] > 0]
    years_with_stat_diff = [r["year"] for r in years if r["duplicate_k4_groups_with_statistical_difference"] > 0]

    out = {
        "schema_version": "1.0.0",
        "status": "FASE_08H_RECORRENCIA_K4_MULTIANOS_ANALISE",
        "method": {
            "scope": "todos os arquivos COTAHIST_A*.ZIP presentes em dados/cotahist/raw/anual no momento da execução",
            "record_type": "01",
            "record_length": 245,
            "k4_fields": list(K4_FIELDS),
            "statistical_fields_compared": list(STAT_FIELDS),
            "classification": {
                "duplicate_k4": "mais de um registro 01 com K4 idêntica",
                "statistically_different": "K4 idêntica e pelo menos um campo estatístico diferente",
                "statistically_identical": "K4 idêntica e os campos estatísticos comparados idênticos; não implica byte-identidade da linha RAW"
            },
            "economic_identity_inferred": False
        },
        "raw_inventory": raw_inventory,
        "coverage": {
            "years_found": [r["year"] for r in years],
            "year_count": len(years),
            "years_with_duplicate_k4": years_with_duplicates,
            "years_with_k4_statistical_difference": years_with_stat_diff
        },
        "totals": dict(totals),
        "years": years,
        "examples_first_100_statistically_different_collisions": all_examples,
        "focus_1986": next((r for r in years if r["year"] == "1986"), None),
        "governance": {
            "raw_changed": False,
            "rows_deleted": False,
            "rows_consolidated": False,
            "economic_identity_inferred": False,
            "causal_explanation_inferred": False,
            "purpose": "verificar se a colisão K4 com estatísticas diferentes observada em 1986 reaparece em outros anos do acervo anual"
        }
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "OK",
        "years": out["coverage"]["years_found"],
        "year_count": len(years),
        "years_with_duplicate_k4": years_with_duplicates,
        "years_with_k4_statistical_difference": years_with_stat_diff,
        "total_duplicate_k4_groups": totals["duplicate_k4_groups_total"],
        "total_statistically_different": totals["duplicate_k4_groups_with_statistical_difference"],
        "output": str(OUT)
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
