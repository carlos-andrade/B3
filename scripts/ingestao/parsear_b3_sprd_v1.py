#!/usr/bin/env python3
"""Parser/validator for B3 SPRD ZIP files.

Scope: derivatives historical PriceReport (BVBG.187.01), with special
attention to WIN, WDO and DI contracts. This parser does not infer
aggressor side or Cumulative Delta from EOD data.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import re
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

TICKER_RE = re.compile(r"^(WIN|WDO|DI1)", re.IGNORECASE)
FIELDS = ["trading_date", "instrument", "ticker", "price", "quantity", "financial_volume", "source_file"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def walk_zip(zf: zipfile.ZipFile, prefix: str = ""):
    for name in zf.namelist():
        if name.endswith("/"):
            continue
        data = zf.read(name)
        yield prefix + name, data


def flatten_xml(data: bytes):
    root = ET.fromstring(data)
    for elem in root.iter():
        yield elem


def text_of(elem, names):
    wanted = set(names)
    for child in elem.iter():
        if local(child.tag) in wanted and child.text:
            return child.text.strip()
    return None


def parse_xml(name: str, data: bytes):
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return []
    rows = []
    # PriceReport structures vary by version; locate repeating instrument/trade-like nodes.
    candidates = [e for e in root.iter() if local(e.tag) in {"PricRpt", "FinInstrm", "InstrmInf", "TradData"}]
    if not candidates:
        candidates = [root]
    for e in candidates:
        ticker = text_of(e, {"TckrSymb", "TckrSymbId", "Symb"})
        if not ticker or not TICKER_RE.match(ticker):
            continue
        rows.append({
            "trading_date": text_of(e, {"TradDt", "TradeDate"}),
            "instrument": ticker[:3].upper(),
            "ticker": ticker,
            "price": text_of(e, {"LastPric", "LastPx", "LastPrice", "ClsPric"}),
            "quantity": text_of(e, {"TradQty", "TradedQty", "Qty"}),
            "financial_volume": text_of(e, {"FinInstrmQty", "FinVol", "FinancialVolume"}),
            "source_file": name,
        })
    return rows


def extract_recursive(data: bytes, name: str):
    out = []
    if zipfile.is_zipfile(io.BytesIO(data)):
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            for child_name, child_data in walk_zip(zf, prefix=name + "!"):
                out.extend(extract_recursive(child_data, child_name))
    elif name.lower().endswith(".xml"):
        out.extend(parse_xml(name, data))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_files", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, default=Path("dados/calendario_economico/normalized/b3_sprd_copom_2026.csv"))
    args = ap.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)
    retrieved_at = datetime.now(timezone.utc).isoformat()

    rows = []
    for path in args.zip_files:
        if not path.exists():
            raise SystemExit(f"FILE_NOT_FOUND={path}")
        if not zipfile.is_zipfile(path):
            raise SystemExit(f"ZIP_INVALID={path}")
        rows.extend(extract_recursive(path.read_bytes(), path.name))

    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"RETRIEVED_AT={retrieved_at}")
    for path in args.zip_files:
        print(f"SHA256 {path} {sha256(path)}")
    print(f"ROWS={len(rows)}")
    print(f"OUT={args.out}")
    print("AGGRESSOR_SIDE=NOT_AVAILABLE_FROM_SPRD_EOD")
    print("CUMULATIVE_DELTA=NOT_AVAILABLE_FROM_SPRD_EOD")


if __name__ == "__main__":
    main()
