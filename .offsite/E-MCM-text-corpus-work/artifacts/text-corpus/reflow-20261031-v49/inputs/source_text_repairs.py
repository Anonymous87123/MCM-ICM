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
    transcriptions = {}
    resolved = set()
    for op in review["operations"]:
        block = blocks.get(op.get("block_id"))
        if not block or not set(block["source_pages"]) <= checked or not op.get("reason"):
            raise ValueError("Text repair lacks checked source coverage")
        bid = block["block_id"]
        if bid in resolved:
            raise ValueError("Hyphen resolution must be the final operation for its block")
        if op.get("operation") == "literal_replace":
            transcriptions.setdefault(bid, []).append(op)
        elif op.get("operation") == "resolve_hyphen_join_review":
            chain = transcriptions.get(bid, [])
            # Separately stored keywords may contain the same checked printed
            # word wraps. Resolving their exact flag does not add them to the
            # author-text reading selection or approve a whole section.
            if (block["kind"] not in {"prose", "list", "mixed", "author_callout", "keywords"} or not chain or
                    op.get("transcription_operations_sha256") != digest(encoded(chain)) or
                    op.get("source_line_ids_sha256") != digest(encoded(block["source_line_ids"]))):
                raise ValueError("Hyphen resolution lacks exact source lines and prior literal transcriptions")
            resolved.add(bid)
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
    elif op["operation"] == "resolve_hyphen_join_review":
        # This explicit, hash-bound operation changes metadata only. A remaining
        # wrapped fragment blocks it, including a fragment at a page boundary.
        if re.search(r"[A-Za-z]-(?:\s|$)", text):
            raise ValueError("Hyphen resolution still contains a pending wrapped fragment")
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
            if op["operation"] == "resolve_hyphen_join_review":
                matching = [d for d in document["defects"] if d.get("block_id") == block["block_id"]
                            and d["code"] == "hyphen_join_review" and d.get("status") != "resolved"]
                if "hyphen_join_review" not in block.get("issues", []) or len(matching) != 1:
                    raise ValueError("Hyphen resolution requires exactly one existing block defect")
                block["issues"].remove("hyphen_join_review")
                matching[0].update(status="resolved", resolution="explicit source-checked wrap transcription",
                                   text_repair_review_sha256=rid)
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
    validate_hyphen_resolutions(document)


def validate_hyphen_resolutions(document):
    """A later mutation cannot retain an earlier wrap-resolution approval."""
    blocks = {b["block_id"]: b for b in document["blocks"]}
    for review in document.get("text_repair_reviews", []):
        for op in review["operations"]:
            if op["operation"] != "resolve_hyphen_join_review":
                continue
            block = blocks[op["block_id"]]
            matching = [d for d in document["defects"] if d.get("block_id") == block["block_id"]
                        and d["code"] == "hyphen_join_review"]
            if (digest(block["text"].encode()) != op["after_text_sha256"] or
                    digest(encoded(block["source_line_ids"])) != op["source_line_ids_sha256"] or
                    "hyphen_join_review" in block.get("issues", []) or len(matching) != 1 or
                    matching[0].get("status") != "resolved" or
                    matching[0].get("text_repair_review_sha256") != digest(encoded(review))):
                raise ValueError("Hyphen resolution no longer binds final block/defect")


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
    validate_hyphen_resolutions(document)
    for review in document.get("text_repair_reviews", []):
        check_review(document, review)
        for proof in review["evidence"]:
            path = (root / proof["path"]).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file() or file_hash(path) != proof["sha256"]:
                raise ValueError("Source-text repair evidence missing or modified")
