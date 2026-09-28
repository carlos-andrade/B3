#!/usr/bin/env python3
"""Atualiza automaticamente o bloco auditável do README do projeto B3.

A rotina não reescreve o README inteiro. Ela mantém apenas um bloco
explicitamente gerenciado pela automação, preservando o conteúdo editorial.
"""

from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"

BEGIN = "<!-- B3_README_AUTO_BEGIN -->"
END = "<!-- B3_README_AUTO_END -->"

RELEVANT_PREFIXES = (
    ".github/workflows/",
    "ativos/",
    "governanca/",
    "scripts/ingestao/",
    "dados/bcb_sgs/",
    "dados/bdi/",
    "dados/calendario_economico/",
    "dados/cotahist/normalized/",
    "dados/cotahist/certificacao/",
    "dados/market_data/",
    "index.html",
    "PROMPT_MESTRE_B3_799_CARACTERES.md",
)

IGNORED_PREFIXES = (
    "dados/cotahist/raw/",
    "dados/market_data/raw/",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stderr=subprocess.DEVNULL,
    ).strip()


def relevant(path: str) -> bool:
    path = path.replace("\\", "/")
    if any(path.startswith(p) for p in IGNORED_PREFIXES):
        return False
    return path in RELEVANT_PREFIXES or any(path.startswith(p) for p in RELEVANT_PREFIXES)


def latest_relevant_commit() -> tuple[str, str, str]:
    format_spec = "%H%x09%cI%x09%s"
    result = git(
        "log",
        "-1",
        f"--format={format_spec}",
        "--",
        *RELEVANT_PREFIXES,
    )
    sha, committed_at, subject = result.split("\t", 2)
    return sha, committed_at, subject


def count_files(prefix: str, suffix: str | None = None) -> int:
    base = ROOT / prefix
    if not base.exists():
        return 0
    files = [p for p in base.rglob("*") if p.is_file()]
    if suffix:
        files = [p for p in files if p.name.endswith(suffix)]
    return len(files)


def workflow_count() -> int:
    return count_files(".github/workflows", ".yml") + count_files(".github/workflows", ".yaml")


def ingestion_script_count() -> int:
    return count_files("scripts/ingestao", ".py")


def top_level_dirs() -> list[str]:
    return sorted(
        p.name
        for p in ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )


def build_block() -> str:
    sha, committed_at, subject = latest_relevant_commit()
    dt = datetime.fromisoformat(committed_at.replace("Z", "+00:00"))
    date_utc = dt.astimezone(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")

    lines = [
        BEGIN,
        "## Atualização automática do README",
        "",
        "> Este bloco é gerenciado pelo workflow `Atualizar README — B3`.",
        "",
        f"- **Última alteração relevante:** `{sha[:12]}` — {date_utc}",
        f"- **Commit de referência:** {subject}",
        f"- **Workflows GitHub Actions:** {workflow_count()}",
        f"- **Scripts Python em `scripts/ingestao/`:** {ingestion_script_count()}",
        f"- **Diretórios operacionais de primeiro nível:** {len(top_level_dirs())}",
        "",
        "**Escopo monitorado:**",
        "",
        "- workflows e automações;",
        "- catálogo e universo de ativos;",
        "- governança e certificação;",
        "- scripts de ingestão;",
        "- dados normalizados e certificados;",
        "- dashboard e documentação operacional.",
        "",
        "**Excluído do gatilho automático:** dados RAW volumosos, para evitar commits",
        "desnecessários no README por simples alteração de arquivos brutos.",
        "",
        "A automação não substitui a revisão editorial. Ela mantém o inventário operacional",
        "e a trilha de atualização sincronizados com o estado efetivo do repositório.",
        END,
    ]
    return "\n".join(lines)


def replace_block(content: str, block: str) -> str:
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        flags=re.DOTALL,
    )
    if pattern.search(content):
        return pattern.sub(block, content, count=1)

    anchor = "\n## Licença e uso\n"
    if anchor in content:
        return content.replace(anchor, "\n" + block + "\n" + anchor, 1)

    return content.rstrip() + "\n\n" + block + "\n"


def main() -> int:
    if not README.exists():
        raise SystemExit("README.md não encontrado.")

    original = README.read_text(encoding="utf-8")
    updated = replace_block(original, build_block())

    if updated == original:
        print("README_SEM_MUDANCA")
        return 0

    README.write_text(updated, encoding="utf-8")
    print("README_ATUALIZADO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
