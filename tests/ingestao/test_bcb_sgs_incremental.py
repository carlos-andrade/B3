from __future__ import annotations

import csv
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.ingestao.importar_bcb_sgs_nucleo_macro_v1 import (
    incremental_window,
    load_existing_normalized,
)


class SgsIncrementalTests(unittest.TestCase):
    def test_window_rechecks_seven_days_before_latest_past_observation(self):
        start = date(1986, 1, 1)
        end = date(2026, 10, 16)
        result = incremental_window(start, end, [date(2026, 10, 10), date(2026, 10, 15)])
        self.assertEqual(result, date(2026, 10, 8))

    def test_first_run_uses_configured_historical_start(self):
        start = date(1984, 11, 28)
        end = date(2026, 10, 16)
        self.assertEqual(incremental_window(start, end, []), start)

    def test_existing_normalized_file_is_read_without_changing_dates_or_values(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "SGS_1.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(["codigo_sgs", "data", "valor"])
                writer.writerow([1, "2026-10-15", "5.4321"])
            rows, dates = load_existing_normalized(path)
            self.assertEqual(dates, [date(2026, 10, 15)])
            self.assertEqual(rows[0]["data"], "15/10/2026")
            self.assertEqual(rows[0]["valor"], "5.4321")

    def test_invalid_normalized_schema_fails_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "SGS_1.csv"
            path.write_text("date,value\n2026-10-15,5.4\n", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                load_existing_normalized(path)


if __name__ == "__main__":
    unittest.main()
