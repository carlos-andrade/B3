"""Testes determinísticos do tratamento de datas das carteiras B3.

ID: B3-TEST-INDICES-001
Projeto: B3 — A BOLSA DO BRASIL
Tipo documental: TESTES_UNITARIOS
Fase: GOVERNANCA / CORREÇÃO DE INGESTÃO
Estado: EM_CURSO
Versão: 1.0.0
Origem: Issue WATCHDOG #11 e falha observada no run 38666819065.
Autoridade: GOVERNANCA — Norma de Cabeçalho e princípios de evidência antes de alegação.
"""

import sys
import unittest
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "ingestao"))

import importar_indices_b3_v1 as ingest


class ReferenceDateTests(unittest.TestCase):
    def test_date_object_is_normalized_to_iso(self):
        self.assertEqual(ingest.iso_date(date(2026, 10, 15)), "2026-10-15")

    def test_datetime_object_is_normalized_to_date_only(self):
        self.assertEqual(
            ingest.iso_date(datetime(2026, 10, 15, 18, 30)),
            "2026-10-15",
        )

    def test_iso_date_string_is_normalized(self):
        self.assertEqual(ingest.iso_date("2026-10-15"), "2026-10-15")

    def test_invalid_date_string_is_rejected(self):
        with self.assertRaises(ValueError):
            ingest.iso_date("15/10/2026")


if __name__ == "__main__":
    unittest.main()
