#!/usr/bin/env python3
import csv,json,sys
from datetime import datetime
from pathlib import Path

csv_path=Path(sys.argv[1]); report_path=Path(sys.argv[2]); year=int(sys.argv[3]); raw_sha=sys.argv[4]; norm_sha=sys.argv[5]
with csv_path.open(encoding="utf-8", newline="") as f:
    reader=csv.DictReader(f)
    rows=list(reader)
    fields=reader.fieldnames or []
if not rows:
    raise SystemExit("NORMALIZED sem registros")
required={"data_pregao","codbdi","codneg","tpmerc","nomres","preabe","premax","premin","premed","preult","totneg","quatot","voltot","codisi","dismes"}
missing=sorted(required-set(fields))
if missing:
    raise SystemExit("campos ausentes: "+str(missing))
dates=[r["data_pregao"] for r in rows]
bad=[]
for d in dates:
    try: datetime.strptime(d,"%Y-%m-%d")
    except ValueError: bad.append(d)
wrong=[d for d in dates if not d.startswith(f"{year}-")]
if bad or wrong:
    raise SystemExit(f"falha de qualidade: invalidas={len(bad)} fora_ano={len(wrong)}")
report={
    "schema_version":"1.0.0","status":"VALIDADO","ano":year,"parser_version":"1.1.0","source":"B3",
    "raw_file":f"COTAHIST_A{year}.ZIP","raw_sha256":raw_sha,
    "normalized_file":f"COTAHIST_A{year}.csv","normalized_sha256":norm_sha,
    "linhas_normalized":len(rows),"campos":len(fields),
    "primeira_data":min(dates),"ultima_data":max(dates),
    "datas_invalidas":0,"datas_fora_do_ano":0
}
report_path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
