#!/usr/bin/env python3
"""Normalizador COTAHIST B3 — layout 245 bytes, registro 01."""

from __future__ import annotations

import argparse
import csv
import sys
import zipfile
from datetime import datetime
from decimal import Decimal
from pathlib import Path


PARSER_VERSION = "1.1.2"

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

HEADER = [field[0] for field in FIELDS]


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
        if value in {"", "00000000"}:
            return ""
        if len(value) != 8 or not value.isdigit():
            raise ValueError(f"data inválida: {value!r}")
        try:
            parsed = datetime.strptime(value, "%Y%m%d")
        except ValueError as exc:
            raise ValueError(f"data inválida: {value!r}") from exc
        return parsed.strftime("%Y-%m-%d")
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


def strip_line_ending(raw: bytes) -> bytes:
    """Remove apenas terminadores de linha CR/LF; nunca remove espaços de dados."""
    return raw.rstrip(b"\r\n")


def _hex_evidence(line: bytes, limit: int = 96) -> str:
    """Representação hexadecimal limitada, sem despejar linhas inteiras nos logs."""
    if len(line) <= limit:
        return line.hex(" ")
    head_size = limit // 2
    tail_size = limit - head_size
    return f"{line[:head_size].hex(' ')} ... {line[-tail_size:].hex(' ')}"


def normalize_line(line: bytes, line_number: int | None = None) -> list[str]:
    if len(line) != 245:
        record_type = line[:2].decode("ascii", errors="backslashreplace") or "<vazio>"
        line_label = str(line_number) if line_number is not None else "desconhecida"
        print(
            "COTAHIST_RECORD_LENGTH_MISMATCH "
            f"line_number={line_label} record_type={record_type!r} "
            f"observed_bytes={len(line)} expected_bytes=245 "
            f"hex={_hex_evidence(line)}",
            file=sys.stderr,
            flush=True,
        )
        raise ValueError(
            f"registro linha {line_label}, tipo {record_type!r}: "
            f"{len(line)} bytes; esperado 245; evidência hexadecimal emitida"
        )
    if line[:2] != b"01":
        raise ValueError("registro não é 01")
    return [parse_field(line[start - 1:end], kind) for _, start, end, kind in FIELDS]


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
        members = [name for name in zf.namelist() if not name.endswith("/")]
        if len(members) != 1:
            raise SystemExit(f"ZIP deve conter exatamente 1 arquivo: {members}")
        with zf.open(members[0]) as src, args.output.open("w", encoding="utf-8", newline="") as dst:
            writer = csv.writer(dst, lineterminator="\n")
            writer.writerow(HEADER)
            for line_number, raw in enumerate(src, start=1):
                line = strip_line_ending(raw)
                if line[:2] != b"01":
                    continue
                row = normalize_line(line, line_number=line_number)
                writer.writerow(row)
                quotes += 1
                date = row[0]
                first_date = date if first_date is None else min(first_date, date)
                last_date = date if last_date is None else max(last_date, date)

    print(f"NORMALIZADO: {args.output}")
    print(f"PARSER_VERSION={PARSER_VERSION}")
    print(f"COTACOES_01={quotes}")
    print(f"PRIMEIRA_DATA={first_date}")
    print(f"ULTIMA_DATA={last_date}")


if __name__ == "__main__":
    main()
