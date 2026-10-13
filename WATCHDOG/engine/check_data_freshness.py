#!/usr/bin/env python3
"""Avalia atualidade dos dados com base em datas de observação declaradas nos manifestos."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "WATCHDOG" / "registry" / "datasets-monitorizados.json"


def parse_date(value: Any) -> dt.date | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        return dt.date.fromisoformat(value[:10])
    except ValueError:
        return None


def read_json(root: Path, relative: str) -> Any:
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"Caminho fora da raiz: {relative}") from exc
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def find_date(entry: dict[str, Any], root: Path) -> tuple[dt.date | None, str | None, str | None]:
    kind = entry.get("kind")
    date_field = entry.get("date_field")
    if kind in {"json_field", "json_series"}:
        manifest = read_json(root, entry["manifest_path"])
        if kind == "json_field":
            date = parse_date(manifest.get(date_field))
            acquired = manifest.get(entry.get("acquired_at_field", "")) if entry.get("acquired_at_field") else None
            return date, entry["manifest_path"], acquired
        rows = manifest.get("series")
        if not isinstance(rows, list):
            return None, entry["manifest_path"], None
        match = next((row for row in rows if row.get(entry.get("series_key")) == entry.get("series_value")), None)
        if not match:
            return None, entry["manifest_path"], None
        return parse_date(match.get(date_field)), entry["manifest_path"], None
    if kind == "glob_json_date":
        candidates = sorted(root.glob(entry["glob"]))
        dated: list[tuple[dt.date, Path]] = []
        for path in candidates:
            try:
                path.resolve().relative_to(root.resolve())
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError, ValueError):
                continue
            date = parse_date(data.get(date_field))
            if date:
                dated.append((date, path))
        if not dated:
            return None, entry["glob"], None
        date, path = max(dated, key=lambda item: item[0])
        return date, path.relative_to(root).as_posix(), None
    raise ValueError(f"Tipo de dataset não suportado: {kind}")


def evaluate_dataset(entry: dict[str, Any], root: Path, today: dt.date) -> dict[str, Any]:
    required = ("id", "name", "kind", "date_field", "max_age_days")
    missing = [key for key in required if key not in entry]
    if missing:
        raise ValueError(f"Dataset sem campos obrigatórios {missing}")
    date, source, acquired_at = find_date(entry, root)
    result = {
        "id": entry["id"],
        "name": entry["name"],
        "state": "UNKNOWN",
        "observation_date": date.isoformat() if date else None,
        "age_days": None,
        "max_age_days": entry["max_age_days"],
        "source": source,
        "acquired_at": acquired_at,
        "details": "",
    }
    if date is None:
        result["details"] = "A data da observação não existe ou não pôde ser lida; não usar a data de ingestão como substituto."
        return result
    age = (today - date).days
    result["age_days"] = age
    if age < 0:
        result["state"] = "UNKNOWN"
        result["details"] = "A data de observação está no futuro relativamente à data de avaliação."
    elif age > int(entry["max_age_days"]):
        result["state"] = "STALE"
        result["details"] = f"Observação com {age} dias; limite declarado: {entry['max_age_days']} dias."
    else:
        result["state"] = "PASS"
        result["details"] = f"Observação com {age} dias dentro do limite declarado."
    if entry.get("note"):
        result["details"] += " " + entry["note"]
    return result


def evaluate(config: dict[str, Any], root: Path = ROOT, today: dt.date | None = None) -> dict[str, Any]:
    if config.get("schema_version") != 1 or not isinstance(config.get("datasets"), list):
        raise ValueError("Configuração inválida: esperado schema_version=1 e datasets como lista.")
    today = today or dt.datetime.now(dt.timezone.utc).date()
    ids: set[str] = set()
    results = []
    for entry in config["datasets"]:
        if not isinstance(entry, dict):
            raise ValueError("Cada dataset deve ser um objeto.")
        if entry.get("id") in ids:
            raise ValueError(f"ID de dataset duplicado: {entry.get('id')}")
        ids.add(entry.get("id"))
        results.append(evaluate_dataset(entry, root, today))
    counts = {state: sum(1 for item in results if item["state"] == state) for state in ("PASS", "STALE", "UNKNOWN")}
    return {
        "schema_version": 1,
        "project": config.get("project", "UNSPECIFIED"),
        "checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "evaluation_date": today.isoformat(),
        "dataset_count": len(results),
        "counts": counts,
        "result": "STALE" if counts["STALE"] else ("UNKNOWN" if counts["UNKNOWN"] else "PASS"),
        "datasets": results,
        "policy": "Data de ingestão não substitui data da observação de mercado.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
        result = evaluate(config, args.root.resolve())
    except (OSError, json.JSONDecodeError, ValueError, KeyError) as exc:
        print(json.dumps({"result": "FAIL", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 1 if result["counts"]["STALE"] else 0


if __name__ == "__main__":
    sys.exit(main())
