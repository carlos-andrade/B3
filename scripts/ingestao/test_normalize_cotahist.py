"""Testes de regressão para o parser de registos COTAHIST."""
import contextlib
import io
import unittest

from scripts.ingestao.normalize_cotahist import normalize_line, strip_line_ending


def valid_record() -> bytes:
    record = bytearray(b" " * 245)
    record[0:2] = b"01"
    record[2:10] = b"20261022"
    return bytes(record)


class NormalizeCotahistTests(unittest.TestCase):
    def test_registo_valido_245_bytes_tem_25_campos(self):
        row = normalize_line(valid_record(), line_number=7)
        self.assertEqual(len(row), 25)
        self.assertEqual(row[0], "2026-10-22")

    def test_crlf_e_removido_sem_remover_espacos_de_dados(self):
        raw = valid_record() + b"\r\n"
        self.assertEqual(strip_line_ending(raw), valid_record())

    def test_espaco_excedente_e_rejeitado_com_evidencia_ate_confirmacao(self):
        bad = valid_record() + b" "
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaisesRegex(ValueError, "246 bytes"):
                normalize_line(bad, line_number=123)
        log = stderr.getvalue()
        self.assertIn("line_number=123", log)
        self.assertIn("record_type='01'", log)
        self.assertIn("observed_bytes=246", log)
        self.assertIn("expected_bytes=245", log)
        self.assertIn("20", log.split("hex=")[-1])

    def test_byte_excedente_nao_espaco_e_rejeitado(self):
        bad = valid_record() + b"X"
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaisesRegex(ValueError, "246 bytes"):
                normalize_line(bad, line_number=124)
        self.assertIn("observed_bytes=246", stderr.getvalue())
        self.assertIn("58", stderr.getvalue().split("hex=")[-1])

    def test_registo_curto_e_rejeitado_com_diagnostico(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaisesRegex(ValueError, "244 bytes"):
                normalize_line(valid_record()[:-1], line_number=125)
        self.assertIn("observed_bytes=244", stderr.getvalue())

    def test_tipo_de_registo_invalido_e_rejeitado(self):
        bad = b"02" + valid_record()[2:]
        with self.assertRaisesRegex(ValueError, "não é 01"):
            normalize_line(bad, line_number=126)


if __name__ == "__main__":
    unittest.main()
