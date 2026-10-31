"""Replayable, source-bound literal transcription and block classification.

This is not a prose rewriter. Raw page evidence stays unchanged. Each short
character replacement is explicit, counted, hash-bound and backed by a local
source-text review. Review files do not by themselves certify a whole section.
"""
from __future__ import annotations

import re
from pathlib import Path

from text_corpus import bad_unicode, digest, encoded, file_hash


def check_review(document, review):
    if (review.get("paper_id") != document["paper_id"] or
            review.get("source_sha256") != document["source_sha256"] or
            review.get("raw_pages_sha256") != document["raw_pages_sha256"] or
            not review.get("reviewer") or not review.get("reason") or
            not review.get("operations") or not review.get("evidence")):
        raise ValueError("Incomplete or stale source-text repair review")
    checked = set(review.get("checked_pages", []))
    blocks = {b["block_id"]: b for b in document["blocks"]}
    for op in review["operations"]:
        block = blocks.get(op.get("block_id"))
        if not block or not set(block["source_pages"]) <= checked or not op.get("reason"):
            raise ValueError("Text repair lacks checked source coverage")
    for proof in review["evidence"]:
        if not proof.get("description") or not re.fullmatch(r"[0-9a-f]{64}", proof.get("sha256", "")):
            raise ValueError("Text repair lacks source evidence binding")


def operation(text, kind, op):
    if digest(text.encode()) != op.get("before_text_sha256"):
        raise ValueError("Text repair preimage changed")
    if op["operation"] == "literal_replace":
        old, new, count = op["old"], op["new"], op["count"]
        if (not isinstance(old, str) or not isinstance(new, str) or
                not 1 <= len(old) <= 8 or not 1 <= len(new) <= 8 or
                old == new or type(count) is not int or count < 1 or text.count(old) != count):
            raise ValueError("Literal transcription must have an exact short replacement/count")
        text = text.replace(old, new)
    elif op["operation"] == "classify":
        allowed = {"prose", "list", "heading", "mixed", "front_matter", "title",
                   "furniture", "caption", "contents", "references", "ai_disclosure", "keywords"}
        if kind != op["from_kind"] or op["to_kind"] not in allowed or kind == op["to_kind"]:
            raise ValueError("Classification repair preimage/kind invalid")
        kind = op["to_kind"]
    else:
        raise ValueError("Unknown source-text repair operation")
    if digest(text.encode()) != op.get("after_text_sha256"):
        raise ValueError("Text repair postimage differs")
    return text, kind


def apply_text_repairs(document, reviews):
    blocks = {b["block_id"]: b for b in document["blocks"]}
    for review in reviews:
        if review["paper_id"] != document["paper_id"]:
            continue
        check_review(document, review)
        rid = digest(encoded(review))
        if any(digest(encoded(r)) == rid for r in document.get("text_repair_reviews", [])):
            raise ValueError("Source-text repair already applied")
        for op in review["operations"]:
            block = blocks[op["block_id"]]
            before_kind = block["kind"]
            text, kind = operation(block["text"], before_kind, op)
            block.setdefault("pre_repair_kind", before_kind)
            block["text"], block["kind"] = text, kind
            ids = block.setdefault("text_repair_review_ids", [])
            if rid not in ids:
                ids.append(rid)
            for issue, remains in (
                    ("private_use_glyph_review", any(0xE000 <= ord(c) <= 0xF8FF for c in text)),
                    ("unresolved_unicode", bad_unicode(text))):
                if issue in block.get("issues", []) and not remains:
                    block["issues"].remove(issue)
                    for defect in document["defects"]:
                        if defect.get("block_id") == block["block_id"] and defect["code"] == issue:
                            defect.update(status="resolved", resolution="literal source transcription",
                                          text_repair_review_sha256=rid)
        document.setdefault("text_repair_reviews", []).append(review)


def replay_block(document, block, original):
    """Reconstruct final bytes from native lines, rejecting missing/extra repairs."""
    kind = block.get("pre_repair_kind", block["kind"])
    applied = []
    for review in document.get("text_repair_reviews", []):
        check_review(document, review)
        relevant = [op for op in review["operations"] if op["block_id"] == block["block_id"]]
        if relevant:
            applied.append(digest(encoded(review)))
        for op in relevant:
            original, kind = operation(original, kind, op)
    if applied != block.get("text_repair_review_ids", []) or kind != block["kind"]:
        raise ValueError("Source-text repair log/classification differs")
    return original


def validate_evidence(root: Path, document):
    for review in document.get("text_repair_reviews", []):
        check_review(document, review)
        for proof in review["evidence"]:
            path = (root / proof["path"]).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file() or file_hash(path) != proof["sha256"]:
                raise ValueError("Source-text repair evidence missing or modified")
