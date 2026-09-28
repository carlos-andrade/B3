#!/usr/bin/env python3
"""Consolida as evidências dos gates de COTAHIST 1987.

Regra: aprovação estrutural não equivale a certificação semântica econômica.
A exceção PRAZOT permanece aberta até evidência histórica primária.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
QUALITY = ROOT / "dados/cotahist/quality"

EVIDENCES = {
    "reconciliacao_raw_normalized": "COTAHIST_1987_RECONCILIACAO_RAW_NORMALIZED_V1.json",
    "chave_logica": "COTAHIST_1987_AUDITORIA_CHAVE_LOGICA_V1.json",
    "ohlc": "COTAHIST_1987_AUDITORIA_OHLC_V1.json",
    "quantidade_volume": "COTAHIST_1987_AUDITORIA_QUANTIDADE_VOLUME_V1.json",
    "calendario": "COTAHIST_1987_AUDITORIA_CALENDARIO_V1.json",
    "semantica": "COTAHIST_1987_AUDITORIA_SEMANTICA_V1.json",
    "prazot_integridade": "COTAHIST_1987_CLASSIFICACAO_PRAZOT_V1.json",
    "prazot_validacao": "COTAHIST_1987_VALIDACAO_INDEPENDENTE_PRAZOT_V1.json",
}

def load(name: str):
    p = QUALITY / name
    if not p.exists():
        raise FileNotFoundError(p)
    return json.loads(p.read_text(encoding="utf-8"))

def gate_reconciliation(x):
    checks = x.get("checks", {})
    numeric = checks.get("numeric", {})
    numeric_ok = all(
        item.get("mismatch_count_sampled", 1) == 0
        for item in numeric.values()
    )
    return (
        bool(checks.get("row_count_equal"))
        and bool(checks.get("date_equal"))
        and bool(checks.get("header", {}).get("all_required_fields_present"))
        and checks.get("identity_mismatch_count_sampled", 1) == 0
        and bool(checks.get("sample_30"))
        and numeric_ok
        and bool(x.get("fail_closed_gates", {}).get("row_count_equal"))
        and bool(x.get("fail_closed_gates", {}).get("header_complete"))
        and bool(x.get("fail_closed_gates", {}).get("dates_equal"))
        and bool(x.get("fail_closed_gates", {}).get("identity_no_sampled_mismatch"))
        and bool(x.get("fail_closed_gates", {}).get("numeric_no_sampled_mismatch"))
        and bool(x.get("fail_closed_gates", {}).get("sample_30_present"))
    )

def gate_key(x):
    return x.get("collision_group_count", 1) == 0 and x.get("exact_duplicate_group_count", 1) == 0 and x.get("same_key_distinct_statistics_group_count", 1) == 0

def gate_ohlc(x):
    return bool(x.get("gates", {}).get("ohlc_order_valid")) and x.get("violation_count", 1) == 0

def gate_qv(x):
    required = {"records_positive", "all_numeric", "no_negative", "no_control_bytes", "raw_normalized_mismatch_zero"}
    gates = x.get("gates", {})
    return all(bool(gates.get(k)) for k in required)

def gate_calendar(x):
    g = x.get("gates", {})
    return all(bool(g.get(k)) for k in (
        "records_positive", "all_dates_valid", "no_weekend_dates",
        "chronological_bounds", "records_chronological", "distinct_dates_positive"
    )) and bool(x.get("fail_closed"))

def main():
    data = {k: load(v) for k, v in EVIDENCES.items()}
    gates = {
        "reconciliacao_raw_normalized": gate_reconciliation(data["reconciliacao_raw_normalized"]),
        "chave_logica": gate_key(data["chave_logica"]),
        "ohlc": gate_ohlc(data["ohlc"]),
        "quantidade_volume": gate_qv(data["quantidade_volume"]),
        "calendario": gate_calendar(data["calendario"]),
    }
    sem = data["semantica"]
    prazot = data["prazot_integridade"]
    prazot_val = data["prazot_validacao"]

    semantic_certified = (
        sem.get("assessment") == "CERTIFICADA"
        and prazot.get("classification") == "RESOLVIDA"
        and prazot_val.get("status") == "VALIDADA"
    )

    structural_approved = all(gates.values())
    status = (
        "CERTIFICACAO_ESTRUTURAL_1987_COM_EXCECAO_SEMANTICA"
        if structural_approved and not semantic_certified
        else "CERTIFICACAO_1987_COMPLETA"
        if structural_approved and semantic_certified
        else "REPROVADO"
    )

    out = {
        "schema_version": "1.0.0",
        "status": status,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "year": 1987,
        "structural_gates": gates,
        "structural_approval": structural_approved,
        "economic_semantics_certified": semantic_certified,
        "prazot_exception": {
            "status": prazot.get("classification"),
            "independent_validation": prazot_val.get("status"),
            "rule": "Não corrigir, substituir, remover ou reinterpretar PRAZOT sem evidência histórica primária."
        },
        "calendar_note": "Os 19 weekday gaps permanecem como candidatos a dias sem pregão; não são classificados como feriados sem fonte histórica primária.",
        "release_rule": "1988 somente após esta consolidação e resolução documental das pendências exigidas pelo protocolo do projeto.",
        "evidence_files": EVIDENCES,
    }

    out_path = QUALITY / "COTAHIST_1987_CERTIFICACAO_FINAL_V1.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if status == "REPROVADO":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
