"""Audit current segmentation rules against every frozen page without a corpus copy.

The create-only report is a prospective diagnostic, not a source approval. It
checks source-line ownership and existing review preimages before a new build.
"""
from __future__ import annotations

import argparse
import copy
import json
from collections import Counter
from pathlib import Path

from audit_text_section_candidates import abstract_findings
from corpus_reader import Catalog
from resegment_text_corpus import apply_reviews
from source_text_repairs import apply_text_repairs
from source_layout_reviews import apply_layout_reviews
from source_absence_reviews import apply_absence_reviews
from text_corpus import (digest, file_hash, json_new, make_document, rows,
                         section_blocks, section_text)


def preview(root: Path):
    catalog = Catalog(root)
    implementation = {name: file_hash(Path(__file__).with_name(name)) for name in
                      ("text_corpus.py", "preview_text_resegmentation.py", "source_layout_reviews.py",
                       "source_absence_reviews.py", "source_text_repairs.py", "resegment_text_corpus.py",
                       "audit_text_section_candidates.py", "corpus_queries.py")}
    totals = Counter(); findings = Counter(); papers = []; errors = []
    for paper in catalog.papers:
        old = catalog.document(paper["paper_id"])
        raw_path = root / "papers" / paper["paper_id"] / "raw/pages.jsonl"
        if file_hash(raw_path) != old["raw_pages_sha256"]:
            raise ValueError("Frozen raw-page evidence changed")
        pages = rows(raw_path)
        meta = {k: old[k] for k in ("paper_id", "problem_type", "year", "queue_position",
                "page_count", "source_relative_path", "source_sha256", "raw_pages_sha256")}
        working_pages=copy.deepcopy(pages)
        layouts=apply_layout_reviews(meta,working_pages,old.get("layout_reviews",[]))
        doc = make_document(meta, working_pages, improved=True)
        doc["layout_reviews"]=layouts
        try:
            apply_text_repairs(doc, old.get("text_repair_reviews", []))
            apply_reviews(doc, [s["review"] for s in old["sections"] if s.get("review")])
            apply_absence_reviews(doc,list(old.get("absence_reviews",{}).values()))
        except ValueError as exc:
            errors.append({"paper_id": paper["paper_id"], "error": str(exc)})
        raw_ids = [line["line_id"] for page in pages for line in page["lines"]]
        owned_ids = [lid for b in doc["blocks"] for lid in b["source_line_ids"]]
        owned_ids += [item["line_id"] for item in doc["excluded_source_lines"]]
        if Counter(raw_ids) != Counter(owned_ids) or len(set(raw_ids)) != len(raw_ids):
            errors.append({"paper_id": paper["paper_id"], "error": "Source-line ownership differs"})
        selected = [s["section_id"] for s in doc["sections"] if s["role"] == "abstract"]
        previous = [s["section_id"] for s in old["sections"] if s["role"] == "abstract"]
        text = section_text(doc, selected); prior = section_text(old, previous)
        found = abstract_findings(doc); findings.update(f["code"] for f in found)
        tocs = [d for d in doc["defects"] if d.get("code")=="contents_page_boundary_review" and d.get("inference")]
        old_heading_lines = {tuple(b["source_line_ids"]): b for b in old["blocks"] if b["kind"] == "heading"}
        new_heading_lines = {tuple(b["source_line_ids"]) for b in doc["blocks"] if b["kind"] == "heading"}
        removed = [dict(source_line_ids=list(ids), text=b["text"], source_pages=b["source_pages"])
                   for ids, b in old_heading_lines.items() if ids not in new_heading_lines]
        totals.update(papers=1, physical_pages=len(pages), source_lines=len(raw_ids),
                      nonempty_abstract_candidates=bool(text),
                      changed_abstract_candidates=(text != prior),
                      inferred_contents_pages=len(tocs), removed_heading_candidates=len(removed))
        papers.append({"paper_id": paper["paper_id"], "queue_position": paper["queue_position"],
                       "source_sha256": old["source_sha256"], "raw_pages_sha256": old["raw_pages_sha256"],
                       "old_document_sha256": paper["document_sha256"], "abstract_text_sha256": digest(text.encode()),
                       "abstract_chars": len(text), "previous_abstract_chars": len(prior),
                       "abstract_source_pages": sorted({p for b in section_blocks(doc, selected) for p in b["source_pages"]}),
                       "findings": found, "inferred_contents_pages": tocs, "removed_heading_candidates": removed})
        if paper["queue_position"] % 50 == 0:
            print(json.dumps({"prospective_papers_checked": paper["queue_position"]}), flush=True)
    if any(file_hash(Path(__file__).with_name(name)) != sha for name, sha in implementation.items()):
        raise ValueError("Segmentation implementation changed during prospective audit; report not frozen")
    return {"parent_dataset_id": catalog.identity, "implementation_sha256": implementation,
            "totals": dict(totals), "finding_counts": dict(findings), "errors": errors, "papers": papers,
            "source_completeness_accepted": False,
            "meaning": "Prospective machine rules only; no review state is promoted or source artifact overwritten."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise ValueError("Prospective report exists; choose a new version")
    result = preview(args.corpus_root.resolve()); json_new(args.report, result)
    print(json.dumps({k: v for k, v in result.items() if k != "papers"}))
