import json
import unittest
from datetime import date
from io import BytesIO
from unittest.mock import patch

from scripts.ingestao.importar_ptax_bcb import PtaxError, build_url, get_payload


class PtaxCaptureTests(unittest.TestCase):
    def test_build_url_uses_official_odata_and_date_aliases(self):
        url = build_url("EUR", date(2026, 10, 1), date(2026, 10, 20))
        self.assertTrue(url.startswith("https://olinda.bcb.gov.br/"))
        self.assertIn("CotacaoMoedaPeriodo", url)
        self.assertIn("%40moeda=%27EUR%27", url)
        self.assertIn("01-10-2026", url)
        self.assertIn("10-20-2026", url)

    def test_rejects_unknown_currency(self):
        with self.assertRaises(PtaxError):
            build_url("GBP", date(2026, 10, 1), date(2026, 10, 2))

    def test_rejects_period_over_45_days(self):
        with self.assertRaises(PtaxError):
            build_url("USD", date(2026, 1, 1), date(2026, 3, 1))

    def test_validates_json_payload_and_required_fields(self):
        raw = json.dumps({"value": [{
            "dataHoraCotacao": "2026-10-20 13:00:00.000",
            "cotacaoCompra": 5.4,
            "cotacaoVenda": 5.5,
        }]}).encode("utf-8")
        with patch("scripts.ingestao.importar_ptax_bcb.urllib.request.urlopen", return_value=BytesIO(raw)):
            returned, payload = get_payload("https://olinda.bcb.gov.br/test")
        self.assertEqual(returned, raw)
        self.assertEqual(len(payload["value"]), 1)

    def test_rejects_empty_observations(self):
        raw = b'{"value":[]}'
        with patch("scripts.ingestao.importar_ptax_bcb.urllib.request.urlopen", return_value=BytesIO(raw)):
            with self.assertRaises(PtaxError):
                get_payload("https://olinda.bcb.gov.br/test")

    def test_rejects_nonofficial_host(self):
        with self.assertRaises(PtaxError):
            get_payload("https://example.com/ptax")


if __name__ == "__main__":
    unittest.main()
