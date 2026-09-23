#!/usr/bin/env python3
"""Baixa arquivos da API CSV oficial da B3 e gera manifesto auditável."""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "dados" / "market_data" / "raw"
MANIFESTS = ROOT / "dados" / "market_data" / "manifests"

ARQUIVOS = {
    "BVBG.028.02": "InstrumentsConsolidated",
    "BVBG.086.01": "TradeInformationConsolidated",
    "BVBG.087.01": "IndexReport",
    "BVBG.186.01": "EquitiesSimplifiedPriceReport",
    "BVBG.187.01": "DerivativesSimplifiedPriceReport",
    "BVBG.029.02": "IndicatorReport",
}

def get_json(url: str) -> dict:
    req = Request(url, headers={"User-Agent": "B3-Dados/1.0"})
    with urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))

def get_bytes(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "B3-Dados/1.0"})
    with urlopen(req, timeout=300) as r:
        return r.read()

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_filename(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name)


def validar_csv(data: bytes, expected_table: str) -> dict:
    text = data.decode("iso-8859-1")
    lines = text.splitlines()
    status = None
    header_idx = None
    for i, line in enumerate(lines[:10]):
        if line.strip().lower().startswith("status do arquivo"):
            status = line.split(":", 1)[-1].strip()
        if ";" in line and ("TckrSymb" in line or "RptDt" in line or "TradeDate" in line):
            header_idx = i
            break
    if header_idx is None:
        raise RuntimeError(f"Cabeçalho CSV não localizado para {expected_table}.")
    reader = csv.DictReader(lines[header_idx:], delimiter=";")
    rows = list(reader)
    if not rows:
        raise RuntimeError(f"CSV sem registros para {expected_table}.")
    fields = reader.fieldnames or []
    return {
        "encoding": "ISO-8859-1",
        "delimiter": ";",
        "status": status,
        "header_line_zero_based": header_idx,
        "columns": len(fields),
        "records": len(rows),
        "required_key_present": any(k in fields for k in ("TckrSymb", "RptDt", "TradeDate")),
    }

def baixar(codigo: str, date: str) -> dict:
    if codigo not in ARQUIVOS:
        raise ValueError(f"Arquivo não suportado: {codigo}")
    table = ARQUIVOS[codigo]
    qs = urlencode({"fileName": table, "date": date, "recaptchaToken": ""})
    info = get_json(f"https://arquivos.b3.com.br/api/download/requestname?{qs}")
    token = info.get("token")
    if not token and info.get("redirectUrl"):
        token = info["redirectUrl"].split("token=", 1)[-1]
    if not token:
        raise RuntimeError(f"Token não retornado para {table}: {info}")
    data = get_bytes(f"https://arquivos.b3.com.br/api/download/?token={token}")
    if not data:
        raise RuntimeError("Resposta vazia.")
    target = RAW / codigo / date
    target.mkdir(parents=True, exist_ok=True)
    supplied_name = ((info.get("file") or {}).get("name") or f"{table}_{date}.csv")
    supplied_ext = ((info.get("file") or {}).get("extension") or "")
    name = safe_filename(supplied_name)
    if supplied_ext and not name.lower().endswith(supplied_ext.lower()):
        name += supplied_ext
    path = target / name
    validation = validar_csv(data, table)
    path.write_bytes(data)
    manifest = {
        "date": date,
        "codigo_b3": codigo,
        "api_file_name": table,
        "source": "B3 Pesquisa por Pregão / API CSV",
        "url_request": f"https://arquivos.b3.com.br/api/download/requestname?fileName={table}&date={date}&recaptchaToken=",
        "file": str(path.relative_to(ROOT)),
        "size_bytes": len(data),
        "sha256": sha256(data),
        "validation": validation,
    }
    mdir = MANIFESTS / codigo
    mdir.mkdir(parents=True, exist_ok=True)
    (mdir / f"{date}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo", action="append", choices=sorted(ARQUIVOS))
    ap.add_argument("--date", required=True)
    args = ap.parse_args()
    codes = args.arquivo or list(ARQUIVOS)
    results = [baixar(c, args.date) for c in codes]
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

# Pipeline auditável; disparo por push usa a data local de Sao Paulo quando --date não é informado pelo evento.
