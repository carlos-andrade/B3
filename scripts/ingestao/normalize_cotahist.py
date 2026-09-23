#!/usr/bin/env python3
"""Normalizador COTAHIST B3 — layout 245 bytes, registro 01."""

from __future__ import annotations

import argparse
import csv
import io
import zipfile
from decimal import Decimal
from pathlib import Path


FIELDS = [
    ("data_pregao", 3, 10, "date"),
    ("codbdi", 11, 12, "str"),
    ("codneg", 13, 24, "str"),
    ("tpmerc", 25, 27, "str"),
    ("nomres", 28, 39, "str"),
    ("especi", 40, 49, "str"),
    ("prazot", 50, 52, "str"),
    ("modref", 53, 56, "str"),
    ("preabe", 57, 69, "price"),
    ("premax", 70, 82, "price"),
    ("premin", 83, 95, "price"),
    ("premed", 96, 108, "price"),
    ("preult", 109, 121, "price"),
    ("preofc", 122, 134, "price"),
    ("preofv", 135, 147, "price"),
    ("totneg", 148, 152, "int"),
    ("quatot", 153, 170, "int"),
    ("voltot", 171, 188, "money"),
    ("preexe", 189, 201, "price"),
    ("indopc", 202, 202, "str"),
    ("datven", 203, 210, "date"),
    ("fatcot", 211, 217, "int"),
    ("ptoexe", 218, 230, "price6"),
    ("codisi", 231, 242, "str"),
    ("dismes", 243, 245, "str"),
]

HEADER = [
    "data_pregao", "codbdi", "codneg", "tpmerc", "nomres", "especi",
    "prazot", "modref", "preabe", "premax", "premin", "premed", "preult",
    "preofc", "preofv", "totneg", "quatot", "voltot", "preexe", "indopc",
    "datven", "fatcot", "ptoexe", "codisi", "dismes",
]


def clean(raw: bytes) -> str:
    return raw.decode("latin-1").strip()


def numeric(raw: bytes, scale: int) -> str:
    value = raw.decode("ascii", "strict").strip()
    if not value:
        return ""
    return str(Decimal(value) / (Decimal(10) ** scale))


def parse_field(raw: bytes, kind: str) -> str:
    if kind == "str":
        return clean(raw)
    if kind == "date":
        value = clean(raw)
        return "" if value in {"", "00000000"} else f"{value[:4]}-{value[4:6]}-{value[6:8]}"
    if kind == "price":
        return numeric(raw, 2)
    if kind == "money":
        return numeric(raw, 2)
    if kind == "price6":
        return numeric(raw, 6)
    if kind == "int":
        value = clean(raw)
        return "" if not value else str(int(value))
    raise ValueError(kind)


def normalize_line(line: bytes) -> list[str]:
    if len(line) != 245:
        raise ValueError(f"registro com {len(line)} bytes; esperado 245")
    if line[:2] != b"01":
        raise ValueError("registro não é 01")
    values = []
    for _, start, end, kind in FIELDS:
        values.append(parse_field(line[start - 1:end], kind))
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    quotes = 0
    first_date = None
    last_date = None

    with zipfile.ZipFile(args.zip) as zf:
        members = [n for n in zf.namelist() if not n.endswith("/")]
        if len(members) != 1:
            raise SystemExit(f"ZIP deve conter exatamente 1 arquivo: {members}")
        with zf.open(members[0]) as src, args.output.open("w", encoding="utf-8", newline="") as dst:
            writer = csv.writer(dst, lineterminator="\n")
            writer.writerow(HEADER)
            for raw in src:
                line = raw.rstrip(b"\r\n")
                if line[:2] != b"01":
                    continue
                row = normalize_line(line)
                writer.writerow(row)
                quotes += 1
                d = row[0]
                first_date = d if first_date is None else min(first_date, d)
                last_date = d if last_date is None else max(last_date, d)

    print(f"NORMALIZADO: {args.output}")
    print(f"COTACOES_01={quotes}")
    print(f"PRIMEIRA_DATA={first_date}")
    print(f"ULTIMA_DATA={last_date}")


if __name__ == "__main__":
    main()
