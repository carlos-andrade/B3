#!/usr/bin/env python3
"""FASE 07F — investigação da colisão residual K4 no COTAHIST 1986."""
from __future__ import annotations
import argparse,json,zipfile,hashlib
from pathlib import Path
from datetime import datetime, timezone

TARGET=("19861010","62","VGO 2","030","VGORACPP","104","PP *C05","060",99991231,0.0,"0","0")

def parse(raw: bytes):
    b=raw.rstrip(b"\r\n")
    if len(b)!=245 or b[:2]!=b"01": return None
    def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
    return {
      "tipo_registro":s(1,2),"data_pregao":s(3,10),"codbdi":s(11,12),"codneg":s(13,24),
      "tpmerc":s(25,27),"nome_resumido":s(28,39),"especi":s(40,49),"prazot":s(50,52),
      "modref":s(52,56),"preab":s(57,69),"premax":s(70,82),"premin":s(83,95),
      "premed":s(96,108),"preult":s(109,121),"preofc":s(122,134),"preofv":s(135,147),
      "totneg":s(148,152),"quatot":s(153,170),"voltot":s(171,188),"preexe":int(s(189,201))/100 if s(189,201) else None,
      "indopc":s(202,202),"ptoexe":int(s(203,210))/100 if s(203,210) else None,"datven":int(s(211,217)) if s(211,217) else None,
      "codisi":s(231,242),"dimes":s(243,245),
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--zip",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
    matches=[]; line_no=0
    with zipfile.ZipFile(a.zip) as z:
      members=[x for x in z.namelist() if not x.endswith("/")]
      if len(members)!=1: raise SystemExit(f"ZIP inválido: {members}")
      with z.open(members[0]) as f:
        for raw in f:
          line_no+=1; r=parse(raw)
          if not r: continue
          key=(r["data_pregao"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dimes"],r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"])
          if key==TARGET:
            rr=dict(r); rr["source_line"]=line_no; rr["raw_sha256"]=hashlib.sha256(raw.rstrip(b"\r\n")).hexdigest(); matches.append(rr)
    differences={}
    if len(matches)>=2:
      for k in sorted(set().union(*(m.keys() for m in matches))):
        vals=[m.get(k) for m in matches]
        if len(set(map(str,vals)))>1: differences[k]=vals
    result={
      "schema_version":"1.0.0","status":"FASE_07F_COLISAO_K4_1986_ANALISE",
      "generated_at_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z"),
      "raw_file":"COTAHIST_A1986.ZIP","target_k4":list(TARGET),
      "match_count":len(matches),"matches":matches,"differences":differences,
      "classification_rule":{"two_rows_same_k4_is_not_automatic_duplicate":True,"economic_identity_not_inferred":True,"raw_unchanged":True,"normalized_unchanged":True},
      "conclusion_status":"REQUIRES_SEMANTIC_REVIEW" if len(matches)==2 else ("NO_MATCH" if len(matches)==0 else "UNEXPECTED_MATCH_COUNT")
    }
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    with open(a.output,"w",encoding="utf-8") as f: json.dump(result,f,ensure_ascii=False,indent=2); f.write("\n")
if __name__=="__main__": main()

# Trigger de execucao auditavel FASE 07


# CI: publicar evidencia somente apos commit local e rebase
