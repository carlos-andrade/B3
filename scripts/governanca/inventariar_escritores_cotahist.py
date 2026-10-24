#!/usr/bin/env python3
"""Inventário estático COTAHIST; não executa nem altera workflows."""
import argparse, json, re
from collections import defaultdict
from pathlib import Path
WORKFLOW_DIR=Path(".github/workflows")
CANONICAL_OWNERS={
" dados/cotahist/certificacao/COTAHIST_CERTIFICACAO_ANUAL_1986_2026_V1.0.csv".strip():".github/workflows/cotahist-main-publisher.yml",
"dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V1.0.json":".github/workflows/cotahist-main-publisher.yml",
"dados/cotahist/oficial/COTAHIST_DATASET_OFICIAL_V2.0.json":".github/workflows/cotahist-main-publisher.yml",
"dados/cotahist/normalized/anual/COTAHIST_A1987.csv":".github/workflows/cotahist-normalized-m1-1987.yml"}
APPROVED_SHARED_EXCEPTIONS={
"dados/cotahist/normalized/anual/COTAHIST_A1987.csv": {
 "exception_writer": ".github/workflows/cotahist-lfs-migracao-controlada-a1987-v1.yml",
 "concurrency_group": "cotahist-normalized-a1987-writer",
 "reason": "migração LFS administrativa exclusivamente manual; M1 permanece proprietário normal do CSV"
}}
def uncomment(t): return "\n".join(x for x in t.splitlines() if not x.lstrip().startswith("#"))
def extract_paths(t):
 p,d,ls=[],[],t.splitlines()
 assignments={}
 for m in re.finditer(r"""(?m)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(['"])([^'"\n]+)\2\s*$""",t):
  assignments[m.group(1)]=m.group(3)
 loop_values={}
 prefix=r"(?:dados/cotahist|docs|registry|\.gitattributes|\.github|README)"
 for m in re.finditer(r"(?ms)^\s*for\s+([A-Za-z_][A-Za-z0-9_]*)\s+in\s+\\\s*\n(.*?)^\s*do\b",t):
  vals=re.findall(r"(?m)^\s*("+prefix+r"[A-Za-z0-9_./*{}-]*)\s*\\?\s*$",m.group(2))
  if vals: loop_values[m.group(1)]=vals
 for m in re.finditer(r"""(?ms)case\s+['"]?\$([A-Za-z_][A-Za-z0-9_]*)['"]?\s+in(.*?)esac""",t):
  var,block=m.group(1),m.group(2)
  allowed=[]
  for line in block.splitlines():
   if ")" not in line: continue
   lhs=line.split(")",1)[0].strip()
   if lhs in {"*",""}: continue
   for token in lhs.split("|"):
    token=token.strip().strip("'\"")
    if token.startswith("$"):
     key=token[1:].strip("{}")
     if key in assignments: allowed.append(assignments[key])
     elif key in loop_values: allowed.extend(loop_values[key])
    elif re.match(r"^"+prefix+r"[A-Za-z0-9_./*{}-]*$",token):
     allowed.append(token)
  if allowed: loop_values[var]=sorted(set(allowed))
 def resolve(value):
  value=value.strip().strip("'\"").rstrip(",;")
  if value.startswith("$"):
   key=value[1:].strip("{}")
   if key in assignments: return [assignments[key]]
   if key in loop_values: return loop_values[key]
   return []
  if value.startswith(("dados/cotahist/","docs/","registry/"," .gitattributes".strip(),".gitattributes",".github/","README")): return [value]
  return []
 i=0
 while i<len(ls):
  line=ls[i]
  if re.search(r"\bgit\s+add\b",line,re.I):
   cmd=line.split("git add",1)[-1].strip()
   while line.rstrip().endswith("\\") and i+1<len(ls):
    i+=1; line=ls[i]; cmd+=" "+line.strip().rstrip("\\")
   for match in re.findall(r'''(?:"([^"]+)"|'([^']+)'|(\S+))''',re.sub(r"\s+#.*$","",cmd)):
    v=next(z for z in match if z).rstrip(",;")
    if v in {".","-A","--all"}: d.append("<entire-repository>")
    elif v.startswith("$"):
     resolved=resolve(v)
     if resolved: p.extend(resolved)
     else: d.append("DYNAMIC:"+v)
    elif "$" in v: d.append("DYNAMIC:"+v)
    elif v.startswith(("dados/cotahist/","docs/","registry/",".gitattributes",".github/","README")): p.append(v)
  i+=1
 return sorted(set(p)),sorted(set(d))

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
 inline_group=re.search(r"(?m)^\s*concurrency:\s*\{\s*group:\s*([^,}]+)",t)
 group_value=group.group(1).strip() if group else (inline_group.group(1).strip().strip("\'").strip('"') if inline_group else "MISSING")
 secrets=sorted(set(re.findall(r"\b(?:secrets|vars)\.([A-Z][A-Z0-9_]*)\b",t)))
 creds=sorted(set(re.findall(r"(?i)\b([A-Z][A-Z0-9_]*(?:TOKEN|PAT|APP_ID|PRIVATE_KEY|PASSWORD|SECRET|CREDENTIAL)[A-Z0-9_]*)\b",t)))
 refs=sorted(set(re.findall(r"(?<![A-Za-z0-9_])dados/cotahist/[A-Za-z0-9_./*{}-]+",t,re.I)))
 return {"workflow":path,"classification":cls,"write_mechanism":{"git_push":bool(pushes),"api_write":api,"local_commit":commit},"branch_target":branch,"write_paths_static":paths,"write_paths_dynamic_or_broad":dyn,"referenced_cotahist_paths":refs,"concurrency_group":group_value,"contents_write_permission":perm,"secret_reference_names":secrets,"credential_or_token_identifiers":creds,"static_evidence_only":True,"runtime_write_confirmed":False}
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
 shared=[{"path":p,"writer_workflows":sorted(set(ws)),"writer_count":len(set(ws)),"canonical_owner":CANONICAL_OWNERS.get(p,"UNASSIGNED_REQUIRES_REVIEW"),"owner_policy":"CONTROLLED_ADMIN_EXCEPTION" if p in APPROVED_SHARED_EXCEPTIONS else "CANONICAL_OWNER" if p in CANONICAL_OWNERS else "UNASSIGNED_REQUIRES_REVIEW","approved_exception":APPROVED_SHARED_EXCEPTIONS.get(p)} for p,ws in sorted(owners.items()) if len(set(ws))>1]\n uncontrolled_shared=[x for x in shared if x["owner_policy"]!="CONTROLLED_ADMIN_EXCEPTION"]
 unresolved_vars=[x["workflow"] for x in records if any(p.startswith("DYNAMIC:") for p in x["write_paths_dynamic_or_broad"])]
 return {"schema_version":"1.0.0","purpose":"Reconciliar workflows COTAHIST sem executar nem modificar produção.","classification_policy":{"WRITER_EFFECTIVE":"push/API detetado sem guarda condicional estática","WRITER_CONDITIONAL":"push/API detetado com guarda condicional","VALIDATOR":"mutação local/permissão sem push/API estático","FALSE_POSITIVE":"referência COTAHIST sem mecanismo de escrita detetado","caveat":"Análise estática; actions externas e chamadas dinâmicas exigem revisão manual."},"workflow_count":len(records),"classification_counts":dict(sorted(classes.items())),"writer_branch_target_counts":dict(sorted(branches.items())),"writer_without_concurrency_count":len(missing),"writer_without_concurrency":missing,"writer_with_unresolved_or_broad_paths_count":len(unresolved),"writer_with_unresolved_or_broad_paths":unresolved,"writer_unresolved_variable_count":len(unresolved_vars),"writer_unresolved_variables":unresolved_vars,"shared_resource_count":len(shared),"shared_resources":shared,"uncontrolled_shared_resource_count":len(uncontrolled_shared),"uncontrolled_shared_resources":uncontrolled_shared,"approved_shared_exceptions":APPROVED_SHARED_EXCEPTIONS,"canonical_owner_policy":CANONICAL_OWNERS,"workflows":records}
def main():
 a=argparse.ArgumentParser(); a.add_argument("--repo-root",type=Path,default=Path(".")); a.add_argument("--output-dir",type=Path,default=Path("build/cotahist-writer-audit")); x=a.parse_args(); root=x.repo_root.resolve(); data=run(root); x.output_dir.mkdir(parents=True,exist_ok=True)
 (x.output_dir/"cotahist-writer-inventory.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 rows=["# Inventário de Escritores COTAHIST — análise estática","","Diagnóstico não normativo; não executa workflows nem confirma escrita em runtime.","",f"- Workflows referenciados: {data['workflow_count']}",f"- Classes: {json.dumps(data['classification_counts'],ensure_ascii=False)}",f"- Escritores sem concurrency: {data['writer_without_concurrency_count']}",f"- Escritores com destino amplo/não resolvido: {data['writer_with_unresolved_or_broad_paths_count']}",f"- Recursos partilhados: {data['shared_resource_count']}","","## Recursos partilhados","","| Recurso | Escritores | Proprietário proposto | Estado |","|---|---:|---|---|"]
 for z in data["shared_resources"]: rows.append(f"| {z['path']} | {z['writer_count']} | {z['canonical_owner']} | {z['owner_policy']} |")
 rows+=["","## Escritores e controlos","","| Workflow | Classe | Branch | Concorrência | Credenciais (nomes) | Paths |","|---|---|---|---|---|---|"]
 for z in data["workflows"]:
  if z["classification"] in {"WRITER_EFFECTIVE","WRITER_CONDITIONAL"}: rows.append("| "+" | ".join([z["workflow"],z["classification"],z["branch_target"],z["concurrency_group"],", ".join(z["secret_reference_names"]+z["credential_or_token_identifiers"]) or "não detetadas",", ".join(z["write_paths_static"]+z["write_paths_dynamic_or_broad"]) or "não resolvidos"])+" |")
 (x.output_dir/"cotahist-writer-inventory.md").write_text("\n".join(rows)+"\n",encoding="utf-8")
 print(json.dumps({"workflow_count":data["workflow_count"],"classification_counts":data["classification_counts"],"shared_resource_count":data["shared_resource_count"],"uncontrolled_shared_resource_count":data["uncontrolled_shared_resource_count"],"writer_unresolved_variable_count":data["writer_unresolved_variable_count"],"writer_with_unresolved_or_broad_paths_count":data["writer_with_unresolved_or_broad_paths_count"],"output_dir":str(x.output_dir)},ensure_ascii=False)); return 0
if __name__=="__main__": raise SystemExit(main())
