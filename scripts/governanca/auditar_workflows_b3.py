#!/usr/bin/env python3
"""Auditoria estática v2 dos workflows B3 contra o Layout Mestre Canônico.

Princípio: diagnóstico somente. O auditor nunca corrige, reexecuta ou promove
workflows. Ele classifica observabilidade, trigger, isolamento, dependências,
permissões, persistência, decisão e sinais de idempotência.
"""
from __future__ import annotations
import datetime as dt
import json
import pathlib
import re

ROOT = pathlib.Path(".")
WORKFLOW_DIR = ROOT / ".github" / "workflows"
MASTER = "docs/governanca/layout/LAYOUT_MESTRE_CANONICO_B3_V1.md"
OUT_JSON = ROOT / "docs/governanca" / "auditorias" / "WORKFLOWS_CONFORMIDADE_B3_ATUAL.json"
OUT_MD = ROOT / "docs" / "governanca" / "auditorias" / "WORKFLOWS_CONFORMIDADE_B3_ATUAL.md"

PHASE_RE = re.compile(r"FASE(?:([0-9]{2})|0?([0-9]))", re.I)

def phase_numbers(text: str) -> list[int]:
    vals = []
    for m in PHASE_RE.finditer(text):
        raw = m.group(1) or m.group(2)
        if raw:
            vals.append(int(raw))
    return sorted(set(vals))

def section(text: str, key: str) -> str:
    """Extrai um bloco YAML por chave, respeitando a indentação real do documento."""
    lines = text.splitlines(True)
    out = []
    active = False
    base_indent = None
    key_re = re.compile(rf"^(\s*){re.escape(key)}:\s*$")
    for line in lines:
        m = key_re.match(line)
        if not active and m:
            active = True
            base_indent = len(m.group(1))
            continue
        if active:
            stripped = line.strip()
            if not stripped:
                out.append(line)
                continue
            indent = len(line) - len(line.lstrip(" "))
            if indent <= base_indent and re.match(r"^[A-Za-z0-9_.-]+:\s*", stripped):
                break
            out.append(line)
    return "".join(out)

def push_paths(text: str) -> list[str]:
    """Retorna apenas valores de paths dentro do bloco push."""
    block = section(text, "push")
    paths = []
    in_paths = False
    for line in block.splitlines():
        if re.match(r"^\s*paths:\s*$", line):
            in_paths = True
            continue
        if in_paths:
            if re.match(r"^\s*[A-Za-z0-9_.-]+:\s*", line) and not re.match(r"^\s*-\s*", line):
                break
            m = re.match(r"^\s*-\s*(.*?)\s*$", line)
            if m:
                paths.append(m.group(1))
    return paths

def check(code: str, ok: bool, detail: str, severity: str = "INFO") -> dict:
    return {"code": code, "ok": bool(ok), "detail": detail, "severity": severity}

def has_git_write(text: str) -> bool:
    return bool(re.search(r"\bgit\s+(?:push|commit|add)\b", text, re.I))

def has_persist_step(text: str) -> bool:
    return bool(re.search(r"GITHUB_STEP_SUMMARY|upload-artifact|git\s+(?:add|commit|push)|write_text\(|to_csv\(|json\.dump|cat\s+>", text, re.I))

def has_decision_signal(text: str) -> bool:
    return bool(re.search(r"\b(?:status|decision|liberado|validado|bloqueado|conclu[ií]da|fail-closed|FAIL-CLOSED)\b", text, re.I))

def audit_workflow(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    name = path.name.lower()
    is_readme = "atualizar-readme" in name
    is_monitor = "b3-monitor" in name
    phases = phase_numbers(name)
    current_phase = max(phases) if phases else None

    checks = [
        check("MASTER_PRESENT", (ROOT / MASTER).is_file(), MASTER, "CRITICA"),
        check("TRIGGER_DECLARED",
              bool(re.search(r"(?m)^on:\s*$", text) or
                   re.search(r"(?m)^on:\s*[^#\n]+", text) or
                   re.search(r"(?m)^true:\s*$", text)),
              "declaração on presente", "ALTA"),
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
        if not forbidden else "; ".join(forbidden), "CRITICA"))

    push = section(text, "push")
    paths = push_paths(text)
    readme_path = any("README" in p.upper() for p in paths)
    generic_docs = any(
        re.fullmatch(r"docs/(?:\\*\\*|\\*)?", p.strip(), flags=re.I)
        for p in paths
    )
    if not is_readme:
        checks.append(check("NO_README_TRIGGER", not readme_path,
                             "sem README em gatilho" if not readme_path else "README aparece nos paths do push",
                             "ALTA"))
        checks.append(check("NO_GENERIC_DOCS_TRIGGER", not generic_docs,
                             "sem docs/ genérico em gatilho" if not generic_docs else "docs/ genérico aparece nos paths do push",
                             "MEDIA"))
    else:
        has_schedule = bool(re.search(r'cron:\s*["\']?55 2 \* \* \*["\']?', text))
        has_push = bool(re.search(r"(?m)^\s*push:", text))
        checks.append(check("README_2355_BRT", has_schedule, "cron 55 2 UTC", "CRITICA"))
        checks.append(check("README_NO_PUSH", not has_push, "README sem push trigger", "CRITICA"))

    has_summary = "GITHUB_STEP_SUMMARY" in text
    checks.append(check("STEP_SUMMARY", has_summary,
                        "GITHUB_STEP_SUMMARY encontrado" if has_summary else "GITHUB_STEP_SUMMARY ausente",
                        "BAIXA"))

    # Dependência direcional: um workflow de fase não deve reagir explicitamente
    # a evidência de fase posterior. Comentários também são ignorados.
    trigger_text = push
    posterior = []
    if current_phase is not None:
        for p in phase_numbers(trigger_text):
            if p > current_phase:
                posterior.append(p)
    checks.append(check(
        "NO_POSTERIOR_PHASE_TRIGGER", not posterior,
        "nenhum gatilho explícito de fase posterior"
        if not posterior else f"gatilho contém fases posteriores: {posterior}",
        "CRITICA"))

    # Sinal de entrada causal para workflows de fase. Não bloqueia workflows
    # manuais/auxiliares, mas registra ausência de evidência de entrada.
    if current_phase is not None and current_phase >= 3 and not is_readme:
        # Avalia somente paths do push, excluindo o próprio workflow.
        # Isso evita falso negativo causado por parsing de blocos YAML e
        # evita classificar o próprio arquivo do workflow como entrada causal.
        workflow_path = rel
        causal_paths = [
            p.strip().strip("'\"")
            for p in paths
            if p.strip().strip("'\"") != workflow_path
        ]
        has_input = any(
            re.search(r"^(?:dados/cotahist/(?:raw|quality|normalized|manifests)|scripts/|\.github/workflows/)", p, re.I)
            for p in causal_paths
        )
        checks.append(check("DIRECTIONAL_INPUT_SIGNAL", has_input,
                            "há sinal de entrada/evidência no trigger"
                            if has_input else "não foi identificado sinal de entrada causal no trigger",
                            "MEDIA"))

    # Permissões mínimas: escrita somente quando há sinais de publicação no repo.
    writes_repo = has_git_write(text)
    permissions_match = re.search(r"(?ms)^permissions:\s*\n((?:^[ \t]+.*\n?)*)", text)
    perm_block = permissions_match.group(1) if permissions_match else ""
    contents_write = bool(re.search(r"contents:\s*write", perm_block))
    contents_read = bool(re.search(r"contents:\s*read", perm_block))
    if writes_repo:
        checks.append(check("PERMISSIONS_MATCH_WRITE", contents_write,
                            "publicação no repositório exige contents: write"
                            if contents_write else "há escrita no repositório sem contents: write explícito",
                            "ALTA"))
    else:
        checks.append(check("PERMISSIONS_MINIMAL", contents_write is False,
                            "sem escrita Git detectada; contents: write não é necessário"
                            if not contents_write else "contents: write presente sem escrita Git evidente",
                            "MEDIA"))

    # Persistência e decisão: diagnóstico, não bloqueio automático.
    checks.append(check("EVIDENCE_PERSISTENCE_SIGNAL", has_persist_step(text),
                        "há sinal de persistência/evidência" if has_persist_step(text)
                        else "não foi identificado mecanismo claro de persistência",
                        "MEDIA"))
    checks.append(check("DECISION_SIGNAL", has_decision_signal(text),
                        "há sinal de status/decisão/fail-closed"
                        if has_decision_signal(text) else "não foi identificado sinal explícito de decisão",
                        "MEDIA"))

    # Idempotência: reconhece padrões fortes; UNKNOWN não reprova o workflow.
    idem = bool(re.search(
        r"git\s+diff\s+(?:--cached\s+)?--quiet|if \[ -f|if \[ -e|changed=false|cmp\s+|cancel-in-progress:\s*false|already (?:exists|synced|validated)|Nenhuma alteração|já está",
        text, re.I))
    checks.append(check("IDEMPOTENCE_SIGNAL", idem,
                        "padrão de idempotência/deduplicação detectado"
                        if idem else "sem padrão estático forte de idempotência; requer validação funcional",
                        "BAIXA"))

    if is_monitor:
        readonly = "actions: read" in text and "contents: read" in text and "contents: write" not in text
        checks.append(check("MONITOR_READONLY", readonly, "monitor com permissões de leitura", "CRITICA"))
        reexec = bool(re.search(r"gh\s+run\s+(?:rerun|watch)|\brerun\b", text, re.I))
        checks.append(check("MONITOR_NO_REEXECUTION", not reexec, "monitor não contém reexecução", "CRITICA"))

    blocking = [c for c in checks if not c["ok"] and c["severity"] in {"CRITICA", "ALTA"}]
    status = "CONFORME" if not blocking else "DIVERGENTE_CRITICA"
    observability_only = [c for c in checks if not c["ok"] and c["severity"] == "BAIXA"]
    if status == "CONFORME" and observability_only:
        status = "CONFORME_COM_OBSERVACAO"

    return {
        "workflow": rel,
        "current_phase": current_phase,
        "status": status,
        "checks": checks,
        "blocking_divergences": [c["code"] for c in blocking],
        "observability_or_advisory": [c["code"] for c in observability_only],
    }

def main() -> int:
    workflows = sorted(WORKFLOW_DIR.glob("*.yml")) + sorted(WORKFLOW_DIR.glob("*.yaml"))
    results = [audit_workflow(p) for p in workflows]
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    payload = {
        "schema_version": "2.0.0",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "normative_source": MASTER,
        "workflow_count": len(results),
        "status_counts": counts,
        "results": results,
        "classification_policy": {
            "blocking": ["CRITICA", "ALTA"],
            "advisory": ["MEDIA", "BAIXA"],
            "step_summary_only": "não deve ser interpretado isoladamente como defeito funcional",
            "historical": "workflow histórico não é reaberto por esta auditoria",
            "correction": "correção ocorre na origem; auditor nunca altera workflow",
        },
        "rule": "O auditor identifica divergências semânticas e estruturais; não corrige, reexecuta ou promove workflows.",
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Auditoria de Conformidade dos Workflows B3 — v2",
        "",
        "Fonte normativa: " + MASTER,
        "Gerado em UTC: " + payload["generated_at_utc"],
        f"Workflows auditados: {len(results)}",
        "",
        "## Regra de decisão",
        "",
        "A v2 separa divergência funcional de observabilidade. Não corrige, reexecuta ou promove workflows.",
        "Falhas CRITICA/ALTA são bloqueadoras; MEDIA/BAIXA são alertas para revisão.",
        "Ausência isolada de GITHUB_STEP_SUMMARY não é defeito funcional de dados.",
        "",
        "## Critérios ampliados",
        "",
        "- Layout Mestre presente.",
        "- Trigger declarado e causal.",
        "- Sem chamada/reexecução de outro workflow.",
        "- Sem README/docs genérico como trigger operacional.",
        "- Sem trigger explícito de fase posterior.",
        "- Dependência direcional identificável.",
        "- Permissões compatíveis com escrita real.",
        "- Persistência de evidência identificável.",
        "- Sinal explícito de status/decisão.",
        "- Sinal de idempotência/deduplicação quando aplicável.",
        "- README exclusivamente na janela 23:55 America/Sao_Paulo.",
        "- Monitor somente leitura e sem reexecução.",
        "",
        "## Matriz",
        "",
        "| Workflow | Fase | Status | Bloqueadores | Alertas |",
        "|---|---:|---|---|---|",
    ]
    for r in results:
        lines.append(
            "| " + r["workflow"] + " | " + (str(r["current_phase"]) if r["current_phase"] is not None else "—")
            + " | **" + r["status"] + "** | "
            + (", ".join(r["blocking_divergences"]) or "—") + " | "
            + (", ".join(r["observability_or_advisory"]) or "—") + " |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({
        "workflow_count": len(results),
        "status_counts": counts,
        "json": str(OUT_JSON),
        "markdown": str(OUT_MD),
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
