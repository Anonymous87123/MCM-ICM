"""Exhaustive candidate-quality inventory, not a source-fidelity certificate.

Find omitted same-page abstract siblings and heading-only candidates without
discarding them or choosing a few good samples. Formula/figure tasks stay paused.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

from corpus_reader import Catalog
from text_corpus import PROSE_KINDS, json_new, section_blocks


def abstract_findings(doc):
    sections = {s["section_id"]: s for s in doc["sections"]}
    ids = [s["section_id"] for s in doc["sections"] if s["role"] == "abstract"]
    selected = section_blocks(doc, ids); wanted = {b["block_id"] for b in selected}
    prose = [b for b in selected if b["kind"] != "heading"]
    findings = []
    toc_blocks = [b["block_id"] for b in selected if len(re.findall(r"\.{5,}\s*\d+",b["text"])) >= 3]
    if toc_blocks:
        findings.append({"code":"abstract_contains_possible_contents_entries","block_ids":toc_blocks,
                         "meaning":"Repeated dotted-leader entries inside abstract selection need source-bound exclusion/resectioning."})
    if not selected:
        findings.append({"code": "abstract_verified_absent" if Catalog.absence_valid(doc,"abstract")
                         else "abstract_empty_unresolved"})
    elif not prose:
        findings.append({"code": "abstract_heading_only", "block_ids": sorted(wanted)})
    prose_pages=sorted({p for b in prose for p in b["source_pages"]})
    if len(prose_pages)>1:
        findings.append({"code":"abstract_multiple_page_scope_review","physical_pages":prose_pages,
                         "meaning":"May be a legitimate long abstract, or a following letter/title/brochure. Review every page boundary; do not truncate automatically."})
    fragment_pairs=[]
    for left,right in zip(prose,prose[1:]):
        if (left["kind"] in {"prose","mixed"} and right["kind"] in {"prose","mixed"} and
                left["section_id"]==right["section_id"] and
                left["source_pages"][-1]==right["source_pages"][0] and
                not re.search(r"[.!?:;][\"')\]\u201d\u2019]*$",left["text"].strip()) and
                re.match(r"^[a-z]",right["text"].strip())):
            fragment_pairs.append([left["block_id"],right["block_id"]])
    if len(fragment_pairs)>=4:
        findings.append({"code":"abstract_possible_line_fragmentation","block_pairs":fragment_pairs,
                         "meaning":"Repeated nonterminal-to-lowercase paragraph breaks need source line-spacing/paragraph checks. No text is joined by this diagnostic."})
    salutations=[b["block_id"] for b in prose if re.fullmatch(
        r"Dear\s+(?:editor(?:s)?|sir(?:\s+or\s+madam)?|madam)[,:]|Your(?:s)?\s+sincerely[,.]?",
        b["text"].strip(),re.I)]
    if salutations:
        findings.append({"code":"abstract_possible_letter_contamination","block_ids":salutations,
                         "meaning":"A separate author letter must be retained and resectioned, not silently deleted or counted as abstract style."})
    form_blocks=[b["block_id"] for b in selected if re.search(
        r"For office use only|[TF][1-4]\s+_{3,}|Mathematical Contest in Modeling",b["text"],re.I)]
    if form_blocks:
        findings.append({"code":"abstract_possible_form_contamination","block_ids":form_blocks,
                         "meaning":"Printed form fields/banner must be source-classified separately from author prose. No deletion by this audit."})
    anchors = [s["section_id"] for s in doc["sections"] if s["role"] == "abstract" and s.get("origin") == "printed-heading"]
    for sid in anchors:
        positions = [i for i,b in enumerate(doc["blocks"]) if b["section_id"] == sid]
        if not positions:
            continue
        start = min(positions); page = doc["blocks"][start]["source_pages"][0]
        omitted = []
        for block in doc["blocks"][start:]:
            if block["source_pages"][0] > page:
                break
            section = sections[block["section_id"]]
            if block["kind"] == "heading" and section["role"] in {"introduction", "contents", "references"}:
                break
            if block["kind"] in PROSE_KINDS and block["block_id"] not in wanted:
                omitted.append(block["block_id"])
        if omitted:
            findings.append({"code": "possible_abstract_envelope_exclusion", "anchor_section_id": sid,
                             "physical_page": page, "block_ids": omitted,
                             "meaning": "Review raw source; not every same-page sibling is necessarily abstract prose."})
    return findings


def audit(root: Path):
    catalog = Catalog(root); papers = []; counts = Counter(); legacy_flags = Counter(); totals = Counter()
    selection = {s["paper_id"]:s for s in catalog.select("abstract")}
    for paper in catalog.papers:
        doc = catalog.document(paper["paper_id"]); findings = abstract_findings(doc)
        counts.update(f["code"] for f in findings)
        flags = Counter(d["code"] for d in doc.get("defects",[]) if d.get("status") != "resolved")
        legacy_flags.update(flags)
        totals.update(papers=1,physical_pages=doc["page_count"],
                      source_boundary_verified=sum(s["boundary_status"] == "verified" for s in doc["sections"]))
        papers.append({"paper_id":doc["paper_id"],"queue_position":paper["queue_position"],
                       "source_sha256":doc["source_sha256"],"document_sha256":paper["document_sha256"],
                       "abstract_selection":selection[doc["paper_id"]],"findings":findings,"open_source_flags":dict(flags)})
    return {"dataset_id":catalog.identity,"totals":dict(totals),"finding_counts":dict(counts),
            "open_source_flag_counts":dict(legacy_flags),"papers":papers,
            "meaning":"Whole-scope diagnostic inventory only; not section completeness or AI comprehension.",
            "source_completeness_accepted":False,"formula_verification":"paused","figure_distillation":"paused"}


if __name__ == "__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--corpus-root",type=Path,required=True);p.add_argument("--report",type=Path,required=True)
    args=p.parse_args();result=audit(args.corpus_root.resolve());json_new(args.report,result)
    print(json.dumps({k:v for k,v in result.items() if k != "papers"}))
