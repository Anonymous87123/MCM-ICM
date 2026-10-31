"""Audit source accounting, hashes, exports and readiness, never promote drafts."""
from __future__ import annotations

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import digest, exported_section_text, file_hash, json_new, read_json, rows, validate_author_export
from source_text_repairs import replay_block, validate_evidence
from resegment_text_corpus import validate_exact_comparisons
from source_absence_reviews import validate_absence_reviews,validate_review_bundle
from source_layout_reviews import validate_layout_reviews
from source_span_metrics import validate_flow_evidence
from source_paragraph_reviews import validate_paragraph_reviews
from source_ocr_page_reviews import validate_ocr_page_reviews


def validate(root: Path, work_root: Path | None = None, verify_pdfs=False) -> dict:
    scope = read_json(root / "scope.json"); cat = Catalog(root)
    errors = []; defects = Counter(); totals = Counter(); expected = scope["records"]; expected_sql = {}
    if [p["paper_id"] for p in cat.papers] != [r["paper_id"] for r in expected]:
        errors.append("Catalog paper list/order differs from frozen scope")
    if file_hash(root / "corpus.sqlite3") != cat.catalog["sqlite_sha256"]:
        errors.append("SQLite hash differs")
    for paper in cat.papers:
        pid = paper["paper_id"]
        if not paper["document"]:
            errors.append(f"{pid}: missing extraction"); continue
        for rel, sha in paper["files"].items():
            path = (root / rel).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file() or file_hash(path) != sha:
                errors.append(f"{pid}: frozen file differs: {rel}")
        doc = cat.document(pid); folder = root / "papers" / pid
        errors.extend(f"{pid}: {message}" for message in validate_author_export(folder, doc))
        if doc.get("author_view_policy"):
            totals["continuous_author_views_checked"] += 1
        pages = rows(folder / "raw/pages.jsonl")
        if [p["page"] for p in pages] != list(range(1, paper["page_count"]+1)):
            errors.append(f"{pid}: physical page coverage invalid")
        if file_hash(folder / "raw/pages.jsonl") != doc["raw_pages_sha256"]:
            errors.append(f"{pid}: raw page binding differs")
        originals = {x["line_id"]: x for p in pages for x in p["lines"]}
        if len(originals) != sum(len(p["lines"]) for p in pages):
            errors.append(f"{pid}: duplicate raw line IDs")
        used = Counter(x for b in doc["blocks"] for x in b["source_line_ids"])
        for excluded in doc.get("excluded_source_lines", []):
            used[excluded["line_id"]] += 1
            rawline = originals[excluded["line_id"]]
            reason = excluded.get("reason")
            okay = reason == "empty native text run" and not rawline["text"].strip()
            if reason == "repeated microtext outside body margins":
                page = pages[rawline["page"]-1]
                okay = (rawline["font_size"] < 4 and len(rawline["text"].strip()) < 8 and
                        (rawline["bbox"][2] < 18 or rawline["bbox"][0] > page["width"]-18))
            if reason == "native text superseded by source-bound OCR candidate":
                page = pages[rawline["page"]-1]
                evidence = page.get("ocr_evidence", {})
                evidence_path = folder / evidence.get("path", "missing")
                okay = bool(rawline.get("superseded_by_ocr") and evidence_path.is_file() and
                            file_hash(evidence_path) == evidence.get("sha256") and
                            any(x.get("engine") == "rapidocr" for x in page["lines"]))
            if not okay:
                errors.append(f"{pid}: unsupported source-line exclusion")
        if set(used) != set(originals) or any(n != 1 for n in used.values()):
            errors.append(f"{pid}: raw source lines lost or duplicated")
        block_ids = [b["block_id"] for b in doc["blocks"]]
        if len(set(block_ids)) != len(block_ids):
            errors.append(f"{pid}: duplicate block IDs")
        owned = Counter(x for s in doc["sections"] for x in s["block_ids"])
        if set(owned) != set(block_ids) or any(n != 1 for n in owned.values()):
            errors.append(f"{pid}: section ownership lost or duplicated")
        try:
            validate_evidence(root, doc)
            validate_absence_reviews(root,doc)
            validate_layout_reviews(doc,pages)
            validate_flow_evidence(root,doc,pages)
            validate_paragraph_reviews(doc)
            for layout_review in doc.get("layout_reviews",[]):
                validate_review_bundle(root,layout_review)
            for paragraph_review in doc.get('paragraph_join_reviews',[]):
                validate_review_bundle(root,paragraph_review)
            validate_exact_comparisons(doc, pages, (folder / "raw/pdftotext.bin").read_bytes())
            validate_ocr_page_reviews(doc, pages)
        except ValueError as exc:
            errors.append(f"{pid}: {exc}")
        for block in doc["blocks"]:
            original = " ".join(originals[x]["text"].strip() for x in block["source_line_ids"])
            try:
                original = replay_block(doc, block, original)
            except ValueError as exc:
                errors.append(f"{pid}/{block['block_id']}: {exc}")
            if original != block["text"]:
                errors.append(f"{pid}/{block['block_id']}: unlogged text transformation")
        sections = {s["section_id"]: s for s in doc["sections"]}
        for s in doc["sections"]:
            seen = {s["section_id"]}; parent = s["parent_id"]
            while parent:
                if parent in seen or parent not in sections:
                    errors.append(f"{pid}: section hierarchy invalid"); break
                seen.add(parent); parent = sections[parent]["parent_id"]
            md = (folder / "sections" / (s["section_id"] + ".md")).read_bytes().decode("utf-8")
            label = "verified source boundary" if s["boundary_status"] == "verified" else "pending boundary review"
            text = exported_section_text(doc, s["section_id"])
            expected_text = f"<!-- {label}; {s['title']} -->\n" + text + "\n"
            expected_sql[(pid, s["section_id"])] = (s["parent_id"], s["title"], s["role"],
                                                   s["boundary_status"], digest(text.encode()))
            if md != expected_text:
                errors.append(f"{pid}/{s['section_id']}: section export mismatch")
        if verify_pdfs:
            pdf = Path(scope["source_root"]) / doc["source_relative_path"]
            if file_hash(pdf) != paper["source_sha256"]:
                errors.append(f"{pid}: source PDF changed")
        totals.update(papers=1, physical_pages=len(pages), source_lines=len(originals),
                      blocks=len(block_ids), sections=len(sections),
                      boundary_verified=sum(s["boundary_status"] == "verified" for s in doc["sections"]))
        defects.update(d["code"] for d in doc["defects"] if d.get("status") != "resolved")
    if work_root:
        preimages = read_json(root / "legacy-preimages.json")
        changed = [rel for rel, sha in preimages.items()
                   if (file_hash(work_root / rel) if (work_root / rel).is_file() else None) != sha]
        errors.extend(f"Protected legacy input changed: {x}" for x in changed)
        totals["protected_legacy_inputs_checked"] = len(preimages)
    con = sqlite3.connect(f"file:{(root / 'corpus.sqlite3').as_posix()}?mode=ro", uri=True)
    try:
        if con.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            errors.append("SQLite integrity invalid")
        if con.execute("SELECT COUNT(*) FROM papers").fetchone()[0] != len(expected):
            errors.append("SQLite paper denominator differs")
        seen = set()
        for pid, sid, parent, title, role, boundary, text, sha in con.execute("SELECT * FROM sections"):
            seen.add((pid, sid))
            actual = (parent, title, role, boundary, digest(text.encode()))
            if expected_sql.get((pid, sid)) != actual or sha != actual[-1]:
                errors.append(f"{pid}/{sid}: SQLite section view mismatch")
        if seen != set(expected_sql):
            errors.append("SQLite section membership differs")
        seen_fts = set()
        for pid, sid, title, text in con.execute("SELECT * FROM section_search"):
            key = (pid, sid); row = expected_sql.get(key)
            if key in seen_fts or not row or title != row[1] or digest(text.encode()) != row[-1]:
                errors.append(f"{pid}/{sid}: SQLite search view mismatch")
            seen_fts.add(key)
        if seen_fts != set(expected_sql):
            errors.append("SQLite search membership differs")
    finally:
        con.close()
    return {"dataset_id": cat.identity, "structural_integrity_pass": not errors, "errors": errors,
            "totals": dict(totals), "defects": dict(defects),
            "source_completeness_accepted": not errors and not defects and totals["papers"] == scope["paper_count"],
            "note": "Structural pass does not certify paragraph/section fidelity or AI reading."}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus-root", type=Path, required=True)
    p.add_argument("--work-root", type=Path)
    p.add_argument("--verify-pdfs", action="store_true")
    p.add_argument("--report", type=Path)
    args = p.parse_args()
    result = validate(args.corpus_root.resolve(), args.work_root, args.verify_pdfs)
    if args.report:
        json_new(args.report, result)
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if result["structural_integrity_pass"] else 1)
