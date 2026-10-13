import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path

from WATCHDOG.engine.check_data_freshness import evaluate, evaluate_dataset


class DataFreshnessTests(unittest.TestCase):
    def test_recent_observation_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sample.json").write_text(json.dumps({"date": "2026-10-12"}), encoding="utf-8")
            entry = {"id": "D1", "name": "Sample", "kind": "json_field",
                     "manifest_path": "sample.json", "date_field": "date", "max_age_days": 2}
            result = evaluate_dataset(entry, root, dt.date(2026, 10, 13))
            self.assertEqual(result["state"], "PASS")
            self.assertEqual(result["age_days"], 1)

    def test_stale_observation_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sample.json").write_text(json.dumps({"date": "2026-09-01"}), encoding="utf-8")
            entry = {"id": "D1", "name": "Sample", "kind": "json_field",
                     "manifest_path": "sample.json", "date_field": "date", "max_age_days": 5}
            result = evaluate_dataset(entry, root, dt.date(2026, 10, 13))
            self.assertEqual(result["state"], "STALE")

    def test_ingestion_timestamp_is_not_market_date(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "sample.json").write_text(json.dumps({"acquired_at_utc": "2026-10-13T00:00:00Z"}), encoding="utf-8")
            entry = {"id": "D1", "name": "Sample", "kind": "json_field",
                     "manifest_path": "sample.json", "date_field": "observation_date",
                     "acquired_at_field": "acquired_at_utc", "max_age_days": 5}
            result = evaluate_dataset(entry, root, dt.date(2026, 10, 13))
            self.assertEqual(result["state"], "UNKNOWN")
            self.assertEqual(result["observation_date"], None)
            self.assertEqual(result["acquired_at"], "2026-10-13T00:00:00Z")

    def test_glob_selects_latest_market_observation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifests = root / "manifests"
            manifests.mkdir()
            (manifests / "older.json").write_text(json.dumps({"ultima_data": "2026-10-08"}), encoding="utf-8")
            (manifests / "newer.json").write_text(json.dumps({"ultima_data": "2026-10-12"}), encoding="utf-8")
            entry = {"id": "D2", "name": "Daily data", "kind": "glob_json_date",
                     "glob": "manifests/*.json", "date_field": "ultima_data", "max_age_days": 2}
            result = evaluate_dataset(entry, root, dt.date(2026, 10, 13))
            self.assertEqual(result["state"], "PASS")
            self.assertEqual(result["observation_date"], "2026-10-12")
            self.assertEqual(result["source"], "manifests/newer.json")

    def test_duplicate_dataset_ids_are_rejected(self):
        entry = {"id": "D1", "name": "Sample", "kind": "json_field",
                 "manifest_path": "sample.json", "date_field": "date", "max_age_days": 2}
        with self.assertRaises(ValueError):
            evaluate({"schema_version": 1, "datasets": [entry, entry]}, Path("."), dt.date(2026, 10, 13))

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            entry = {"id": "D1", "name": "Sample", "kind": "json_field",
                     "manifest_path": "../outside.json", "date_field": "date", "max_age_days": 2}
            with self.assertRaises(ValueError):
                evaluate_dataset(entry, root, dt.date(2026, 10, 13))


if __name__ == "__main__":
    unittest.main()
