#!/usr/bin/env python3
"""
Projeto: B3 — A BOLSA DO BRASIL
Arquivo: watchdog_b3.py
Caminho: WATCHDOG/scripts/watchdog_b3.py
Data de criação: 2026-10-09
Versão: 1.0.0
Finalidade: auditoria estática, somente leitura, do código e da infraestrutura GitHub Actions.
"""

from __future__ import annotations

import ast
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path(__file__).resolve().parents[2])).resolve()
OUT = Path(os.environ.get("WATCHDOG_OUTPUT_DIR", ROOT / "watchdog-output")).resolve()
REQUIRED_FILES = (
    "README.md",
    "governanca/CARTA_DE_CONFIANCA_WORKFLOWS.md",
    "WATCHDOG/CARTA_WATCHDOG_B3_V1.md",
    "WATCHDOG/POLITICA_DE_ALERTAS_V1.json",
)
EXCLUDED_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__",
    ".mypy_cache", ".pytest_cache", "site-packages",
}


def add(checks: list[dict[str, Any]], check_id: str, status: str,
        severity: str, message: str, path: str | None = None) -> None:
    item: dict[str, Any] = {
        "id": check_id, "status": status, "severity": severity,
        "message": message,
    }
    if path:
        item["path"] = path
    checks.append(item)


def python_files() -> list[Path]:
    found: list[Path] = []
    for path in ROOT.rglob("*.py"):
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            continue
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.is_file():
            found.append(path)
    return sorted(found)


def workflow_files() -> list[Path]:
    base = ROOT / ".github" / "workflows"
    if not base.exists():
        return []
    return sorted(p for p in base.iterdir()
                  if p.is_file() and p.suffix.lower() in {".yml", ".yaml"})


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    checks: list[dict[str, Any]] = []
    errors = warnings = 0

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if path.is_file() and path.stat().st_size > 0:
            add(checks, "required_file:" + relative, "PASS", "INFO",
                "Documento essencial presente e não vazio.", relative)
        else:
            add(checks, "required_file:" + relative, "FAIL", "CRITICAL",
                "Documento essencial ausente ou vazio.", relative)
            errors += 1

    policy_path = ROOT / "WATCHDOG/POLITICA_DE_ALERTAS_V1.json"
    try:
        json.loads(policy_path.read_text(encoding="utf-8"))
        add(checks, "watchdog_policy_json", "PASS", "INFO",
            "Política de alertas contém JSON válido.", "WATCHDOG/POLITICA_DE_ALERTAS_V1.json")
    except (OSError, json.JSONDecodeError) as exc:
        add(checks, "watchdog_policy_json", "FAIL", "CRITICAL",
            "Política de alertas inválida: " + str(exc),
            "WATCHDOG/POLITICA_DE_ALERTAS_V1.json")
        errors += 1

    py_files = python_files()
    syntax_errors = 0
    for path in py_files:
        rel = path.relative_to(ROOT).as_posix()
        try:
            source = path.read_text(encoding="utf-8-sig")
            ast.parse(source, filename=rel)
        except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
            syntax_errors += 1
            detail = f"{type(exc).__name__}: {exc}"
            add(checks, "python_syntax:" + rel, "FAIL", "CRITICAL",
                "Falha ao analisar sintaxe Python — " + detail, rel)
        else:
            add(checks, "python_syntax:" + rel, "PASS", "INFO",
                "Sintaxe Python analisada sem executar o módulo.", rel)
    if syntax_errors:
        errors += syntax_errors
    add(checks, "python_inventory", "INFO", "INFO",
        f"{len(py_files)} arquivo(s) Python analisado(s); execução de módulos não realizada.")

    workflows = workflow_files()
    if not workflows:
        add(checks, "workflow_inventory", "FAIL", "CRITICAL",
            "Nenhum workflow YAML encontrado em .github/workflows.")
        errors += 1
    else:
        for path in workflows:
            rel = path.relative_to(ROOT).as_posix()
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                add(checks, "workflow_read:" + rel, "FAIL", "CRITICAL",
                    "Não foi possível ler o workflow: " + str(exc), rel)
                errors += 1
                continue

            if not re.search(r"(?m)^on\s*:", text) and not re.search(r"(?m)^['\"]on['\"]\s*:", text):
                add(checks, "workflow_trigger:" + rel, "WARN", "WARNING",
                    "Não foi detectada declaração textual de gatilho; verificar manualmente.", rel)
                warnings += 1

            if not re.search(r"(?m)^permissions\s*:", text):
                add(checks, "workflow_permissions:" + rel, "WARN", "WARNING",
                    "Workflow sem bloco permissions explícito; revisar princípio do menor privilégio.", rel)
                warnings += 1

            if not re.search(r"(?m)^\s*timeout-minutes\s*:", text):
                add(checks, "workflow_timeout:" + rel, "WARN", "WARNING",
                    "Não foi detectado timeout-minutes; jobs podem consumir runner além do esperado.", rel)
                warnings += 1

            action_refs = re.findall(r"(?m)^\s*uses:\s*([^\s#]+)", text)
            floating = [ref for ref in action_refs if "@" in ref and
                        not re.search(r"@[0-9a-fA-F]{40}$", ref)]
            if floating:
                add(checks, "workflow_action_pinning:" + rel, "WARN", "WARNING",
                    "Referências de Actions não fixadas em SHA completo: " +
                    ", ".join(floating), rel)
                warnings += 1

        add(checks, "workflow_inventory", "INFO", "INFO",
            f"{len(workflows)} workflow(s) YAML inspecionado(s) por regras textuais.")
    status = "FAIL" if errors else ("WARN" if warnings else "PASS")
    now = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    report: dict[str, Any] = {
        "schema_version": "1.0.0",
        "component": "B3-WATCHDOG",
        "generated_at_utc": now,
        "commit": os.environ.get("GITHUB_SHA", "local"),
        "branch": os.environ.get("GITHUB_REF_NAME", "local"),
        "status": status,
        "summary": {
            "critical_errors": errors,
            "warnings": warnings,
            "checks": len(checks),
            "python_files": len(py_files),
            "workflow_files": len(workflows),
        },
        "checks": checks,
        "limitations": [
            "Análise estática não prova correção semântica ou financeira.",
            "Os workflows são inspecionados por regras textuais; não é um parser YAML.",
            "Nenhum módulo Python é executado e nenhum arquivo do repositório é alterado.",
        ],
    }
    json_path = OUT / "watchdog-report.json"
    md_path = OUT / "watchdog-report.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Relatório Watchdog B3",
        "",
        f"- **Estado:** {status}",
        f"- **Gerado em UTC:** {now}",
        f"- **Commit:** {report['commit']}",
        f"- **Branch/ref:** {report['branch']}",
        f"- **Erros críticos:** {errors}",
        f"- **Avisos:** {warnings}",
        f"- **Arquivos Python:** {len(py_files)}",
        f"- **Workflows:** {len(workflows)}",
        "",
        "## Verificações",
        "",
        "| Estado | Severidade | Verificação | Detalhe |",
        "|---|---|---|---|",
    ]
    for item in checks:
        msg = str(item["message"]).replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {item['status']} | {item['severity']} | {item['id']} | {msg} |")
    lines.extend([
        "",
        "## Limitações",
        "",
        "- A análise estática não certifica semântica de mercado nem correção financeira.",
        "- Inspeção de workflows é textual; validação completa do YAML requer ferramenta própria.",
        "- Nenhum módulo Python é executado e nenhum arquivo de código/dados é modificado.",
        "",
    ])
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Watchdog status={status}; errors={errors}; warnings={warnings}; "
          f"python={len(py_files)}; workflows={len(workflows)}")
    print(f"Reports: {md_path} ; {json_path}")
    return 1 if errors else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FATAL: watchdog internal error: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
