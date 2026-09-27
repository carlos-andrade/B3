#!/usr/bin/env python3
import csv
import hashlib
import json
import re
import sys
import time
from datetime import date, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import base64
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
CODES = [
    "AGFS","BDRX","GPTW","IBBR","IBEE","IBEP","IBEW","IBHB","IBLV","IBOV",
    "IBRA","IBRX","IBRX50","IBSD","ICO2","ICON","IDIV","IDVR","IEE","IFIL",
    "IFIX","IFNC","IGCNM","IGCT","IGCX","IMAT","IMOB","INDX","ISE","ITAG",
    "IVBX2","MLCX","SMLL","UTIL"
]
API_URL = "https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/{encoded}"
CODE_ALIAS = {"IBRX": "IBXX", "IBRX50": "IBXL", "ISE": "ISEE", "IVBX2": "IVBX"}
TZ = ZoneInfo("America/Sao_Paulo")
NOW = datetime.now(TZ)
TODAY = NOW.date()

RAW_DIR = ROOT / "dados" / "indices_b3" / "raw"
NORM_DIR = ROOT / "dados" / "indices_b3" / "normalized"
MAN_DIR = ROOT / "dados" / "indices_b3" / "manifests"
OFF_DIR = ROOT / "dados" / "indices_b3" / "oficial"
for p in (RAW_DIR, NORM_DIR, MAN_DIR, OFF_DIR):
    p.mkdir(parents=True, exist_ok=True)

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def fetch(code):
    api_code = CODE_ALIAS.get(code, code)
    payload = {"language": "pt-br", "pageNumber": 1, "pageSize": 1000, "index": api_code, "segment": "1"}
    encoded = base64.b64encode(str(payload).encode("utf-8")).decode("utf-8")
    url = API_URL.format(encoded=encoded)
    last = None
    for attempt in range(1, 6):
        try:
            req = Request(url, headers={"User-Agent": "B3-Indices-Ingestao/1.1 (+https://github.com/carlos-andrade/B3)", "Accept": "application/json"})
            with urlopen(req, timeout=30) as r:
                data = r.read()
                ctype = (r.headers.get("Content-Type") or "").lower()
                if not data:
                    raise ValueError("resposta vazia")
                try:
                    obj = json.loads(data.decode("utf-8"))
                except json.JSONDecodeError as e:
                    raise ValueError(f"resposta nao JSON; content-type={ctype}; preview={data[:200]!r}") from e
                if not isinstance(obj, dict) or not isinstance(obj.get("results"), list):
                    raise ValueError("resposta JSON sem lista 'results'")
                return data, obj, url
        except (HTTPError, URLError, TimeoutError, ValueError) as e:
            last = str(e)
            if attempt < 5: time.sleep(2 ** (attempt - 1))
    raise RuntimeError(last or "falha desconhecida")

def parse_api(code, obj):
    header = obj.get("header") or {}
    candidates = []
    def collect_dates(value):
        if isinstance(value, dict):
            for k, v in value.items():
                if "date" in str(k).lower() or "data" in str(k).lower(): candidates.append(v)
                collect_dates(v)
        elif isinstance(value, list):
            for v in value: collect_dates(v)
    collect_dates(header)
    d = None
    for value in candidates:
        if isinstance(value, str):
            for fmt in ("%d/%m/%Y", "%d/%m/%y", "%Y-%m-%d"):
                try: d = datetime.strptime(value.strip(), fmt).date(); break
                except ValueError: pass
        if d: break
    if d is None: raise ValueError("data de referencia nao encontrada no header da API")
    if d > TODAY: raise ValueError(f"data futura na fonte: {d.isoformat()} > {TODAY.isoformat()}")
    rows = []
    for item in obj["results"]:
        if not isinstance(item, dict): continue
        asset_code = str(item.get("cod", "")).strip()
        asset = str(item.get("asset", "")).strip()
        typ = str(item.get("type", "")).strip()
        qty = str(item.get("theoricalQty", "")).strip()
        part = str(item.get("part", "")).strip()
        if not asset_code or not re.fullmatch(r"[A-Z0-9]{4,6}", asset_code): continue
        if not qty or not part: raise ValueError(f"campos obrigatorios ausentes para {asset_code}")
        rows.append({"index_code": code, "source_index_code": CODE_ALIAS.get(code, code), "reference_date": d.isoformat(), "asset_code": asset_code, "asset_name": asset, "asset_type": typ, "theoretical_quantity": qty.replace(".", "").replace(",", "."), "participation_pct": part.replace(".", "").replace(",", ".")})
    if not rows: raise ValueError("nenhum componente de carteira encontrado na API")
    assets = [r["asset_code"] for r in rows]
    if len(assets) != len(set(assets)): raise ValueError("duplicidade de ativo dentro da carteira")
    parts = [float(r["participation_pct"]) for r in rows]
    total = round(sum(parts), 3)
    if abs(total - 100.0) > 0.02: raise ValueError(f"soma de participacoes invalida: {total}")
    redutor = header.get("reductor") or header.get("redutor")
    return d, rows, total, redutor

def strip_html(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def parse_page(code, raw):
    html = raw.decode("utf-8", errors="replace")
    m = re.search(r"Carteira do Dia\s*[-–]\s*(\d{2}/\d{2}/\d{2})", html, re.I)
    if not m:
        raise ValueError("data de referencia nao encontrada")
    d = datetime.strptime(m.group(1), "%d/%m/%y").date()
    if d > TODAY:
        raise ValueError(f"data futura na fonte: {d.isoformat()} > {TODAY.isoformat()}")

    rows = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, flags=re.I | re.S):
        cells = [strip_html(x) for x in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, flags=re.I | re.S)]
        if len(cells) >= 5 and cells[0] not in ("Código", "Codigo", "Quantidade Teórica Total"):
            code0, asset, typ, qty, part = cells[:5]
            if re.fullmatch(r"[A-Z0-9]{4,6}", code0):
                rows.append({
                    "index_code": code,
                    "reference_date": d.isoformat(),
                    "asset_code": code0,
                    "asset_name": asset,
                    "asset_type": typ,
                    "theoretical_quantity": qty.replace(".", "").replace(",", "."),
                    "participation_pct": part.replace(".", "").replace(",", ".")
                })

    if not rows:
        raise ValueError("nenhum componente de carteira encontrado")

    assets = [r["asset_code"] for r in rows]
    if len(assets) != len(set(assets)):
        raise ValueError("duplicidade de ativo dentro da carteira")

    parts = [float(r["participation_pct"]) for r in rows]
    total = round(sum(parts), 3)
    if abs(total - 100.0) > 0.02:
        raise ValueError(f"soma de participacoes invalida: {total}")

    redutor = None
    rm = re.search(r"Redutor.*?([0-9][0-9\.,]+)", html, re.I | re.S)
    if rm:
        redutor = rm.group(1)

    return d, rows, total, redutor

def main():
    results = []
    failed = []
    captured_at = NOW.isoformat()

    for code in CODES:
        try:
            raw, api_obj, url = fetch(code)
            raw_sha = sha256_bytes(raw)
            ref_date, rows, total, redutor = parse_api(code, api_obj)

            raw_path = RAW_DIR / ref_date[:4] / f"{code}_{ref_date}.json"
            norm_path = NORM_DIR / ref_date[:4] / f"{code}_{ref_date}.csv"
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            norm_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_bytes(raw)

            with norm_path.open("w", newline="", encoding="utf-8") as f:
                fields = list(rows[0].keys())
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                w.writerows(rows)

            norm_sha = sha256_bytes(norm_path.read_bytes())
            manifest = {
                "schema_version": "1.0.0",
                "dataset": "INDICES_B3_COMPOSICAO_CARTEIRA",
                "index_code": code,
                "source": "B3",
                "source_url": url,
                "source_page_url": f"https://sistemaswebb3-listados.b3.com.br/indexPage/day/{CODE_ALIAS.get(code, code)}?language=pt-br",
                "captured_at": captured_at,
                "reference_date": ref_date.isoformat(),
                "raw_file": str(raw_path.relative_to(ROOT)).replace("\\","/"),
                "raw_sha256": raw_sha,
                "normalized_file": str(norm_path.relative_to(ROOT)).replace("\\","/"),
                "normalized_sha256": norm_sha,
                "rows": len(rows),
                "participation_sum_pct": total,
                "redutor": redutor,
                "duplicates": 0,
                "future_reference_date": False,
                "status": "VALIDADO",
                "fail_closed": True
            }
            mp = MAN_DIR / f"{code}_{ref_date}.json"
            mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            results.append(manifest)
        except Exception as e:
            failed.append({"index_code": code, "status": "REJEITADO", "error": str(e)})

    summary = {
        "schema_version": "1.0.0",
        "dataset": "INDICES_B3_COMPOSICAO_CARTEIRA",
        "source": "B3",
        "captured_at": captured_at,
        "requested_indices": CODES,
        "validated_count": len(results),
        "rejected_count": len(failed),
        "results": results,
        "rejected": failed,
        "status": "VALIDADO" if not failed and results else "REJEITADO",
        "fail_closed": True
    }
    (MAN_DIR / "INDICES_B3_quality.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if not failed:
        ref_dates = sorted({r["reference_date"] for r in results})
        current = {
            "schema_version": "1.0.0",
            "dataset_id": "INDICES_B3_COMPOSICAO_CARTEIRA",
            "status": "VIGENTE",
            "status_frescor": "VALIDADO",
            "source": "B3",
            "generated_at": captured_at,
            "reference_dates": ref_dates,
            "indices": [
                {
                    "index_code": r["index_code"],
                    "reference_date": r["reference_date"],
                    "normalized_file": r["normalized_file"],
                    "manifest": str((MAN_DIR / f'{r["index_code"]}_{r["reference_date"]}.json').relative_to(ROOT)).replace("\\","/")
                } for r in results
            ],
            "fail_closed": True
        }
        (OFF_DIR / "INDICES_B3_DATASET_ATUAL_V1.0.json").write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("INDICES_B3")
    print(f"VALIDADOS={len(results)}")
    print(f"REJEITADOS={len(failed)}")
    print(f"STATUS={summary['status']}")
    if failed:
        for x in failed:
            print(f"REJEITADO {x['index_code']}: {x['error']}")
        sys.exit(1)

if __name__ == "__main__":
    main()
