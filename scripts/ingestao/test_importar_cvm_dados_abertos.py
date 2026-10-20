import unittest

from scripts.ingestao.importar_cvm_dados_abertos import SourceError, select_resource


def package(package_id="cia_aberta-doc-dfp", license_id="odc-odbl"):
    stem = "dfp" if package_id.endswith("dfp") else "itr"
    return {
        "name": package_id,
        "private": False,
        "isopen": True,
        "license_id": license_id,
        "license_title": "Open Data Commons Open Database License (ODbL)",
        "metadata_modified": "2026-10-19T11:00:00",
        "resources": [
            {
                "id": "old",
                "name": f"{stem} old",
                "format": "ZIP",
                "state": "active",
                "url": f"https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/{stem.upper()}/DADOS/{stem}_cia_aberta_2025.zip",
            },
            {
                "id": "current",
                "name": f"{stem} current",
                "format": "ZIP",
                "state": "active",
                "metadata_modified": "2026-10-19T11:00:00",
                "url": f"https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/{stem.upper()}/DADOS/{stem}_cia_aberta_2026.zip",
            },
        ],
    }


class CvmOpenDataTests(unittest.TestCase):
    def test_selects_latest_year(self):
        result = select_resource("cia_aberta-doc-dfp", package())
        self.assertEqual(result["year"], 2026)
        self.assertEqual(result["resource_id"], "current")
        self.assertEqual(result["package_license_id"], "odc-odbl")

    def test_rejects_non_odbl_license(self):
        with self.assertRaises(SourceError):
            select_resource("cia_aberta-doc-dfp", package(license_id="other"))

    def test_rejects_package_identity_mismatch(self):
        with self.assertRaises(SourceError):
            select_resource("cia_aberta-doc-dfp", package("cia_aberta-doc-itr"))

    def test_rejects_unallowlisted_package(self):
        with self.assertRaises(SourceError):
            select_resource("fundos-informe", package("fundos-informe"))

    def test_rejects_nonofficial_resource_host(self):
        p = package()
        p["resources"][1]["url"] = "https://example.com/dfp_cia_aberta_2026.zip"
        with self.assertRaises(SourceError):
            select_resource("cia_aberta-doc-dfp", p)

    def test_rejects_closed_package(self):
        p = package()
        p["isopen"] = False
        with self.assertRaises(SourceError):
            select_resource("cia_aberta-doc-dfp", p)


if __name__ == "__main__":
    unittest.main()
