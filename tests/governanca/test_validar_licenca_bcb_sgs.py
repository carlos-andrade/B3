from __future__ import annotations

import unittest

from scripts.governanca.validar_licenca_bcb_sgs import verify_series


def search_with(datasets):
    def fake(term):
        return {"results": datasets}
    return fake


class BcbSgsLicenseTests(unittest.TestCase):
    def test_exact_series_with_odbl_is_allowed(self):
        datasets = [{
            "name": "432-taxa-de-juros---meta-selic-definida-pelo-copom",
            "title": "Meta Selic",
            "license_id": "odc-odbl",
            "license_title": "Open Data Commons Open Database License",
            "resources": [{
                "name": "json_serie-sgs-432",
                "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json",
            }],
        }]
        result = verify_series(432, search_with(datasets))
        self.assertTrue(result["authorized"])
        self.assertEqual(result["license"], "ODbL")

    def test_public_url_without_open_license_is_blocked(self):
        datasets = [{
            "name": "series-432",
            "license_id": "other",
            "resources": [{
                "name": "json_serie-sgs-432",
                "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json",
            }],
        }]
        result = verify_series(432, search_with(datasets))
        self.assertFalse(result["authorized"])

    def test_license_without_exact_series_resource_is_blocked(self):
        datasets = [{
            "name": "unrelated",
            "license_id": "odc-odbl",
            "resources": [{
                "name": "json_serie-sgs-433",
                "url": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json",
            }],
        }]
        result = verify_series(432, search_with(datasets))
        self.assertFalse(result["authorized"])

    def test_catalog_failure_is_blocked(self):
        def broken(term):
            raise RuntimeError("offline")
        result = verify_series(432, broken)
        self.assertFalse(result["authorized"])
        self.assertGreaterEqual(len(result["errors"]), 2)


if __name__ == "__main__":
    unittest.main()
