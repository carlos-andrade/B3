#!/usr/bin/env python3
import json, sys, zipfile
from collections import Counter
from pathlib import Path

FIELDS=["tipreg","data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
WIDTHS=[2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,13,5,18,18,13,1,8,7,13,12,3]

def parse(line):
    p=0; d={}
    for name,w in zip(FIELDS,WIDTHS):
        d[name]=line[p:p+w].decode("latin-1").strip(); p+=w
    return d

def read_year(path):
    rows=0; term=0; keys=Counter(); base=Counter(); invalid=[]
    with zipfile.ZipFile(path) as z:
        names=[n for n in z.namelist() if not n.endswith("/")]
        data_name=None
        for name in names:
            with z.open(name) as f:
                for raw in f:
                    line=raw.rstrip(b"\r\n")
                    if len(line)>=245 and line[:2]==b"01":
                        data_name=name; break
            if data_name: break
        if not data_name: raise RuntimeError(f"Nenhum registro tipo 01 em {path}")
        with z.open(data_name) as f:
            for raw in f:
                line=raw.rstrip(b"\r\n")
                if len(line)<245 or line[:2]!=b"01": continue
                d=parse(line[:245]); rows+=1
                if d["tpmerc"]!="030": continue
                term+=1
                p=d["prazot"]
                if not p.isdigit(): invalid.append({"data_pregao":d["data_pregao"],"codneg":d["codneg"],"prazot":p})
                keys[(d["data_pregao"],d["codbdi"],d["codneg"],d["tpmerc"],p)]+=1
                base[(d["data_pregao"],d["codbdi"],d["codneg"],d["tpmerc"])]+=1
    dup=sum(v-1 for v in keys.values() if v>1)
    base_multi=sum(1 for v in Counter(base).values() if v>1)
    return {"rows_total":rows,"term_rows":term,"candidate_key_groups":len(keys),"candidate_duplicate_groups":sum(1 for v in keys.values() if v>1),"candidate_duplicate_extra_rows":dup,"base_groups":len(base),"base_groups_multiple_rows":base_multi,"invalid_prazot":invalid[:100]}

def main():
    inputs=sys.argv[1:-1]; out=Path(sys.argv[-1])
    years={}
    for raw in inputs:
        y=Path(raw).stem.split("A")[-1]
        years[y]=read_year(Path(raw))
    out.parent.mkdir(parents=True,exist_ok=True)
    result={"schema_version":"1.0.0","phase":"FASE07C","status":"ANALISE_CHAVE_PRAZOT_ANOS_ADJACENTES","candidate_key":["data_pregao","codbdi","codneg","tpmerc","prazot"],"years":years,"governance":["A chave candidata deve ser testada por ano antes de qualquer promoção.","Duplicidade da chave candidata é bloqueador de promoção.","Nenhum RAW ou dado normalizado é alterado.","A validação de 1998 é comparada com 1997 e 1999; ausência de duplicidade não prova, isoladamente, semântica econômica universal."]}
    result["decision"]="CANDIDATA_SEM_DUPLICIDADE_NOS_ANOS_TESTADOS" if all(v["candidate_duplicate_groups"]==0 and not v["invalid_prazot"] for v in years.values()) else "BLOQUEADA_POR_DUPLICIDADE_OU_PRAZOT"
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"decision":result["decision"],"years":years},ensure_ascii=False))

if __name__=="__main__": main()
