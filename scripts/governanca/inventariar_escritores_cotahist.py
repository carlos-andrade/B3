#!/usr/bin/env python3
"""Inventário estático COTAHIST; não executa nem altera workflows."""
import argparse, json, re
from collections import defaultdict
from pathlib import Path
WORKFLOW_DIR=Path(".github/workflows")
CANONICAL_OWNERS={
" dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv".strip():".github/workflows/cotahist-main-publisher.yml",
"dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json":".github/workflows/cotahist-main-publisher.yml",
"dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json":".github/workflows/cotahist-main-publisher.yml"}
def uncomment(t): return "\n".join(x for x in t.splitlines() if not x.lstrip().startswith("#"))
def extract_paths(t):
 p,d,ls=[],[],t.splitlines(); i=0
 while i<len(ls):
  line=ls[i]
  if re.search(r"\bgit\s+add\b",line,re.I):
   cmd=line.split("git add",1)[-1].strip()
   while line.rstrip().endswith("\\") and i+1<len(ls):
    i+=1; line=ls[i]; cmd+=" "+line.strip().rstrip("\\")
   for m in re.findall(r'''(?:"([^"]+)"|'([^']+)'|(\S+))''',re.sub(r"\s+#.*$","",cmd)):
    v=next(z for z in m if z).rstrip(",;")
    if v in {".","-A","--all"}: d.append("<entire-repository>")
    elif v.startswith("$") or "$" in v: d.append(v)
    elif v.startswith(("dados/cotahist/","docs/","registry/",".gitattributes",".github/","README")) and v not in p: p.append(v)
  i+=1
 return sorted(p),sorted(set(d))
def classify(path,raw):
 t=uncomment(raw)
 if "cotahist" not in path.lower() and not re.search(r"dados/cotahist",t,re.I): return None
 pushes=re.findall(r"(?i)\bgit\s+push\b([^\n]*)",t)
 api=bool(re.search(r"createOrUpdateFileContents|repos\.createOrUpdateFileContents|git\.push\(|push_files|contents\.create|update_file\(",t,re.I))
 commit=bool(re.search(r"\bgit\s+commit\b",t,re.I))
 perm=bool(re.search(r"(?m)^\s*contents:\s*write\s*$",t)) or bool(re.search(r"permissions:\s*\{[^}]*contents:\s*write",t,re.I))
 paths,dyn=extract_paths(t); writer=bool(pushes or api)
 conditional=bool(re.search(r"(?m)^\s*if:\s*\$\{\{",t)) or bool(re.search(r"\bif\s+\[|\bif\s+\[\[|\bif\s+\$\{",t))
 validator_signal=bool(re.search(r"\b(?:valid|auditor|audit|reconcil|verificar|verify|check|gate|assert|pytest|unittest|sha256sum)\w*\b", path + " " + t, re.I))
 cls="WRITER_CONDITIONAL" if writer and conditional else "WRITER_EFFECTIVE" if writer else "VALIDATOR" if commit or perm or validator_signal else "FALSE_POSITIVE" if not paths else "VALIDATOR"
 flat=" ".join(pushes); branch="NONE"
 if re.search(r"(?:HEAD\s*:\s*main|origin\s+main\b|refs/heads/main)",flat,re.I): branch="main"
 elif re.search(r"github\.ref_name",flat,re.I): branch="github.ref_name"
 elif re.search(r"github\.ref\b",flat,re.I): branch="github.ref"
 elif pushes: branch="UPSTREAM_OR_IMPLICIT"
 elif api: branch="API_TARGET_UNRESOLVED"
 group=re.search(r"(?m)^\s*group:\s*(.+?)\s*$",t)
 secrets=sorted(set(re.findall(r"\b(?:secrets|vars)\.([A-Z][A-Z0-9_]*)\b",t)))
 creds=sorted(set(re.findall(r"(?i)\b([A-Z][A-Z0-9_]*(?:TOKEN|PAT|APP_ID|PRIVATE_KEY|PASSWORD|SECRET|CREDENTIAL)[A-Z0-9_]*)\b",t)))
 refs=sorted(set(re.findall(r"(?<![A-Za-z0-9_])dados/cotahist/[A-Za-z0-9_./*{}-]+",t,re.I)))
 return {"workflow":path,"classification":cls,"write_mechanism":{"git_push":bool(pushes),"api_write":api,"local_commit":commit},"branch_target":branch,"write_paths_static":paths,"write_paths_dynamic_or_broad":dyn,"referenced_cotahist_paths":refs,"concurrency_group":group.group(1).strip() if group else "MISSING","contents_write_permission":perm,"secret_reference_names":secrets,"credential_or_token_identifiers":creds,"static_evidence_only":True,"runtime_write_confirmed":False}
def run(root):
 files=sorted((root/WORKFLOW_DIR).glob("*.yml"))+sorted((root/WORKFLOW_DIR).glob("*.yaml")); records=[]
 for f in files:
  x=classify(f.relative_to(root).as_posix(),f.read_text(encoding="utf-8",errors="replace"))
  if x: records.append(x)
 owners=defaultdict(list); branches=defaultdict(int); classes=defaultdict(int); missing=[]; unresolved=[]
 for x in records:
  classes[x["classification"]]+=1
  if x["classification"] in {"WRITER_EFFECTIVE","WRITER_CONDITIONAL"}:
   branches[x["branch_target"]]+=1
   if x["concurrency_group"]=="MISSING": missing.append(x["workflow"])
   if x["write_paths_dynamic_or_broad"] or not x["write_paths_static"]: unresolved.append(x["workflow"])
   for p in x["write_paths_static"]: owners[p].append(x["workflow"])
 shared=[{"path":p,"writer_workflows":sorted(set(ws)),"writer_count":len(set(ws)),"canonical_owner":CANONICAL_OWNERS.get(p,"UNASSIGNED_REQUIRES_REVIEW"),"owner_policy":"CENTRAL_PUBLISHER" if p in CANONICAL_OWNERS else "PROPOSED_NOT_APPROVED"} for p,ws in sorted(owners.items()) if len(set(ws))>1]
 return {"schema_version":"1.0.0","purpose":"Reconciliar workflows COTAHIST sem executar nem modificar produção.","classification_policy":{"WRITER_EFFECTIVE":"push/API detetado sem guarda condicional estática","WRITER_CONDITIONAL":"push/API detetado com guarda condicional","VALIDATOR":"mutação local/permissão sem push/API estático","FALSE_POSITIVE":"referência COTAHIST sem mecanismo de escrita detetado","caveat":"Análise estática; actions externas e chamadas dinâmicas exigem revisão manual."},"workflow_count":len(records),"classification_counts":dict(sorted(classes.items())),"writer_branch_target_counts":dict(sorted(branches.items())),"writer_without_concurrency_count":len(missing),"writer_without_concurrency":missing,"writer_with_unresolved_or_broad_paths_count":len(unresolved),"writer_with_unresolved_or_broad_paths":unresolved,"shared_resource_count":len(shared),"shared_resources":shared,"canonical_owner_policy":CANONICAL_OWNERS,"workflows":records}
def main():
 a=argparse.ArgumentParser(); a.add_argument("--repo-root",type=Path,default=Path(".")); a.add_argument("--output-dir",type=Path,default=Path("build/cotahist-writer-audit")); x=a.parse_args(); root=x.repo_root.resolve(); data=run(root); x.output_dir.mkdir(parents=True,exist_ok=True)
 (x.output_dir/"cotahist-writer-inventory.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 rows=["# Inventário de Escritores COTAHIST — análise estática","","Diagnóstico não normativo; não executa workflows nem confirma escrita em runtime.","",f"- Workflows referenciados: {data['workflow_count']}",f"- Classes: {json.dumps(data['classification_counts'],ensure_ascii=False)}",f"- Escritores sem concurrency: {data['writer_without_concurrency_count']}",f"- Escritores com destino amplo/não resolvido: {data['writer_with_unresolved_or_broad_paths_count']}",f"- Recursos partilhados: {data['shared_resource_count']}","","## Recursos partilhados","","| Recurso | Escritores | Proprietário proposto | Estado |","|---|---:|---|---|"]
 for z in data["shared_resources"]: rows.append(f"| {z['path']} | {z['writer_count']} | {z['canonical_owner']} | {z['owner_policy']} |")
 rows+=["","## Escritores e controlos","","| Workflow | Classe | Branch | Concorrência | Credenciais (nomes) | Paths |","|---|---|---|---|---|---|"]
 for z in data["workflows"]:
  if z["classification"] in {"WRITER_EFFECTIVE","WRITER_CONDITIONAL"}: rows.append("| "+" | ".join([z["workflow"],z["classification"],z["branch_target"],z["concurrency_group"],", ".join(z["secret_reference_names"]+z["credential_or_token_identifiers"]) or "não detetadas",", ".join(z["write_paths_static"]+z["write_paths_dynamic_or_broad"]) or "não resolvidos"])+" |")
 (x.output_dir/"cotahist-writer-inventory.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
 print(json.dumps({"workflow_count":data["workflow_count"],"classification_counts":data["classification_counts"],"shared_resource_count":data["shared_resource_count"],"output_dir":str(x.output_dir)},ensure_ascii=False)); return 0
if __name__=="__main__": raise SystemExit(main())
