#!/usr/bin/env python3
"""Recover CESU-8-like surrogate text into a separate, explicitly partial view.

Never rewrites extraction/page text, reads figures, changes visual status, or
claims equation/layout fidelity. A fresh extraction is kept as a distinct source
generation; layout/encoding differences are reported, never silently equated.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import unicodedata
from pathlib import Path

import stage_integrity_repair as storage
import stage_d38727_language_repair as language_repair
import validate_language_anticopy as anticopy

ROOT = storage.ROOT
PID = language_repair.PID
SHA = language_repair.SHA
BASE = Path("artifacts/staging/integrity-repair-20261025-v5") / PID


def line_endings(raw):
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def physical_pages(raw, count):
    parts = line_endings(raw).split(b"\f")
    if parts and not parts[-1].strip(): parts.pop()
    if len(parts) != count:
        raise ValueError(f"unexpected physical page count: {len(parts)} != {count}")
    return parts


def recover(raw):
    # Surrogatepass accepts encoded surrogate codepoints, but still rejects
    # unrelated malformed UTF-8. Never use errors=ignore or silently replace.
    text = raw.decode("utf-8", errors="surrogatepass")
    out, unresolved = [], []
    index, pairs = 0, 0
    while index < len(text):
        cp = ord(text[index])
        if 0xD800 <= cp <= 0xDBFF and index + 1 < len(text) and 0xDC00 <= ord(text[index + 1]) <= 0xDFFF:
            out.append(chr(0x10000 + ((cp - 0xD800) << 10) + ord(text[index + 1]) - 0xDC00))
            pairs += 1
            index += 2
            continue
        if 0xD800 <= cp <= 0xDFFF:
            marker = f"[UNPAIRED-U+{cp:04X}]"
            out.append(marker)
            unresolved.append({"input_character_offset": index, "line": text.count("\n", 0, index) + 1,
                               "codepoint": f"U+{cp:04X}", "marker": marker})
        else:
            out.append(text[index])
        index += 1
    decoded = "".join(out)
    decoded.encode("utf-8", errors="strict")
    return decoded, {"recovered_pairs": pairs, "unresolved": unresolved}


def legacy_view(raw):
    decoded, report = recover(raw)
    for item in report["unresolved"]:
        decoded = decoded.replace(item["marker"], "?")
    return decoded


def build(output):
    output.mkdir(parents=True, exist_ok=False)
    storage.put_new(output / "recipe.py", Path(__file__).read_bytes())
    base = ROOT / BASE
    validation = storage.read_json(base / "validation.json")
    frozen = validation["input_sha256"].copy()
    raw_path = ROOT / f"artifacts/papers/{PID}/text/full.txt"
    frozen[str(raw_path)] = storage.digest(raw_path.read_bytes())
    candidate_path = base / "language-units.draft.json"
    frozen[str(candidate_path)] = storage.digest(candidate_path.read_bytes())
    if frozen[str(candidate_path)] != validation["candidate_sha256"]:
        raise ValueError("candidate generation changed")
    if any(storage.digest(Path(p).read_bytes()) != h for p, h in frozen.items()):
        raise ValueError("bound source generation changed")
    manifest = language_repair.language.find_manifest_record(ROOT / "artifacts/corpus/manifest.jsonl", PID)
    source = ROOT.parent / "MCM-ICM-master" / manifest["relative_path"]
    if storage.digest(source.read_bytes()) != SHA or manifest["sha256"] != SHA or manifest["page_count"] != 19:
        raise ValueError("PDF identity changed")
    executable = shutil.which("pdftotext")
    if not executable: raise RuntimeError("pdftotext unavailable; no recovery certified")
    native = output / "fresh-native-full.bin"
    result = subprocess.run([executable, "-layout", "-enc", "UTF-8", str(source), str(native)],
                            capture_output=True, check=False)
    if result.returncode != 0: raise RuntimeError("fresh text extraction failed")
    raw = raw_path.read_bytes()
    raw_generations_equal = line_endings(native.read_bytes()) == line_endings(raw)
    fresh_text = native.read_bytes().decode("utf-8", errors="strict")
    fresh_parts = physical_pages(native.read_bytes(), 19)
    storage.put_new(output / "original-raw-full.bin", raw)
    parts = physical_pages(raw, 19)
    decoded_pages, normalized_pages, page_reports = [], [], []
    fresh_pages = []
    loss_checks = []
    for number, part in enumerate(parts, 1):
        live_page = ROOT / f"artifacts/papers/{PID}/text/pages/page-{number:04d}.txt"
        lossy = part.decode("utf-8", errors="replace")
        live_text = live_page.read_text(encoding="utf-8")
        match = lossy.rstrip() + "\n" == live_text if lossy else live_text == ""
        loss_checks.append(match)
        decoded, report = recover(part)
        normalized = unicodedata.normalize("NFKC", decoded)
        decoded_pages.append(decoded)
        normalized_pages.append(normalized)
        fresh_page = fresh_parts[number - 1].decode("utf-8", errors="strict")
        fresh_pages.append(fresh_page)
        for item in report["unresolved"]: item["physical_page"] = number
        page_reports.append({"physical_page": number, **report,
                             "lossy_page_matches_live": match,
                             "lossy_page_replacement_characters": lossy.count("\ufffd")})
        storage.put_new(output / "decoded/pages" / f"page-{number:04d}.txt", (decoded.rstrip() + "\n").encode("utf-8"))
        storage.put_new(output / "nfkc-preview/pages" / f"page-{number:04d}.txt", (normalized.rstrip() + "\n").encode("utf-8"))
        storage.put_new(output / "fresh-native/pages" / f"page-{number:04d}.txt", (fresh_page.rstrip() + "\n").encode("utf-8"))
    if not all(loss_checks): raise ValueError("old raw-to-live-page provenance mismatch")
    joined = "\n\f\n".join(normalized_pages)
    storage.put_new(output / "decoded-full.txt", "\n\f\n".join(decoded_pages).encode("utf-8"))
    storage.put_new(output / "nfkc-preview-full.txt", joined.encode("utf-8"))
    record = storage.read_json(candidate_path)
    witnesses, fresh_witnesses = 0, 0
    for unit in record["units"]:
        for occurrence in unit["occurrences"]:
            if language_repair.normalized(occurrence["source_excerpt"]) not in language_repair.normalized(decoded_pages[occurrence["page"] - 1]):
                raise ValueError("language witness changed in recovered source")
            witnesses += 1
            if language_repair.normalized(occurrence["source_excerpt"]) not in language_repair.normalized(fresh_pages[occurrence["page"] - 1]):
                raise ValueError("language witness missing in fresh PDF text generation")
            fresh_witnesses += 1
    profile = anticopy.build_source_profile(joined, 8)
    scans = [anticopy.scan_unit_with_profile(u, profile, 8, set(record["source_specific_terms"])) for u in record["units"]]
    if any(s["result"] != "pass" for s in scans): raise ValueError("recovered-source anti-copy check failed")
    fresh_profile = anticopy.build_source_profile(unicodedata.normalize("NFKC", fresh_text), 8)
    fresh_scans = [anticopy.scan_unit_with_profile(u, fresh_profile, 8, set(record["source_specific_terms"])) for u in record["units"]]
    if any(s["result"] != "pass" for s in fresh_scans): raise ValueError("fresh-source anti-copy check failed")
    old = ROOT / "tmp/q275-text.txt"
    old_comparison = None
    if old.exists():
        # The old writer used default Windows newline translation on a CRLF
        # input, producing CRCRLF. Verify exact bytes, not merely word overlap.
        expected = legacy_view(raw).replace("\n", "\r\n").encode("utf-8")
        old_comparison = {"path": str(old), "sha256": storage.digest(old.read_bytes()),
                          "matches_after_recorded_windows_newline_translation": old.read_bytes() == expected,
                          "CRCRLF_count": old.read_bytes().count(b"\r\r\n")}
    if any(storage.digest(Path(p).read_bytes()) != h for p, h in frozen.items()):
        raise ValueError("input changed during recovery; output not certified")
    report = {"paper_id": PID, "source_sha256": SHA, "status": "text-recovered-not-equation-or-visual-authority",
        "source_pdf": str(source), "fresh_extraction_matches_original_raw_after_line_endings": raw_generations_equal,
        "generation_policy": "Fresh PDF text and repaired historical text are distinct views; no full equivalence claim or live replacement.",
        "pdftotext_executable": executable, "pdftotext_executable_sha256": storage.digest(Path(executable).read_bytes()),
        "fresh_native_sha256": storage.digest(native.read_bytes()), "input_sha256": frozen,
        "physical_pages": 19, "recovered_surrogate_pairs": sum(p["recovered_pairs"] for p in page_reports),
        "unresolved_surrogate_count": sum(len(p["unresolved"]) for p in page_reports),
        "lossy_page_provenance_matches": sum(loss_checks), "page_reports": page_reports,
        "legacy_reference": old_comparison, "language_witnesses_retained": witnesses,
        "fresh_generation_language_witnesses_retained": fresh_witnesses,
        "fresh_generation_surrogate_codepoints": sum(0xD800 <= ord(c) <= 0xDFFF for c in fresh_text),
        "fresh_generation_math_alphanumerics": sum(0x1D400 <= ord(c) <= 0x1D7FF for c in fresh_text),
        "language_unit_anticopy_results": scans, "original_examples": sum(s["example_count"] for s in scans),
        "fresh_generation_anticopy_results": fresh_scans,
        "maximum_shared_content_run": max(s["maximum_shared_content_run"] for s in scans),
        "decoded_full_sha256": storage.digest((output / "decoded-full.txt").read_bytes()),
        "nfkc_preview_sha256": storage.digest((output / "nfkc-preview-full.txt").read_bytes()),
        "frozen_recipe_sha256": storage.digest((output / "recipe.py").read_bytes()),
        "limits": ["Eight unpaired surrogate codepoints remain explicitly tagged, never guessed or erased.",
            "NFKC preview flattens mathematical typography and must not be treated as authoritative notation.",
            "Text extraction can scramble reading order, fractions or columns; exact equations still need separate verification.",
            "No figure/table reading, fresh image rendering, visual status change, live text replacement or transaction append."]}
    storage.put_new(output / "recovery-report.json", storage.encoded(report))
    print(json.dumps({k: v for k, v in report.items() if k not in {"input_sha256", "page_reports", "language_unit_anticopy_results", "fresh_generation_anticopy_results"}}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
