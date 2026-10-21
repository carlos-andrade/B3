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
ALLOWED = {"AUTHORIZED", "AUTHORIZED_WITH_CONDITIONS", "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED"}


def authorization_decision(row: dict | None) -> tuple[str, bool, str]:
    if row is None:
        return "NOT_REGISTERED", False, "Endpoint ausente do registo; bloqueio por omissão."

    status = row.get("authorization_status", "NOT_REGISTERED")
    evidence = row.get("evidence") or []

    if status == "OFFICIAL_DIRECT_FILE_CHANNEL_SCOPE_LIMITED":
        # Decisão operacional limitada; não equivale a licença nem autoriza publicação/redistribuição.
        decision = str(row.get("decision") or "")
        limits = row.get("scope_limits") or []
        has_internal_scope = (
            row.get("automated_collection") == "ALLOW_CONTROLLED_ACQUISITION_FOR_VALIDATION"
            and row.get("storage_and_redistribution") == "REVIEW_REQUIRED_BEFORE_PUBLICATION"
            and any("validação técnica" in str(item).lower() or "processamento interno" in str(item).lower()
                    for item in limits)
            and any("não" in str(item).lower() and ("publicar" in str(item).lower() or "redistribuir" in str(item).lower())
                    for item in limits)
            and "não presumir" in decision.lower()
        )
        allowed = bool(has_internal_scope)
        reason = (
            "Aquisição controlada permitida apenas para validação técnica/processamento interno; publicação e redistribuição continuam bloqueadas."
            if allowed else
            "Âmbito operacional limitado sem controlos completos no registo; bloqueio por omissão."
        )
        return status, allowed, reason

    if status == "AUTHORIZED_WITH_CONDITIONS":
        valid_open_license = any(
            item.get("type") == "official_open_data_license"
            and item.get("url")
            and item.get("license_name")
            and item.get("scope")
            for item in evidence
        )
        allowed = bool(valid_open_license)
        reason = (
            "Licença aberta oficial identificada; cumprir as condições e limitar o uso ao âmbito declarado."
            if allowed else
            "Licença aberta oficial sem evidência completa de licença, URL e âmbito; bloqueio por omissão."
        )
        return status, allowed, reason

    if status == "AUTHORIZED":
        approval = row.get("approval") or {}
        valid_approval = all(approval.get(key) for key in (
            "reference", "approved_by", "approved_at", "valid_until", "scope", "evidence_sha256"
        ))
        valid_approval = valid_approval and any(
            item.get("type") in {"contract", "written_authorization", "license_agreement"}
            and item.get("url")
            for item in evidence
        )
        allowed = bool(valid_approval)
        reason = (
            "Autorização contratual/escrita com escopo, validade e hash de evidência registados."
            if allowed else
            "Estado AUTHORIZED sem aprovação contratual/escrita completa e evidência identificável; bloqueio por omissão."
        )
        return status, allowed, reason

    return status, False, row.get("decision") or "Autorização não demonstrada; operação bloqueada."


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
    status, allowed, reason = authorization_decision(row)

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
