#!/usr/bin/env python3
"""Auditoria reprodutível dos hashes canónicos de documentos Markdown B3.

Regra: UTF-8, remover BOM inicial, normalizar CRLF/CR para LF e excluir
apenas as linhas de metadados SHA-256 canónico e Commit de referência.
Este utilitário é somente leitura; nunca reescreve documentos.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

SHA_LABEL = "**SHA-256 (conteúdo canónico)**"
COMMIT_LABEL = "**Commit de referência"
HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def tracked_markdown() -> list[Path]:
    raw = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md", "*.MD"],
        check=True, capture_output=True,
    ).stdout
    paths = [Path(x.decode("utf-8")) for x in raw.split(b"\0") if x]
    return sorted(set(paths), key=lambda p: p.as_posix().casefold())


def canonical_digest(text: str) -> str:
    normalized = text.removeprefix("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    kept = []
    removed_sha = 0
    removed_commit = 0
    for line in normalized.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        if stripped.startswith("|") and SHA_LABEL in stripped:
            removed_sha += 1
            continue
        if stripped.startswith("|") and COMMIT_LABEL in stripped:
            removed_commit += 1
            continue
        kept.append(line)
    if removed_sha != 1 or removed_commit != 1:
        raise ValueError(f"linhas de controlo esperadas: SHA={removed_sha}, commit={removed_commit}")
    payload = "".join(kept).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def read_status(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        return {"path": path.as_posix(), "status": "ERRO_LEITURA", "detail": str(exc)}
    if not text.startswith("# "):
        return {"path": path.as_posix(), "status": "SEM_CABECALHO_H1"}
    lines = text.removeprefix("\ufeff").replace("\r\n", "\n").replace("\r", "\n").splitlines()
    sha_lines = [line for line in lines if line.startswith("|") and SHA_LABEL in line]
    commit_lines = [line for line in lines if line.startswith("|") and COMMIT_LABEL in line]
    if len(sha_lines) != 1 or len(commit_lines) != 1:
        return {
            "path": path.as_posix(), "status": "CABECALHO_CONTROLO_INVALIDO",
            "sha_lines": len(sha_lines), "commit_lines": len(commit_lines),
        }
    match = re.match(r"^\|\s*\*\*SHA-256 \(conteúdo canónico\)\*\*\s*\|\s*(.*?)\s*\|\s*$", sha_lines[0])
    declared = match.group(1).strip() if match else ""
    if not declared or "PENDENTE" in declared.upper() or "CALCULAR" in declared.upper():
        return {"path": path.as_posix(), "status": "PENDENTE", "declared": declared}
    if not HASH_RE.fullmatch(declared):
        return {"path": path.as_posix(), "status": "FORMATO_HASH_INVALIDO", "declared": declared}
    try:
        calculated = canonical_digest(text)
    except ValueError as exc:
        return {"path": path.as_posix(), "status": "CABECALHO_CONTROLO_INVALIDO", "detail": str(exc)}
    return {
        "path": path.as_posix(),
        "status": "CONFORME" if declared.lower() == calculated else "DIVERGENTE",
        "declared": declared.lower(),
        "calculated": calculated,
    }


def main() -> int:
    paths = tracked_markdown()
    rows = [read_status(path) for path in paths]
    counts: dict[str, int] = {}
    for row in rows:
        status = row["status"]
        counts[status] = counts.get(status, 0) + 1
    report = {
        "schema_version": "1.0.0",
        "project": "B3 — A BOLSA DO BRASIL",
        "repository": "carlos-andrade/B3",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "algorithm": {
            "encoding": "UTF-8",
            "bom": "removed if present",
            "line_endings": "LF",
            "excluded_metadata_lines": [SHA_LABEL, "Commit de referência (versão anterior)"],
            "git_blob_sha_is_not_canonical_sha256": True,
            "mode": "read-only; no files rewritten",
        },
        "files_scanned": len(rows),
        "status_counts": counts,
        "results": rows,
    }
    out = Path("sha256_documental_b3_report.json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"files_scanned": len(rows), "status_counts": counts, "report": str(out)}, ensure_ascii=False))
    print(f"::notice::Relatório criado: {out}; auditoria somente de leitura.")
    return 1 if counts.get("ERRO_LEITURA", 0) or counts.get("CABECALHO_CONTROLO_INVALIDO", 0) else 0


if __name__ == "__main__":
    sys.exit(main())
