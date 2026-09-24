#!/usr/bin/env python3
"""Skeleton validator for B3 Negocio a Negocio trade files.

The implementation deliberately refuses to invent aggressor side.
Layout-specific field mappings must be supplied only after the official
B3 file/layout is identified and captured.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path

REQUIRED = [
    "trading_date",
    "timestamp",
    "instrument",
    "ticker",
    "contract",
    "price",
    "quantity",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_csv(path: Path) -> tuple[int, list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        missing = [x for x in REQUIRED if x not in fields]
        if missing:
            return 0, [f"MISSING_FIELD={x}" for x in missing]
        rows = 0
        for row in reader:
            rows += 1
            for field in REQUIRED:
                if row.get(field) in (None, ""):
                    return rows, [f"EMPTY_REQUIRED_FIELD={field}"]
        return rows, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", type=Path)
    args = ap.parse_args()

    for path in args.files:
        if not path.exists():
            raise SystemExit(f"FILE_NOT_FOUND={path}")
        print(f"FILE={path}")
        print(f"SHA256={sha256(path)}")
        if path.suffix.lower() == ".csv":
            rows, errors = validate_csv(path)
            print(f"ROWS={rows}")
            for error in errors:
                print(error)
        else:
            print("FORMAT_VALIDATION=DEFERRED_UNTIL_OFFICIAL_LAYOUT_IS_IDENTIFIED")

    print("AGGRESSOR_SIDE=DO_NOT_INFER")
    print("CUMULATIVE_DELTA=CALCULATE_ONLY_AFTER_DEFENSIBLE_AGGRESSOR_CLASSIFICATION")


if __name__ == "__main__":
    main()
