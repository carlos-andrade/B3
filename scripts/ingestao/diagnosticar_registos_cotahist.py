#!/usr/bin/env python3
"""Diagnóstico read-only de comprimentos COTAHIST; não normaliza nem persiste dados."""

from __future__ import annotations

import io
import urllib.error
import urllib.request
import zipfile
from collections import Counter
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

BASE_URL = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist"
EXPECTED_LENGTH = 245


def scan_day(day):
    date_ref = day.strftime("%d%m%Y")
    name = f"COTAHIST_D{date_ref}"
    url = f"{BASE_URL}/{name}.ZIP"
    request = urllib.request.Request(
        url, headers={"User-Agent": "B3-repository-ingestion/1.1"}
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            archive = response.read()
    except urllib.error.HTTPError as exc:
        if exc.code in (404, 410):
            print(f"NO_FILE date={day.isoformat()} http={exc.code}")
            return 0
        raise

    counts = Counter()
    examples = []
    with zipfile.ZipFile(io.BytesIO(archive)) as zf:
        members = [name for name in zf.namelist() if not name.endswith("/")]
        if len(members) != 1:
            raise RuntimeError(f"ZIP inesperado para {day.isoformat()}: {members!r}")
        with zf.open(members[0]) as stream:
            for line_number, raw in enumerate(stream, start=1):
                line = raw.rstrip(b"\r\n")
                if line[:2] != b"01":
                    continue
                counts[len(line)] += 1
                if len(line) != EXPECTED_LENGTH and len(examples) < 10:
                    examples.append({
                        "date": day.isoformat(),
                        "line": line_number,
                        "length": len(line),
                        "prefix_hex": line[:12].hex(),
                        "suffix_hex": line[-12:].hex(),
                        "suffix_repr": repr(line[-12:]),
                        "byte_246_hex": line[245:246].hex(),
                        "byte_246_repr": repr(line[245:246]),
                    })
    print(f"SUMMARY date={day.isoformat()} lengths={dict(sorted(counts.items()))}")
    for example in examples:
        print("ANOMALOUS_RECORD " + repr(example))
    return sum(count for length, count in counts.items() if length != EXPECTED_LENGTH)


def main():
    today = datetime.now(ZoneInfo("America/Sao_Paulo")).date()
    anomalies = 0
    scanned = 0
    for offset in range(0, 8):
        day = today - timedelta(days=offset)
        try:
            anomalies += scan_day(day)
            scanned += 1
        except urllib.error.URLError as exc:
            print(f"FETCH_ERROR date={day.isoformat()} error={exc!r}")
            raise
    print(f"DIAGNOSTIC_COMPLETE days_scanned={scanned} anomalous_records={anomalies}")
    print("READ_ONLY=true publication=false normalization=false")


if __name__ == "__main__":
    main()
