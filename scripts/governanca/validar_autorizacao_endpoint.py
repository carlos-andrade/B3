#!/usr/bin/env python3
"""Gate fail-closed para autorização de endpoints do projeto B3.

Não testa nem consulta endpoints. Apenas lê o registo de autorização versionado.
Uma resposta HTTP positiva nunca é interpretada como prova de licença.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "docs/governanca/licenciamento/REGISTRO_AUTORIZACOES_ENDPOINTS_B3_2026-10-16.json"
ALLOWED = {"AUTHORIZED", "AUTHORIZED_WITH_CONDITIONS"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint-id", required=True)
    parser.add_argument("--allow-blocked", action="store_true",
                        help="Não falha o processo; escreve authorized=false para gates GitHub Actions.")
    parser.add_argument("--github-output", default="")
    args = parser.parse_args()

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    entries = {row["id"]: row for row in registry.get("endpoints", [])}
    row = entries.get(args.endpoint_id)
    if row is None:
        status, allowed, reason = "NOT_REGISTERED", False, "Endpoint ausente do registo; bloqueio por omissão."
    else:
        status = row.get("authorization_status", "NOT_REGISTERED")
        evidence = row.get("evidence") or []
        has_source = any(item.get("url") for item in evidence)
        allowed = status in ALLOWED and has_source
        reason = (
            "Registo de autorização permite a operação, sujeito às condições documentadas."
            if allowed else
            row.get("decision") or "Autorização não demonstrada; operação bloqueada."
        )

    print(json.dumps({
        "endpoint_id": args.endpoint_id,
        "authorization_status": status,
        "authorized": allowed,
        "reason": reason,
        "registry": str(REGISTRY.relative_to(ROOT)),
    }, ensure_ascii=False))

    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as output:
            output.write(f"authorized={'true' if allowed else 'false'}\n")
            output.write(f"authorization_status={status}\n")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as out:
            out.write(f"## Gate de autorização — {args.endpoint_id}\n\n")
            out.write(f"- Estado: **{status}**\n")
            out.write(f"- Captura autorizada: **{'SIM' if allowed else 'NÃO'}**\n")
            out.write(f"- Decisão: {reason}\n")
            out.write(f"- Registo: {REGISTRY.relative_to(ROOT)}\n")

    if not allowed and not args.allow_blocked:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
