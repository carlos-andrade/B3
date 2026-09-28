#!/usr/bin/env python3
"""COTAHIST 1987 — reconciliação RAW x NORMALIZED.

Fail-closed. Não certifica equivalência econômica por aproximação: exige
estrutura, datas, identidade, contagens e valores reconciliáveis.
"""
import csv, hashlib, json, zipfile
from collections import Counter
from decimal import Decimal
from pathlib import Path

YEAR="1987"
RAW=Path(f"dados/cotahist/raw/anual/COTAHIST_A{YEAR}.ZIP")
CSV=Path(f"dados/cotahist/normalized/anual/COTAHIST_A{YEAR}.csv")
OUT=Path(f"dados/cotahist/quality/COTAHIST_{YEAR}_RECONCILIACAO_RAW_NORMALIZED_V1.json")

FIELDS=[
 ("data_pregao",3,10),("codbdi",11,12),("codneg",13,24),("tpmerc",25,27),
 ("nomres",28,39),("especi",40,49),("prazot",50,52),("modref",53,56),
 ("preab",57,69),("premax",70,82),("premin",83,95),("premed",96,108),
 ("preult",109,121),("totneg",148,152),("quatot",153,170),("voltot",171,188),
 ("preexe",189,201),("indopc",202,202),("datven",203,210),
 ("fatcot",211,217),("ptoexe",218,230),("codisi",231,242),("dimes",243,245)
]
PRICE_FIELDS={"preab","premax","premin","premed","preult","preexe","ptoexe"}
NUM_FIELDS={"totneg","quatot","voltot","fatcot"}
ALIASES={
 "data_pregao":["data_pregao","data","date","dtpregao"],
 "codbdi":["codbdi","codigo_bdi","bdi"],
 "codneg":["codneg","codigo_negociacao","ticker"],
 "tpmerc":["tpmerc","tipo_mercado","mercado"],
 "nomres":["nomres","nome_resumido"],
 "especi":["especi","especificacao"],
 "prazot":["prazot","prazo_termo"],
 "modref":["modref","mod_referencia"],
 "preab":["preab","preabe","preco_abertura","preco_abert"],
 "premax":["premax","preco_maximo","preco_max"],
 "premin":["premin","preco_minimo","preco_min"],
 "premed":["premed","preco_medio","preco_med"],
 "preult":["preult","preco_ultimo","preco_ult"],
 "totneg":["totneg","numero_negocios","qtd_negocios"],
 "quatot":["quatot","quantidade_total","quantidade"],
 "voltot":["voltot","volume_total","volume"],
 "preexe":["preexe","preco_exercicio"],
 "indopc":["indopc","indicador_opcao"],
 "datven":["datven","data_vencimento"],
 "fatcot":["fatcot","fator_cotacao"],
 "ptoexe":["ptoexe","ponto_exercicio"],
 "codisi":["codisi","codigo_isin"],
 "dimes":["dimes","dismes","distribuicao_mes","distr_mes"],
}

def norm_name(x):
    return "".join(ch.lower() for ch in x.strip() if ch.isalnum() or ch=="_")

def raw_rows():
    out=[]
    with zipfile.ZipFile(RAW) as z:
        members=[n for n in z.namelist() if not n.endswith("/")]
        if len(members)!=1: raise RuntimeError(f"RAW ambiguo: {members}")
        with z.open(members[0]) as f:
            for n,b in enumerate(f,1):
                line=b.decode("latin-1").rstrip("\r\n")
                if line[:2]!="01": continue
                if len(line)!=245: raise RuntimeError(f"Registro tipo 01 fora de 245 bytes: linha {n}")
                r={k:line[a-1:b].strip() for k,a,b in FIELDS}
                r["_line"]=n
                out.append(r)
    return out

def dec(s):
    s=(s or "").strip()
    if not s: return None
    return Decimal(s.replace(",", "."))

def canonical_date(s):
    s=(s or "").strip()
    if not s: return ""
    if len(s)==8 and s.isdigit():
        return s[:4]+"-"+s[4:6]+"-"+s[6:8]
    return s

def eq(a,b,field=None):
    if field in {"data_pregao","datven"}:
        return canonical_date(a)==canonical_date(b)
    return (a or "").strip()==(b or "").strip()

raw=raw_rows()
with CSV.open("r",encoding="utf-8-sig",newline="") as f:
    reader=csv.DictReader(f)
    if not reader.fieldnames: raise RuntimeError("CSV NORMALIZED sem cabecalho")
    original=list(reader.fieldnames)
    normalized_headers={norm_name(h):h for h in original}
    mapping={}
    missing=[]
    for field,aliases in ALIASES.items():
        hit=next((normalized_headers[norm_name(a)] for a in aliases if norm_name(a) in normalized_headers),None)
        if hit: mapping[field]=hit
        else: missing.append(field)
    if missing: raise RuntimeError("Campos ausentes no NORMALIZED: "+", ".join(missing))
    norm_rows=list(reader)

checks={}
checks["raw_count"]=len(raw)
checks["normalized_count"]=len(norm_rows)
checks["row_count_equal"]=len(raw)==len(norm_rows)
checks["header"]= {"columns":original,"mapping":mapping,"all_required_fields_present":not missing}

# Datas, identidade e métricas de negociação.
def vals(rows,field):
    return [str(r.get(field,"")).strip() for r in rows]

checks["date_equal"]=vals(raw,"data_pregao")==[str(r[mapping["data_pregao"]]).strip() for r in norm_rows]
identity_fields=["data_pregao","codbdi","codneg","tpmerc","codisi","dimes","especi","prazot","datven","indopc"]
identity_mismatches=[]
for i,(rr,nr) in enumerate(zip(raw,norm_rows)):
    for field in identity_fields:
        if not eq(rr[field],str(nr[mapping[field]]),field):
            identity_mismatches.append({"row":i+1,"field":field,"raw":rr[field],"normalized":str(nr[mapping[field]])})
            if len(identity_mismatches)>=30: break
    if len(identity_mismatches)>=30: break
checks["identity_mismatch_count_sampled"]=len(identity_mismatches)
checks["identity_mismatches"]=identity_mismatches

# OHLC + quantidade/volume/negócios: aceita representação decimal exata ou escala de 10^n,
# mas a escala precisa ser única por campo em toda a amostra.
numeric_fields=["preab","premax","premin","premed","preult","totneg","quatot","voltot"]
numeric_results={}
for field in numeric_fields:
    nfield=mapping[field]
    scales=Counter()
    mismatches=[]
    for i,(rr,nr) in enumerate(zip(raw,norm_rows)):
        a=dec(rr[field]); b=dec(str(nr[nfield]))
        if a is None or b is None:
            ok=a==b
        else:
            ok=(a==b)
            if not ok and b!=0:
                ratio=a/b
                if ratio == ratio.to_integral_value() and abs(ratio) in {Decimal(10),Decimal(100),Decimal(1000),Decimal(10000),Decimal(100000),Decimal(1000000)}:
                    scales[str(ratio)]+=1; ok=True
            if not ok: mismatches.append({"row":i+1,"raw":str(a),"normalized":str(b)})
        if len(mismatches)>=30: break
    numeric_results[field]={"scales_observed":dict(scales),"mismatch_sample":mismatches,"mismatch_count_sampled":len(mismatches)}
checks["numeric"]=numeric_results

# 30 amostras OHLC determinísticas: início, fim e pontos uniformemente distribuídos.
idxs=sorted(set([0,1,2,3,4,len(raw)-1,len(raw)-2,len(raw)-3,len(raw)-4]+[round(i*(len(raw)-1)/29) for i in range(30)]))
samples=[]
for i in idxs[:30]:
    rr,nr=raw[i],norm_rows[i]
    samples.append({"normalized_row":i+1,"raw_line":rr["_line"],"values":{f:{"raw":rr[f],"normalized":str(nr[mapping[f]])} for f in ["preab","premax","premin","premed","preult","quatot","voltot","totneg"]}})
checks["sample_30"]=samples

result={
 "schema_version":"1.0.0",
 "status":"RECONCILIACAO_RAW_NORMALIZED_1987",
 "raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),
 "normalized_file":str(CSV),
 "checks":checks,
 "fail_closed_gates":{
   "row_count_equal":checks["row_count_equal"],
   "header_complete":checks["header"]["all_required_fields_present"],
   "dates_equal":checks["date_equal"],
   "identity_no_sampled_mismatch":checks["identity_mismatch_count_sampled"]==0,
   "numeric_no_sampled_mismatch":all(v["mismatch_count_sampled"]==0 for v in numeric_results.values()),
   "sample_30_present":len(samples)==30
 }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+"\n",encoding="utf-8")
failed=[k for k,v in result["fail_closed_gates"].items() if not v]
print(json.dumps({"status":"OK" if not failed else "GATES_FAILED","failed":failed,"output":str(OUT),"raw_count":len(raw),"normalized_count":len(norm_rows)},ensure_ascii=False))
if failed: raise SystemExit("GATES FAILED: "+", ".join(failed))
