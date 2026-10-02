#!/usr/bin/env python3
import csv, hashlib, json
from pathlib import Path
RAW=Path("dados/cotahist/raw/anual/COTAHIST_A1998.ZIP")
MANIFEST=Path("dados/cotahist/normalized/manifests/COTAHIST_A1998_quality.json")
NORMALIZED=Path("dados/cotahist/normalized/anual/COTAHIST_A1998.csv")
EVIDENCE=Path("dados/cotahist/quality/COTAHIST_1998_FASE13_MATERIALIZACAO_V1.json")
EXPECTED=["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()
def main():
    failures=[]
    for p,n in ((RAW,"RAW_1998_AUSENTE"),(MANIFEST,"MANIFESTO_1998_AUSENTE"),(NORMALIZED,"NORMALIZED_1998_AUSENTE")):
        if not p.exists(): failures.append(n)
    m=json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    raw_sha=sha(RAW) if RAW.exists() else None
    norm_sha=sha(NORMALIZED) if NORMALIZED.exists() else None
    if m.get("status")!="VALIDADO": failures.append("MANIFESTO_1998_NAO_VALIDADO")
    if m.get("parser_version")!="1.1.0": failures.append("PARSER_VERSION_DIVERGENTE")
    if m.get("campos")!=25: failures.append("CAMPOS_DIVERGENTES")
    if raw_sha and raw_sha!=m.get("raw_sha256"): failures.append("RAW_SHA256_DIVERGENTE")
    rows=0; fields=0; invalid=0; outside=0; first=None; last=None
    if NORMALIZED.exists():
        with NORMALIZED.open(encoding="utf-8",newline="") as f:
            r=csv.reader(f); header=next(r,[]); fields=len(header)
            if header!=EXPECTED: failures.append("HEADER_DIVERGENTE")
            import datetime as dt
            for row in r:
                rows+=1
                if len(row)!=25: failures.append("REGISTRO_COM_25_CAMPOS_INCORRETO"); continue
                d=row[0]
                try:
                    dt.date(int(d[:4]),int(d[5:7]),int(d[8:10]))
                    if int(d[:4])!=1998: outside+=1
                    first=d if first is None or d<first else first
                    last=d if last is None or d>last else last
                except Exception: invalid+=1
    if norm_sha and norm_sha!=m.get("normalized_sha256"): failures.append("NORMALIZED_SHA256_DIVERGENTE")
    if rows!=m.get("linhas_normalized"): failures.append("LINHAS_NORMALIZED_DIVERGENTES")
    if invalid!=m.get("datas_invalidas",0): failures.append("DATAS_INVALIDAS_DIVERGENTES")
    if outside!=m.get("datas_fora_do_ano",0): failures.append("DATAS_FORA_DO_ANO_DIVERGENTES")
    out={"schema_version":"1.0.0","phase":"FASE_13","year":1998,"purpose":"MATERIALIZACAO_NORMALIZED",
      "raw_path":str(RAW),"manifest_path":str(MANIFEST),"normalized_path":str(NORMALIZED),
      "raw_sha256_actual":raw_sha,"raw_sha256_manifest":m.get("raw_sha256"),
      "normalized_sha256_actual":norm_sha,"normalized_sha256_manifest":m.get("normalized_sha256"),
      "rows_normalized":rows,"rows_manifest":m.get("linhas_normalized"),"fields":fields,
      "first_date":first,"last_date":last,"invalid_dates":invalid,"dates_outside_year":outside,
      "failures":failures,"status":"VALIDADO" if not failures else "INVALIDADO",
      "decision":"NORMALIZED_1998_MATERIALIZADO" if not failures else "FASE_13_BLOQUEADA"}
    EVIDENCE.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if failures: raise SystemExit("FAIL-CLOSED: "+"; ".join(failures))
if __name__=="__main__": main()
