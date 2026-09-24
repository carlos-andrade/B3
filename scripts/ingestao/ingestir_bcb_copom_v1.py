#!/usr/bin/env python3
"""Captura RAW dos recursos oficiais de documentos do Copom.

Uso:
  python ingestir_bcb_copom_v1.py <url> <saida_raw>
A URL deve apontar para um recurso oficial BCB/Dados Abertos.
"""
from __future__ import annotations
import hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

UA = "B3-INGESTAO/1.0 (+https://github.com/carlos-andrade/B3)"

def capture(url: str, output: str) -> None:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/plain,*/*"})
    with urlopen(req, timeout=30) as r:
        payload = r.read()
        content_type = r.headers.get("Content-Type", "")
        final_url = r.geturl()
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
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("uso: ingestir_bcb_copom_v1.py <url> <saida_raw>")
    capture(sys.argv[1], sys.argv[2])
