#!/usr/bin/env python3
"""Auditoria COTAHIST B3 1986-2026 V2: integridade, continuidade e identidade."""

import argparse, csv, hashlib, json, os, zipfile
from collections import defaultdict
from datetime import date

FIELDS = ["data_pregao","codbdi","codneg","tpmerc","nomres","especi","prazot","modref","preabe","premax","premin","premed","preult","preofc","preofv","totneg","quatot","voltot","preexe","indopc","datven","fatcot","ptoexe","codisi","dismes"]
IDENTITY_IDX = (0,1,2,3,23,24)
MAX_GAP_DAYS = 4

def parse(raw):
    b = raw.rstrip(b"\r\n")
    if len(b) != 245 or b[:2] != b"01": return None
    def s(a,z): return b[a-1:z].decode("latin-1",errors="replace").strip()
    def n(a,z,scale=0):
        x=s(a,z)
        if not x: return None
        v=int(x)
        return v/(10**scale) if scale else v
    return [s(3,10),s(11,12),s(13,24),s(25,27),s(28,39),s(40,49),s(50,52),s(53,56),n(57,69,2),n(70,82,2),n(83,95,2),n(96,108,2),n(109,121,2),n(122,134,2),n(135,147,2),n(148,152),n(153,170),n(171,188,2),n(189,201,2),s(202,202),s(203,210),n(211,217),n(218,230,6),s(231,242),s(243,245)]

def audit_year(path,year):
    sha=hashlib.sha256(); dates=set(); exact=defaultdict(int); ident=defaultdict(int)
    exact_ex=[]; ident_ex=[]; isin_to_t=defaultdict(set); t_to_i=defaultdict(set); t_to_n=defaultdict(set)
    total=valid=badlen=non01=ohlc=0; ohlc_ex=[]
    with open(path,"rb") as f:
        for raw in f:
            sha.update(raw); total+=1; body=raw.rstrip(b"\r\n")
            if len(body)!=245: badlen+=1; continue
            if body[:2]!=b"01": non01+=1; continue
            row=parse(raw)
            if row is None: continue
            valid+=1; d=row[0]
            if len(d)==8 and d.isdigit():
                try: dates.add(date(int(d[:4]),int(d[4:6]),int(d[6:8])))
                except ValueError: pass
            ik=tuple(row[i] for i in IDENTITY_IDX); fk=tuple(row)
            exact[fk]+=1; ident[ik]+=1
            if exact[fk]==2 and len(exact_ex)<20: exact_ex.append({"identity":list(ik)})
            if ident[ik]==2 and len(ident_ex)<20: ident_ex.append({"identity":list(ik)})
            codneg,codisi,nomres=row[2],row[23],row[4]
            if codneg and codisi: isin_to_t[codisi].add(codneg); t_to_i[codneg].add(codisi)
            if codneg and nomres: t_to_n[codneg].add(nomres)
            hi,lo,op,cl=row[9],row[10],row[8],row[12]
            if None not in (hi,lo,op,cl):
                if hi<lo or op>hi or op<lo or cl>hi or cl<lo:
                    ohlc+=1
                    if len(ohlc_ex)<10: ohlc_ex.append({"codneg":codneg,"data":d,"preabe":op,"premax":hi,"premin":lo,"preult":cl})
    ordered=sorted(dates); gaps=[]
    for a,b in zip(ordered,ordered[1:]):
        delta=(b-a).days
        if delta>MAX_GAP_DAYS: gaps.append({"from":a.isoformat(),"to":b.isoformat(),"calendar_days":delta})
    return {"ano":year,"raw_file":os.path.basename(path),"raw_sha256":sha.hexdigest(),"linhas_totais":total,"registros_tipo_01_validos":valid,"linhas_comprimento_diferente_245":badlen,"linhas_nao_tipo_01":non01,"datas_unicas":len(ordered),"primeira_data":ordered[0].isoformat() if ordered else None,"ultima_data":ordered[-1].isoformat() if ordered else None,"candidatos_intervalo_longo":gaps[:100],"candidatos_intervalo_longo_total":len(gaps),"duplicidade_registro_exato_grupos":sum(v>1 for v in exact.values()),"duplicidade_registro_exato_excesso_linhas":sum(v-1 for v in exact.values() if v>1),"duplicidade_identidade_instrumento_grupos":sum(v>1 for v in ident.values()),"duplicidade_identidade_instrumento_excesso_linhas":sum(v-1 for v in ident.values() if v>1),"duplicidade_registro_exato_exemplos":exact_ex,"duplicidade_identidade_instrumento_exemplos":ident_ex,"isin_com_multiplos_codneg":{k:sorted(v) for k,v in isin_to_t.items() if len(v)>1},"codneg_com_multiplos_isin":{k:sorted(v) for k,v in t_to_i.items() if len(v)>1},"codneg_com_multiplos_nomres":{k:sorted(v) for k,v in t_to_n.items() if len(v)>1},"inconsistencias_ohlc":ohlc,"exemplos_inconsistencia_ohlc":ohlc_ex}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--raw-dir",required=True); ap.add_argument("--output",required=True); ap.add_argument("--start-year",type=int,default=1986); ap.add_argument("--end-year",type=int,default=2026); args=ap.parse_args()
    reports=[]
    for year in range(args.start_year,args.end_year+1):
        path=os.path.join(args.raw_dir,f"COTAHIST_A{year}.ZIP")
        if not os.path.isfile(path): raise SystemExit(f"Arquivo ausente: {path}")
        with zipfile.ZipFile(path) as z:
            members=z.namelist()
            if len(members)!=1: raise SystemExit(f"{path}: ZIP deve conter exatamente 1 membro")
            z.extract(members[0],"/tmp/cotahist-audit-v2"); extracted=os.path.join("/tmp/cotahist-audit-v2",members[0])
            try: reports.append(audit_year(extracted,year))
            finally:
                try: os.remove(extracted)
                except OSError: pass
    first=[r["primeira_data"] for r in reports if r["primeira_data"]]; last=[r["ultima_data"] for r in reports if r["ultima_data"]]
    out={"schema_version":"2.0.0","status":"AUDITORIA_CONTINUIDADE_CONCLUIDA_V2","escopo":{"inicio":args.start_year,"fim":args.end_year},"criterio_intervalo_longo_dias":MAX_GAP_DAYS,"criterio_intervalo_longo_nota":"Intervalos de calendario sao candidatos; nao sao classificados como pregoes ausentes sem calendario oficial independente.","anos_processados":len(reports),"anos_com_erro_estrutural":[r["ano"] for r in reports if r["linhas_comprimento_diferente_245"]],"anos_com_duplicidade_registro_exato":[r["ano"] for r in reports if r["duplicidade_registro_exato_excesso_linhas"]],"anos_com_duplicidade_identidade_instrumento":[r["ano"] for r in reports if r["duplicidade_identidade_instrumento_excesso_linhas"]],"anos_com_inconsistencia_ohlc":[r["ano"] for r in reports if r["inconsistencias_ohlc"]],"primeira_data_global":min(first) if first else None,"ultima_data_global":max(last) if last else None,"por_ano":reports}
    with open(args.output,"w",encoding="utf-8") as f: json.dump(out,f,ensure_ascii=False,indent=2)
    print(json.dumps({k:out[k] for k in ("status","anos_processados","anos_com_erro_estrutural","anos_com_duplicidade_registro_exato","anos_com_duplicidade_identidade_instrumento","anos_com_inconsistencia_ohlc","primeira_data_global","ultima_data_global")},ensure_ascii=False,indent=2))
if __name__=="__main__": main()
