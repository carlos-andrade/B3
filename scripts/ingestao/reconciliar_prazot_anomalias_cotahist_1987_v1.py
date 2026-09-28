#!/usr/bin/env python3
"""Reconciliacao dos bytes anomalos de PRAZOT no COTAHIST 1987."""
import csv, json, zipfile
from collections import Counter
from pathlib import Path

YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
CSV_PATH=Path(f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_PRAZOT_ANOMALIAS_V1.json")
CONTROL=set(range(0,32)) | {127}
FIELDS=[("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),("especi",40,49),("prazot",50,52)]

# CSV e usado apenas para reconciliar o resultado da normalizacao; o RAW continua sendo a evidencia primaria.
norm={}
with CSV_PATH.open("r",encoding="utf-8",newline="") as f:
    for row_no,row in enumerate(csv.DictReader(f),2):
        norm[row_no-1]=row

samples=[]
counts=Counter()
with zipfile.ZipFile(RAW) as z:
    member=[n for n in z.namelist() if not n.endswith("/")][0]
    with z.open(member) as f:
        record_no=0
        for line_no,b in enumerate(f,1):
            if b[:2]!=b"01":
                continue
            record_no += 1
            line=b.rstrip(b"\r\n")
            raw=line[49:52]
            bad=[x for x in raw if x in CONTROL]
            if not bad:
                continue
            vals={}
            for name,a,end in FIELDS:
                vals[name]=line[a-1:end].decode("latin-1")
            n=norm.get(record_no+1) or norm.get(record_no)
            tp=vals["tpmerc"].strip()
            counts[("tpmerc",tp)]+=1
            counts[("raw_hex",raw.hex())]+=1
            counts[("norm_prazot", (n or {}).get("prazot","<missing>"))]+=1
            if len(samples)<100:
                samples.append({
                    "raw_line":line_no,
                    "record_no":record_no,
                    "date":vals["data_pregao"],
                    "codbdi":vals["codbdi"],
                    "codneg":vals["codneg"],
                    "tpmerc":tp,
                    "especi":vals["especi"],
                    "prazot_raw_hex":raw.hex(),
                    "prazot_raw_latin1":raw.decode("latin-1"),
                    "normalized_prazot":(n or {}).get("prazot","<missing>"),
                })

result={
 "schema_version":"1.0.0",
 "status":"PRAZOT_ANOMALIAS_1987",
 "anomaly_count":len(samples),
 "distribution":{f"{k[0]}={k[1]}":v for k,v in counts.items()},
 "samples":samples,
 "interpretation":"Os bytes anormais permanecem preservados como evidencia RAW. Esta auditoria verifica se a anomalia fica concentrada em contexto de mercado e como foi representada na normalizacao; nao atribui significado economico sem fonte historica."
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","anomaly_count":len(samples)}))
