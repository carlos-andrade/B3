#!/usr/bin/env python3
"""Captura e normaliza um snapshot operacional do Copom a partir da API oficial BCB.

A rotina preserva as respostas RAW separadamente e cria um envelope NORMALIZED
somente quando os recursos de lista/detalhe respondem com JSON válido.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "https://www.bcb.gov.br/api/servico/sitebcb/copom"
UA = "B3-INGESTAO/2.0 (+https://github.com/carlos-andrade/B3)"
TZ = "America/Sao_Paulo"

def get_json(url: str) -> tuple[bytes, str]:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urlopen(req, timeout=45) as r:
        return r.read(), r.geturl()

def save_raw(root: Path, name: str, requested: str, payload: bytes, final_url: str) -> dict:
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(payload)
    meta = {
        "source_url": requested,
        "final_url": final_url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "content_type": "application/json",
        "timezone": TZ,
    }
    p.with_suffix(p.suffix + ".meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return meta

def text_from_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", value).strip()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quantidade", type=int, default=5)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    root = Path(args.output)
    raw_dir = root / "raw"
    norm_dir = root / "normalized"
    raw_dir.mkdir(parents=True, exist_ok=True)
    norm_dir.mkdir(parents=True, exist_ok=True)

    captured = {}
    for kind, endpoint in (("atas", "atas"), ("comunicados", "comunicados")):
        url = f"{BASE}/{endpoint}?{urlencode({'quantidade': args.quantidade})}"
        payload, final_url = get_json(url)
        captured[kind] = json.loads(payload.decode("utf-8"))
        save_raw(raw_dir, f"{endpoint}_lista.json", url, payload, final_url)

    atas = captured["atas"].get("conteudo", [])
    comunicados = captured["comunicados"].get("conteudo", [])
    meetings = sorted(
        {int(x["nroReuniao"]) for x in atas + comunicados if x.get("nroReuniao", x.get("nro_reuniao")) is not None},
        reverse=True,
    )
    if not meetings:
        raise RuntimeError("Nenhuma reunião encontrada na API do BCB")

    meeting = meetings[0]
    detail = {}
    for kind, endpoint, key in (
        ("ata", "atas_detalhes", "nro_reuniao"),
        ("comunicado", "comunicados_detalhes", "nro_reuniao"),
    ):
        url = f"{BASE}/{endpoint}?{urlencode({key: meeting})}"
        payload, final_url = get_json(url)
        detail[kind] = json.loads(payload.decode("utf-8"))
        save_raw(raw_dir, f"{endpoint}_{meeting}.json", url, payload, final_url)

    ata = (detail["ata"].get("conteudo") or [{}])[0]
    com = (detail["comunicado"].get("conteudo") or [{}])[0]
    ata_text = text_from_html(ata.get("textoAta", ""))
    com_text = text_from_html(com.get("textoComunicado", ""))

    decision_text = ata_text + " " + com_text
    m_rate = re.search(r"taxa (?:básica de juros|Selic).*?(?:em|para)\s+(\d+(?:[.,]\d+)?)%\s*a\.?a\.?", decision_text, re.I)
    rate = float(m_rate.group(1).replace(",", ".")) if m_rate else None

    scheduled_date = ata.get("dataReferencia") or com.get("dataReferencia")
    published_at = ata.get("dataPublicacao") or None
    normalized = {
        "schema_version": "2.0",
        "source": "Banco Central do Brasil",
        "normalized_at": datetime.now(timezone.utc).isoformat(),
        "event_count": 1,
        "events": [{
            "event_id": f"BCB-COPOM-{meeting}",
            "source": "BCB",
            "source_url": BASE,
            "event_name": f"COPOM {meeting}ª reunião",
            "event_code": "COPOM_DECISION",
            "meeting_number": meeting,
            "scheduled_date": scheduled_date,
            "scheduled_time": None,
            "event_time_status": "UNKNOWN",
            "published_at": published_at,
            "information_available_at": published_at,
            "status": "RELEASED",
            "decision_rate_percent_aa": rate,
            "decision_text": com.get("titulo"),
            "votes_text": None,
            "ata_title": ata.get("titulo"),
            "ata_pdf_url": ata.get("urlPdfAta"),
            "ata_text": ata.get("textoAta"),
            "comunicado_text": com.get("textoComunicado"),
            "evidence": {
                "ata_list_sha256": captured.get("atas") and hashlib.sha256(
                    json.dumps(captured["atas"], ensure_ascii=False, separators=(",", ":")).encode()
                ).hexdigest(),
                "raw_directory": str(raw_dir),
            },
            "backtest_rule": "information_available_at <= bar_timestamp"
        }]
    }
    out = norm_dir / f"copom_{meeting}.json"
    out.write_text(json.dumps(normalized, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"meeting": meeting, "normalized": str(out), "rate": rate}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
