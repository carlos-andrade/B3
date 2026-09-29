#!/usr/bin/env python3
"""Publica a documentação WIKI/ no repositório da Wiki nativa do B3."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("uso: sincronizar_wiki_b3.py <diretorio-da-wiki>", file=sys.stderr)
        return 2

    repo_root = Path(__file__).resolve().parents[2]
    source = repo_root / "WIKI"
    target = Path(sys.argv[1]) / "B3"

    if not source.is_dir():
        print(f"diretório de origem não encontrado: {source}", file=sys.stderr)
        return 1

    target.mkdir(parents=True, exist_ok=True)

    for child in target.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    for item in source.rglob("*"):
        if item.is_dir():
            continue
        relative = item.relative_to(source)
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, destination)

    home = Path(sys.argv[1]) / "Home.md"
    home.write_text(
        "# B3 — A BOLSA DO BRASIL\n\n"
        "> Documentação publicada automaticamente a partir de "
        "carlos-andrade/B3/WIKI/.\n\n"
        "## Documentação\n\n"
        "- [Wiki técnica](B3/README.md)\n"
        "- [Visão geral](B3/00-INICIO/VISAO_GERAL.md)\n"
        "- [Estado atual](B3/00-INICIO/ESTADO_ATUAL.md)\n"
        "- [Governança](B3/01-GOVERNANCA/MODELO_DE_GOVERNANCA.md)\n"
        "- [Política de evidências](B3/01-GOVERNANCA/POLITICA_DE_EVIDENCIAS.md)\n"
        "- [Arquitetura](B3/02-ARQUITETURA/ARQUITETURA_GERAL.md)\n"
        "- [Automação da Wiki](B3/09-AUTOMACAO/WIKI_NATIVA.md)\n\n"
        "A Wiki nativa é uma camada de publicação. A fonte de verdade é o "
        "repositório principal.\n",
        encoding="utf-8",
    )

    print(f"Wiki sincronizada a partir de {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
