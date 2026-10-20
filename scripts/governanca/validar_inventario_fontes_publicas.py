#!/usr/bin/env python3
"""Validador estrutural do inventário de fontes públicas gratuitas B3.

Não declara licenças nem consulta endpoints. Valida apenas a qualidade e
consistência do registo versionado.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATH = ROOT / "dados/fontes/INVENTARIO_FONTES_PUBLICAS_GRATUITAS_V1.json"
STATUSES = {
    "CAPTURA_OPERACIONAL",
    "AUTORIZADO_COM_CONDICOES",
    "PENDENTE_IMPLEMENTACAO",
    "REVISAO_TERMO_ESPECIFICO",
    "BLOQUEADO_RESTRICAO_DOCUMENTADA",
    "FONTE_NAO_CONFIRMADA",
}
REQUIRED = {
    "id", "provider", "domain", "dataset", "discovery_url", "endpoint",
    "access", "license", "automation_status", "current_state", "priority",
}


def validate(document: dict) -> list[str]:
    errors: list[str] = []
    if document.get("schema_version") != "1.0.0":
        errors.append("schema_version deve ser 1.0.0")
    if not document.get("project") or not document.get("repository"):
        errors.append("project e repository são obrigatórios")
    sources = document.get("sources")
    if not isinstance(sources, list) or not sources:
        return errors + ["sources deve ser uma lista não vazia"]

    seen: set[str] = set()
    for index, row in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{prefix} deve ser objeto")
            continue
        missing = sorted(REQUIRED - set(row))
        if missing:
            errors.append(f"{prefix} campos ausentes: {', '.join(missing)}")
        source_id = row.get("id")
        if not isinstance(source_id, str) or not source_id.strip():
            errors.append(f"{prefix}.id inválido")
        elif source_id in seen:
            errors.append(f"id duplicado: {source_id}")
        else:
            seen.add(source_id)
        status = row.get("automation_status")
        if status not in STATUSES:
            errors.append(f"{prefix}.automation_status desconhecido: {status}")
        for field in ("discovery_url", "endpoint"):
            value = row.get(field)
            parsed = urlparse(value if isinstance(value, str) else "")
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{prefix}.{field} deve ser URL HTTPS absoluta")
        if row.get("automation_status") == "BLOQUEADO_RESTRICAO_DOCUMENTADA":
            evidence = row.get("capture_evidence")
            if not isinstance(evidence, str) or not evidence.startswith("https://"):
                errors.append(f"{prefix}: fonte bloqueada precisa de URL de evidência")
        if row.get("automation_status") == "AUTORIZADO_COM_CONDICOES":
            license_text = str(row.get("license", "")).lower()
            if not license_text or any(term in license_text for term in ("não demonstrada", "não confirmada", "a confirmar")):
                errors.append(f"{prefix}: estado autorizado contradiz o campo license")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default=str(DEFAULT_PATH))
    args = parser.parse_args()
    path = Path(args.path)
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors = validate(document)
    result = {
        "valid": not errors,
        "path": str(path),
        "source_count": len(document.get("sources", [])) if isinstance(document, dict) else 0,
        "status_counts": {
            status: sum(1 for row in document.get("sources", []) if row.get("automation_status") == status)
            for status in sorted(STATUSES)
        } if isinstance(document, dict) else {},
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
