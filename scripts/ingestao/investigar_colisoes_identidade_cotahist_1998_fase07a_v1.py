#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

FIELDS = ["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
          "preabe","premax","premin","premed","preult","preofc","preofv","totneg",
          "quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]

KEY_BASE = ["data_pregao","codbdi","codneg","tpmerc"]
KEY_EXT = ["codisi","dismes"]
CONTRACT = ["especi","prazot","datven","preexe","indopc","ptoexe"]
ALL_DISTINGUISHERS = KEY_EXT + CONTRACT + ["modref"]

def parse(raw):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    def s(a,z):
        return b[a-1:z].decode("latin-1", errors="replace").strip()
    vals = [s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),
            s(53,56),s(57,69),s(70,82),s(83,95),s(96,108),s(109,121),s(122,134),
            s(135,147),s(148,152),s(153,170),s(171,188),s(189,201),s(202,202),
            s(203,210),s(211,217),s(218,230),s(231,242),s(243,245)]
    return dict(zip(FIELDS, vals))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--max-examples", type=int, default=100)
    a = ap.parse_args()

    groups = defaultdict(list)
    rows = 0
    with zipfile.ZipFile(a.zip) as z:
        members = [x for x in z.namelist() if not x.endswith("/")]
        if len(members) != 1:
            raise SystemExit(f"ZIP invalido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                r = parse(raw)
                if not r:
                    continue
                rows += 1
                key = tuple(r[x] for x in KEY_BASE)
                groups[key].append(r)

    collisions = {k:v for k,v in groups.items() if len(v) > 1}
    diff_counter = Counter()
    diff_combo_counter = Counter()
    tpmerc_counter = Counter()
    codbdi_counter = Counter()
    size_counter = Counter()
    examples = []

    for key, rs in collisions.items():
        size_counter[len(rs)] += 1
        tpmerc_counter[key[3]] += 1
        codbdi_counter[key[1]] += 1
        differing = [f for f in ALL_DISTINGUISHERS if len({r[f] for r in rs}) > 1]
        for f in differing:
            diff_counter[f] += 1
        diff_combo_counter[tuple(differing)] += 1
        examples.append({
            "key": list(key),
            "count": len(rs),
            "differing_fields": differing,
            "rows": [{f:r[f] for f in FIELDS} for r in rs]
        })

    examples.sort(key=lambda x:(-len(x["differing_fields"]), -x["count"], x["key"]))
    def dist(c):
        return [{"value":k,"groups":v} for k,v in sorted(c.items(), key=lambda x:(-x[1],str(x[0])))]

    # Exact duplicate check on all 25 fields, and on the base key + contract.
    exact_dup_groups = 0
    exact_dup_rows = 0
    contract_collision_groups = 0
    for rs in collisions.values():
        sigs = Counter(tuple(r[f] for f in FIELDS) for r in rs)
        dups = sum(v-1 for v in sigs.values() if v>1)
        if dups:
            exact_dup_groups += 1
            exact_dup_rows += dups
        csigs = {tuple(r[f] for f in KEY_BASE + KEY_EXT + CONTRACT) for r in rs}
        if len(csigs) < len(rs):
            contract_collision_groups += 1

    out = {
        "schema_version":"1.0.0",
        "status":"FASE_07A_COLISOES_IDENTIDADE_1998_ANALISE",
        "raw_file":Path(a.zip).name,
        "rows":rows,
        "base_key":KEY_BASE,
        "distinguishing_fields_tested":ALL_DISTINGUISHERS,
        "collision_metrics":{
            "base_key_groups":len(groups),
            "collision_groups":len(collisions),
            "rows_in_collision_groups":sum(len(v) for v in collisions.values()),
            "max_group_size":max((len(v) for v in collisions.values()), default=0),
            "group_size_distribution":dist(size_counter),
            "exact_duplicate_groups":exact_dup_groups,
            "exact_duplicate_extra_rows":exact_dup_rows,
            "contractual_key_collisions":contract_collision_groups
        },
        "collisions_by_tpmerc":dist(tpmerc_counter),
        "collisions_by_codbdi":dist(codbdi_counter),
        "field_difference_frequency":dist(diff_counter),
        "difference_pattern_frequency":[
            {"fields":list(k),"groups":v}
            for k,v in sorted(diff_combo_counter.items(), key=lambda x:(-x[1],str(x[0])))
        ],
        "representative_collisions":examples[:a.max_examples],
        "governance":[
            "Esta fase investiga a causa das colisões da chave DATA+CDBDI+CODNEG+TPMERC.",
            "Nenhum campo histórico é corrigido, descartado ou sobrescrito.",
            "K4 não é promovida automaticamente a chave econômica; sua unicidade é tratada como evidência, não como prova semântica.",
            "Colisões são classificadas pelos campos que efetivamente variam dentro do mesmo grupo-base."
        ]
    }
    p=Path(a.output)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"status":out["status"],"rows":rows,"collision_groups":len(collisions),
                      "rows_in_collision_groups":out["collision_metrics"]["rows_in_collision_groups"],
                      "field_difference_frequency":out["field_difference_frequency"]},
                     ensure_ascii=False))
if __name__=="__main__":
    main()
