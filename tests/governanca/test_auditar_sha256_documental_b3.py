from __future__ import annotations

import sys
import unittest
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "governanca"))

from auditar_sha256_documental_b3 import canonical_digest, read_status


class CanonicalDigestTests(unittest.TestCase):
    def test_excludes_only_two_control_lines(self) -> None:
        text = (
            "# Título\n\n"
            "| Campo | Valor |\n|---|---|\n"
            "| **ID** | X |\n"
            "| **SHA-256 (conteúdo canónico)** | PENDENTE |\n"
            "| **Commit de referência (versão anterior)** | N/A |\n"
            "| **Estado** | RASCUNHO |\n\n"
            "## Corpo\ntexto\n"
        )
        self.assertEqual(
            canonical_digest(text),
            "60a240eb8789c434e0cd29249cf5f559b4939b0f54988b214e9384e3a9a066b4",
        )

    def test_bom_and_crlf_are_normalized(self) -> None:
        base = (
            "# Título\n\n| Campo | Valor |\n|---|---|\n"
            "| **ID** | X |\n"
            "| **SHA-256 (conteúdo canónico)** | PENDENTE |\n"
            "| **Commit de referência (versão anterior)** | N/A |\n"
            "| **Estado** | RASCUNHO |\n\n## Corpo\ntexto\n"
        )
        converted = "\ufeff" + base.replace("\n", "\r\n")
        self.assertEqual(canonical_digest(converted), canonical_digest(base))


    def test_pending_status_exposes_calculated_digest(self) -> None:
        content = (
            "# Título\\n\\n| Campo | Valor |\\n|---|---|\\n"
            "| **ID** | X |\\n"
            "| **SHA-256 (conteúdo canónico)** | PENDENTE |\\n"
            "| **Commit de referência (versão anterior)** | N/A |\\n"
            "| **Estado** | RASCUNHO |\\n\\n## Corpo\\ntexto\\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pending.md"
            path.write_text(content, encoding="utf-8")
            result = read_status(path)
        self.assertEqual(result["status"], "PENDENTE")
        self.assertEqual(result["calculated"], canonical_digest(content))

    def test_missing_control_line_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            canonical_digest("# Sem tabela\n")


if __name__ == "__main__":
    unittest.main()
