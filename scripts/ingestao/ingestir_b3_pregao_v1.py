#!/usr/bin/env python3
"""Captura arquivos públicos da Pesquisa por Pregão B3.

O endpoint histórico observado publicamente pela B3/GitHub usa:
https://www.b3.com.br/pesquisapregao/download?filelist=<identificador>

IMPORTANTE:
- o identificador filelist deve ser confirmado para o arquivo/data desejados;
- o script não inventa identificadores;
- a resposta recebida é preservada byte-for-byte;
- SHA-256 e metadados são gravados ao lado do RAW.

Uso:
  python ingestir_b3_pregao_v1.py "<url_confirmada>" <saida_raw>
"""
from __future__ import annotations
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

UA = "B3-INGESTAO/1.0 (+https://github.com/carlos-andrade/B3)"

def capture(url: str, output: str) -> None:
    req = Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "application/zip,application/octet-stream,*/*",
        },
    )
    with urlopen(req, timeout=60) as response:
        payload = response.read()
        content_type = response.headers.get("Content-Type", "")
        final_url = response.geturl()

    digest = hashlib.sha256(payload).hexdigest()
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(payload)

    meta = {
        "source_url": url,
        "final_url": final_url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": digest,
        "bytes": len(payload),
        "content_type": content_type,
        "timezone": "America/Sao_Paulo",
    }
    out.with_suffix(out.suffix + ".meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(
            "uso: ingestir_b3_pregao_v1.py '<url_confirmada>' <saida_raw>"
        )
    capture(sys.argv[1], sys.argv[2])
