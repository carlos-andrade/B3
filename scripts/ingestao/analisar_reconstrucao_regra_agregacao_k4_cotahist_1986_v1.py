#!/usr/bin/env python3
import hashlib, json, zipfile
from collections import Counter, defaultdict
from pathlib import Path

RAW=Path("dados/cotahist/raw/anual/COTAHIST_A1986.ZIP")
OUT=Path("dados/cotahist/quality/COTAHIST_1986_FASE08I_RECONSTRUCAO_REGRA_AGREGACAO_V1.json")

def sub(l,a,b): return l[a-1:b]
def parse(path):
    rows=[]
    with zipfile.ZipFile(path) as z:
        member=next(n for n in z.namelist() if not n.endswith("/"))
        with z.open(member) as f:
            for ln,b in enumerate(f,1):
                s=b.decode("latin-1").rstrip("\r\n")
                if len(s)!=245 or s[:2]!="01": continue
                def iv(a,b):
                    x=sub(s,a,b).strip()
                    return int(x) if x else 0
                rows.append({
                    "line":ln,"date":sub(s,3,10),"codbdi":sub(s,11,12),
                    "codneg":sub(s,13,24).strip(),"tpmerc":sub(s,25,27),
                    "nomres":sub(s,28,39).strip(),"especi":sub(s,40,49).strip(),
                    "prazot":sub(s,50,52).strip(),"preab":iv(57,69),"premax":iv(70,82),
                    "premin":iv(83,95),"premed":iv(96,108),"preult":iv(109,121),
                    "totneg":iv(148,152),"quatot":iv(153,170),"voltot":iv(171,188),
                    "preexe":iv(189,201),"indopc":sub(s,202,202),"datven":sub(s,203,210),
                    "fatcot":iv(211,217),"ptoexe":iv(218,230),"codisi":sub(s,231,242).strip(),
                    "dimes":sub(s,243,245).strip()
                })
    return rows

def k4(r):
    return (r["date"],r["codbdi"],r["codneg"],r["tpmerc"],r["codisi"],r["dimes"],
            r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"])
def stat(r):
    return {x:r[x] for x in ("preab","premax","premin","premed","preult","totneg","quatot","voltot","fatcot")}
def ctx(r):
    return {"line":r["line"],"date":r["date"],"codbdi":r["codbdi"],"codneg":r["codneg"],
            "tpmerc":r["tpmerc"],"nomres":r["nomres"],"especi":r["especi"],"prazot":r["prazot"],
            "datven":r["datven"],"codisi":r["codisi"],"dimes":r["dimes"],"stats":stat(r)}

rows=parse(RAW)
target=[r for r in rows if r["line"] in (140808,140809)]
# Neighborhood: dates 19861006..19861017, restricted to VGO 2.
window=[r for r in rows if r["codneg"]=="VGO 2" and "19861006"<=r["date"]<="19861017"]
# Same-day term groups for every CODNEG, to identify normal separating dimensions.
g=defaultdict(list)
for r in rows:
    if r["codbdi"]=="62" and r["tpmerc"]=="030":
        g[(r["date"],r["codneg"])].append(r)
multi=[]
for key,rs in g.items():
    if len(rs)>1:
        diffs={}
        fields=("codbdi","tpmerc","codisi","dimes","especi","prazot","datven","preexe","indopc","ptoexe")
        for f in fields:
            vals=sorted(set(r[f] for r in rs))
            if len(vals)>1: diffs[f]=vals
        multi.append({"date":key[0],"codneg":key[1],"rows":len(rs),"differing_k4_fields":diffs,
                      "rows_detail":[ctx(r) for r in rs[:10]]})
# Groups at the same day/asset/term where all K4 fields match except statistics.
latent=defaultdict(list)
for r in rows:
    if r["codbdi"]=="62" and r["tpmerc"]=="030":
        latent[(r["date"],r["codneg"],r["codisi"],r["dimes"],r["especi"],r["prazot"],r["datven"],r["preexe"],r["indopc"],r["ptoexe"])].append(r)
latent_multi=[{"key":list(k),"rows":len(v),"rows_detail":[ctx(x) for x in v]} for k,v in latent.items() if len(v)>1]
# Same-day spot comparison.
spot=[r for r in rows if r["date"]=="19861010" and r["codneg"]=="VGO 2" and r["codbdi"]=="02" and r["tpmerc"]=="010"]
out={
 "schema_version":"1.0.0","status":"FASE_08I_RECONSTRUCAO_REGRA_AGREGACAO_1986_ANALISE",
 "raw_file":RAW.name,"raw_sha256":hashlib.sha256(RAW.read_bytes()).hexdigest(),"records_type01":len(rows),
 "research_question":"qual dimensão operacional pode explicar duas linhas no mesmo pregão com K4 idêntica e estatísticas distintas?",
 "target":{"k4":list(k4(target[0])),"rows":[ctx(r) for r in target]},
 "window_19861006_19861017_vgo2":[ctx(r) for r in window],
 "same_day_term_multi_codneg_count":len(multi),
 "same_day_term_multi_codneg_examples_first_100":multi[:100],
 "same_day_term_same_k4_statistical_collision_count":len(latent_multi),
 "same_day_term_same_k4_statistical_collisions":[x for x in latent_multi[:100]],
 "same_day_spot_vgo2_19861010":[ctx(r) for r in spot],
 "assessment":{
   "facts":[
     "A K4 inclui prazo, data de vencimento, especificação, CODISI, DIMES e campos de exercício/indicador.",
     "A colisão-alvo mantém todos esses campos iguais e altera somente campos estatísticos.",
     "No universo 1986, a busca por múltiplos registros a termo do mesmo ativo no mesmo pregão mostra que, quando existem múltiplas linhas, a separação normalmente ocorre por algum campo estrutural da K4.",
     "A colisão-alvo é um caso em que essa dimensão estrutural não está presente na K4."
   ],
   "hypothesis":"A causa mais tecnicamente plausível passa a ser uma dimensão operacional/negocial que não foi preservada nos campos K4 do COTAHIST, ou uma regra de agregação/publicação que produziu dois agregados sob a mesma identidade estrutural.",
   "not_proven":[
     "que a dimensão ausente seja taxa de termo",
     "que seja corretagem, modalidade, registro ou lote",
     "que a duplicidade seja erro de processamento",
     "que as duas linhas representem dois contratos economicamente distintos"
   ],
   "important_negative":"Não foi encontrada, no layout COTAHIST vigente, uma coluna explícita de taxa de termo dentro da K4."
 },
 "governance":{"raw_changed":False,"rows_deleted":False,"rows_consolidated":False,"economic_identity_inferred":False,"causal_explanation_inferred":False}
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","records":len(rows),"target_rows":len(target),"same_day_term_multi_codneg_count":len(multi),"same_day_term_same_k4_statistical_collision_count":len(latent_multi),"raw_sha256":out["raw_sha256"]},ensure_ascii=False))
