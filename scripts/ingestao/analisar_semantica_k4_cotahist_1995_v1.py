#!/usr/bin/env python3
"""FASE 08 — Semântica da identidade K4 para COTAHIST 1995.

Não altera RAW/NORMALIZED. Avalia a chave contratual K4 e a reutilização
temporal de CODNEG, preservando evidência auditável para a fase seguinte.
"""
from __future__ import annotations
import argparse, hashlib, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

FIELDS = [
    "data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot",
    "modref","preabe","premax","premin","premed","preult","preofc","preofv",
    "totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe",
    "codisi","dismes",
]
K4 = ["data_pregao","codbdi","codneg","tpmerc","codisi","dismes","especi",
      "prazot","datven","preexe","indopc","ptoexe"]

def parse(raw: bytes):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01":
        return None
    def s(a,z): return b[a-1:z].decode("latin-1", errors="replace").strip()
    vals=[s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56)]
    for a,z in [(57,69),(70,82),(83,95),(96,108),(109,121),(122,134),(135,147)]:
        x=s(a,z); vals.append(int(x)/100 if x else None)
    vals += [
        int(s(148,152)) if s(148,152) else None,
        int(s(153,170)) if s(153,170) else None,
        int(s(171,188))/100 if s(171,188) else None,
        int(s(189,201))/100 if s(189,201) else None,
        s(202,202), s(203,210), s(211,217),
        int(s(218,230))/1_000_000 if s(218,230) else None,
        s(231,242), s(243,245)
    ]
    return dict(zip(FIELDS, vals))

def ctx(r):
    return {k:r.get(k) for k in ["data_pregao","codbdi","codneg","tpmerc","nomres",
        "especi","prazot","preexe","indopc","datven","ptoexe","codisi","dismes",
        "totneg","quatot","voltot"]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--zip", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--max-examples", type=int, default=25)
    a=ap.parse_args()

    rows=[]
    with zipfile.ZipFile(a.zip) as z:
        members=[x for x in z.namelist() if not x.endswith("/")]
        if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for n,raw in enumerate(f,1):
                r=parse(raw)
                if r:
                    r["_source_line"]=n
                    rows.append(r)
    if not rows: raise SystemExit("Nenhum registro tipo 01")
    if any(r["data_pregao"][:4] != "1995" for r in rows):
        raise SystemExit("FAIL-CLOSED: registro fora de 1995")

    counts=Counter(tuple(r[k] for k in K4) for r in rows)
    dup={k:v for k,v in counts.items() if v>1}
    codneg=defaultdict(list)
    for r in rows: codneg[r["codneg"]].append(r)

    reuse=[]
    for code,rs in codneg.items():
        variants={f:sorted({str(r[f]) for r in rs}) for f in
                  ["tpmerc","codbdi","codisi","dismes","especi","prazot","datven","indopc"]}
        varying={k:v for k,v in variants.items() if len(v)>1}
        if varying:
            reuse.append({"codneg":code,"rows":len(rs),"dates":len({r["data_pregao"] for r in rs}),
                          "varying_attributes":varying,
                          "first_date":min(r["data_pregao"] for r in rs),
                          "last_date":max(r["data_pregao"] for r in rs)})
    reuse.sort(key=lambda x:(-x["dates"],x["codneg"]))

    by_date_code=defaultdict(list)
    for r in rows: by_date_code[(r["data_pregao"],r["codneg"])].append(r)
    same_day_reuse=[]
    for (d,c),rs in by_date_code.items():
        signatures={tuple(r[k] for k in K4 if k!="data_pregao") for r in rs}
        if len(rs)>1:
            same_day_reuse.append({"date":d,"codneg":c,"rows":len(rs),
                                   "distinct_k4_without_date":len(signatures),
                                   "contexts":[ctx(r) for r in rs[:a.max_examples]]})

    code_cardinality={k:len({r[k] for r in rows}) for k in
                      ["codneg","codisi","tpmerc","codbdi","dismes","especi","prazot","datven","indopc"]}
    out={
      "schema_version":"1.0.0",
      "status":"VALIDADO",
      "phase":"FASE08_SEMANTICA_K4_1995",
      "raw_file":Path(a.zip).name,
      "raw_sha256":hashlib.sha256(Path(a.zip).read_bytes()).hexdigest(),
      "records_type01":len(rows),
      "trading_dates":len({r["data_pregao"] for r in rows}),
      "k4_definition":K4,
      "k4_metrics":{
        "groups":len(counts),"unique_groups":sum(v==1 for v in counts.values()),
        "repeated_groups":len(dup),"rows_in_repeated_groups":sum(dup.values()),
        "duplicate_excess_rows":sum(v-1 for v in dup.values()),
        "max_group_size":max(counts.values())
      },
      "duplicate_k4_examples":[{"key":list(k),"count":v} for k,v in
          sorted(dup.items(),key=lambda x:(-x[1],str(x[0])))[:a.max_examples]],
      "codneg_reuse":{
        "distinct_codneg":len(codneg),
        "with_multiple_attribute_values":len(reuse),
        "examples":reuse[:a.max_examples]
      },
      "same_day_codneg_reuse":{
        "groups":len(same_day_reuse),
        "examples":same_day_reuse[:a.max_examples]
      },
      "code_cardinality":code_cardinality,
      "governance":[
        "K4 e uma chave contratual candidata, nao uma afirmacao automatica de identidade economica.",
        "Duplicidades K4 nao devem ser eliminadas sem evidencia de que representam duplicacao fisica do mesmo registro.",
        "Reutilizacao de CODNEG ao longo do tempo exige contexto temporal e contratual.",
        "CODBDI e TPMERC sao atributos classificatorios; nao devem ser usados isoladamente como chave economica.",
        "RAW e NORMALIZED nao sao alterados pela FASE08."
      ],
      "decision":"LIBERADO_PARA_FASE09"
    }
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":out["status"],"decision":out["decision"],"records":len(rows),
                      "k4_repeated_groups":len(dup),"same_day_reuse_groups":len(same_day_reuse)},
                     ensure_ascii=False))

if __name__=="__main__":
    main()
