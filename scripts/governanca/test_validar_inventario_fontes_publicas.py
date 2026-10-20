import unittest

from scripts.governanca.validar_inventario_fontes_publicas import validate


def source(source_id="A", **overrides):
    row = {
        "id": source_id,
        "provider": "Fonte",
        "domain": "mercado",
        "dataset": "Dados",
        "discovery_url": "https://example.gov.br/dados",
        "endpoint": "https://api.example.gov.br/dados",
        "access": "Público",
        "license": "ODbL confirmada no catálogo oficial",
        "automation_status": "AUTORIZADO_COM_CONDICOES",
        "capture_evidence": "https://example.gov.br/dados",
        "current_state": "A validar",
        "priority": "P1",
    }
    row.update(overrides)
    return row


def document(*rows):
    return {
        "schema_version": "1.0.0",
        "project": "B3",
        "repository": "carlos-andrade/B3",
        "sources": list(rows),
    }


class InventoryValidationTests(unittest.TestCase):
    def test_accepts_valid_source(self):
        self.assertEqual(validate(document(source())), [])

    def test_rejects_duplicate_ids(self):
        errors = validate(document(source("DUP"), source("DUP")))
        self.assertTrue(any("id duplicado" in error for error in errors))

    def test_rejects_non_https_endpoint(self):
        errors = validate(document(source(endpoint="http://example.gov.br/data")))
        self.assertTrue(any("endpoint deve ser URL HTTPS" in error for error in errors))

    def test_rejects_unknown_status(self):
        errors = validate(document(source(automation_status="FREE_ACCESS")))
        self.assertTrue(any("automation_status desconhecido" in error for error in errors))

    def test_blocked_source_requires_evidence(self):
        errors = validate(document(source(
            automation_status="BLOQUEADO_RESTRICAO_DOCUMENTADA",
            capture_evidence="",
            license="restrição explícita",
        )))
        self.assertTrue(any("precisa de URL de evidência" in error for error in errors))

    def test_authorized_source_cannot_have_unconfirmed_license(self):
        errors = validate(document(source(license="licença a confirmar")))
        self.assertTrue(any("contradiz o campo license" in error for error in errors))

    def test_requires_unique_fields(self):
        row = source()
        del row["dataset"]
        errors = validate(document(row))
        self.assertTrue(any("dataset" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
