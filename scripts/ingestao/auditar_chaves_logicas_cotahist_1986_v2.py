#!/usr/bin/env python3
"""Auditoria de chaves lógicas COTAHIST 1986; somente leitura do RAW."""
from __future__ import annotations
import argparse,json,zipfile
from collections import Counter,defaultdict
from decimal import Decimal
from pathlib import Path

FIELDS=["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]

def parse(raw):
    b=raw.rstrip(b"\r\n")
    if len(b)!=245 or b[:2]!=b"01":
        return None
    def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
    vals=[s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56)]
    for a,z in [(57,69),(70,82),(83,95),(96,108),(109,121),(122,134),(135,147)]:
        x=s(a,z); vals.append(Decimal(x)/100 if x else None)
    vals += [
        int(s(148,152)) if s(148,152) else None,
        int(s(153,170)) if s(153,170) else None,
        Decimal(s(171,188))/100 if s(171,188) else None,
        Decimal(s(189,201))/100 if s(189,201) else None,
        s(202,202),s(203,210),
        int(s(211,217)) if s(211,217) else None,
        Decimal(s(218,230))/Decimal(10**6) if s(218,230) else None,
        s(231,242),s(243,245)
    ]
    return dict(zip(FIELDS,vals))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--zip",required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--repeat-samples",type=int,default=100)
    a=ap.parse_args()

    key_defs={
        "K1_data_codneg_tpmerc":["data_pregao","codneg","tpmerc"],
        "K2_data_codbdi_codneg_tpmerc":["data_pregao","codbdi","codneg","tpmerc"],
        "K3_data_codbdi_codneg_tpmerc_codisi_dismes":["data_pregao","codbdi","codneg","tpmerc","codisi","dismes"],
        "K4_contractual":["data_pregao","codbdi","codneg","tpmerc","especi","prazot","datven","preexe","indopc","codisi","dismes"],
    }
    counters={k:Counter() for k in key_defs}
    repeat_samples={k:[] for k in key_defs}
    k4_rows_by_key=defaultdict(list)
    raw_rows=0

    with zipfile.ZipFile(a.zip) as z:
        members=[x for x in z.namelist() if not x.endswith("/")]
        if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
        with z.open(members[0]) as f:
            for raw in f:
                r=parse(raw)
                if not r: continue
                raw_rows+=1
                for name,fields in key_defs.items():
                    key=tuple(r[x] for x in fields)
                    counters[name][key]+=1
                    if name=="K4_contractual":
                        k4_rows_by_key[key].append(r)
                    if name=="K4_contractual":
                        k4_rows_by_key[key].append(r)

    for name,c in counters.items():
        repeated=[(k,n) for k,n in c.items() if n>1]
        repeated.sort(key=lambda x:(-x[1],x[0]))
        repeat_samples[name]=[
            {"key":list(k),"rows":n} for k,n in repeated[:a.repeat_samples]
        ]
        if name=="K4_contractual":
            for item in repeat_samples[name]:
                key=tuple(item["key"])
                item["row_details"]=k4_rows_by_key[key]
        if name=="K4_contractual":
            for item in repeat_samples[name]:
                key=tuple(item["key"])
                item["row_details"]=k4_rows_by_key[key]

    out={
        "schema_version":"2.0.0",
        "status":"AUDITORIA_CHAVES_LOGICAS_COTAHIST_1986",
        "raw_file":Path(a.zip).name,
        "record_type_01_rows":raw_rows,
        "keys":{}
    }
    for name,fields in key_defs.items():
        c=counters[name]
        out["keys"][name]={
            "fields":fields,
            "distinct_keys":len(c),
            "repeated_groups":sum(n>1 for n in c.values()),
            "rows_inside_repeated_groups":sum(n for n in c.values() if n>1),
            "max_rows_same_key":max(c.values(),default=0),
            "repeat_samples":repeat_samples[name]
        }

    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2,default=str)+"\n",encoding="utf-8")
    print(json.dumps(out["keys"],ensure_ascii=False,default=str))

if __name__=="__main__":
    main()
