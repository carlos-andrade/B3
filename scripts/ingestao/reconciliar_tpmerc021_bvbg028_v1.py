#!/usr/bin/env python3
"""Reconciliação controlada COTAHIST TPMERC=021 x BVBG.028.02 Market."""
from __future__ import annotations
import csv, json, re, zipfile, hashlib
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(".")
COTAHIST=ROOT/"dados/cotahist/raw/anual/COTAHIST_A2026.ZIP"
BVBG=ROOT/"ativos/catalogo/raw/IN260922.zip"
OUT=ROOT/"dados/cotahist/quality/COTAHIST_A2026_TPMERC021_BVBG028_RECONCILIACAO_V1.json"

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def local(tag): return tag.rsplit("}",1)[-1]

def attrs(record, wanted):
    out={}
    for el in record.iter():
        t=local(el.tag); txt=(el.text or "").strip()
        if txt and t in wanted and t not in out: out[t]=txt
    return out

# 1. Extract TPMERC=021 from COTAHIST.
samples=[]
counts=Counter()
by_ticker=Counter()
dates=Counter()
with zipfile.ZipFile(COTAHIST) as z:
    members=[n for n in z.namelist() if not n.endswith("/")]
    if len(members)!=1: raise SystemExit(f"COTAHIST ZIP ambiguo: {members}")
    with z.open(members[0]) as f:
        for line_no, raw in enumerate(f,1):
            line=raw.rstrip(b"\r\n")
            if len(line)!=245 or line[:2]!=b"01": continue
            tp=line[24:27].decode("ascii","replace")
            if tp!="021": continue
            date=line[2:10].decode("ascii","replace")
            codbdi=line[10:12].decode("latin-1","replace").strip()
            codneg=line[12:24].decode("latin-1","replace").strip()
            counts[(codbdi,codneg)]+=1
            by_ticker[codneg]+=1
            dates[date]+=1
            if len(samples)<50:
                samples.append({"line":line_no,"data_pregao":date,"codbdi":codbdi,"codneg":codneg,"tpmerc":tp})

# 2. Parse the selected BVBG.028.02 snapshot.
wanted={"TckrSymb","Id","MktIdrCd","MktNm","Asst","AsstDesc","CFICd","SctyCtgy"}
market21={}
ticker_any={}
with zipfile.ZipFile(BVBG) as outer:
    inner_names=[n for n in outer.namelist() if n.lower().endswith(".zip")]
    if not inner_names: raise SystemExit("BVBG outer ZIP sem membro ZIP")
    inner=outer.read(inner_names[0])
with zipfile.ZipFile(__import__("io").BytesIO(inner)) as z:
    xmls=[]
    for n in z.namelist():
        if not n.lower().endswith(".xml"): continue
        with z.open(n) as f: head=f.read(16384).decode("utf-8","ignore")
        ts=(re.search(r"<CreDtAndTm>([^<]+)",head) or [None,""])[1]
        declared=(re.search(r"<TtlNbOfMsg>([^<]+)",head) or [None,None])[1]
        xmls.append((ts,n,declared))
    if not xmls: raise SystemExit("BVBG sem XML")
    xml_name=max(xmls)[1]
    with z.open(xml_name) as xf:
        for event,elem in ET.iterparse(xf,events=("end",)):
            if local(elem.tag)!="Instrm": continue
            d=attrs(elem,wanted)
            t=d.get("TckrSymb","").strip()
            if t:
                ticker_any.setdefault(t,d)
                if d.get("MktIdrCd","").strip()=="21":
                    market21[t]=d
            elem.clear()

# 3. Cross-match COTAHIST 021 tickers with BVBG Market=21.
matches=[]
matched_counts=Counter()
for t,n in by_ticker.items():
    d=market21.get(t)
    if d:
        matches.append({
            "codneg":t,
            "cotahist_records_tpmerc_021":n,
            "bvbg_MktIdrCd":d.get("MktIdrCd",""),
            "bvbg_MktNm":d.get("MktNm",""),
            "bvbg_Id":d.get("Id",""),
            "bvbg_Asst":d.get("Asst",""),
            "bvbg_AsstDesc":d.get("AsstDesc",""),
            "bvbg_CFICd":d.get("CFICd",""),
            "bvbg_SctyCtgy":d.get("SctyCtgy","")
        })
        matched_counts["records"]+=n
        matched_counts["tickers"]+=1

result={
 "schema_version":"1.0-tpmerc021-bvbg028-reconciliation",
 "status":"EVIDENCE_CROSS_MATCH",
 "source_repositories":{"cotahist":"carlos-andrade/B3","bvbg028":"carlos-andrade/B3"},
 "raw":{"cotahist_path":str(COTAHIST),"cotahist_sha256":sha256(COTAHIST),"bvbg_path":str(BVBG),"bvbg_sha256":sha256(BVBG)},
 "cotahist_021":{"record_count":sum(by_ticker.values()),"distinct_codneg":len(by_ticker),"distinct_dates":len(dates),"date_distribution":dict(sorted(dates.items())),"samples":samples},
 "bvbg028":{"source_snapshot":"IN260922.zip","market_code":"21","market_code_basis":"MktIdrCd field","market21_tickers":len(market21),"mkt_idr_cd_distribution":dict(Counter(ticker_any[t].get("MktIdrCd","").strip() for t in ticker_any).most_common(50)),"mkt_nm_distribution":dict(Counter(ticker_any[t].get("MktNm","").strip() for t in ticker_any).most_common(50)),"q_suffix_bvbg":{"tickers":sum(1 for t in ticker_any if t.endswith("Q")),"mkt_idr_cd_distribution":dict(Counter(ticker_any[t].get("MktIdrCd","").strip() for t in ticker_any if t.endswith("Q")).most_common(50))}},
 "cotahist_021_semantics":{"all_codneg_end_q":all(t.endswith("Q") for t in by_ticker),"q_suffix_count":sum(1 for t in by_ticker if t.endswith("Q")),"non_q_tickers":sorted(t for t in by_ticker if not t.endswith("Q")),"codbdi_distribution":dict(Counter(c for c,t in ((k[0],k[1]) for k in counts) for _ in range(counts[(c,t)])).most_common(20))},
 "cross_match":{"distinct_codneg_matched":matched_counts["tickers"],"records_matched":matched_counts["records"],"match_rate_by_records":(matched_counts["records"]/sum(by_ticker.values()) if by_ticker else 0),"matches":sorted(matches,key=lambda x:(-x["cotahist_records_tpmerc_021"],x["codneg"]))},
 "interpretation":{"tpmerc021_equals_market21":"NOT_PROVEN_BY_THIS_CROSS_MATCH_ALONE","evidence_strength":"STRONG_CORROBORATIVE","reason":"A correspondência entre CODNEG de registros COTAHIST com TPMERC=021 e instrumentos BVBG.028.02 com MktIdrCd=21 é evidência de correlação entre os dois domínios, mas não substitui uma especificação B3 que declare explicitamente a equivalência dos campos.","raw_modified":False}
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"tpmerc021_records":result["cotahist_021"]["record_count"],"matched_records":result["cross_match"]["records_matched"],"matched_tickers":result["cross_match"]["distinct_codneg_matched"],"match_rate":result["cross_match"]["match_rate_by_records"],"output":str(OUT)},ensure_ascii=False))
