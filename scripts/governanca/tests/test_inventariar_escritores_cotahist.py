import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "inventariar_escritores_cotahist.py"
SPEC = importlib.util.spec_from_file_location("writer_audit", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class Tests(unittest.TestCase):
    def test_push(self):
        source = "permissions:\n  contents: write\nsteps:\n  - run: |\n      git add dados/cotahist/a.json\n      git commit -m update\n      git push origin HEAD:main\n"
        item = MODULE.classify(".github/workflows/cotahist-test.yml", source)
        self.assertEqual(item["classification"], "WRITER_EFFECTIVE")
        self.assertEqual(item["branch_target"], "main")
        self.assertIn("dados/cotahist/a.json", item["write_paths_static"])

    def test_conditional(self):
        source = "if: " + chr(36) + "{{ github.ref == 'refs/heads/main' }}\nsteps:\n  - run: git push origin HEAD:main\n"
        item = MODULE.classify(".github/workflows/cotahist-test.yml", source)
        self.assertEqual(item["classification"], "WRITER_CONDITIONAL")

    def test_permission_only_is_not_writer(self):
        source = "permissions:\n  contents: write\nsteps:\n  - run: python validate.py\n"
        item = MODULE.classify(".github/workflows/cotahist-test.yml", source)
        self.assertEqual(item["classification"], "VALIDATOR")
        self.assertFalse(item["write_mechanism"]["git_push"])

    def test_reference_only(self):
        item = MODULE.classify(".github/workflows/cotahist-reference.yml", 'steps:\n  - run: echo "dados/cotahist/normalized/anual"\n')
        self.assertEqual(item["classification"], "FALSE_POSITIVE")

    def test_validation_signal_is_validator(self):
        item = MODULE.classify(".github/workflows/cotahist-workflow.yml", "steps:\\n  - run: python scripts/ingestao/validar_cotahist.py\\n")
        self.assertEqual(item["classification"], "VALIDATOR")

    def test_secret_names_only(self):
        source = "env:\n  GH_TOKEN: " + chr(36) + "{{ secrets.B3_PUBLISH_TOKEN }}\nsteps:\n  - run: git push origin HEAD:main\n"
        item = MODULE.classify(".github/workflows/cotahist-test.yml", source)
        self.assertEqual(item["secret_reference_names"], ["B3_PUBLISH_TOKEN"])
        self.assertNotIn("secrets.B3_PUBLISH_TOKEN", json.dumps(item))

    def test_inline_concurrency_group_is_detected(self):
        source = """permissions: {contents: write}
concurrency: {group: cotahist-inline-group, cancel-in-progress: false}
steps:
  - run: |
      git add dados/cotahist/quality/EVIDENCE.json
      git push origin HEAD:main
"""
        item = MODULE.classify(".github/workflows/cotahist-inline-test.yml", source)
        self.assertEqual(item["concurrency_group"], "cotahist-inline-group")

    def test_resolves_static_shell_variables_and_loop_allowlists(self):
        source = """evidence="dados/cotahist/quality/EVIDENCE.json"
norm="dados/cotahist/normalized/anual/COTAHIST_A2015.csv"
for f in \\
  dados/cotahist/quality/ONE.json \\
  dados/cotahist/quality/TWO.json
do
  git add "$f"
done
git add "$evidence" "$norm"
git push origin HEAD:main
"""
        item = MODULE.classify(".github/workflows/cotahist-path-test.yml", source)
        self.assertIn("dados/cotahist/quality/ONE.json", item["write_paths_static"])
        self.assertIn("dados/cotahist/quality/TWO.json", item["write_paths_static"])
        self.assertIn("dados/cotahist/quality/EVIDENCE.json", item["write_paths_static"])
        self.assertIn("dados/cotahist/normalized/anual/COTAHIST_A2015.csv", item["write_paths_static"])
        self.assertEqual(item["write_paths_dynamic_or_broad"], [])

    def test_repository_has_no_uncontrolled_or_shared_static_writers(self):
        data = MODULE.run(Path.cwd())
        self.assertEqual(data["writer_without_concurrency_count"], 0, data["writer_without_concurrency"])
        self.assertEqual(data["shared_resource_count"], 0, data["shared_resources"])

    def test_inventory_does_not_write_to_repo(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workflows = root / ".github" / "workflows"
            workflows.mkdir(parents=True)
            (workflows / "cotahist-reference.yml").write_text("name: reference\non: workflow_dispatch\nsteps:\n  - run: echo neutral\n")
            data = MODULE.run(root)
            self.assertEqual(data["workflow_count"], 1)
            self.assertEqual(data["workflow_count"], 1)
            self.assertFalse((root / "docs").exists())

if __name__ == "__main__":
    unittest.main()
