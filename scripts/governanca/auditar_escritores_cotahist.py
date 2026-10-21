#!/usr/bin/env python3
"""Static inventory of COTAHIST-related GitHub Actions workflows."""
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DIR=ROOT/".github/workflows"
REMOTE_WRITE=re.compile(r"\bgit\s+push\b|create-pull-request|git-auto-commit-action|gh api[^\n]*(?:git/refs|contents/)|repository\.createCommit|createCommit\s*\(",re.I)
LOCAL_COMMIT=re.compile(r"\bgit\s+commit\b",re.I)
PERM=re.compile(r"contents:\s*write|permissions:\s*write-all|pull-requests:\s*write",re.I)
DRY=re.compile(r"dry.?run|--dry-run|\bdryrun\b",re.I)
RES=re.compile(r"(?:dados/cotahist|docs/cotahist|reports/cotahist)[^\s\"']*",re.I)
def classify(p):
 t=p.read_text(encoding="utf-8",errors="replace")
 wp=bool(PERM.search(t)); ew=bool(REMOTE_WRITE.search(t)); lc=bool(LOCAL_COMMIT.search(t))
 candidate=wp and (lc or bool(re.search(r"\b(?:python|python3|bash|sh)\s+[^\n]*(?:cotahist|ingest|normaliz|public|reconcil|certific|manifest)",t,re.I)))
 kind="WRITER_CONFIRMED_STATIC" if ew else "WRITER_CANDIDATE_SCRIPT_REVIEW" if candidate else "WRITE_PERMISSION_REVIEW_REQUIRED" if wp else "DRY_RUN_READ_ONLY" if DRY.search(t) else "READ_ONLY" if re.search(r"contents:\s*read",t,re.I) else "NO_STATIC_WRITE_SIGNAL_REVIEW_REQUIRED"
 g=re.search(r"^\s*group:\s*(.+?)\s*$",t,re.M); ci=re.search(r"^\s*cancel-in-progress:\s*(.+?)\s*$",t,re.M)
 branches=[]
 for m in re.finditer(r"^\s*branches:\s*\[([^\]]+)\]",t,re.M): branches += [x.strip().strip("\"'") for x in m.group(1).split(",")]
 target="main" if re.search(r"HEAD:main|git push origin main|git push origin HEAD:main|origin/main",t) else "push-target-review-required" if re.search(r"git push",t) else "not-statically-determined"
 return {"file":p.relative_to(ROOT).as_posix(),"workflow_name":(re.search(r"^name:\s*(.+)$",t,re.M).group(1).strip() if re.search(r"^name:\s*(.+)$",t,re.M) else p.name),"classification":kind,"write_permission":wp,"remote_write_signal":ew,"local_commit_signal":lc,"invoked_writer_candidate":candidate,"concurrency_group":g.group(1) if g else None,"cancel_in_progress":ci.group(1) if ci else "default","trigger_branches":branches,"target_branch":target,"resource_paths":sorted({x.rstrip(";,") for x in RES.findall(t)})}
def main():
 records=[]
 for p in sorted(DIR.iterdir()):
  if p.is_file() and p.suffix.lower() in {".yml",".yaml"}:
   t=p.read_text(encoding="utf-8",errors="replace")
   if "cotahist" in p.name.lower() or "cotahist" in t.lower(): records.append(classify(p))
 counts={}
 for r in records: counts[r["classification"]]=counts.get(r["classification"],0)+1
 writers=[r for r in records if r["classification"] in {"WRITER_CONFIRMED_STATIC","WRITER_CANDIDATE_SCRIPT_REVIEW","WRITE_PERMISSION_REVIEW_REQUIRED"}]
 resource_owners={}
 for row in writers:
  for resource in row["resource_paths"]:
   resource_owners.setdefault(resource,[]).append(row["file"])
 shared_resources={k:sorted(set(v)) for k,v in resource_owners.items() if len(set(v))>1}
 report={"schema_version":"1.0.0","workflow_count":len(records),"classification_counts":counts,"writers":writers,"shared_resources":shared_resources,"workflows":records,"limitations":["Static scan only; inspect scripts invoked by candidate workflows.","Branch/resource inference is heuristic.","GitHub concurrency retains at most one pending run per group; newer pending runs can replace older pending runs."]}
 Path("cotahist-writer-inventory.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 lines=["# Inventário de escritores COTAHIST","",f"- Workflows analisados: {len(records)}",f"- Escritores confirmados por sinais estáticos: {counts.get('WRITER_CONFIRMED_STATIC',0)}",f"- Candidatos a revisão de script: {counts.get('WRITER_CANDIDATE_SCRIPT_REVIEW',0)}",f"- Permissões de escrita sem sinal conclusivo: {counts.get('WRITE_PERMISSION_REVIEW_REQUIRED',0)}","","| Workflow | Classe | Branch | Grupo | Cancel | Recursos |","|---|---|---|---|---|---|"]
 for r in writers: lines.append("| "+ " | ".join([r["file"],r["classification"],r["target_branch"],r["concurrency_group"] or "NONE",r["cancel_in_progress"],", ".join(r["resource_paths"][:3]) or "a rever"])+" |")
 lines += ["","## Recursos partilhados (mesmo caminho literal)","","| Recurso | Número de workflows | Workflows |","|---|---:|---|"]
 for resource, owners in sorted(shared_resources.items()):
  lines.append("| "+resource+" | "+str(len(owners))+" | "+", ".join(owners[:8])+(" …" if len(owners)>8 else "")+" |")
 lines += ["","Limitações: análise estática; rever scripts chamados, branch e recursos antes de considerar inventário certificado.",""]
 Path("cotahist-writer-inventory.md").write_text("\n".join(lines),encoding="utf-8")
 print(json.dumps({"workflow_count":len(records),"classification_counts":counts,"writer_count":len(writers)},ensure_ascii=False))
if __name__=="__main__": main()
