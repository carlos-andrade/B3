#!/usr/bin/env python3
"""FASE 07 — Identidade histórica COTAHIST 1986.
Analisa chaves candidatas sem alterar RAW/NORMALIZED.
"""
from __future__ import annotations
import argparse, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

FIELDS = [
    "data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot",
    "modref","preabe","premax","premin","premed","preult","preofc","preofv",
    "totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe",
    "codisi","dismes"
]

def parse(raw: bytes):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    def s(a,z):
        return b[a-1:z].decode("latin-1", errors="replace").strip()
    vals=[s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56)]
    for a,z in [(57,69),(70,82),(83,95),(96,108),(109,121),(122,134),(135,147)]:
        x=s(a,z); vals.append(int(x)/100 if x else None)
    vals += [
        int(s(148,152)) if s(148,152) else None,
        int(s(153,170)) if s(153,170) else None,
        int(s(171,188))/100 if s(171,188) else None,
        int(s(189,201))/100 if s(189,201) else None,
        s(202,202), s(203,210),
        s(211,217),
        int(s(218,230))/1_000_000 if s(218,230) else None,
        s(231,242), s(243,245)
    ]
    return dict(zip(FIELDS, vals))

KEYS = {
    "K1_data_codneg_tpmerc": ["data_pregao","codneg","tpmerc"],
    "K2_data_codbdi_codneg_tpmerc": ["data_pregao","codbdi","codneg","tpmerc"],
    "K3_data_codbdi_codneg_tpmerc_codisi_dismes": ["data_pregao","codbdi","codneg","tpmerc","codisi","dismes"],
    "K4_contractual": ["data_pregao","codbdi","codneg","tpmerc","codisi","dismes","especi","prazot","datven","preexe","indopc","ptoexe"],
}

def key(r, fields): return tuple(r.get(f) for f in fields)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--max-examples", type=int, default=25)
    a=ap.parse_args()

    stats={name: {"groups":0,"repeated_groups":0,"rows_in_repeated_groups":0,"max_group_size":0}
           for name in KEYS}
    examples=defaultdict(list)
    codneg_dates=defaultdict(set)
    codneg_variants=defaultdict(lambda: {"tpmerc":set(),"codbdi":set(),"codisi":set(),"dismes":set(),"especi":set()})
    code_counts={k:Counter() for k in ("codneg","codisi","tpmerc","codbdi","dismes","especi")}
    rows=0

    with zipfile.ZipFile(a.zip) as z:
        members=[x for x in z.namelist() if not x.endswith("/")]
        if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                r=parse(raw)
                if not r: continue
                rows += 1
                for c in code_counts: code_counts[c][str(r[c])] += 1
                cn=str(r["codneg"])
                codneg_dates[cn].add(r["data_pregao"])
                for c in codneg_variants[cn]:
                    codneg_variants[cn][c].add(str(r[c]))
                for name, fields in KEYS.items():
                    k=key(r,fields)
                    bucket=examples[name]
                    if len(bucket)<a.max_examples:
                        bucket.append({"key":list(k),"sample":{"data_pregao":r["data_pregao"],"codbdi":r["codbdi"],"codneg":r["codneg"],"tpmerc":r["tpmerc"],"codisi":r["codisi"],"dismes":r["dismes"],"especi":r["especi"],"prazot":r["prazot"],"datven":r["datven"],"preexe":r["preexe"],"indopc":r["indopc"],"ptoexe":r["ptoexe"]}})
    
    # Re-read compactly to calculate exact key cardinalities.
    keysets={name:set() for name in KEYS}
    keycounts={name:Counter() for name in KEYS}
    with zipfile.ZipFile(a.zip) as z:
        with z.open([x for x in z.namelist() if not x.endswith("/")][0]) as f:
            for raw in f:
                r=parse(raw)
                if not r: continue
                for name, fields in KEYS.items():
                    k=key(r,fields); keysets[name].add(k); keycounts[name][k]+=1
    for name in KEYS:
        c=keycounts[name]
        rep=[n for n in c.values() if n>1]
        stats[name]={"groups":len(c),"unique_groups":sum(n==1 for n in c.values()),
                      "repeated_groups":len(rep),"rows_in_repeated_groups":sum(rep),
                      "max_group_size":max(c.values(),default=0),
                      "rows":rows}
        examples[name]=[
            {"key":list(k),"count":n}
            for k,n in sorted(c.items(), key=lambda x:(-x[1],str(x[0]))) if n>1
        ][:a.max_examples]

    multi_variant=[]
    for cn,v in codneg_variants.items():
        if any(len(v[c])>1 for c in v):
            multi_variant.append({"codneg":cn,"dates":len(codneg_dates[cn]),
                                  "variants":{c:sorted(v[c]) for c in v if len(v[c])>1}})
    multi_variant.sort(key=lambda x:(-x["dates"],x["codneg"]))

    out={
      "schema_version":"1.0.0",
      "status":"FASE_07_IDENTIDADE_HISTORICA_1986_ANALISE",
      "raw_file":Path(a.zip).name,
      "rows":rows,
      "key_candidates":KEYS,
      "key_metrics":stats,
      "repeated_key_examples":dict(examples),
      "codneg_reuse_analysis":{"distinct_codneg":len(codneg_dates),
        "codneg_with_multiple_attribute_values":len(multi_variant),
        "examples":multi_variant[:a.max_examples]},
      "code_cardinality":{k:len(v) for k,v in code_counts.items()},
      "governance":[
        "Nenhuma chave candidata e declarada como chave economica definitiva apenas por unicidade.",
        "CODNEG e identificador de negociacao; sua reutilizacao ao longo do tempo exige contexto temporal e contratual.",
        "CODBDI e TPMERC permanecem atributos classificatorios e nao substituem a identificacao economica.",
        "Para derivativos e instrumentos contratuais, atributos como DATVEN, PREEXE, INDOPC, PTOEXE, PRAZOT e ESPECI podem ser materialmente relevantes.",
        "RAW e NORMALIZED nao sao alterados por esta analise."
      ]
    }
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":out["status"],"rows":rows,"keys":stats,"distinct_codneg":len(codneg_dates)},ensure_ascii=False))

if __name__=="__main__":
    main()

# CI: validar parser alinhado ao layout B3
