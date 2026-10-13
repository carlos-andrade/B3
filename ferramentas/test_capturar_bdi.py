import datetime as dt
import unittest

from ferramentas.capturar_bdi import candidate_dates


class CaptureBDITests(unittest.TestCase):
    def test_auto_search_starts_with_previous_day_and_goes_back_seven_days(self):
        dates = candidate_dates("auto", today=dt.date(2026, 10, 13))
        self.assertEqual(dates[0], dt.date(2026, 10, 12))
        self.assertEqual(dates[-1], dt.date(2026, 10, 6))
        self.assertEqual(len(dates), 7)

    def test_explicit_date_is_not_changed(self):
        dates = candidate_dates("2026-09-22", today=dt.date(2026, 10, 13))
        self.assertEqual(dates, [dt.date(2026, 9, 22)])

    def test_invalid_explicit_date_is_rejected(self):
        with self.assertRaises(ValueError):
            candidate_dates("22-09-2026", today=dt.date(2026, 10, 13))


if __name__ == "__main__":
    unittest.main()
