from __future__ import annotations

import json
import py_compile
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GATE = ROOT / "scripts/governanca/validar_autorizacao_endpoint.py"


def run_gate(endpoint_id: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(GATE), "--endpoint-id", endpoint_id],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class AuthorizationGateTests(unittest.TestCase):
    def test_explicitly_prohibited_endpoint_is_blocked(self):
        result = run_gate("B3_PESQUISA_POR_PREGAO_API")
        self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["authorized"] is False)

    def test_unconfirmed_b3_endpoints_are_blocked(self):
        for endpoint in ("B3_BDI_TABLE_API", "B3_COTAHIST_DAILY", "B3_DRP_RAPINEGOCIOS", "BCB_COPOM_PDF_ATTACHMENT"):
            with self.subTest(endpoint=endpoint):
                result = run_gate(endpoint)
                self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
                self.assertFalse(json.loads(result.stdout)["authorized"])

    def test_bcb_open_data_api_is_allowed_with_conditions(self):
        result = run_gate("BCB_COPOM_API_JSON")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["authorized"])

    def test_unknown_endpoint_fails_closed(self):
        result = run_gate("ENDPOINT_NOT_REGISTERED")
        self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
        self.assertFalse(json.loads(result.stdout)["authorized"])

    def test_capture_scripts_compile_without_network_access(self):
        paths = (
            "scripts/governanca/validar_autorizacao_endpoint.py",
            "scripts/ingestao/importar_cotahist_diario_v1.py",
            "scripts/ingestao/capturar_bcb_copom_v2.py",
            "ferramentas/capturar_bdi.py",
            "ferramentas/importar_pesquisa_pregao.py",
        )
        for relative in paths:
            with self.subTest(path=relative):
                py_compile.compile(str(ROOT / relative), doraise=True)


if __name__ == "__main__":
    unittest.main()
