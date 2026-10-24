from __future__ import annotations

import unittest

from scripts.ingestao.gerar_dataset_oficial_cotahist_v2 import policy_exclusion_for_2026


class DatasetV2PolicyTests(unittest.TestCase):
    def test_2026_remains_excluded_when_integrity_is_valid_but_publication_is_not_authorized(self):
        result = policy_exclusion_for_2026(
            {"status": "BLOQUEADO", "ano": 2026},
            {
                "id": "B3_COTAHIST_DAILY",
                "authorization_status": "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED",
                "storage_and_redistribution": "REVIEW_REQUIRED_BEFORE_PUBLICATION",
                "publication_authorized": False,
            },
        )
        self.assertEqual(result["status"], "BLOQUEADO_AUTORIZACAO_FONTE")
        self.assertFalse(result["publication_authorized"])
        self.assertEqual(result["quality_manifest_status"], "BLOQUEADO")

    def test_even_authorized_2026_requires_a_versioned_scope_change(self):
        result = policy_exclusion_for_2026(
            {"status": "VALIDADO", "ano": 2026},
            {
                "id": "B3_COTAHIST_DAILY",
                "authorization_status": "AUTHORIZED",
                "storage_and_redistribution": "AUTHORIZED",
                "publication_authorized": True,
            },
        )
        self.assertEqual(result["status"], "EXCLUDED_BY_VERSION_SCOPE")


if __name__ == "__main__":
    unittest.main()
