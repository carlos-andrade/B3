#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,zipfile,collections,hashlib
from datetime import datetime

def parse(raw):
    b=raw.rstrip(b"\r\n")
    if len(b)!=245 or b[:2]!=b"01": return None
    def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
    return {"data_pregao":s(3,10),"codbdi":s(11,12),"codneg":s(13,24),"tpmerc":s(25,27),
      "especi":s(40,49),"prazot":s(50,51),"preexe":s(189,201),"indopc":s(202,202),
      "ptoexe":s(203,215),"datven":s(216,223),"codisi":s(231,242),"dimes":s(243,245)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    rows=0; keys={k:collections.Counter() for k in ("K1","K2","K3","K4")}; ca=collections.defaultdict(set); residual=[]
    with zipfile.ZipFile(a.zip) as z:
      members=[x for x in z.namelist() if not x.endswith("/")]
      if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
      with z.open(members[0]) as f:
       for raw in f:
        r=parse(raw)
        if not r: continue
        rows+=1
        ca[r["codneg"]].add((r["codbdi"],r["tpmerc"],r["codisi"],r["dimes"],r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"]))
        k1=(r["data_pregao"],r["codneg"],r["tpmerc"]); k2=(r["data_pregao"],r["codbdi"],r["codneg"],r["tpmerc"])
        k3=k2+(r["codisi"],r["dimes"]); k4=k3+(r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"])
        for n,k in (("K1",k1),("K2",k2),("K3",k3),("K4",k4)): keys[n][k]+=1
        if k4==("19861010","62","VGO 2","030","VGORACPP","104","PP *C05","060","99991231","0.0","0","0.0"):
            residual.append({"record_sha256":hashlib.sha256(raw.rstrip(b"\r\n")).hexdigest(),"fields":r})
    matrix={}
    for n,c in keys.items():
      rep=[v for v in c.values() if v>1]
      matrix[n]={"groups":len(c),"unitary_groups":sum(v==1 for v in c.values()),"repeated_groups":len(rep),"rows_in_repeated_groups":sum(v for v in c.values() if v>1),"max_group":max(c.values())}
    result={"schema_version":"1.0.0","status":"FASE_07G_MATRIZ_IDENTIDADE_1986","generated_at_utc":datetime.utcnow().replace(microsecond=0).isoformat()+"Z","rows":rows,
      "matrix":matrix,"codneg":{"distinct":len(ca),"with_multiple_attribute_contexts":sum(len(v)>1 for v in ca.values())},
      "semantic_rules":{"codneg":"código de negociação, não identidade econômica permanente","tpmerc":"tipo de mercado","codbdi":"classificação BDI","codisi":"em 1986, código interno do papel; não ISIN","dimes":"atributo histórico de distribuição/estado de direito","k4":"chave analítica enriquecida, não chave econômica definitiva"},
      "residual_k4_records":residual,"residual_k4_count":len(residual),
      "governance":{"raw_unchanged":True,"normalized_unchanged":True,"no_economic_identity_inferred":True},
      "closure":"FASE_07G_REQUER_CONFIRMACAO_DA_COLISAO_K4" if len(residual)==2 else "FASE_07G_ANALISE_EXECUTADA"}
    with open(a.output,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2); f.write("\n")
if __name__=="__main__": main()
