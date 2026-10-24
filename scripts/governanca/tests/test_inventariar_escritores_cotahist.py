import importlib.util, json, tempfile, unittest
from pathlib import Path
SCRIPT=Path(__file__).resolve().parents[1]/"inventariar_escritores_cotahist.py"
SPEC=importlib.util.spec_from_file_location("writer_audit",SCRIPT)
MODULE=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)
class Tests(unittest.TestCase):
 def test_push(self):
  x=MODULE.classify(".github/workflows/cotahist-test.yml","permissions:\n  contents: write\nsteps:\n  - run: |\n      git add dados/cotahist/a.json\n      git commit -m update\n      git push origin HEAD:main\n")
  self.assertEqual(x["classification"],"WRITER_EFFECTIVE"); self.assertEqual(x["branch_target"],"main"); self.assertIn("dados/cotahist/a.json",x["write_paths_static"])
 def test_conditional(self):
  x=MODULE.classify(".github/workflows/cotahist-test.yml","if: \${{ github.ref == 'refs/heads/main' }}\nsteps:\n  - run: git push origin HEAD:main\n")
  self.assertEqual(x["classification"],"WRITER_CONDITIONAL")
 def test_permission_only(self):
  x=MODULE.classify(".github/workflows/cotahist-test.yml","permissions:\n  contents: write\nsteps:\n  - run: python validate.py\n")
  self.assertEqual(x["classification"],"VALIDATOR"); self.assertFalse(x["write_mechanism"]["git_push"])
 def test_reference_only(self):
  x=MODULE.classify(".github/workflows/cotahist-reference-check.yml",'steps:\n  - run: echo "dados/cotahist/normalized/anual"\n')
  self.assertEqual(x["classification"],"FALSE_POSITIVE")
 def test_secret_names_only(self):
  x=MODULE.classify(".github/workflows/cotahist-test.yml","env:\n  GH_TOKEN: \${{ secrets.B3_PUBLISH_TOKEN }}\nsteps:\n  - run: git push origin HEAD:main\n")
  self.assertEqual(x["secret_reference_names"],["B3_PUBLISH_TOKEN"]); self.assertNotIn("secrets.B3_PUBLISH_TOKEN",json.dumps(x))
 def test_read_only_no_mutation(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t); wf=root/".github/workflows"; wf.mkdir(parents=True); (wf/"cotahist-validator.yml").write_text("name: validator\non: workflow_dispatch\nsteps:\n  - run: echo validate\n")
   data=MODULE.run(root); self.assertEqual(data["workflow_count"],1); self.assertEqual(data["classification_counts"]["FALSE_POSITIVE"],1); self.assertFalse((root/"docs").exists())
if __name__=="__main__": unittest.main()
