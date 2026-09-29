#!/usr/bin/env python3
"""Valida integridade independente do COTAHIST NORMALIZED 1990 — FASE 10."""

from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YEAR = 1990
RAW = ROOT / "dados/cotahist/raw/anual/COTAHIST_A1990.ZIP"
NORM = ROOT / "dados/cotahist/normalized/anual/COTAHIST_A1990.csv"
MANIFEST = ROOT / "dados/cotahist/normalized/manifests/COTAHIST_A1990_quality.json"
EVIDENCE = ROOT / "dados/cotahist/quality/COTAHIST_1990_FASE10_INTEGRIDADE_V1.json"

EXPECTED_FIELDS = ["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]

def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    failures=[]
    if not RAW.is_file(): failures.append(f"missing: {RAW}")
    if not NORM.is_file(): failures.append(f"missing: {NORM}")
    if not MANIFEST.is_file(): failures.append(f"missing: {MANIFEST}")
    if failures:
        raise SystemExit("FAIL-CLOSED: " + "; ".join(failures))

    m=json.loads(MANIFEST.read_text(encoding="utf-8"))
    raw_hash=sha256(RAW); norm_hash=sha256(NORM)
    if raw_hash != m.get("raw_sha256"): failures.append("raw_sha256 mismatch")
    if norm_hash != m.get("normalized_sha256"): failures.append("normalized_sha256 mismatch")

    pathspec=NORM.as_posix()
    attr=subprocess.run(["git","check-attr","filter","--",pathspec],capture_output=True,text=True,check=True).stdout.strip()
    pointer=subprocess.run(["git","cat-file","-p",f"HEAD:{pathspec}"],capture_output=True,text=True,check=True).stdout.strip()
    pointer_lines=pointer.splitlines()
    pointer_oid=next((line.split(" ",1)[1] for line in pointer_lines if line.startswith("oid sha256:")), "")
    pointer_size=next((line.split(" ",1)[1] for line in pointer_lines if line.startswith("size ")), "")
    tracked=pointer.startswith("version https://git-lfs.github.com/spec/v1") and bool(pointer_oid) and bool(pointer_size) and attr.endswith("filter: lfs")
    entry=f"HEAD:{pathspec} oid sha256:{pointer_oid} size {pointer_size}" if tracked else ""
    if not tracked: failures.append("normalized not tracked by Git LFS")

    with zipfile.ZipFile(RAW) as z:
        members=z.namelist()
        if len(members)!=1: failures.append(f"raw zip member_count={len(members)}")
        data=z.read(members[0])
        lines=data.splitlines()
        type01=[x for x in lines if x[:2]==b"01"]
        bad=[x for x in type01 if len(x)!=245]
        if not type01: failures.append("no type-01 records")
        if bad: failures.append(f"type01_bad_length={len(bad)}")
        raw_type01=len(type01); bad_len=len(bad)

    import csv
    with NORM.open(encoding="utf-8",newline="") as f:
        rows=list(csv.reader(f))
    header=rows[0] if rows else []
    data_rows=rows[1:]
    dates=[r[0] for r in data_rows if r]
    invalid=[]
    outside=[]
    from datetime import date
    for d in dates:
        try:
            dt=date.fromisoformat(d)
            if dt.year != YEAR: outside.append(d)
        except ValueError:
            invalid.append(d)
    if header != EXPECTED_FIELDS: failures.append("normalized header mismatch")
    if len(data_rows) != m.get("linhas_normalized"): failures.append("normalized row count mismatch")
    if invalid: failures.append(f"invalid_dates={len(invalid)}")
    if outside: failures.append(f"dates_outside_year={len(outside)}")
    if m.get("status")!="VALIDADO": failures.append("manifest status not VALIDADO")
    if m.get("parser_version")!="1.1.0": failures.append("parser_version mismatch")

    evidence={
      "schema_version":"1.0.0","phase":"FASE_10","year":YEAR,
      "raw_path":RAW.as_posix(),"normalized_path":NORM.as_posix(),"manifest_path":MANIFEST.as_posix(),
      "raw_immutable":True,"correction_applied":False,
      "hashes":{"raw_sha256_actual":raw_hash,"raw_sha256_manifest":m.get("raw_sha256"),"normalized_sha256_actual":norm_hash,"normalized_sha256_manifest":m.get("normalized_sha256")},
      "raw_zip":{"member_count":len(members),"members":members,"type01_records":raw_type01,"type01_bad_length_records":bad_len},
      "normalized":{"header":header,"column_count":len(header),"row_count":len(data_rows),"first_date":dates[0] if dates else None,"last_date":dates[-1] if dates else None,"invalid_dates":len(invalid),"dates_outside_year":len(outside),"manifest_row_count":m.get("linhas_normalized"),"manifest_field_count":m.get("campos")},
      "git_lfs":{"tracked":tracked,"entry":entry,"filter_attribute":attr,"pointer_oid":pointer_oid,"pointer_size":pointer_size},
      "checks":{"manifest_status_validated":m.get("status")=="VALIDADO","parser_version_1_1_0":m.get("parser_version")=="1.1.0","raw_hash_matches_manifest":raw_hash==m.get("raw_sha256"),"normalized_hash_matches_manifest":norm_hash==m.get("normalized_sha256"),"raw_zip_single_member":len(members)==1,"raw_type01_positive":raw_type01>0,"raw_type01_length_245":bad_len==0,"normalized_header_25":len(header)==25 and header==EXPECTED_FIELDS,"normalized_rows_match_manifest":len(data_rows)==m.get("linhas_normalized"),"normalized_invalid_dates_zero":len(invalid)==0,"normalized_dates_inside_1990":len(outside)==0,"normalized_lfs_tracked":tracked and attr.endswith("filter: lfs")},
      "status":"VALIDADO" if not failures else "INVALIDADO","failures":failures,
      "decision":"FASE_10_CONCLUIDA_E_RELEASE_NORMALIZADO_AUTORIZADO" if not failures else "FASE_10_BLOQUEADA"
    }
    EVIDENCE.parent.mkdir(parents=True,exist_ok=True)
    EVIDENCE.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if failures: raise SystemExit("FAIL-CLOSED: "+json.dumps(failures,ensure_ascii=False))

if __name__=="__main__":
    main()
