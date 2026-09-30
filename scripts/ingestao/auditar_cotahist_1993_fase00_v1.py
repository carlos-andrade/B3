import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "dados/cotahist/quality/COTAHIST_1993_FASE00_GOVERNANCA_PRE_CONDICOES_V1.json"

REQUIRED = [
    "docs/cotahist/WORKFLOW_ORDEM_E_DEPENDENCIAS_V1.md",
    "docs/cotahist/WORKFLOW_CATALOGO_V1.json",
    "docs/cotahist/MATRIZ_DEPENDENCIAS_COTAHIST_V1.md",
    "dados/cotahist/manifests/COTAHIST_A1993.json",
    "dados/cotahist/checksums/COTAHIST_A1993.ZIP.sha256",
]

checks = {p: (ROOT / p).is_file() for p in REQUIRED}
missing = [p for p, ok in checks.items() if not ok]

out = {
    "schema_version": "1.0.0",
    "ano": 1993,
    "phase": "FASE00",
    "status": "VALIDADO" if not missing else "BLOQUEADO",
    "natureza": "governanca_e_pre_condicoes",
    "escopo": "COTAHIST anual 1993",
    "fonte_esperada": "B3",
    "pipeline_canonico": "00->01->02->03->04->05->06->07->08->09->10->11->12",
    "checks": checks,
    "missing": missing,
    "criterio": "A fase 00 confirma que a governanca, a ordem canonica e a identificacao da fonte/ano estao documentadas antes da promocao das fases de dados.",
    "decision": "VALIDADO" if not missing else "BLOQUEADO",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, ensure_ascii=False))
if missing:
    raise SystemExit(1)
