#!/usr/bin/env python3
"""Auditoria semantica de duplicidades da chave candidata COTAHIST.

Entrada: ZIP COTAHIST anual.
Saida: JSON com grupos duplicados, classificacao por igualdade/diferenca dos
demais campos e distribuicao dos campos divergentes.
"""
import csv, io, json, sys, zipfile
from collections import Counter, defaultdict

FIELDS = [
"data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
"preabe","premax","premin","premed","preult","preofc","preofv","totneg",
"quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"
]
KEY = ["data_pregao","codbdi","codneg","tpmerc","dismes"]

def parse(line):
    b=line.rstrip(b"\r\n")
    def s(a,z): return b[a-1:z].decode("latin-1", errors="replace").strip()
    def n(a,z,scale=0):
        x=s(a,z)
        if not x: return None
        v=int(x)
        return v/(10**scale) if scale else v
    return [
      s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56),
      n(57,69,2),n(70,82,2),n(83,95,2),n(96,108,2),n(109,121,2),n(122,134,2),
      n(135,147,2),n(148,152),n(153,170),n(171,188,2),n(189,201,2),s(202,202),
      s(203,210),n(211,217),n(218,230,6),s(231,242),s(243,245)
    ]

def main(path):
    groups=defaultdict(list)
    with zipfile.ZipFile(path) as z:
        members=z.namelist()
        if len(members)!=1: raise ValueError(f"ZIP deve conter 1 membro: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                if raw[:2]==b"01":
                    row=parse(raw)
                    key=tuple(row[FIELDS.index(k)] for k in KEY)
                    groups[key].append(row)
    dup={k:v for k,v in groups.items() if len(v)>1}
    identical=0; differing=0; diff_fields=Counter(); examples=[]
    for k, rows in dup.items():
        sigs={tuple(r) for r in rows}
        if len(sigs)==1: identical += 1
        else:
            differing += 1
            for i,name in enumerate(FIELDS):
                vals={r[i] for r in rows}
                if len(vals)>1 and name not in KEY: diff_fields[name]+=1
            if len(examples)<25:
                examples.append({"key":list(k),"occurrences":len(rows),
                    "distinct_full_rows":len(sigs),
                    "rows": [dict(zip(FIELDS,r)) for r in rows[:5]]})
    out={
      "schema_version":"1.0.0","status":"AUDITORIA_SEMANTICA_CONCLUIDA",
      "raw_file":path,"candidate_key":KEY,
      "duplicate_groups":len(dup),
      "duplicate_rows_excess":sum(len(v)-1 for v in dup.values()),
      "groups_identical_full_row":identical,
      "groups_different_full_row":differing,
      "different_field_group_counts":dict(diff_fields),
      "examples":examples
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("uso: audit_duplicate_cotahist.py COTAHIST_AAAA.ZIP")
    main(sys.argv[1])
