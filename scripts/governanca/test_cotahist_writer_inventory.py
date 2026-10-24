from __future__ import annotations

import unittest
from pathlib import Path

from scripts.governanca.auditar_workflows_b3 import classify_cotahist_writer


class CotahistWriterInventoryTests(unittest.TestCase):
    def test_classifies_main_writer_and_resources(self):
        workflow = Path(".github/workflows/cotahist-test-writer.yml")
        text = """
permissions:
  contents: write
concurrency:
  group: b3-cotahist-main-publish-${{ github.ref }}
  cancel-in-progress: false
steps:
  - run: |
      git add dados/cotahist/oficial/dataset.json
      git commit -m publish
      git push origin HEAD:main
"""
        result = classify_cotahist_writer(workflow, text)
        self.assertIsNotNone(result)
        self.assertEqual(result["classification"], "REPO_WRITER")
        self.assertEqual(result["branch_target"], "main")
        self.assertIn("dados/cotahist/oficial/dataset.json", result["write_paths"])
        self.assertIn("b3-cotahist-main-publish", result["concurrency_group"])

    def test_classifies_read_only_workflow(self):
        result = classify_cotahist_writer(
            Path(".github/workflows/cotahist-read-only.yml"),
            "permissions:\n  contents: read\njobs:\n  inspect:\n    steps:\n      - run: python scripts/check.py\n",
        )
        self.assertIsNotNone(result)
        self.assertEqual(result["classification"], "READ_ONLY_OR_ARTIFACT_ONLY")
        self.assertEqual(result["branch_target"], "NONE")


if __name__ == "__main__":
    unittest.main()
