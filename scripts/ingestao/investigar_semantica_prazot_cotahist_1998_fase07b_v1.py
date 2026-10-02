#!/usr/bin/env python3
import json, sys, zipfile
from collections import Counter, defaultdict
from pathlib import Path

ZIP_PATH = Path(sys.argv[1])
OUT_PATH = Path(sys.argv[2])

FIELDS = [
    "tipreg","data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref",
    "preabe","premax","premin","premed","preult","preofc","preofv","totneg",
    "quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"
]
WIDTHS = [2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,13,5,18,18,13,1,8,7,13,12,3]

def parse(line):
    p=0; d={}
    for name,w in zip(FIELDS,WIDTHS):
        d[name]=line[p:p+w].decode("latin-1").strip()
        p += w
    return d

rows=0
term_rows=[]
prazot_counts=Counter()
prazot_by_month=defaultdict(Counter)
suffix_counts=Counter()
base_groups=defaultdict(set)
key_groups=defaultdict(int)
codneg_by_prazot=defaultdict(set)
codneg_dates=defaultdict(set)
invalid_prazot=[]

with zipfile.ZipFile(ZIP_PATH) as z:
    names=[n for n in z.namelist() if not n.endswith("/")]
    if not names:
        raise RuntimeError("Nenhum arquivo de dados encontrado no ZIP")
    # O ZIP pode conter arquivos auxiliares. Seleciona o membro que efetivamente
    # contem registros COTAHIST tipo 01, validando a primeira linha de 245 bytes.
    data_name=None
    for name in names:
        with z.open(name) as probe:
            for raw_probe in probe:
                probe_line=raw_probe.rstrip(b"\\r\\n")
                if len(probe_line) >= 245 and probe_line[:2] == b"01":
                    data_name=name
                    break
        if data_name:
            break
    if not data_name:
        raise RuntimeError("Nenhum membro com registros COTAHIST tipo 01 encontrado no ZIP")
    with z.open(data_name) as f:
        for raw in f:
            line=raw.rstrip(b"\r\n")
            if len(line) < 245 or line[:2] != b"01":
                continue
            d=parse(line[:245]); rows += 1
            if d["tpmerc"] != "030":
                continue
            term_rows.append(d)
            p=d["prazot"]
            prazot_counts[p] += 1
            prazot_by_month[d["data_pregao"][:6]][p] += 1
            codneg_by_prazot[p].add(d["codneg"])
            codneg_dates[d["codneg"]].add(d["data_pregao"])
            suffix_counts["ends_T" if d["codneg"].rstrip().endswith("T") else "other"] += 1
            base=(d["data_pregao"],d["codbdi"],d["codneg"],d["tpmerc"])
            base_groups[base].add(p)
            key=(d["data_pregao"],d["codbdi"],d["codneg"],d["tpmerc"],p)
            key_groups[key] += 1
            if not p.isdigit():
                invalid_prazot.append({"data_pregao":d["data_pregao"],"codneg":d["codneg"],"prazot":p})

multi_prazot_bases={str(k):sorted(v) for k,v in base_groups.items() if len(v)>1}
duplicate_full_keys=sum(1 for v in key_groups.values() if v>1)
rows_duplicate_full_keys=sum(v-1 for v in key_groups.values() if v>1)

out={
 "schema_version":"1.0.0",
 "status":"FASE_07B_SEMANTICA_PRAZOT_TPMERC030_1998_ANALISE",
 "raw_file":ZIP_PATH.name,
 "rows_total":rows,
 "term_rows":len(term_rows),
 "official_interpretation":{
   "tpmerc_030":"TERMO",
   "prazot":"PRAZO EM DIAS DO MERCADO A TERMO",
   "source":"B3 Historical Quotations Layout"
 },
 "prazot_distribution":[{"value":k,"rows":v} for k,v in sorted(prazot_counts.items())],
 "prazot_monthly":[{"month":m,"values":dict(sorted(c.items()))} for m,c in sorted(prazot_by_month.items())],
 "codneg_suffix":{
   "ends_T":suffix_counts["ends_T"],
   "other":suffix_counts["other"],
   "ends_T_rate": round(suffix_counts["ends_T"]/len(term_rows),8) if term_rows else 0
 },
 "base_key_semantics":{
   "base_key":["data_pregao","codbdi","codneg","tpmerc"],
   "base_groups":len(base_groups),
   "groups_with_multiple_prazot":len(multi_prazot_bases),
   "examples":[{"base_key":list(eval(k)) if k.startswith("(") else k,"prazot_values":v} for k,v in list(multi_prazot_bases.items())[:50]]
 },
 "candidate_row_key":{
   "key":["data_pregao","codbdi","codneg","tpmerc","prazot"],
   "groups":len(key_groups),
   "duplicate_groups":duplicate_full_keys,
   "duplicate_extra_rows":rows_duplicate_full_keys
 },
 "invalid_prazot":invalid_prazot[:100],
 "governance":[
   "PRAZOT nao deve ser descartado em TPMERC=030: a especificacao oficial o define como prazo em dias do mercado a termo.",
   "DATA+CODBDI+CODNEG+TPMERC nao representa necessariamente uma unica linha de termo quando ha varios PRAZOT no mesmo pregao.",
   "A chave DATA+CODBDI+CODNEG+TPMERC+PRAZOT e candidata a chave de observacao diaria do termo, sujeita a validacao em anos adjacentes.",
   "Nenhum dado RAW ou normalizado e alterado por esta investigacao."
 ]
}
# serializar exemplos diretamente como arrays estruturados; nunca usar repr/eval de tuplas
out["base_key_semantics"]["examples"]=[]
for k,v in list(multi_prazot_bases.items())[:50]:
    out["base_key_semantics"]["examples"].append({"base_key":list(k),"prazot_values":v})
OUT_PATH.parent.mkdir(parents=True,exist_ok=True)
OUT_PATH.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"rows_total":rows,"term_rows":len(term_rows),"prazot_distribution":dict(prazot_counts),"base_groups":len(base_groups),"groups_with_multiple_prazot":len(multi_prazot_bases),"candidate_duplicate_groups":duplicate_full_keys},ensure_ascii=False))
