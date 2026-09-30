#!/usr/bin/env python3
import hashlib,json,zipfile
from pathlib import Path
YEAR="1993"
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP"
OUT=ROOT/f"dados/cotahist/quality/COTAHIST_{YEAR}_FASE02_INTEGRIDADE_FONTE_V1.json"
if not RAW.exists(): raise SystemExit("RAW ausente")
sha=hashlib.sha256(RAW.read_bytes()).hexdigest()
with zipfile.ZipFile(RAW) as z:
    bad=z.testzip()
    members=[n for n in z.namelist() if not n.endswith("/")]
    sizes=[z.getinfo(n).file_size for n in members]
result={"schema_version":"1.0.0","year":1993,"phase":"FASE02","status":"VALIDADO" if bad is None and len(members)==1 and sizes[0]>0 else "BLOQUEADO","raw_file":str(RAW),"raw_sha256":sha,"raw_size_bytes":RAW.stat().st_size,"zip_testzip_error":bad,"zip_file_count":len(members),"zip_members":members,"uncompressed_member_sizes":sizes,"gates":{"raw_exists":True,"zip_integrity":bad is None,"single_data_member":len(members)==1,"member_nonempty":bool(sizes and sizes[0]>0)},"decision":"VALIDADO" if bad is None and len(members)==1 and sizes[0]>0 else "BLOQUEADO","note":"Integridade da fonte: existencia, SHA-256, ZIP legivel e membro unico nao vazio. Nao certifica semantica do conteudo."}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"
",encoding="utf-8")
print(json.dumps({"status":result["status"],"sha256":sha,"members":len(members)},ensure_ascii=False))
if result["status"]!="VALIDADO": raise SystemExit(1)
