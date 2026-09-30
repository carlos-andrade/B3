import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "dados/cotahist/raw/anual/COTAHIST_A1993.ZIP"
MANIFEST = ROOT / "dados/cotahist/manifests/COTAHIST_A1993.json"
CHECKSUM = ROOT / "dados/cotahist/checksums/COTAHIST_A1993.ZIP.sha256"
OUT = ROOT / "dados/cotahist/quality/COTAHIST_1993_FASE01_AQUISICAO_RAW_V1.json"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

missing = [str(p.relative_to(ROOT)) for p in (RAW, MANIFEST, CHECKSUM) if not p.is_file()]
errors = []
observed = {}

if not missing:
    observed["raw_sha256"] = sha256(RAW)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected_sha = manifest.get("sha256")
    checksum_sha = CHECKSUM.read_text(encoding="utf-8").split()[0]
    observed["manifest_sha256"] = expected_sha
    observed["checksum_sha256"] = checksum_sha
    if observed["raw_sha256"] != expected_sha:
        errors.append("RAW_SHA256_DIVERGENTE_DO_MANIFESTO")
    if observed["raw_sha256"] != checksum_sha:
        errors.append("RAW_SHA256_DIVERGENTE_DO_CHECKSUM")

    try:
        with zipfile.ZipFile(RAW) as z:
            bad = z.testzip()
            names = [n for n in z.namelist() if not n.endswith("/")]
            observed["zip_test"] = bad
            observed["zip_non_directory_members"] = names
            if bad is not None:
                errors.append("ZIP_CORROMPIDO")
            if names != ["COTAHIST.A1993"]:
                errors.append("MEMBRO_ZIP_INESPERADO")
            if names:
                with z.open(names[0]) as f:
                    header = f.readline()
                    record_count = 0
                    invalid_lengths = 0
                    type_counts = {}
                    first_date = None
                    last_date = None
                    for raw in f:
                        line = raw.rstrip(b"\r\n")
                        if not line:
                            continue
                        if len(line) != 245:
                            invalid_lengths += 1
                            continue
                        typ = line[0:2].decode("ascii", errors="replace")
                        type_counts[typ] = type_counts.get(typ, 0) + 1
                        if typ == "01":
                            record_count += 1
                            d = line[2:10].decode("ascii", errors="replace")
                            if first_date is None:
                                first_date = d
                            last_date = d
                    observed["header_length"] = len(header.rstrip(b"\r\n"))
                    observed["record_count_01"] = record_count
                    observed["invalid_record_lengths"] = invalid_lengths
                    observed["type_counts"] = type_counts
                    observed["first_date_raw"] = first_date
                    observed["last_date_raw"] = last_date
                    if observed["header_length"] != 245:
                        errors.append("HEADER_COMPRIMENTO_INVALIDO")
                    if invalid_lengths:
                        errors.append("REGISTRO_245_BYTES_INVALIDO")
                    if type_counts.get("99", 0) != 1:
                        errors.append("TRAILER_99_AUSENTE_OU_DUPLICADO")
                    if record_count == 0:
                        errors.append("SEM_REGISTROS_01")
    except zipfile.BadZipFile:
        errors.append("ZIP_INVALIDO")

status = "VALIDADO" if not missing and not errors else "BLOQUEADO"
out = {
    "schema_version": "1.0.0",
    "ano": 1993,
    "phase": "FASE01",
    "status": status,
    "entrada": "dados/cotahist/raw/anual/COTAHIST_A1993.ZIP",
    "missing": missing,
    "errors": errors,
    "observed": observed,
    "criterio": "RAW adquirido e preservado, checksum coerente, ZIP integro e membro COTAHIST.A1993 estruturalmente verificavel.",
    "decision": status,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, ensure_ascii=False))
if status != "VALIDADO":
    raise SystemExit(1)
