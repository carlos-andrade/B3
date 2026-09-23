#!/usr/bin/env python3
"""Processa BVBG.028.02 (InstrumentReport) de um IN{YYMMDD}.zip da B3.

Seleciona o snapshot XML mais recente pelo CreDtAndTm, valida TtlNbOfMsg
e gera inventário UTF-8/semicolon, estatísticas e log de validação.
"""
import csv, json, os, re, sys, zipfile, hashlib, urllib.request
from collections import Counter
from datetime import datetime
from xml.etree import ElementTree as ET

DATE = os.environ.get("DATA", sys.argv[1] if len(sys.argv) > 1 else "2026-09-22")
YYMMDD = datetime.strptime(DATE, "%Y-%m-%d").strftime("%y%m%d")
ZIP_PATH = f"ativos/catalogo/raw/IN{YYMMDD}.zip"
URL = f"https://www.b3.com.br/pesquisapregao/download?filelist=IN{YYMMDD}.zip"
os.makedirs(os.path.dirname(ZIP_PATH), exist_ok=True)
if not os.path.exists(ZIP_PATH):
    urllib.request.urlretrieve(URL, ZIP_PATH)

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""): h.update(b)
    return h.hexdigest()

def local(tag): return tag.rsplit("}",1)[-1]

def children_map(el):
    return {local(c.tag): c for c in list(el)}

def text_at(root, *path):
    cur=root
    for p in path:
        found=None
        for c in list(cur):
            if local(c.tag)==p:
                found=c; break
        if found is None: return ""
        cur=found
    return (cur.text or "").strip()

def attrs(record):
    out={}
    for el in record.iter():
        t=local(el.tag)
        txt=(el.text or "").strip()
        if not txt: continue
        # Keep selected leaf names; first occurrence is retained.
        if t in WANT and t not in out: out[t]=txt
    return out

WANT={
"RptDt","TckrSymb","Id","Tp","Prtry","MktIdrCd","Asst","AsstDesc","SgmtNm","MktNm",
"Desc","ISIN","CFICd","SctyCtgy","XprtnDt","XprtnCd","TradgStartDt","TradgEndDt",
"BaseCd","OptnTp","CtrctMltplr","TradgCcy","CrpnNm","MktCptlstn","SttlmTp","Undrlyg",
"StrkPric","ExrcPric","OptnStyle","OptnTp","UnitOfMeasr","LotSize","Issr"
}
FIELDS=["RptDt","TckrSymb","Id","Tp","Prtry","MktIdrCd","Asst","AsstDesc","SgmtNm","MktNm",
"Desc","ISIN","CFICd","SctyCtgy","XprtnDt","XprtnCd","TradgStartDt","TradgEndDt","BaseCd",
"OptnTp","CtrctMltplr","TradgCcy","CrpnNm","MktCptlstn","SttlmTp","Undrlyg","StrkPric",
"ExrcPric","OptnStyle","UnitOfMeasr","LotSize","Issr"]

with zipfile.ZipFile(ZIP_PATH) as outer:
    inner_name=next(n for n in outer.namelist() if n.lower().endswith(".zip"))
    inner=outer.read(inner_name)
with zipfile.ZipFile(__import__("io").BytesIO(inner)) as z:
    xmls=[]
    for n in z.namelist():
        if not n.lower().endswith(".xml"): continue
        with z.open(n) as f:
            head=f.read(16384).decode("utf-8","ignore")
        m=re.search(r"<CreDtAndTm>([^<]+)",head)
        ts=m.group(1) if m else ""
        m2=re.search(r"<TtlNbOfMsg>([^<]+)",head)
        declared=int(m2.group(1)) if m2 else None
        xmls.append((ts,n,declared))
    xmls.sort(reverse=True)
    ts, xml_name, declared=xmls[0]
    out_csv=f"ativos/catalogo/INVENTARIO_B3_{DATE}.csv"
    os.makedirs(os.path.dirname(out_csv),exist_ok=True)
    type_counts=Counter(); rows=0; missing_ticker=0; ids=set(); duplicate_ids=0
    with z.open(xml_name) as xf, open(out_csv,"w",newline="",encoding="utf-8") as out:
        w=csv.DictWriter(out,fieldnames=FIELDS,delimiter=";",extrasaction="ignore")
        w.writeheader()
        for event,elem in ET.iterparse(xf,events=("end",)):
            if local(elem.tag)!="Instrm": continue
            d=attrs(elem)
            w.writerow({k:d.get(k,"") for k in FIELDS})
            rows+=1
            if not d.get("TckrSymb"): missing_ticker+=1
            ident=d.get("Id","")
            if ident:
                if ident in ids: duplicate_ids+=1
                ids.add(ident)
            # Approximate instrument family from the first informative category fields.
            family=d.get("AsstDesc") or d.get("Asst") or d.get("SctyCtgy") or "SEM_CLASSIFICACAO"
            type_counts[family]+=1
            elem.clear()

valid=(declared is not None and rows==declared)
stats={
"capture_date":DATE,"source_url":URL,"layout":"BVBG.028.02","raw_file":ZIP_PATH,
"raw_size_bytes":os.path.getsize(ZIP_PATH),"raw_sha256":sha256(ZIP_PATH),
"selected_snapshot":xml_name,"creation_timestamp":ts,"declared_records":declared,
"parsed_records":rows,"count_validation":valid,"missing_ticker":missing_ticker,
"duplicate_fin_instrm_id":duplicate_ids,"family_counts":dict(type_counts.most_common())
}
os.makedirs("ativos/catalogo/estatisticas",exist_ok=True)
with open(f"ativos/catalogo/estatisticas/ESTATISTICAS_BVBG028_{DATE}.json","w",encoding="utf-8") as f:
    json.dump(stats,f,ensure_ascii=False,indent=2)
os.makedirs("ativos/catalogo/logs",exist_ok=True)
with open(f"ativos/catalogo/logs/VALIDACAO_BVBG028_{DATE}.json","w",encoding="utf-8") as f:
    json.dump(stats,f,ensure_ascii=False,indent=2)
if not valid:
    raise SystemExit(f"VALIDACAO_FALHOU: declarado={declared} parseado={rows}")
print(json.dumps(stats,ensure_ascii=False,indent=2))
