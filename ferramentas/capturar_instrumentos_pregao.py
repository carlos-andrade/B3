#!/usr/bin/env python3
"""Captura e valida o arquivo BVBG.028.02 da Pesquisa por Pregão.

Fonte oficial:
https://www.b3.com.br/pesquisapregao/download?filelist=IN{YYMMDD}.zip

O arquivo é tratado como artefato bruto. O script:
1. baixa o ZIP;
2. calcula SHA-256;
3. inspeciona ZIP externo e interno;
4. identifica os XMLs de snapshot;
5. lê CreDtAndTm e TtlNbOfMsg do header;
6. registra tamanho, membros e metadados em manifesto.

Não grava o ZIP bruto no Git por padrão, pois a B3 pode publicar artefatos
superiores ao limite de arquivo do GitHub. O manifesto registra o hash para
auditoria; o workflow preserva o bruto como artifact do GitHub Actions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import urllib.request
import zipfile
from datetime import datetime
from pathlib import Path

BASE = "https://www.b3.com.br/pesquisapregao/download"
ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = ROOT / "ativos" / "catalogo" / "fontes"
STAMP_RE = re.compile(rb"<CreDtAndTm>([^<]+)</CreDtAndTm>")
COUNT_RE = re.compile(rb"<TtlNbOfMsg>([^<]+)</TtlNbOfMsg>")


def download(url: str, path: Path) -> tuple[int, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "B3-Dados/1.0", "Accept": "*/*"},
    )
    total = 0
    digest = hashlib.sha256()
    with urllib.request.urlopen(request, timeout=300) as response, path.open("wb") as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)
            digest.update(chunk)
            total += len(chunk)
    return total, digest.hexdigest()


def inspect_archive(path: Path) -> dict:
    with zipfile.ZipFile(path) as outer:
        outer_members = outer.namelist()
        inner_names = [n for n in outer_members if n.lower().endswith(".zip")]
        xml_direct = [n for n in outer_members if n.lower().endswith(".xml")]
        snapshots = []

        if xml_direct:
            sources = [(path, n) for n in xml_direct]
        else:
            if not inner_names:
                raise RuntimeError("ZIP externo não contém ZIP/XML.")
            # IN*.zip é normalmente um ZIP contendo o arquivo XML de instrumentos.
            inner_name = inner_names[0]
            with outer.open(inner_name) as src:
                inner_bytes = src.read()
            inner_path = path.with_suffix(".inner.zip")
            inner_path.write_bytes(inner_bytes)
            sources = []
            with zipfile.ZipFile(inner_path) as inner:
                for name in inner.namelist():
                    if name.lower().endswith(".xml"):
                        with inner.open(name) as stream:
                            probe = stream.read(4096)
                        stamp = STAMP_RE.search(probe)
                        count = COUNT_RE.search(probe)
                        snapshots.append(
                            {
                                "member": name,
                                "creation_timestamp": stamp.group(1).decode() if stamp else None,
                                "declared_records": int(count.group(1)) if count else None,
                                "header_probe_bytes": len(probe),
                            }
                        )
            inner_path.unlink(missing_ok=True)
            return {
                "outer_members": outer_members,
                "inner_zip": inner_name,
                "snapshots": snapshots,
            }

        for name in xml_direct:
            with outer.open(name) as stream:
                probe = stream.read(4096)
            stamp = STAMP_RE.search(probe)
            count = COUNT_RE.search(probe)
            snapshots.append(
                {
                    "member": name,
                    "creation_timestamp": stamp.group(1).decode() if stamp else None,
                    "declared_records": int(count.group(1)) if count else None,
                    "header_probe_bytes": len(probe),
                }
            )
        return {"outer_members": outer_members, "snapshots": snapshots}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    args = parser.parse_args()

    date_ref = datetime.strptime(args.date, "%Y-%m-%d").date()
    file_name = f"IN{date_ref:%y%m%d}.zip"
    url = f"{BASE}?filelist={file_name}"

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / file_name
        size, sha256 = download(url, path)
        archive = inspect_archive(path)

    snapshots = archive.get("snapshots", [])
    if not snapshots:
        raise RuntimeError("Nenhum XML BVBG.028.02 encontrado.")
    if any(s["creation_timestamp"] is None for s in snapshots):
        raise RuntimeError("Snapshot sem CreDtAndTm.")
    if any(s["declared_records"] is None for s in snapshots):
        raise RuntimeError("Snapshot sem TtlNbOfMsg.")

    manifest = {
        "capture_date": args.date,
        "source": "B3 Pesquisa por Pregão",
        "layout": "BVBG.028.02",
        "file_name": file_name,
        "url": url,
        "size_bytes": size,
        "sha256": sha256,
        "outer_members": archive["outer_members"],
        "snapshots": sorted(
            snapshots, key=lambda x: x["creation_timestamp"], reverse=True
        ),
    }

    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    target = MANIFEST_DIR / f"INSTRUMENTOS_BVBG028_02_{args.date}.json"
    target.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
