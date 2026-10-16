#!/usr/bin/env python3
"""Preflight de licença para séries SGS antes de qualquer captura.

Consulta exclusivamente o catálogo oficial de Dados Abertos do BCB. Cada série
só passa quando o catálogo identifica um recurso da própria série e licença ODbL.
Acesso HTTP, por si só, nunca é prova de licença. Sem correspondência exata,
a série é bloqueada (fail-closed).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API = "https://dadosabertos.bcb.gov.br/api/3/action/package_search"
LICENSES = {"odc-odbl"}
USER_AGENT = "B3-Fonte-Gratuita-Preflight/1.0 (+https://github.com/carlos-andrade/B3)"


def fetch_search(term: str) -> dict:
    url = API + "?" + urlencode({"q": term, "rows": 100})
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if payload.get("success") is not True or not isinstance(payload.get("result"), dict):
        raise RuntimeError(f"Resposta inválida do catálogo BCB para a consulta {term!r}")
    return payload["result"]


def resource_matches(resource: dict, code: int) -> bool:
    marker = f"serie-sgs-{code}"
    url = str(resource.get("url") or "").lower()
    name = str(resource.get("name") or "").lower()
    description = str(resource.get("description") or "").lower()
    return marker in url or marker in name or marker in description or f"bcdata.sgs.{code}/dados" in url


def verify_series(code: int, search_fn=fetch_search) -> dict:
    errors = []
    seen = {}
    for term in (f"serie-sgs-{code}", str(code)):
        try:
            result = search_fn(term)
        except Exception as exc:
            errors.append(f"{term}: {type(exc).__name__}: {exc}")
            continue
        for dataset in result.get("results", []):
            name = str(dataset.get("name") or dataset.get("id") or "")
            seen[name] = dataset
    matches = []
    for dataset in seen.values():
        resources = dataset.get("resources") or []
        exact_resources = [r for r in resources if resource_matches(r, code)]
        if not exact_resources:
            continue
        license_id = str(dataset.get("license_id") or "").lower()
        license_title = str(dataset.get("license_title") or "")
        if license_id in LICENSES:
            matches.append({
                "dataset_name": dataset.get("name"),
                "dataset_title": dataset.get("title"),
                "license_id": license_id,
                "license_title": license_title,
                "dataset_url": f"https://dadosabertos.bcb.gov.br/dataset/{dataset.get('name')}",
                "resources": [
                    {"name": r.get("name"), "url": r.get("url")}
                    for r in exact_resources
                ],
            })
    allowed = bool(matches)
    return {
        "series_code": code,
        "authorized": allowed,
        "license": "ODbL" if allowed else None,
        "matches": matches,
        "errors": errors,
        "decision": (
            "Catálogo oficial identifica recurso exato da série com licença ODbL; cumprir atribuição e obrigações da licença."
            if allowed else
            "Nenhuma correspondência exata com licença ODbL foi demonstrada no catálogo; captura bloqueada."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--series", required=True, help="Códigos SGS separados por vírgula")
    parser.add_argument("--json-output", default="")
    parser.add_argument("--allow-partial", action="store_true", help="Aceita executar apenas as séries com ODbL demonstrada.")
    args = parser.parse_args()
    try:
        codes = sorted({int(x.strip()) for x in args.series.split(",") if x.strip()})
    except ValueError as exc:
        parser.error(f"Código SGS inválido: {exc}")
    if not codes or any(code <= 0 for code in codes):
        parser.error("Indique pelo menos um código SGS positivo.")

    results = [verify_series(code) for code in codes]
    report = {
        "schema_version": "1.0.0",
        "source": "Portal de Dados Abertos do Banco Central do Brasil",
        "catalog_api": API,
        "license_required": "odc-odbl",
        "policy": "FAIL_CLOSED",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "series_count": len(results),
        "eligible_count": sum(1 for row in results if row["authorized"]),
        "blocked_count": sum(1 for row in results if not row["authorized"]),
        "results": results,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    print(rendered, end="")
    if args.json_output:
        output = Path(args.json_output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    if report["eligible_count"] == 0:
        return 2
    return 0 if report["blocked_count"] == 0 or args.allow_partial else 2


if __name__ == "__main__":
    raise SystemExit(main())
