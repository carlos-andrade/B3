from __future__ import annotations

import json
import py_compile
import subprocess
import sys
import unittest
from pathlib import Path

from scripts.governanca.validar_autorizacao_endpoint import authorization_decision

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
        for endpoint in ("B3_BDI_TABLE_API", "B3_DRP_RAPINEGOCIOS", "BCB_COPOM_PDF_ATTACHMENT"):
            with self.subTest(endpoint=endpoint):
                result = run_gate(endpoint)
                self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
                self.assertFalse(json.loads(result.stdout)["authorized"])

    def test_cotahist_direct_file_allows_only_limited_internal_validation(self):
        result = run_gate("B3_COTAHIST_DAILY")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["authorized"])
        self.assertEqual(payload["authorization_status"], "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED")
        self.assertEqual(payload["operation_scope"], "INTERNAL_VALIDATION_ONLY")
        self.assertFalse(payload["publication_authorized"])

    def test_limited_scope_without_required_controls_fails_closed(self):
        cases = [
            {
                "id": "FAKE_LIMITED_NO_AUTOMATION_CONTROL",
                "authorization_status": "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED",
                "storage_and_redistribution": "REVIEW_REQUIRED_BEFORE_PUBLICATION",
                "decision": "permitir aquisição limitada; não presumir autorização de publicação",
                "scope_limits": ["Aquisição limitada para validação técnica e processamento interno.",
                                 "Não publicar novo RAW nem redistribuir o ficheiro até os termos aplicáveis estarem documentados."]
            },
            {
                "id": "FAKE_LIMITED_NO_STORAGE_CONTROL",
                "authorization_status": "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED",
                "automated_collection": "ALLOW_CONTROLLED_ACQUISITION_FOR_VALIDATION",
                "decision": "permitir aquisição limitada; não presumir autorização de publicação",
                "scope_limits": ["Aquisição limitada para validação técnica e processamento interno.",
                                 "Não publicar novo RAW nem redistribuir o ficheiro até os termos aplicáveis estarem documentados."]
            },
            {
                "id": "FAKE_LIMITED_NO_PUBLICATION_LIMIT",
                "authorization_status": "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED",
                "automated_collection": "ALLOW_CONTROLLED_ACQUISITION_FOR_VALIDATION",
                "storage_and_redistribution": "REVIEW_REQUIRED_BEFORE_PUBLICATION",
                "decision": "permitir aquisição limitada; não presumir autorização de publicação",
                "scope_limits": ["Aquisição limitada para validação técnica e processamento interno."]
            },
            {
                "id": "FAKE_LIMITED_NO_NON_PRESUMPTION",
                "authorization_status": "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED",
                "automated_collection": "ALLOW_CONTROLLED_ACQUISITION_FOR_VALIDATION",
                "storage_and_redistribution": "REVIEW_REQUIRED_BEFORE_PUBLICATION",
                "decision": "aquisição e publicação autorizadas",
                "scope_limits": ["Aquisição limitada para validação técnica e processamento interno.",
                                 "Não publicar novo RAW nem redistribuir o ficheiro até os termos aplicáveis estarem documentados."]
            },
        ]
        for row in cases:
            with self.subTest(endpoint=row["id"]):
                status, allowed, _ = authorization_decision(row)
                self.assertEqual(status, "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED")
                self.assertFalse(allowed)

    def test_limited_scope_requires_all_controls_to_allow_internal_validation(self):
        status, allowed, reason = authorization_decision({
            "id": "FAKE_LIMITED_VALID",
            "authorization_status": "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED",
            "automated_collection": "ALLOW_CONTROLLED_ACQUISITION_FOR_VALIDATION",
            "storage_and_redistribution": "REVIEW_REQUIRED_BEFORE_PUBLICATION",
            "decision": "permitir aquisição limitada; não presumir autorização de publicação",
            "scope_limits": ["Aquisição limitada para validação técnica e processamento interno.",
                             "Não publicar novo RAW nem redistribuir o ficheiro até os termos aplicáveis estarem documentados."]
        })
        self.assertEqual(status, "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED")
        self.assertTrue(allowed)
        self.assertIn("publicação e redistribuição continuam bloqueadas", reason)

    def test_bcb_open_data_api_is_allowed_with_conditions(self):
        result = run_gate("BCB_COPOM_API_JSON")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["authorized"])

    def test_bcb_sgs_is_allowed_only_with_dynamic_series_preflight(self):
        result = run_gate("BCB_SGS_API")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["authorized"])
        self.assertEqual(payload["authorization_status"], "AUTHORIZED_WITH_CONDITIONS")

    def test_unknown_endpoint_fails_closed(self):
        result = run_gate("ENDPOINT_NOT_REGISTERED")
        self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
        self.assertFalse(json.loads(result.stdout)["authorized"])

    def test_authorized_status_without_contract_evidence_still_blocks(self):
        status, allowed, _ = authorization_decision({
            "id": "FAKE_B3_ENDPOINT",
            "authorization_status": "AUTHORIZED",
            "evidence": [{"type": "technical_source", "url": "https://example.invalid"}],
        })
        self.assertEqual(status, "AUTHORIZED")
        self.assertFalse(allowed)

    def test_open_license_requires_explicit_license_and_scope(self):
        status, allowed, _ = authorization_decision({
            "id": "FAKE_OPEN_DATA",
            "authorization_status": "AUTHORIZED_WITH_CONDITIONS",
            "evidence": [{
                "type": "official_open_data_license",
                "url": "https://example.invalid/license",
                "license_name": "ODbL",
                "scope": "JSON dataset",
            }],
        })
        self.assertEqual(status, "AUTHORIZED_WITH_CONDITIONS")
        self.assertTrue(allowed)

    def test_capture_scripts_compile_without_network_access(self):
        paths = (
            "scripts/governanca/validar_autorizacao_endpoint.py",
            "scripts/governanca/validar_licenca_bcb_sgs.py",
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
