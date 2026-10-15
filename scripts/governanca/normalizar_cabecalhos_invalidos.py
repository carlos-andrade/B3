#!/usr/bin/env python3
"""Normalização controlada de cabeçalhos Markdown legados do projeto B3.

Preserva o conteúdo original, cria um cabeçalho documental canónico e calcula
SHA-256 segundo a norma GOVERNANCA 1.0.3. Não altera dados não-Markdown.
"""
from __future__ import annotations

import hashlib
import subprocess
from datetime import date
from pathlib import Path

SHA_LABEL = "**SHA-256 (conteúdo canónico)**"
COMMIT_LABEL = "**Commit de referência"
REPO = "https://github.com/carlos-andrade/B3"
AUTHORITY = "https://github.com/carlos-andrade/GOVERNANCA/blob/main/CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md"
TODAY = date.today().isoformat()


def canonical_digest(text: str) -> str:
    normalized = text.removeprefix("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    kept = []
    sha_count = commit_count = 0
    for line in normalized.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        if stripped.startswith("|") and SHA_LABEL in stripped:
            sha_count += 1
            continue
        if stripped.startswith("|") and COMMIT_LABEL in stripped:
            commit_count += 1
            continue
        kept.append(line)
    if sha_count != 1 or commit_count != 1:
        raise ValueError(f"linhas de controlo inválidas: SHA={sha_count}, commit={commit_count}")
    return hashlib.sha256("".join(kept).encode("utf-8")).hexdigest()


def tracked_markdown() -> list[Path]:
    raw = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md", "*.MD"],
        check=True, capture_output=True,
    ).stdout
    return sorted(
        (Path(item.decode("utf-8")) for item in raw.split(b"\0") if item),
        key=lambda p: p.as_posix().casefold(),
    )


def kind_for(path: str) -> str:
    if "/raw/" in path:
        return "EVIDENCIA_RAW_DOCUMENTAL"
    if "/manifests/" in path:
        return "MANIFESTO_OPERACIONAL"
    if "/cotahist/" in path:
        return "DOCUMENTO_TECNICO_COTAHIST"
    if "/auditorias/" in path or "AUDITORIA" in path.upper():
        return "RELATORIO_DE_AUDITORIA"
    if "/fontes/" in path:
        return "DOCUMENTO_DE_FONTES"
    if "/catalogo/" in path:
        return "DOCUMENTO_DE_CATALOGO"
    return "DOCUMENTO_TECNICO"


def make_table(path: str, baseline: str) -> list[str]:
    import re
    path_id = hashlib.sha256(path.encode("utf-8")).hexdigest()[:12].upper()
    return [
        "",
        "| Campo | Valor |",
        "|---|---|",
        f"| **ID** | B3-DOC-{path_id} |",
        "| **Projeto** | B3 — A BOLSA DO BRASIL |",
        f"| **Repositório** | [carlos-andrade/B3]({REPO}) |",
        f"| **Tipo documental** | {kind_for(path)} |",
        "| **Fase** | NORMALIZACAO_DOCUMENTAL |",
        "| **Estado** | EM_REVISAO |",
        "| **Versão** | 1.0.0 |",
        f"| {SHA_LABEL} | CALCULAR |",
        f"| **Commit de referência (versão anterior)** | [{baseline}]({REPO}/commit/{baseline}) |",
        "| **Data de criação** | N/A — data original não identificada no ficheiro-base |",
        f"| **Data de atualização** | {TODAY} |",
        "| **Responsável** | Manutenção técnica do projeto B3 |",
        "| **Aprovador** | Pendente — validação do proprietário do repositório, quando aplicável |",
        "| **Origem** | Conteúdo preexistente preservado; consultar as evidências e referências no corpo |",
        f"| **Autoridade superior** | [Norma de cabeçalho GOVERNANCA v1.0.3]({AUTHORITY}) |",
        "| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |",
        "",
    ]


def main() -> int:
    baseline = subprocess.run(
        ["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()
    changed = []
    unresolved = []
    for path_obj in tracked_markdown():
        path = path_obj.as_posix()
        raw = path_obj.read_text(encoding="utf-8")
        text = raw.removeprefix("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
        lines = text.splitlines(keepends=True)
        if not text.startswith("# "):
            unresolved.append(f"{path}: falta H1")
            continue
        sha_rows = [x for x in text.splitlines() if x.startswith("|") and SHA_LABEL in x]
        commit_rows = [x for x in text.splitlines() if x.startswith("|") and COMMIT_LABEL in x]
        if len(sha_rows) == 1 and len(commit_rows) == 1:
            try:
                canonical_digest(text)
                continue
            except ValueError:
                pass
        # Remover apenas linhas de controlo preexistentes; preservar todo o restante texto.
        body = []
        for line in lines:
            plain = line.rstrip("\n")
            if plain.startswith("|") and (SHA_LABEL in plain or COMMIT_LABEL in plain):
                continue
            body.append(line)
        clean = "".join(body).removeprefix("\ufeff")
        clean_lines = clean.splitlines(keepends=True)
        if not clean_lines or not clean_lines[0].startswith("# "):
            unresolved.append(f"{path}: H1 inválido após limpeza")
            continue
        title = clean_lines[0].rstrip("\n")
        rest = "".join(clean_lines[1:])
        content = title + "\n" + "\n".join(make_table(path, baseline)) + rest
        # Garantir separação entre tabela canónica e o corpo preservado.
        if not content.endswith("\n"):
            content += "\n"
        digest = canonical_digest(content)
        content = content.replace(f"| {SHA_LABEL} | CALCULAR |", f"| {SHA_LABEL} | {digest} |", 1)
        if canonical_digest(content) != digest:
            unresolved.append(f"{path}: hash canónico não reproduzível")
            continue
        if content != raw:
            path_obj.write_text(content, encoding="utf-8", newline="\n")
            changed.append(path)
    print(f"Documentos normalizados: {len(changed)}")
    print(f"Documentos não resolvidos: {len(unresolved)}")
    for item in unresolved:
        print(f"ERRO: {item}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
