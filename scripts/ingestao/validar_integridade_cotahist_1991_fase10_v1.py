#!/usr/bin/env python3
"""Valida integridade independente do COTAHIST NORMALIZED 1991 — FASE 10."""
from __future__ import annotations
import csv, hashlib, json, subprocess, zipfile
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; YEAR=1991
RAW=ROOT/"dados/cotahist/raw/anual/COTAHIST_A1991.ZIP"
NORM=ROOT/"dados/cotahist/normalized/anual/COTAHIST_A1991.csv"
MANIFEST=ROOT/"dados/cotahist/normalized/manifests/COTAHIST_A1991_quality.json"
EVIDENCE=ROOT/"dados/cotahist/quality/COTAHIST_1991_FASE10_INTEGRIDADE_V1.json"
FIELDS=["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
def sha256(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
 return h.hexdigest()
def main():
 failures=[]
 for p in (RAW,NORM,MANIFEST):
  if not p.is_file(): failures.append(f"missing: {p}")
 if failures: raise SystemExit("FAIL-CLOSED: "+"; ".join(failures))
 m=json.loads(MANIFEST.read_text(encoding="utf-8"))
 rh,nh=sha256(RAW),sha256(NORM)
 if rh!=m.get("raw_sha256"): failures.append("raw_sha256 mismatch")
 if nh!=m.get("normalized_sha256"): failures.append("normalized_sha256 mismatch")
 pathspec="dados/cotahist/normalized/anual/COTAHIST_A1991.csv"
 attr=subprocess.run(["git","check-attr","filter","--",pathspec],capture_output=True,text=True,check=True).stdout.strip()
 pointer=subprocess.run(["git","cat-file","-p",f"HEAD:{pathspec}"],capture_output=True,text=True,check=True).stdout.strip()
 pl=pointer.splitlines()
 poid=next((x.split(" ",1)[1] for x in pl if x.startswith("oid sha256:")),"")
 psize=next((x.split(" ",1)[1] for x in pl if x.startswith("size ")),"")
 tracked=pointer.startswith("version https://git-lfs.github.com/spec/v1") and bool(poid) and bool(psize) and attr.endswith("filter: lfs")
 if not tracked: failures.append("normalized not tracked by Git LFS")
 with zipfile.ZipFile(RAW) as z:
  members=z.namelist(); data=z.read(members[0]); lines=data.splitlines()
  type01=[x for x in lines if x[:2]==b"01"]; bad=[x for x in type01 if len(x)!=245]
  if len(members)!=1: failures.append(f"raw zip member_count={len(members)}")
  if not type01: failures.append("no type-01 records")
  if bad: failures.append(f"type01_bad_length={len(bad)}")
 with NORM.open(encoding="utf-8",newline="") as f: rows=list(csv.reader(f))
 header=rows[0] if rows else []; data_rows=rows[1:]; dates=[r[0] for r in data_rows if r]
 invalid=[]; outside=[]
 for d in dates:
  try:
   if date.fromisoformat(d).year!=YEAR: outside.append(d)
  except ValueError: invalid.append(d)
 checks={"manifest_status_validated":m.get("status")=="VALIDADO","parser_version_1_1_0":m.get("parser_version")=="1.1.0","raw_hash_matches_manifest":rh==m.get("raw_sha256"),"normalized_hash_matches_manifest":nh==m.get("normalized_sha256"),"raw_zip_single_member":len(members)==1,"raw_type01_positive":len(type01)>0,"raw_type01_length_245":len(bad)==0,"normalized_header_25":len(header)==25 and header==FIELDS,"normalized_rows_match_manifest":len(data_rows)==m.get("linhas_normalized"),"normalized_invalid_dates_zero":len(invalid)==0,"normalized_dates_inside_1991":len(outside)==0,"normalized_lfs_tracked":tracked}
 evidence={"schema_version":"1.0.0","phase":"FASE_10","year":YEAR,"raw_path":"dados/cotahist/raw/anual/COTAHIST_A1991.ZIP","normalized_path":"dados/cotahist/normalized/anual/COTAHIST_A1991.csv","manifest_path":"dados/cotahist/normalized/manifests/COTAHIST_A1991_quality.json","raw_immutable":True,"correction_applied":False,"hashes":{"raw_sha256_actual":rh,"raw_sha256_manifest":m.get("raw_sha256"),"normalized_sha256_actual":nh,"normalized_sha256_manifest":m.get("normalized_sha256")},"raw_zip":{"member_count":len(members),"members":members,"type01_records":len(type01),"type01_bad_length_records":len(bad)},"normalized":{"header":header,"column_count":len(header),"row_count":len(data_rows),"first_date":dates[0] if dates else None,"last_date":dates[-1] if dates else None,"invalid_dates":len(invalid),"dates_outside_year":len(outside),"manifest_row_count":m.get("linhas_normalized"),"manifest_field_count":m.get("campos")},"git_lfs":{"tracked":tracked,"entry":f"HEAD:{pathspec} oid {poid} size {psize}" if tracked else "","filter_attribute":attr,"pointer_oid":poid,"pointer_size":psize},"checks":checks,"status":"VALIDADO" if not failures else "INVALIDADO","failures":failures,"decision":"FASE_10_CONCLUIDA_E_RELEASE_NORMALIZADO_AUTORIZADO" if not failures else "FASE_10_BLOQUEADA"}
 EVIDENCE.parent.mkdir(parents=True,exist_ok=True); EVIDENCE.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 if failures: raise SystemExit("FAIL-CLOSED: "+json.dumps(failures,ensure_ascii=False))
if __name__=="__main__": main()
