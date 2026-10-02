#!/usr/bin/env python3
import json,sys,zipfile,datetime,re
from collections import Counter
from pathlib import Path
FIELDS=["tipreg","data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
WIDTHS=[2,8,2,12,3,12,10,3,4,13,13,13,13,13,13,5,18,18,13,1,8,7,13,12,3]
def parse(line):
 p=0;d={}
 for n,w in zip(FIELDS,WIDTHS): d[n]=line[p:p+w].decode("latin-1").strip();p+=w
 return d
def main():
 zpath=Path(sys.argv[1]); out=Path(sys.argv[2]); rows=0; dates=Counter(); bad_dates=[]; weekend=[]; bad_numeric=[]; term=0
 nums=["preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","fatcot","ptoexe"]
 with zipfile.ZipFile(zpath) as z:
  name=None
  for n in z.namelist():
   if n.endswith("/"): continue
   with z.open(n) as f:
    for raw in f:
     line=raw.rstrip(b"\r\n")
     if len(line)>=245 and line[:2]==b"01": name=n;break
   if name: break
  with z.open(name) as f:
   for raw in f:
    line=raw.rstrip(b"\r\n")
    if len(line)<245 or line[:2]!=b"01": continue
    d=parse(line[:245]); rows+=1; ds=d["data_pregao"]; dates[ds]+=1
    try:
     dt=datetime.datetime.strptime(ds,"%Y%m%d").date()
     if dt.year!=1998: bad_dates.append(ds)
     if dt.weekday()>=5: weekend.append(ds)
    except: bad_dates.append(ds)
    for n in nums:
     v=d[n]
     if v and not re.fullmatch(r"-?\d+",v): bad_numeric.append({"field":n,"value":v,"data_pregao":ds,"codneg":d["codneg"]})
    if d["tpmerc"]=="030": term+=1
 trading=sorted(dates)
 out.write_text(json.dumps({"schema_version":"1.0.0","phase":"FASE08","status":"VALIDADO","year":1998,"raw_file":zpath.name,"rows_total":rows,"trading_dates":len(trading),"first_date":trading[0],"last_date":trading[-1],"weekend_records":sorted(set(weekend)),"invalid_dates":bad_dates[:100],"numeric_field_errors":bad_numeric[:100],"term_rows":term,"date_multiplicity_max":max(dates.values()),"governance":["Validação estrutural/calendário não reescreve dados.","Registros TERM não são rejeitados por geometria OHLC clássica.","Anomalias documentadas permanecem preservadas."]},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 assert rows>0 and not bad_dates and not weekend and not bad_numeric
 print(json.dumps({"rows_total":rows,"trading_dates":len(trading),"term_rows":term}))
if __name__=="__main__": main()
