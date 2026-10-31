"""Versioned prose corpus primitives. No dependency on legacy learning artifacts."""
from __future__ import annotations

import hashlib
import json
import re
import statistics
from collections import Counter
from pathlib import Path

SCHEMA = 1
ROLES = ("abstract", "introduction", "assumptions", "notation", "data", "model",
         "results", "validation", "sensitivity", "discussion", "strengths_weaknesses",
         "conclusion", "recommendations", "memo", "appendix", "references",
         "contents", "ai_disclosure", "other")
ALIASES = {"summary": "abstract", "summary sheet": "abstract", "摘要": "abstract",
           "引言": "introduction", "introduction": "introduction", "结论": "conclusion",
           "假设": "assumptions", "结果": "results", "敏感性分析": "sensitivity"}
PROSE_KINDS = {"prose", "list", "heading", "mixed"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def encoded(value) -> bytes:
    # ASCII escapes preserve even malformed PDF glyph values in the raw layer.
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n").encode()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_new(path: Path, data: bytes | str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as f:
        f.write(data.encode("utf-8") if isinstance(data, str) else data)


def json_new(path: Path, value) -> None:
    write_new(path, encoded(value))


def rows(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def canonical_role(value: str) -> str:
    value = value.strip().casefold()
    return ALIASES.get(value, value)


def title_role(title: str, page: int) -> str:
    t = re.sub(r"^\s*(?:\d+(?:\.\d+)*[.)]?|[IVX]+[.)])\s+", "", title).strip().lower()
    if re.fullmatch(r"(?:executive )?(?:abstract|summary)(?: sheet)?[.:]?", t):
        return "abstract" if page <= 3 else "conclusion"
    patterns = [
        ("ai_disclosure", r"(?:report on|use of|usage of|generative)\s+ai|ai use|ai usage"),
        ("contents", r"^(?:table of )?contents$"),
        ("references", r"^(?:references|bibliography|works cited)\b"),
        ("appendix", r"^(?:appendix|appendices|supplement)\b"),
        ("introduction", r"\bintroduction\b|^background(?: and .*)?$|^problem restatement$"),
        ("strengths_weaknesses", r"\bstrengths?\b|\bweakness(?:es)?\b|\bshortcomings?\b"),
        ("sensitivity", r"\bsensitivity\b"),
        ("assumptions", r"\bassumptions?\b"),
        ("notation", r"\bnotations?\b|^symbols?$|^nomenclature$"),
        ("conclusion", r"\bconclusions?\b|\bclosing remarks\b"),
        ("recommendations", r"\brecommendations?\b|^policy suggestions"),
        ("memo", r"\bmemorandum\b|^memo\b|^letter\b|^report to\b"),
        ("validation", r"\bvalidation\b|\bverification\b|\bmodel (?:testing|evaluation)\b"),
        ("discussion", r"\bdiscussion\b|\bfurther work\b|\bfuture work\b"),
        ("results", r"\bresults?\b|\bsolutions?\b"),
        ("data", r"\bdata (?:collection|processing|preparation|analysis|sources?)\b"),
        ("model", r"\bmodels?\b|\bmodeling\b|\bmodelling\b|\balgorithms?\b"),
    ]
    return next((role for role, pattern in patterns if re.search(pattern, t)), "other")


def bad_unicode(text: str) -> bool:
    return any(c == "\ufffd" or 0xD800 <= ord(c) <= 0xDFFF for c in text)


def normalized_lines(lines: list[dict]) -> tuple[str, list[dict]]:
    """Only join line wraps; ambiguous hyphens remain intact and are flagged."""
    texts = [x["text"].strip() for x in lines]
    repairs = []
    out = ""
    for i, text in enumerate(texts):
        if i:
            repairs.append({"operation": "line_wrap_to_space", "left": lines[i-1]["line_id"],
                            "right": lines[i]["line_id"]})
        out += (" " if out and text else "") + text
    return out, repairs


def is_heading(line: dict, body_size: float) -> bool:
    t = line["text"].strip()
    if not t or len(t) > 170 or len(t.split()) > 22 or re.search(r"\.{3,}\s*\d+\s*$", t):
        return False
    if re.match(r"^(?:Figure|Fig\.|Table)\s*\d", t, re.I):
        return False
    role = title_role(t, line["page"])
    exact = re.fullmatch(r"(?:Abstract|Summary(?: Sheet)?|(?:Table of )?Contents|Introduction|"
                        r"Assumptions?|Notations?|References|Bibliography|Conclusion(?:s)?|"
                        r"Appendi(?:x|ces)(?:\s+[A-Z])?|Report on Use of AI)", t, re.I)
    numbered = bool(re.match(r"^(?:\d+(?:\.\d+)*[.)]?|[IVX]+[.)])\s+[A-Za-z]", t))
    emphasized = line["font_size"] >= body_size + .4 or line["bold"]
    title_like = (len(t.split()) <= 12 and not re.search(r"[.!?;]$", t)
                  and not re.match(r"^(?:We|Our|They|This|These|Then|Furthermore|Therefore|However|For|To)\b", t)
                  and sum(c.isalpha() or c.isspace() for c in t) / max(len(t), 1) > .7)
    # A paper title that mentions a model is not a model-section boundary.
    unnumbered = role != "other" and title_like and not (line["page"] == 1 and role == "model")
    return bool(exact or (emphasized and (numbered or unnumbered)))


def order_lines(lines: list[dict], width: float) -> tuple[list[dict], bool]:
    """Column bands, with full-width headings acting as barriers, not row interleave."""
    mid = width / 2
    left = [x for x in lines if x["bbox"][2] < mid + 8]
    right = [x for x in lines if x["bbox"][0] > mid - 8]
    if len(left) < 5 or len(right) < 5:
        return sorted(lines, key=lambda x: (round(x["bbox"][1], 1), x["bbox"][0])), False
    ly = [x["bbox"][1] for x in left]; ry = [x["bbox"][1] for x in right]
    overlap = min(max(ly), max(ry)) - max(min(ly), min(ry))
    if overlap < 80:
        return sorted(lines, key=lambda x: (x["bbox"][1], x["bbox"][0])), False
    narrow = {x["line_id"] for x in left + right}
    wide = sorted([x for x in lines if x["line_id"] not in narrow], key=lambda x: x["bbox"][1])
    out = []; remaining = list(left + right)
    for barrier in wide:
        band = [x for x in remaining if x["bbox"][1] < barrier["bbox"][1]]
        out.extend(sorted(band, key=lambda x: (x["bbox"][0] > mid - 8, x["bbox"][1], x["bbox"][0])))
        used = {x["line_id"] for x in band}
        remaining = [x for x in remaining if x["line_id"] not in used]
        out.append(barrier)
    out.extend(sorted(remaining, key=lambda x: (x["bbox"][0] > mid - 8, x["bbox"][1], x["bbox"][0])))
    return out, True


def furniture_key(text: str) -> str:
    return re.sub(r"\d+", "#", re.sub(r"\s+", " ", text.strip().lower()))


def make_document(meta: dict, pages: list[dict]) -> dict:
    lines = [line for page in pages for line in page["lines"]]
    sizes = [x["font_size"] for x in lines if len(x["text"].split()) >= 8]
    body_size = statistics.median(sizes) if sizes else 11
    repeated = Counter(furniture_key(x["text"]) for page in pages for x in page["lines"]
                       if x["bbox"][1] < 65 or x["bbox"][3] > page["height"] - 45)
    blocks = []; sections = []; defects = []; current = None; stack = []

    def new_section(title, role, level, origin):
        nonlocal current, stack
        sid = f"s{len(sections)+1:04d}"
        while stack and stack[-1][0] >= level:
            stack.pop()
        current = {"section_id": sid, "title": title, "role": role, "level": level,
                   "parent_id": stack[-1][1] if stack else None, "origin": origin,
                   "boundary_status": "pending", "block_ids": []}
        sections.append(current); stack.append((level, sid))

    # This is explicitly an unverified candidate, never a verified untitled abstract.
    new_section("Opening text (candidate summary)", "abstract", 1, "inferred-opening")
    for page in pages:
        ordered, multi = order_lines(page["lines"], page["width"])
        if multi:
            defects.append({"code": "column_order_review", "page": page["page"]})
        pending = []

        def flush(kind="prose"):
            nonlocal pending
            if not pending:
                return
            text, repairs = normalized_lines(pending)
            bid = f"b{len(blocks)+1:06d}"
            issues = []
            if bad_unicode(text):
                issues.append("unresolved_unicode")
            if any(re.search(r"[A-Za-z]-\s*$", x["text"]) for x in pending[:-1]):
                issues.append("hyphen_join_review")
            if any(0xE000 <= ord(c) <= 0xF8FF for c in text):
                issues.append("private_use_glyph_review")
            blocks.append({"block_id": bid, "section_id": current["section_id"], "kind": kind,
                           "text": text, "source_line_ids": [x["line_id"] for x in pending],
                           "source_pages": sorted({x["page"] for x in pending}),
                           "repairs": repairs, "issues": issues})
            current["block_ids"].append(bid)
            for issue in issues:
                defects.append({"code": issue, "block_id": bid, "page": pending[0]["page"]})
            pending = []

        previous = None
        for line in ordered:
            t = line["text"].strip()
            edge = line["bbox"][1] < 65 or line["bbox"][3] > page["height"] - 45
            header = bool(re.search(r"^(?:Team\s*(?:Number|Control Number|#|No\.?|:)|Page\s+\d+\s+of\b)", t, re.I))
            watermark = bool(re.search(r"精品数模|关注.*公众号|数学建模.*(?:资料|交流)", t))
            repeat = edge and len(t) < 160 and repeated[furniture_key(t)] >= max(3, len(pages) // 3)
            if not t or header or watermark or repeat:
                flush(); pending = [line]; flush("furniture"); previous = None; continue
            heading = is_heading(line, body_size)
            if current["role"] == "contents" and line["font_size"] < body_size + .4 and not line["bold"]:
                heading = False  # A TOC entry is not a new source section.
            if heading:
                flush()
                number = re.match(r"^(\d+(?:\.\d+)*)[.)]?\s+", t)
                level = number.group(1).count(".")+1 if number else 1
                role = title_role(t, page["page"])
                # An explicit abstract supersedes the empty inferred section, not its text.
                new_section(t, role, level, "printed-heading")
                pending = [line]; flush("heading"); previous = None; continue
            if current["role"] == "abstract" and page["page"] > 3:
                flush(); new_section("Unresolved body text", "other", 1, "inferred-body")
            kind = "prose"
            if re.match(r"^(?:Figure|Fig\.|Table)\s*\d+[.:\s]", t, re.I):
                kind = "caption"
            elif current["role"] in {"contents", "references", "ai_disclosure"}:
                kind = current["role"]
            elif re.match(r"^(?:Keywords?|Key words)\s*[:：]", t, re.I):
                kind = "keywords"
            elif page["page"] == 1 and line["font_size"] > body_size * 1.35 and len(t.split()) < 30:
                kind = "title"
            # No minimum word/letter filter: short and mixed prose stays readable.
            if kind != "prose":
                flush(); pending = [line]; flush(kind); previous = None; continue
            if previous is not None:
                gap = line["bbox"][1] - previous["bbox"][3]
                indent = line["bbox"][0] - previous["bbox"][0]
                native_change = line["native_block"] != previous["native_block"]
                if native_change or gap > body_size * .6 or (indent > body_size and re.search(r"[.!?:;]$", previous["text"].strip())):
                    flush()
            pending.append(line); previous = line
        flush()
        if not page["lines"]:
            defects.append({"code": "native_text_empty_ocr_required", "page": page["page"]})
        if page.get("comparison", {}).get("status") != "agreement":
            defects.append({"code": "cross_engine_review", "page": page["page"]})
    # Do not guess cross-page joins: mark and retain both fragments until reviewed.
    prose = [b for b in blocks if b["kind"] in {"prose", "mixed"}]
    for a, b in zip(prose, prose[1:]):
        if (a["section_id"] == b["section_id"] and a["source_pages"][-1] + 1 == b["source_pages"][0]
                and not re.search(r"[.!?:;][\"')\]]*$", a["text"])):
            defects.append({"code": "cross_page_join_review", "left": a["block_id"], "right": b["block_id"]})
    for section in sections:
        defects.append({"code": "section_boundary_pending", "section_id": section["section_id"]})
    return {"schema_version": SCHEMA, **meta, "status": "machine-draft", "body_font_size": body_size,
            "sections": sections, "blocks": blocks, "defects": defects,
            "verified_absent_roles": [], "formula_review": "paused", "figure_distillation": "paused"}


def section_blocks(document: dict, selected: list[str]) -> list[dict]:
    wanted = set(selected)
    for section in document["sections"]:
        if section["parent_id"] in wanted:
            wanted.add(section["section_id"])
    return [b for b in document["blocks"] if b["section_id"] in wanted and b["kind"] in PROSE_KINDS]


def section_text(document: dict, selected: list[str]) -> str:
    return "\n\n".join(b["text"] for b in section_blocks(document, selected))


def export_document(target: Path, document: dict) -> None:
    json_new(target / "document.json", document)
    full = [f"# {document['paper_id']}\n\nStatus: machine-draft; not source-verified.\n"]
    for b in document["blocks"]:
        # All non-prose is retained and identified, not silently thrown away.
        full.append(f"<!-- {b['block_id']} | {b['kind']} | pages {b['source_pages']} -->\n{b['text']}")
    write_new(target / "full.md", "\n\n".join(full) + "\n")
    for s in document["sections"]:
        write_new(target / "sections" / (s["section_id"] + ".md"),
                  f"<!-- pending boundary review; {s['title']} -->\n" + section_text(document, [s["section_id"]]) + "\n")
