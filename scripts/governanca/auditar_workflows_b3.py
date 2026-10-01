#!/usr/bin/env python3
"""Auditoria estática dos workflows B3 contra o Layout Mestre Canônico."""
from __future__ import annotations
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(".")
WORKFLOW_DIR = ROOT / ".github" / "workflows"
MASTER = "docs/governanca/LAYOUT_MESTRE_CANONICO_B3_V1.md"
OUT_JSON = ROOT / "docs" / "governanca" / "auditorias" / "WORKFLOWS_CONFORMIDADE_B3_ATUAL.json"
OUT_MD = ROOT / "docs" / "governanca" / "auditorias" / "WORKFLOWS_CONFORMIDADE_B3_ATUAL.md"

def section(text: str, key: str) -> str:
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*\n((?:^\s+.*\n?)*)", text)
    return m.group(1) if m else ""

def check(code: str, ok: bool, detail: str) -> dict:
    return {"code": code, "ok": bool(ok), "detail": detail}

def audit_workflow(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    name = path.name
    is_readme = "atualizar-readme" in name
    is_monitor = "b3-monitor" in name
    checks = [
        check("MASTER_PRESENT", (ROOT / MASTER).is_file(), MASTER),
        check("TRIGGER_DECLARED",
              bool(re.search(r"(?m)^on:\s*$", text)
                   or re.search(r"(?m)^on:\s*[^#\n]+", text)
                   or re.search(r"(?m)^true:\s*$", text)),
              "declaração on presente"),
    ]
    forbidden = []
    for pattern in (
        r"(?m)^\s*workflow_run:",
        r"(?m)^\s*workflow_call:",
        r"(?m)^\s*repository_dispatch:",
        r"gh\s+(?:workflow\s+run|api\s+.*?/actions/workflows)",
        r"/actions/workflows/",
    ):
        if re.search(pattern, text, re.I):
            forbidden.append(pattern)
    checks.append(check(
        "NO_CROSS_WORKFLOW_EXECUTION", not forbidden,
        "nenhuma chamada/reexecução de outro workflow detectada"
        if not forbidden else "; ".join(forbidden)))
    push = section(text, "push")
    readme_path = bool(re.search(r'(?mi)^\s*-?\s*["\']?[^"\']*README[^"\']*["\']?\s*$', push))
    generic_docs = bool(
        re.search(r'(?mi)^\s*-?\s*["\']?docs/(?:\*\*|\*)?["\']?\s*$', push)
        or re.search(r"(?mi)^\s*paths:.*docs/", push)
    )
    if not is_readme:
        checks.append(check("NO_README_TRIGGER", not readme_path,
                             "sem README em gatilho" if not readme_path else "README aparece nos paths do push"))
        checks.append(check("NO_GENERIC_DOCS_TRIGGER", not generic_docs,
                             "sem docs/ genérico em gatilho" if not generic_docs else "docs/ genérico aparece nos paths do push"))
    else:
        has_schedule = bool(re.search(r'cron:\s*["\']?55 2 \* \* \*["\']?', text))
        has_push = bool(re.search(r"(?m)^\s*push:", text))
        checks.append(check("README_2355_BRT", has_schedule, "cron 55 2 UTC"))
        checks.append(check("README_NO_PUSH", not has_push, "README sem push trigger"))
    has_summary = "GITHUB_STEP_SUMMARY" in text
    checks.append(check("STEP_SUMMARY", has_summary,
                        "GITHUB_STEP_SUMMARY encontrado" if has_summary else "GITHUB_STEP_SUMMARY ausente"))
    if is_monitor:
        readonly = "actions: read" in text and "contents: read" in text and "contents: write" not in text
        checks.append(check("MONITOR_READONLY", readonly, "monitor com permissões de leitura"))
        reexec = bool(re.search(r"gh\s+run\s+(?:rerun|watch)|rerun", text, re.I))
        checks.append(check("MONITOR_NO_REEXECUTION", not reexec, "monitor não contém reexecução"))
    return {
        "workflow": str(path.relative_to(ROOT)).replace("\\", "/"),
        "status": "CONFORME" if all(c["ok"] for c in checks) else "DIVERGENTE",
        "checks": checks,
    }

def main() -> int:
    workflows = sorted(WORKFLOW_DIR.glob("*.yml")) + sorted(WORKFLOW_DIR.glob("*.yaml"))
    results = [audit_workflow(p) for p in workflows]
    conformes = sum(r["status"] == "CONFORME" for r in results)
    divergentes = len(results) - conformes
    payload = {
        "schema_version": "1.0.0",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "normative_source": MASTER,
        "workflow_count": len(results),
        "conforme": conformes,
        "divergente": divergentes,
        "results": results,
        "rule": "O auditor identifica divergências; não altera workflows automaticamente.",
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Auditoria de Conformidade dos Workflows B3",
        "",
        "Fonte normativa: " + MASTER,
        "Gerado em UTC: " + payload["generated_at_utc"],
        "Workflows auditados: " + str(len(results)),
        "Conformes: " + str(conformes),
        "Divergentes: " + str(divergentes),
        "",
        "## Regra de decisão",
        "",
        "Este auditor é diagnóstico. Ele não corrige, reexecuta ou promove workflows.",
        "Correções devem ocorrer no workflow em que a divergência existe.",
        "",
        "## Critérios",
        "",
        "- Layout Mestre presente.",
        "- Gatilho declarado.",
        "- Sem chamada/reexecução de outro workflow.",
        "- Sem README como gatilho operacional.",
        "- Sem docs/ genérico como gatilho operacional.",
        "- GITHUB_STEP_SUMMARY presente.",
        "- README somente no cron 23:55 America/Sao_Paulo (02:55 UTC).",
        "- Monitor em modo somente leitura e sem reexecução.",
        "",
        "## Matriz",
        "",
        "| Workflow | Status | Divergências |",
        "|---|---|---|",
    ]
    for r in results:
        bad = [c["code"] for c in r["checks"] if not c["ok"]]
        lines.append("| " + r["workflow"] + " | **" + r["status"] + "** | " + (", ".join(bad) if bad else "—") + " |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({
        "workflow_count": len(results),
        "conforme": conformes,
        "divergente": divergentes,
        "json": str(OUT_JSON),
        "markdown": str(OUT_MD),
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
