"""Versioned prose corpus primitives. No dependency on legacy learning artifacts."""
from __future__ import annotations

import hashlib
import json
import re
import statistics
from collections import Counter
from pathlib import Path

SCHEMA = 1
ROLES = ("abstract", "introduction", "problem_restatement", "problem_analysis", "assumptions", "notation", "data", "model",
         "results", "validation", "sensitivity", "discussion", "strengths_weaknesses",
         "conclusion", "recommendations", "memo", "appendix", "references",
         "contents", "ai_disclosure", "improvements", "other")
ALIASES = {"summary": "abstract", "summary sheet": "abstract", "摘要": "abstract",
           "引言": "introduction", "introduction": "introduction", "结论": "conclusion",
           "假设": "assumptions", "模型假设":"assumptions", "model_assumptions":"assumptions",
           "问题重述":"problem_restatement", "问题分析":"problem_analysis", "符号说明":"notation",
           "问题建立与求解":"model_building_and_solution", "敏感性与检验":"sensitivity_validation",
           "改进与评价":"improvements_evaluation", "全部作者文字":"all_author_text",
           "全文":"all_author_text", "结果": "results", "敏感性分析": "sensitivity",
           **{f"问题{i}建立与求解":f"task_{i}" for i in range(1,5)}}
PROSE_KINDS = {"prose", "list", "heading", "mixed", "author_callout"}
CHAPTER_VIEW_POLICY = "query-selected-v1"
HEADING_NUMBER = (r"(?:\d{1,2}(?:\.\d{1,2})*(?:-[a-z])?[.)]?|"
                  r"[IVXLCDM]+(?:\.\d{1,2})*[.)]?|[A-Z]\s*\d{1,2}[.)]?)")


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
    t = re.sub(r"^\s*"+HEADING_NUMBER+r"\s+", "", title).strip().lower()
    if page <= 3 and re.search(r"\bsummary sheet\s*$", t):
        return "abstract"
    if page <= 3 and re.fullmatch(r"\d{4} mathematical contest in modeling \((?:mcm|icm)\) summary(?: sheet)?",title.strip(),re.I):
        return "abstract"  # The word Sheet may be on the next printed line.
    if re.fullmatch(r"(?:executive )?(?:abstract|summary)(?: sheet)?[.:]?", t):
        return "abstract" if page <= 3 else "conclusion"
    patterns = [
        ("ai_disclosure", r"(?:report on|use of|usage of|generative)\s+ai|ai use|ai usage"),
        ("contents", r"^(?:table of )?contents?$"),
        ("references", r"^(?:references?|bibliograph(?:y|ies)|works cited|参考文献|参考资料)[\s.:：]*$"),
        ("appendix", r"^(?:appendix|appendices|supplement)\b"),
        ("problem_restatement",r"^(?:restatement of (?:the )?problem|problem restatement|problem (?:description|statement)|问题重述)$"),
        ("problem_analysis",r"^(?:analysis of (?:the )?problem|problem analysis|breaking down the problem|问题分析)$"),
        ("improvements",r"\b(?:improvements?|refinements?|extensions?)\b|模型改进"),
        ("introduction", r"\bintroduction\b|^background(?: and .*)?$"),
        ("strengths_weaknesses", r"\bstrengths?\b|\bweakness(?:es)?\b|\bshortcomings?\b"),
        ("sensitivity", r"\bsensitivity\b"),
        ("assumptions", r"\bassumptions?\b"),
        ("notation", r"\bnotations?\b|^symbols?$|^nomenclatures?$"),
        ("conclusion", r"\bconclusions?\b|\bclosing remarks\b"),
        ("recommendations", r"\brecommendations?\b|^policy suggestions"),
        ("memo", r"\bmemorandum\b|^memo\b|^letter\b|^a letter to\b|^report to\b"),
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
    if not t or len(t) > 170 or len(t.split()) > 22 or re.search(r"(?:[.·\-]\s*){3,}", t):
        return False
    if re.match(r"^(?:Figure|Fig\.|Table)\s*\d", t, re.I):
        return False
    if re.match(r"^[•●➢\-–]\s*", t):
        return False  # A bold list lead-in is still part of the current paragraph/section.
    role = title_role(t, line["page"])
    exact = re.fullmatch(r"(?:Abstract|Summary(?: Sheet)?|(?:Table of )?Contents?|Introduction|"
                        r"Assumptions?|Notations?|References?|Bibliograph(?:y|ies)|参考文献|参考资料|Conclusion(?:s)?|"
                        r"Appendi(?:x|ces)(?:\s+[A-Z])?|Report on Use of AI)", t, re.I)
    form_heading = line["page"] <= 3 and re.fullmatch(
        r"\d{4} Mathematical Contest in Modeling \((?:MCM|ICM)\) Summary(?: Sheet)?", t, re.I)
    # Some printed appendices have exactly the body font. A named colon title
    # must end bibliography ownership; ordinary sentences referring to an
    # appendix remain prose. This is still a pending source-boundary candidate.
    named_appendix = (line['font_size'] >= body_size and re.fullmatch(
        r"Appendi(?:x|ces)(?:\s+(?:[A-Z]|\d{1,2}|[IVXLCDM]+))?\s*[:：]\s*[A-Z][^.!?;]+", t))
    prefix = re.match(r"^"+HEADING_NUMBER+r"\s+(?=[A-Za-z])", t)
    if not prefix:
        prefix = re.match(r"^\d{1,2}(?:\.\d{1,2})+[.)]?(?=[A-Z])",t)
    emphasized = line["font_size"] >= body_size + .4 or line["bold"]
    # Bold is common throughout a summary, not evidence that each wrapped line
    # mentioning a model/result is a heading. Keep sentence punctuation, numeric
    # results and lowercase continuations in their original paragraph instead.
    title_like = (len(t.split()) <= 12 and not re.search(r"[.!?;]", t)
                  and not re.match(r"^[a-z]|^\d(?!-D\b)", t)
                  and not re.match(r"^(?:We|Our|They|This|These|Then|Furthermore|Therefore|However|For|To|"
                                   r"Afterwards|Finally|Before|Based|In|As|Also|According|By|Fourthly)\b", t)
                  and not re.search(r"\b(?:are|is|were|was|have|has|showed|indicate|indicates|reveal|reveals|"
                                    r"confirms|confirmed|demonstrated|performed)\b", t, re.I)
                  and not re.match(r"^(?:Keywords?|Key words)\s*[:：]", t, re.I)
                  and not re.search(r"[:：]\s*\(?[ivx]+\)", t, re.I)
                  and sum(c.isalpha() or c.isspace() for c in t) / max(len(t), 1) > .7)
    # A paper title that mentions a model is not a model-section boundary.
    unnumbered = role != "other" and title_like and not (line["page"] == 1 and role == "model")
    # Questions and comma-containing chapter titles are legitimate. Reject
    # numeric-result sentences by their clause/length, not by punctuation alone.
    numbered_title = t[prefix.end():] if prefix else ""
    question = re.match(r"^(?:Where|Why|What|How|Which|When|Can|Is|Does|Do|Are)\b",numbered_title,re.I)
    clause = re.search(r"\b(?:are|is|were|was|have|has|showed|indicate|indicates|reveal|reveals|"
                       r"confirms|confirmed|demonstrated|performed)\b",numbered_title,re.I)
    numbered = (prefix is not None and not re.match(r"^[a-z]",numbered_title) and
                len(numbered_title.split()) <= 14 and (not clause or question))
    return bool(exact or form_heading or named_appendix or (emphasized and (numbered or unnumbered)))


def dense_untitled_contents(lines: list[dict], page: int) -> dict | None:
    """Conservative opening-page TOC candidate, never a source review approval.

    Separate chapter-number fragments are allowed; author prose outside the
    entries prevents whole-page classification. Every line stays in raw/blocks.
    """
    if page > 3:
        return None
    nonempty = [x for x in lines if x["text"].strip()]
    entries = [x for x in nonempty if re.search(
        r"[A-Za-z].*(?:[.\-]\s*){5,}\s*\d+\s*$", x["text"].strip())]
    fragments = [x for x in nonempty if re.fullmatch(r"\d{1,2}(?:\.\d{1,2})*[.)]?", x["text"].strip())]
    denominator = len(nonempty) - len(fragments)
    other = [x for x in nonempty if x not in entries and x not in fragments]
    prose = [x for x in other if len(x["text"].split()) >= 20 and not re.match(
        r"^(?:Team\s*(?:Number|Control Number|#|No\.?|:)|Page\s+\d+\s+of\b)", x["text"].strip(), re.I)]
    if len(entries) < 8 or len(entries) / max(denominator, 1) < .75 or prose:
        return None
    return {"rule": "dense-untitled-opening-contents-v1", "entry_line_ids": [x["line_id"] for x in entries],
            "number_fragment_line_ids": [x["line_id"] for x in fragments],
            "entry_count": len(entries), "nonempty_line_count": len(nonempty),
            "review_status": "machine-candidate; source boundary check still required"}


def prose_flow_line(line: dict) -> dict:
    """Use ordinary prose geometry when an inline math font has a tall bbox.

    This changes a working copy's vertical flow box only. Raw evidence, text,
    horizontal geometry and inline glyph order are untouched. Math-only lines
    and sparse labels cannot establish a prose baseline. Every inference remains
    an explicit source-review candidate, never a formula or source approval.
    """
    if line.get("flow_geometry_candidate",{}).get("rule")=="pdf-span-origin-flow-v1":
        return line  # Exact source-origin sidecar already supplies the candidate.
    spans = line.get("spans", [])
    math = [i for i, s in enumerate(spans) if re.search(
        r"math|symbol|mt\s*extra", s.get("font", ""), re.I) and s.get("text", "").strip()]
    ordinary = [i for i, s in enumerate(spans) if i not in math and
                re.search(r"[A-Za-z]{2,}", s.get("text", ""))]
    words = re.findall(r"[A-Za-z]{2,}", " ".join(spans[i]["text"] for i in ordinary))
    if not math or len(words) < 4 or sum(map(len, words)) < 16:
        return line
    if any(len(spans[i].get("bbox", [])) != 4 for i in math + ordinary):
        return line
    top = statistics.median(spans[i]["bbox"][1] for i in ordinary)
    bottom = statistics.median(spans[i]["bbox"][3] for i in ordinary)
    height = bottom - top
    if height <= 0 or any(abs(spans[i]["bbox"][1]-top) > height*.25 or
                          abs(spans[i]["bbox"][3]-bottom) > height*.25 for i in ordinary):
        return line
    outliers = [i for i in math if spans[i]["bbox"][3]-spans[i]["bbox"][1] > height*2 and
                (top-spans[i]["bbox"][1] > height*.5 or spans[i]["bbox"][3]-bottom > height*.5)]
    if not outliers:
        return line
    # All nonempty non-outlier spans must agree with the prose baseline. A
    # separate displayed expression or drop-cap cannot be silently collapsed.
    if any(s.get("text", "").strip() and i not in outliers and
           (s["bbox"][1] < top-height*.35 or s["bbox"][3] > bottom+height*.35)
           for i, s in enumerate(spans)):
        return line
    bbox = [line["bbox"][0], top, line["bbox"][2], bottom]
    return dict(line, bbox=bbox, flow_geometry_candidate={
        "rule": "ordinary-prose-baseline-with-tall-inline-math-v1",
        "source_line_id": line["line_id"], "raw_bbox": list(line["bbox"]),
        "flow_bbox": bbox, "prose_span_indices": ordinary, "outlier_span_indices": outliers})


def order_lines(lines: list[dict], width: float) -> tuple[list[dict], bool]:
    """Column bands, with full-width headings acting as barriers, not row interleave."""
    mid = width / 2
    left = [x for x in lines if x["bbox"][2] < mid + 8]
    left_ids = {x["line_id"] for x in left}
    right = [x for x in lines if x["bbox"][0] > mid - 8 and x["line_id"] not in left_ids]
    def prose_candidate(x):
        return x["font_size"] >= 6 and len(re.findall(r"[A-Za-z]{2,}", x["text"])) >= 4
    left_prose = [x for x in left if prose_candidate(x)]
    right_prose = [x for x in right if prose_candidate(x)]
    if len(left_prose) < 5 or len(right_prose) < 5:
        return sorted(lines, key=lambda x: (round(x["bbox"][1], 1), x["bbox"][0])), False
    ly = [x["bbox"][1] for x in left_prose]; ry = [x["bbox"][1] for x in right_prose]
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


def prose_gap_limit(ordered: list[dict], body_size: float) -> tuple[float, dict | None]:
    """Recognize repeated wide line spacing, not a paragraph at every PDF block.

    Only long, same-font, horizontally aligned nonterminal prose wraps support
    a baseline. Sparse complete sentences cannot establish an expanded baseline.
    This remains a machine candidate; a review flag preserves uncertainty.
    """
    limit = body_size * .6
    samples = []
    for left, right in zip(ordered, ordered[1:]):
        gap = right["bbox"][1] - left["bbox"][3]
        if (len(left["text"].split()) >= 8 and len(right["text"].split()) >= 6 and
                not re.search(r"[.!?:;][\"')\]\u201d\u2019]*$", left["text"].strip()) and
                all(abs(x["font_size"]-body_size) < 1.5 and
                    x["bbox"][2]-x["bbox"][0] >= body_size*20 for x in (left,right)) and
                abs(left["bbox"][0]-right["bbox"][0]) <= body_size*1.5 and
                0 <= gap <= body_size*1.5 and
                not is_heading(left,body_size) and not is_heading(right,body_size)):
            samples.append(gap)
    if len(samples) < 5:
        return limit,None
    baseline = statistics.median(samples)
    consistent = [x for x in samples if abs(x-baseline) <= body_size*.15]
    if baseline <= limit or len(consistent)/len(samples) < .75:
        return limit,None
    return baseline+body_size*.35, {"rule":"repeated-wide-prose-line-spacing-v1",
            "baseline_gap":baseline,"sample_count":len(samples),"consistent_count":len(consistent)}


def competition_instruction(text):
    return bool(re.match(r"^(?:(?:Sheet\s+)?\(Attach a copy of this page to (?:each copy of )?your solution paper\.\)|"
                         r"Type a summary of your results on this page\. Do not include|"
                         r"the name of your school, advisor, or team members on this page\.)\s*$",text,re.I))


def competition_form_line_ids(pages):
    """Identify only pure form fragments before author prose on opening pages.

    A cluster of printed form labels is required before standalone control
    numbers, problem letters or years qualify. Author sentences remain intact.
    """
    ids=set()
    label=re.compile(r"(?:For office use only|[TF][1-4]\s+_+|Problem Chosen|"
                     r"(?:Team|Group)\s*(?:Control\s*)?(?:Number|#|No\.?)\s*:?\s*\d*|"
                     r"Team Control|Number)",re.I)
    banner=re.compile(r"(?:\d{4}\s+)?Mathematical Contest in Modeling \((?:MCM|ICM|MCM/ICM)\) Summary(?: Sheet)?",re.I)
    for page in pages[:3]:
        ordered=sorted((x for x in page["lines"] if x["text"].strip() and not x.get("superseded_by_ocr")),
                       key=lambda x:(x["bbox"][1],x["bbox"][0]))
        labels=[x for x in ordered if label.fullmatch(x["text"].strip())]
        if len(labels)<3 or not any(re.fullmatch(r"For office use only|Problem Chosen",x["text"].strip(),re.I) for x in labels):
            continue
        body_starts=[x["bbox"][1] for x in ordered if len(x["text"].split())>=16 and
                     not label.fullmatch(x["text"].strip()) and not banner.fullmatch(x["text"].strip())]
        cutoff=min(body_starts) if body_starts else page["height"]*.45
        for x in ordered:
            t=x["text"].strip()
            if x["bbox"][1] < cutoff and (label.fullmatch(t) or banner.fullmatch(t) or re.fullmatch(r"\d{4,8}|[A-F]",t)):
                ids.add(x["line_id"])
    return ids


def combine_heading_fragments(lines, body_size):
    """Join same-baseline number/title fragments without losing raw line IDs."""
    result = []; index = 0
    while index < len(lines):
        a = lines[index]; b = lines[index+1] if index+1 < len(lines) else None
        prefix = re.fullmatch(r"(?:\d+(?:\.\d+)*[.]?|[IVXLCDM]+[.]?)", a["text"].strip())
        if b and prefix and a["native_block"] == b["native_block"] and a["native_block"] >= 0:
            title = b["text"].strip()
            same_row = abs(a["bbox"][1]-b["bbox"][1]) < 1
            gap = b["bbox"][0]-a["bbox"][2]
            short_title = len(title.split()) <= 12 and not re.search(r"[.!?;]$", title)
            if (same_row and 0 <= gap <= max(50, body_size*6) and short_title and
                    (a["font_size"] > body_size+.4 or a["bold"]) and
                    (b["font_size"] > body_size+.4 or b["bold"])):
                combined = dict(a, text=a["text"].strip()+" "+title,
                                bbox=[a["bbox"][0], min(a["bbox"][1], b["bbox"][1]),
                                      b["bbox"][2], max(a["bbox"][3], b["bbox"][3])],
                                flow_source_line_ids=[a["line_id"], b["line_id"]])
                if is_heading(combined, body_size):
                    result.append(combined); index += 2; continue
        result.append(a); index += 1
    return result


def classify_opening_metadata(document, pages):
    """Conservative draft classification; preserve every source byte/block ID.

    Only opening material before the first author paragraph is eligible. These
    labels are machine candidates, not source-bound section review approvals.
    """
    originals = {line["line_id"]: line for page in pages for line in page["lines"]}
    sections = {s["section_id"]: s for s in document["sections"]}
    date = re.compile(r"(?:(?:January|February|March|April|May|June|July|August|September|October|November|December)"
                      r"\s+\d{1,2},?\s+\d{4}|\d{1,2}[/-]\d{1,2}[/-]\d{4})[.]?", re.I)
    form = re.compile(r"(?:For office use only|[TF][1-4]\s+_+|Problem Chosen|"
                      r"(?:Team|Group)\s*(?:Control\s*)?(?:Number|#|No\.?)\s*:?\s*\d*|"
                      r"\(Attach a copy of this page to each copy of your solution paper\.\))", re.I)
    cover_pages = set()
    form_ids=competition_form_line_ids(pages)
    preceding_title_ids=set()
    for page in pages[:3]:
        anchors=[x for x in page["lines"] if re.fullmatch(r"Abstract|Summary(?: Sheet)?",x["text"].strip(),re.I)]
        if not anchors:
            continue
        top=min(x["bbox"][1] for x in anchors)
        for x in page["lines"]:
            if (x["bbox"][3]<=top and x["font_size"]>document["body_font_size"]*1.2 and
                    2<=len(x["text"].split())<30 and
                    title_role(x["text"],page["page"]) not in {"abstract","introduction","contents","references"} and
                    not re.match(r"^"+HEADING_NUMBER+r"\s+[A-Za-z]",x["text"].strip())):
                preceding_title_ids.add(x["line_id"])
    for page in pages[:3]:
        lines = [x for x in page["lines"] if x["text"].strip()]
        if (lines and len(lines) <= 12 and max(x["font_size"] for x in lines) > document["body_font_size"]*1.5 and
                any(date.fullmatch(x["text"].strip()) for x in lines) and
                any(re.fullmatch(r"(?:Team|Group)\s*#\s*\d+",x["text"].strip(),re.I) for x in lines) and
                all(len(x["text"].split()) <= 15 and
                    (date.fullmatch(x["text"].strip()) or
                     re.fullmatch(r"(?:Team|Group)\s*#\s*\d+|\d+",x["text"].strip(),re.I) or
                     (x["font_size"] > document["body_font_size"]*1.2 and
                      title_role(x["text"],page["page"]) != "abstract" and
                      not re.search(r"[.!?]$",x["text"].strip()))) for x in lines)):
            cover_pages.add(page["page"])
    author_started = False
    for block in document["blocks"]:
        if block["source_pages"][0] > 3:
            break
        if block["source_line_ids"] and set(block["source_line_ids"])<=form_ids:
            block.setdefault("classification_candidates",[]).append({"from_kind":block["kind"],
                "to_kind":"front_matter","rule":"opening-form-cluster-fragments-v1",
                "review_status":"machine-candidate; source check still required"})
            block["kind"]="front_matter"
            continue
        if block["source_line_ids"] and set(block["source_line_ids"])<=preceding_title_ids:
            block.setdefault("classification_candidates",[]).append({"from_kind":block["kind"],
                "to_kind":"title","rule":"large-title-before-opening-summary-v1",
                "review_status":"machine-candidate; source check still required"})
            block["kind"]="title"
            continue
        if set(block["source_pages"]) <= cover_pages:
            block.setdefault("classification_candidates", []).append({
                "from_kind": block["kind"], "to_kind": "front_matter", "rule": "sparse-title-cover-page-v1",
                "review_status": "machine-candidate; source check still required"})
            block["kind"] = "front_matter"
            continue
        if sections[block["section_id"]]["role"] != "abstract" or author_started:
            continue
        text = block["text"].strip()
        source = [originals[lid] for lid in block["source_line_ids"]]
        kind = None; rule = None
        if (block["kind"] in {"heading", "prose"} and
                re.fullmatch(r"\d{4} Mathematical Contest in Modeling \((?:MCM|ICM)\) Summary(?: Sheet)?", text, re.I)):
            kind, rule = "front_matter", "competition-summary-form-heading-v1"
        elif block["kind"] == "prose":
            if date.fullmatch(text):
                kind, rule = "front_matter", "opening-date-only-v1"
            elif all(form.fullmatch(line["text"].strip()) for line in source):
                kind, rule = "front_matter", "opening-competition-form-fields-v1"
            elif (block["source_pages"] == [1] and len(text.split()) < 30 and
                  min(line["font_size"] for line in source) > document["body_font_size"] * 1.2):
                kind, rule = "title", "opening-large-font-title-v1"
            else:
                author_started = True
        if kind:
            block.setdefault("classification_candidates", []).append({
                "from_kind": block["kind"], "to_kind": kind, "rule": rule,
                "review_status": "machine-candidate; source check still required"})
            block["kind"] = kind


def make_document(meta: dict, pages: list[dict], *, improved=False) -> dict:
    lines = [line for page in pages for line in page["lines"]]
    sizes = [x["font_size"] for x in lines if len(x["text"].split()) >= 8]
    body_size = statistics.median(sizes) if sizes else 11
    repeated = Counter(furniture_key(x["text"]) for page in pages for x in page["lines"]
                       if x["bbox"][1] < 65 or x["bbox"][3] > page["height"] - 45)
    blocks = []; sections = []; defects = []; current = None; stack = []; excluded = []

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
        flow = page["lines"]
        if improved:
            superseded = [x for x in flow if x.get("superseded_by_ocr")]
            excluded.extend({"line_id": x["line_id"], "reason": "native text superseded by source-bound OCR candidate"} for x in superseded)
            flow = [x for x in flow if not x.get("superseded_by_ocr")]
            excluded.extend({"line_id": x["line_id"], "reason": "empty native text run"} for x in flow if not x["text"].strip())
            flow = [x for x in flow if x["text"].strip()]
            micro = [x for x in flow if x["font_size"] < 4 and len(x["text"].strip()) < 8 and
                     (x["bbox"][2] < 18 or x["bbox"][0] > page["width"]-18) and
                     repeated[furniture_key(x["text"])] >= 3]
            if micro:
                excluded.extend({"line_id": x["line_id"], "reason": "repeated microtext outside body margins"} for x in micro)
                micro_ids = {x["line_id"] for x in micro}
                flow = [x for x in flow if x["line_id"] not in micro_ids]
                defects.append({"code": "margin_microtext_exclusion_review", "page": page["page"]})
            flow = [prose_flow_line(x) for x in flow]
            geometry = [x["flow_geometry_candidate"] for x in flow if x.get("flow_geometry_candidate")]
            if geometry:
                defects.append({"code": "inline_math_prose_flow_review", "page": page["page"],
                                "inference": geometry})
            if not page.get('reviewed_text_groups'):
                flow = combine_heading_fragments(flow, body_size)
        ordered, multi = order_lines(flow, page["width"])
        gap_limit, spacing_candidate = prose_gap_limit(ordered,body_size) if improved else (body_size*.6,None)
        if spacing_candidate:
            defects.append({"code":"expanded_line_spacing_review","page":page["page"],
                            "inference":spacing_candidate})
        body_lefts = [x["bbox"][0] for x in flow if len(x["text"].split()) >= 6 and
                      abs(x["font_size"]-body_size) < 1.5]
        body_left = min(body_lefts) if body_lefts else 0
        contents_title = next((x for x in flow if title_role(x["text"], page["page"]) == "contents"), None)
        summary_sheet_page = page["page"] <= 3 and any(
            re.search(r"\bsummary sheet\s*$",x["text"].strip(),re.I) or re.fullmatch(
                r"\d{4} Mathematical Contest in Modeling \((?:MCM|ICM)\) Summary",x["text"].strip(),re.I)
            for x in flow)
        inferred_contents = dense_untitled_contents(flow, page["page"]) if improved and contents_title is None else None
        contents_page = improved and (inferred_contents is not None or (contents_title is not None and sum(
            bool(re.search(r"(?:[.·\-]\s*){3,}",x["text"])) for x in flow) >= 3))
        if contents_page:
            # An exceptional source-checked page may finish author prose ABOVE
            # its Contents heading. Its reviewed groups perform the transition
            # at that exact heading; keep the page-level review flag below.
            reviewed_contents_heading = any(g.get('opens_section', {}).get('role') == 'contents'
                                            for g in page.get('reviewed_text_groups', []))
            if not reviewed_contents_heading:
                new_section(contents_title["text"].strip() if contents_title else "Untitled contents page (candidate)",
                            "contents", 1, "printed-contents-page" if contents_title else "inferred-dense-contents-page")
            defects.append({"code": "contents_page_boundary_review", "page": page["page"],
                            **({"inference": inferred_contents} if inferred_contents else {})})
        if multi:
            defects.append({"code": "column_order_review", "page": page["page"]})
        pending = []

        def flush(kind="prose"):
            nonlocal pending
            if not pending:
                return
            text, repairs = normalized_lines(pending)
            repairs += [{"operation": "same_baseline_heading_fragments",
                         "source_line_ids": x["flow_source_line_ids"]}
                        for x in pending if x.get("flow_source_line_ids")]
            repairs += [{"operation": "prose_flow_geometry_candidate", **x["flow_geometry_candidate"]}
                        for x in pending if x.get("flow_geometry_candidate")]
            bid = f"b{len(blocks)+1:06d}"
            issues = []
            if bad_unicode(text):
                issues.append("unresolved_unicode")
            if any(re.search(r"[A-Za-z]-\s*$", x["text"]) for x in pending[:-1]):
                issues.append("hyphen_join_review")
            if any(0xE000 <= ord(c) <= 0xF8FF for c in text):
                issues.append("private_use_glyph_review")
            blocks.append({"block_id": bid, "section_id": current["section_id"], "kind": kind,
                           "text": text, "source_line_ids": [lid for x in pending
                                for lid in x.get("flow_source_line_ids", [x["line_id"]])],
                           "source_pages": sorted({x["page"] for x in pending}),
                           "repairs": repairs, "issues": issues})
            current["block_ids"].append(bid)
            for issue in issues:
                defects.append({"code": issue, "block_id": bid, "page": pending[0]["page"]})
            pending = []

        previous = None
        if page.get("reviewed_text_groups"):
            # Source-bound reading lanes preserve callouts without inserting
            # them inside main prose. Raw native evidence remains unmodified.
            by_id = {x["line_id"]: x for x in flow}
            groups_by_id = {g['group_id']: g for g in page['reviewed_text_groups']}
            for group in page["reviewed_text_groups"]:
                pending = [by_id[lid] for lid in group["source_line_ids"]]
                if group.get('opens_section'):
                    opening=group['opens_section']
                    trailing = opening.get('trailing_label_group_id')
                    label = groups_by_id[trailing] if trailing else group
                    title,_=normalized_lines([by_id[lid] for lid in label['source_line_ids']])
                    inline = opening.get('inline_title_prefix')
                    if inline:
                        title = inline
                    origin = ('reviewed-trailing-appendix-label' if trailing else
                              'reviewed-inline-heading' if inline else 'reviewed-printed-heading')
                    new_section(title,opening['role'],opening['level'],origin)
                    if inline:
                        current['source_inline_heading_prefix'] = inline
                    if trailing:
                        current['source_label_group_id'] = trailing
                        current['source_label_line_ids'] = list(label['source_line_ids'])
                flush(group["kind"])
                blocks[-1]["layout_group_id"] = group["group_id"]
                blocks[-1]["layout_review_sha256"] = page["layout_review_sha256"]
            if page.get("comparison", {}).get("status") != "agreement":
                defects.append({"code":"cross_engine_review","page":page["page"]})
            if page.get("ocr_status") == "candidate":
                defects.append({"code":"ocr_candidate_source_review","page":page["page"]})
            continue
        author_line_seen = False
        for line in ordered:
            t = line["text"].strip()
            edge = line["bbox"][1] < 65 or line["bbox"][3] > page["height"] - 45
            header = bool(re.search(r"^(?:Team\s*(?:Number|Control Number|#|No\.?|:)|Page\s+\d+\s+of\b)", t, re.I))
            watermark = bool(re.search(r"精品数模|关注.*公众号|数学建模.*(?:资料|交流)", t))
            if improved and line["font_size"] < 4 and len(t) < 8 and (line["bbox"][2] < 18 or line["bbox"][0] > page["width"]-18):
                watermark = repeated[furniture_key(t)] >= 3
            repeat = edge and len(t) < 160 and repeated[furniture_key(t)] >= max(3, len(pages) // 3)
            if not t or header or watermark or repeat:
                flush(); pending = [line]; flush("furniture"); previous = None; continue
            if page["page"] <= 3 and competition_instruction(t):
                flush(); pending = [line]; flush("front_matter"); previous = None; continue
            if (improved and not author_line_seen and page["page"] <= 3 and
                    current["role"] == "abstract" and not summary_sheet_page and
                    re.fullmatch(r"Dear\s+(?:editor(?:s)?|sir(?:\s+or\s+madam)?|madam)[,:]",t,re.I)):
                flush(); new_section(t,"memo",1,"opening-letter-salutation-candidate")
                pending = [line]; flush(); previous = None; author_line_seen = True
                defects.append({"code":"opening_letter_boundary_review","page":page["page"],
                                "source_line_id":line["line_id"]})
                continue
            author_line_seen = True
            heading = is_heading(line, body_size)
            opening_title = (page["page"] == 1 and current["role"] == "abstract" and
                             line["font_size"] > body_size*1.25 and len(t.split()) < 30 and
                             title_role(t,page["page"]) not in {"abstract","introduction","contents"} and
                             not re.match(r"^"+HEADING_NUMBER+r"\s+[A-Za-z]",t))
            if improved and opening_title:
                heading = False  # A large paper-title line is not a new chapter.
            if contents_page:
                flush(); pending = [line]
                flush("heading" if contents_title and line["line_id"] == contents_title["line_id"] else "contents")
                previous = None; continue
            if current["role"] == "contents" and line["font_size"] < body_size + .4 and not line["bold"]:
                heading = False  # A TOC entry is not a new source section.
            if heading:
                flush()
                number = re.match(r"^(\d+(?:\.\d+)*)[.)]?\s+", t)
                level = number.group(1).count(".")+1 if number else 1
                role = title_role(t, page["page"])
                origin = "printed-heading"
                # The official Summary Sheet can itself have named internal
                # headings. Preserve them as children, not unrelated chapters.
                # A plain Abstract followed by a separate section is NOT enough
                # evidence for this rule, nor is a numbered body chapter.
                abstract_ancestor = next((sid for _,sid in reversed(stack)
                                          if next(s for s in sections if s["section_id"]==sid)["role"]=="abstract"),None)
                roman_number = re.match(r"^[IVX]+[.)]\s+",t)
                if (improved and summary_sheet_page and abstract_ancestor and not number and not roman_number and
                        role not in {"abstract","introduction","contents","references","ai_disclosure"}):
                    level = next(s["level"] for s in sections if s["section_id"]==abstract_ancestor)+1
                    origin = "summary-sheet-internal-heading-candidate"
                    defects.append({"code":"summary_sheet_subheading_scope_review","page":page["page"],
                                    "source_line_id":line["line_id"],"abstract_parent_id":abstract_ancestor})
                # An explicit abstract supersedes the empty inferred section, not its text.
                new_section(t, role, level, origin)
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
            elif page["page"] == 1 and line["font_size"] > body_size * 1.25 and len(t.split()) < 30:
                kind = "title"
            # No minimum word/letter filter: short and mixed prose stays readable.
            if kind != "prose":
                flush(); pending = [line]; flush(kind); previous = None; continue
            if previous is not None:
                gap = line["bbox"][1] - previous["bbox"][3]
                indent = line["bbox"][0] - previous["bbox"][0]
                native_change = line["native_block"] != previous["native_block"]
                if improved:
                    new_paragraph = (gap > gap_limit or
                                     re.match(r"^[\u2022\u25cf\uf0b7\uf0d8]\s+",t) is not None or
                                     ((indent > body_size * .65 or (not multi and body_lefts and
                                        line["bbox"][0] > body_left+body_size*.65)) and gap > -body_size*.2 and
                                      re.search(r"[.!?:;][\"')\]\u201d\u2019]*$", previous["text"].strip())))
                else:
                    new_paragraph = native_change or gap > body_size * .6 or (indent > body_size and re.search(r"[.!?:;]$", previous["text"].strip()))
                if new_paragraph:
                    flush()
            pending.append(line); previous = line
        flush()
        if not page["lines"]:
            defects.append({"code": "native_text_empty_ocr_required", "page": page["page"]})
        if page.get("ocr_status") == "candidate":
            defects.append({"code": "ocr_candidate_source_review", "page": page["page"]})
        if page.get("comparison", {}).get("status") != "agreement":
            defects.append({"code": "cross_engine_review", "page": page["page"]})
    # Do not guess cross-page joins: mark and retain both fragments until reviewed.
    prose = [b for b in blocks if b["kind"] in {"prose", "mixed"}]
    previous_prose = None; merged = set()
    for b in prose:
        a = previous_prose
        if a is None:
            previous_prose = b; continue
        if (a["section_id"] == b["section_id"] and a["source_pages"][-1] + 1 == b["source_pages"][0]
                and not re.search(r"[.!?:;][\"')\]]*$", a["text"])):
            defects.append({"code": "cross_page_join_review", "left": a["block_id"], "right": b["block_id"]})
            if improved and not a.get("layout_group_id") and not b.get("layout_group_id"):
                a["text"] += " " + b["text"]
                a["source_line_ids"] += b["source_line_ids"]
                a["source_pages"] = sorted(set(a["source_pages"]+b["source_pages"]))
                a["issues"] += b["issues"]
                a["repairs"] += [{"operation": "cross_page_join_candidate", "merged_block_id": b["block_id"]}] + b["repairs"]
                merged.add(b["block_id"])
                for defect in defects:
                    if defect.get("block_id") == b["block_id"]:
                        defect["block_id"] = a["block_id"]
                continue
        previous_prose = b
    if merged:
        blocks = [b for b in blocks if b["block_id"] not in merged]
        for s in sections:
            s["block_ids"] = [b for b in s["block_ids"] if b not in merged]
    for section in sections:
        defects.append({"code": "section_boundary_pending", "section_id": section["section_id"]})
    document = {"schema_version": SCHEMA, **meta, "status": "machine-draft", "body_font_size": body_size,
            "sections": sections, "blocks": blocks, "defects": defects, "excluded_source_lines": excluded,
            "verified_absent_roles": [], "formula_review": "paused", "figure_distillation": "paused"}
    if improved:
        classify_opening_metadata(document, pages)
    return document


def section_blocks(document: dict, selected: list[str], *, excluded_roles=(), kinds=None) -> list[dict]:
    excluded_roles=set(excluded_roles)
    by_id={s["section_id"]:s for s in document["sections"]}
    def excluded(sid):
        seen=set()
        while sid:
            if sid in seen or sid not in by_id:
                raise ValueError("Section hierarchy invalid")
            seen.add(sid)
            if by_id[sid]["role"] in excluded_roles:
                return True
            sid=by_id[sid]["parent_id"]
        return False
    wanted = {sid for sid in selected if not excluded_roles or not excluded(sid)}
    for section in document["sections"]:
        if section["parent_id"] in wanted and (not excluded_roles or not excluded(section["section_id"])):
            wanted.add(section["section_id"])
    allowed = PROSE_KINDS if kinds is None else set(kinds)
    return [b for b in document["blocks"] if b["section_id"] in wanted and b["kind"] in allowed]


def text_with_block_spans(blocks: list[dict]) -> tuple[str, list[dict]]:
    """Render checked paragraph continuity while retaining exact block offsets."""
    text = ""; spans = []; previous = None
    for block in blocks:
        if text:
            continued = previous is not None and block.get('paragraph_continues_from') == previous['block_id']
            text += " " if continued else "\n\n"
        start = len(text); text += block['text']
        spans.append({'block_id':block['block_id'],'section_id':block['section_id'],
                      'pages':block['source_pages'],'start':start,'end':len(text)})
        previous = block
    return text, spans


def section_text(document: dict, selected: list[str]) -> str:
    return text_with_block_spans(section_blocks(document, selected))[0]


def exported_section_text(document: dict, section_id: str) -> str:
    """Versioned derived view; canonical section_text review hashes stay stable."""
    policy = document.get("chapter_view_policy")
    if policy is None:
        return section_text(document, [section_id])
    if policy != CHAPTER_VIEW_POLICY:
        raise ValueError("Unknown chapter export policy")
    from corpus_queries import section_view_text
    return section_view_text(document, section_id)


def absence_review_valid(document: dict, role: str, review: dict) -> bool:
    """A missing heading or empty extraction alone cannot prove source absence."""
    count = document.get("page_count", 0)
    checked = review.get("checked_pages", [])
    proofs = review.get("evidence", [])
    # Query families/task identities also need honest whole-source absence. The
    # explicit-title selector prevents a task absence proof hiding model prose.
    from corpus_queries import QUERY_FAMILIES,TASK_QUERIES,select_sections
    ids,excluded=select_sections(document,role)
    allowed=role in ROLES or role in TASK_QUERIES or (role in QUERY_FAMILIES and role!="all_author_text")
    return bool(allowed and review.get("schema") == "source-absence-review-v1" and
                review.get("role") == role and review.get("paper_id") == document["paper_id"] and
                review.get("reviewer") and review.get("reason") and
                review.get("source_sha256") == document["source_sha256"] and
                review.get("raw_pages_sha256") == document.get("raw_pages_sha256") and
                type(count) is int and count > 0 and review.get("page_count") == count and
                checked == list(range(1, count+1)) and
                review.get("full_native_prose_read") is True and
                review.get("physical_page_heading_layout_checked") is True and
                isinstance(proofs,list) and proofs and all(isinstance(p,dict) and p.get("path") and
                    p.get("description") and re.fullmatch(r"[a-f0-9]{64}",p.get("sha256","")) for p in proofs) and
                not "\n\n".join(b["text"] for b in section_blocks(document,ids,excluded_roles=excluded)).strip())


def export_document(target: Path, document: dict) -> None:
    document = {**document, "chapter_view_policy": CHAPTER_VIEW_POLICY}
    json_new(target / "document.json", document)
    full = [f"# {document['paper_id']}\n\nStatus: machine-draft; not source-verified.\n"]
    for b in document["blocks"]:
        # All non-prose is retained and identified, not silently thrown away.
        full.append(f"<!-- {b['block_id']} | {b['kind']} | pages {b['source_pages']} -->\n{b['text']}")
    write_new(target / "full.md", "\n\n".join(full) + "\n")
    for s in document["sections"]:
        label = "verified source boundary" if s["boundary_status"] == "verified" else "pending boundary review"
        write_new(target / "sections" / (s["section_id"] + ".md"),
                  f"<!-- {label}; {s['title']} -->\n" + exported_section_text(document, s["section_id"]) + "\n")
