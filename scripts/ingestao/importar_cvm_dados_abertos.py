#!/usr/bin/env python3
"""Captura conjuntos CVM públicos com licença ODbL confirmada via API CKAN.

Baixa o recurso ZIP do ano mais recente publicado para os pacotes explicitamente
permitidos, valida a licença do pacote e a integridade ZIP, e grava RAW + manifesto.
Não extrai nem promove o conteúdo para NORMALIZED/CERTIFIED.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
API = "https://dados.cvm.gov.br/api/3/action/package_show"
RAW_ROOT = ROOT / "dados/cvm/raw"
MANIFEST_ROOT = ROOT / "dados/cvm/manifests"
ALLOWED_PACKAGES = {
    "cia_aberta-doc-dfp": re.compile(r"dfp_cia_aberta_(\d{4})\.zip$", re.I),
    "cia_aberta-doc-itr": re.compile(r"itr_cia_aberta_(\d{4})\.zip$", re.I),
}
MAX_BYTES = 90 * 1024 * 1024


class SourceError(RuntimeError):
    pass


def get_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "B3-PublicData-Ingestion/1.0", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            raw = response.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SourceError(f"Falha ao consultar metadados CKAN: {exc}") from exc
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SourceError("A resposta CKAN não é JSON UTF-8 válido.") from exc
    if not isinstance(value, dict) or value.get("success") is not True:
        raise SourceError("CKAN não confirmou sucesso para package_show.")
    result = value.get("result")
    if not isinstance(result, dict):
        raise SourceError("CKAN não devolveu objeto result.")
    return result


def select_resource(package_id: str, package: dict) -> dict:
    if package_id not in ALLOWED_PACKAGES:
        raise SourceError(f"Pacote não permitido por allowlist: {package_id}")
    if package.get("name") != package_id:
        raise SourceError(f"Identidade do pacote divergente para {package_id}.")
    if package.get("private") is True or package.get("isopen") is not True:
        raise SourceError(f"Pacote {package_id} não está marcado como aberto no catálogo.")
    if package.get("license_id") != "odc-odbl":
        raise SourceError(
            f"Licença inesperada para {package_id}: {package.get('license_id')!r}; "
            "exigido odc-odbl."
        )
    pattern = ALLOWED_PACKAGES[package_id]
    matches = []
    for resource in package.get("resources", []):
        if resource.get("state") != "active" or str(resource.get("format", "")).upper() != "ZIP":
            continue
        url = resource.get("url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != "dados.cvm.gov.br":
            continue
        match = pattern.search(parsed.path)
        if match:
            matches.append((int(match.group(1)), resource))
    if not matches:
        raise SourceError(f"Nenhum recurso ZIP anual válido encontrado para {package_id}.")
    matches.sort(key=lambda item: (item[0], item[1].get("metadata_modified", "")))
    year, resource = matches[-1]
    return {
        "package_id": package_id,
        "year": year,
        "resource_id": resource.get("id"),
        "resource_name": resource.get("name"),
        "resource_url": resource["url"],
        "resource_format": "ZIP",
        "package_license_id": package["license_id"],
        "package_license_title": package.get("license_title"),
        "package_url": f"https://dados.cvm.gov.br/dataset/{package_id}",
        "metadata_modified": package.get("metadata_modified"),
    }


def download(url: str) -> bytes:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != "dados.cvm.gov.br":
        raise SourceError("URL de download fora do domínio oficial permitido.")
    request = urllib.request.Request(
        url, headers={"User-Agent": "B3-PublicData-Ingestion/1.0", "Accept": "application/zip"}
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = response.read(MAX_BYTES + 1)
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SourceError(f"Falha ao baixar recurso CVM: {exc}") from exc
    if not data:
        raise SourceError("Recurso descarregado vazio.")
    if len(data) > MAX_BYTES:
        raise SourceError(
            f"Recurso excede limite de segurança de {MAX_BYTES} bytes; "
            "avaliar armazenamento Git LFS/externo antes de persistir."
        )
    try:
        with zipfile.ZipFile(BytesIO(data)) as archive:
            if archive.testzip() is not None:
                raise SourceError("O ZIP contém um membro corrompido.")
            if not archive.namelist():
                raise SourceError("O ZIP não contém membros.")
    except zipfile.BadZipFile as exc:
        raise SourceError("O recurso não é um ZIP válido.") from exc
    return data


def ingest(package_id: str) -> dict:
    query = urllib.parse.urlencode({"id": package_id})
    package = get_json(f"{API}?{query}")
    selected = select_resource(package_id, package)
    data = download(selected["resource_url"])
    digest = hashlib.sha256(data).hexdigest()
    filename = Path(urlparse(selected["resource_url"]).path).name
    raw_dir = RAW_ROOT / package_id
    raw_dir.mkdir(parents=True, exist_ok=True)
    MANIFEST_ROOT.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / filename
    raw_path.write_bytes(data)
    manifest = {
        "schema_version": "1.0.0",
        "source": "CVM Portal Dados Abertos / CKAN",
        **selected,
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "http_method": "GET",
        "bytes": len(data),
        "sha256": digest,
        "raw_path": str(raw_path.relative_to(ROOT)),
        "validation": {
            "https_official_domain": True,
            "package_is_open": True,
            "license_id_odc_odbl": True,
            "zip_integrity": "PASS",
            "promoted_to_normalized": False,
            "certified": False,
        },
    }
    manifest_path = MANIFEST_ROOT / f"{package_id}_{selected['year']}.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return {
        "package_id": package_id,
        "year": selected["year"],
        "bytes": len(data),
        "sha256": digest,
        "raw_path": str(raw_path.relative_to(ROOT)),
        "manifest_path": str(manifest_path.relative_to(ROOT)),
        "zip_integrity": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", action="append", choices=sorted(ALLOWED_PACKAGES), required=True)
    args = parser.parse_args()
    results, errors = [], []
    for package_id in args.package:
        try:
            results.append(ingest(package_id))
        except (SourceError, OSError) as exc:
            errors.append({"package_id": package_id, "error": str(exc)})
    print(json.dumps({"results": results, "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
