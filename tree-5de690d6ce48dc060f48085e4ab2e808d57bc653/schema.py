"""Field schema and validators for the figure-distillation records.

Every exhibit record carries five blocks read off the page: place, mention, caption,
geometry, and — for printed tables — table. Nothing here decides a family or a
position; the coder reads it from the crop and the text layer, these functions only
refuse records that are incomplete, out of vocabulary, or quote text that is not
on the page.

The quoted-sentence check is the point of the module: a "verbatim" sentence that is
not a substring of the normalised text layer of one of the pages it claims to come
from is a paraphrase, and a paraphrase is a fabrication in a census.
"""

from __future__ import annotations

import re
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PAPERS = LANE.parents[1] / "artifacts" / "papers"

SECTION_KINDS = {
    "abstract", "introduction", "assumption", "symbols", "model", "solution",
    "result", "sensitivity", "test", "evaluation", "appendix", "other",
}
PAGE_ZONES = {"top", "middle", "bottom"}
LEAD_PATTERNS = {"direct", "figure-n-shows", "as-shown-in", "parenthetical", "none"}
NUMBERINGS = {"Figure N:", "Figure N.", "Figure N", "FIGURE N", "Fig. N", "Table N:",
              "Table N.", "Table N", "TABLE N", "none"}
VOICES = {"active", "passive", "none"}
POSITIONS = {"above", "below"}
LEGENDS = {"none", "inside", "outside-left", "outside-right", "below", "above"}
THREE_D = {"no", "perspective-bars", "surface-mesh", "isometric"}
RULE_STYLES = {"booktabs", "boxed", "no-rules", "vertical-rules"}
WIDTHS = {"full", "half", "column"}
ORIENTATIONS = {"portrait", "landscape"}
CAPTION_SOURCES = {"text-layer", "typed-from-crop", "none"}
CONFIDENCE = {"high", "medium", "low"}

MAX_QUOTE_WORDS = 25


def norm(text: str) -> str:
    return " ".join(text.split())


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'.,%/()-]*", text)


def page_text(pid: str, page: int) -> str:
    """Normalised text layer of one page, empty when the page has no text."""
    path = PAPERS / pid / "text" / "pages" / f"page-{page:04d}.txt"
    if not path.exists():
        return ""
    return norm(path.read_text(encoding="utf-8", errors="replace"))


def printed_lines(pid: str) -> set[str]:
    """Every normalised raw line of the paper's text layer.

    Used as the fallback for a section label the layout pass failed to index: a
    heading printed on the page is still a heading even when the heading detector
    missed it, so `check_place` accepts a label that is a printed line verbatim.
    A mistyped label is not a printed line and is still refused.
    """
    out: set[str] = set()
    for path in sorted((PAPERS / pid / "text" / "pages").glob("page-*.txt")):
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = norm(raw)
            if not line:
                continue
            out.add(line)
            # A heading can share its line with a watermark glyph run on either side,
            # so the numbered tail of the line and the line with the stray run
            # collapsed are both accepted spellings of the same printed heading.
            for match in re.finditer(r"\b\d+(?:\.\d+)*\s+\S", line):
                out.add(line[match.start():])
            collapsed = norm(re.sub(r"[^\x00-\x7f]+", " ", line))
            if collapsed:
                out.add(collapsed)
    return out


RUNNING_HEAD = re.compile(r"^(team\s*#?\s*\d+|page\s+\d+\s+of\s+\d+|[\d\s]+)$", re.I)


def page_units(pid: str, page: int) -> list[str]:
    """Prose units of one page: visual lines accumulated until a sentence ends.

    String-level sentence splitting on a text layer that interleaves typeset maths
    produces paragraph-sized blobs, so units are cut at line ends that carry final
    punctuation. Every unit is still an exact substring of the normalised page text,
    which is what the quote check needs.
    """
    path = PAPERS / pid / "text" / "pages" / f"page-{page:04d}.txt"
    if not path.exists():
        return []
    units: list[str] = []
    cur: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = norm(raw)
        if not line or RUNNING_HEAD.match(line):
            continue
        cur.append(line)
        if re.search(r"[.!?][\"'”]?$", line):
            units.append(" ".join(cur))
            cur = []
    if cur:
        units.append(" ".join(cur))
    return units


def sentences(text: str) -> list[str]:
    """Crude sentence split, only for counting and for locating a quote's page."""
    text = norm(text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\"'])", text)
    return [p for p in parts if p.strip()]


class Bad(Exception):
    pass


def need(cond: bool, msg: str) -> None:
    if not cond:
        raise Bad(msg)


def need_enum(value, allowed, label: str) -> None:
    need(value in allowed, f"{label} {value!r} not in {sorted(allowed)}")


def need_int(value, label: str, minimum: int = 0) -> None:
    need(isinstance(value, int) and not isinstance(value, bool) and value >= minimum,
         f"{label} must be an int >= {minimum}")


def check_quote(text: str, pid: str, pages: list[int], label: str,
                limit: int | None = MAX_QUOTE_WORDS) -> None:
    """A quoted sentence must be a substring of the page it says it came from.

    `limit` caps the length of lead/trail sentences. Captions are quoted whole, so
    they pass limit=None and are only checked for being on the page.
    """
    q = norm(text)
    need(bool(q), f"{label}: empty quote")
    if limit is not None:
        need(len(words(q)) <= limit,
             f"{label}: {len(words(q))} words, limit {limit}")
    for page in pages:
        if q in page_text(pid, page):
            return
    tried = ", ".join(str(p) for p in pages)
    raise Bad(f"{label}: quote not found verbatim on page(s) {tried}: {q[:80]!r}")


def check_place(place: dict, pid: str, headings: list[dict], label: str) -> None:
    need(isinstance(place, dict), f"{label}.place must be an object")
    for key in ("section_path", "section_numbered", "section_kind", "doc_order",
                "page_order", "page_zone", "area_frac", "solo_page"):
        need(key in place, f"{label}.place missing {key}")
    need(isinstance(place["section_path"], list) and place["section_path"],
         f"{label}.place.section_path must be a non-empty list of heading labels")
    need_enum(place["section_kind"], SECTION_KINDS, f"{label}.place.section_kind")
    need_enum(place["page_zone"], PAGE_ZONES, f"{label}.place.page_zone")
    need_int(place["doc_order"], f"{label}.place.doc_order", 1)
    need_int(place["page_order"], f"{label}.place.page_order", 1)
    need(isinstance(place["solo_page"], bool), f"{label}.place.solo_page must be bool")
    need(isinstance(place["area_frac"], (int, float)) and 0 < place["area_frac"] <= 1,
         f"{label}.place.area_frac must be in (0, 1]")

    known = {norm(h["label"]) for h in headings}
    known |= {norm(h["title"]) for h in headings if h.get("title")}
    printed: set[str] | None = None
    for part in place["section_path"]:
        label_norm = norm(part)
        if place["section_numbered"]:
            if label_norm not in known:
                if printed is None:
                    printed = printed_lines(pid)
                need(label_norm in printed,
                     f"{label}.place.section_path item {part!r} is not a heading in the "
                     "text layer; either fix the label or set section_numbered=false")
        else:
            need(label_norm.startswith("未编号标题"),
                 f"{label}.place.section_path unnumbered items must start with "
                 f"未编号标题, got {part!r}")


def check_mention(mention: dict, pid: str, page: int, label: str,
                  allowed_pages: list[int]) -> None:
    need(isinstance(mention, dict), f"{label}.mention must be an object")
    for key in ("first_page", "lead_pages", "style", "count", "lead_sentence",
                "trail_sentence", "lead_pattern", "read_sentences", "gap_sentences"):
        need(key in mention, f"{label}.mention missing {key}")
    need_enum(mention["lead_pattern"], LEAD_PATTERNS, f"{label}.mention.lead_pattern")
    need_int(mention["count"], f"{label}.mention.count")
    need_int(mention["read_sentences"], f"{label}.mention.read_sentences")
    need(mention["gap_sentences"] is None or isinstance(mention["gap_sentences"], int),
         f"{label}.mention.gap_sentences must be an int or null")
    need(isinstance(mention["style"], list), f"{label}.mention.style must be a list")
    for spelling in mention["style"]:
        need(norm(spelling) in norm(" ".join(page_text(pid, p) for p in allowed_pages)),
             f"{label}.mention.style {spelling!r} never appears in the paper text")
    if mention["first_page"] is None:
        need(mention["lead_pages"] is None, f"{label}.mention.lead_pages must be null "
             "when first_page is null")
    else:
        need_int(mention["first_page"], f"{label}.mention.first_page", 1)
        need(mention["lead_pages"] == page - mention["first_page"],
             f"{label}.mention.lead_pages must equal exhibit page {page} minus first "
             f"mention page {mention['first_page']}")
    for key in ("lead_sentence", "trail_sentence"):
        value = mention[key]
        if value in ("", None):
            continue
        check_quote(value, pid, sorted(set(allowed_pages) | {page}), f"{label}.mention.{key}")


def check_caption(caption: dict, label: str) -> None:
    need(isinstance(caption, dict), f"{label}.caption must be an object")
    for key in ("verbatim", "numbering", "words", "sentences", "units", "variables",
                "variable_count", "conditions", "concludes", "voice", "position"):
        need(key in caption, f"{label}.caption missing {key}")
    need_int(caption["variable_count"], f"{label}.caption.variable_count")
    need(caption["variables"] == (caption["variable_count"] > 0),
         f"{label}.caption.variables must be true exactly when variable_count > 0")
    need_enum(caption["numbering"], NUMBERINGS, f"{label}.caption.numbering")
    need_enum(caption["voice"], VOICES, f"{label}.caption.voice")
    need_enum(caption["position"], POSITIONS, f"{label}.caption.position")
    need_int(caption["words"], f"{label}.caption.words")
    need_int(caption["sentences"], f"{label}.caption.sentences")
    for key in ("units", "variables", "conditions", "concludes"):
        need(isinstance(caption[key], bool), f"{label}.caption.{key} must be bool")
    if caption["verbatim"]:
        need(caption["words"] == len(words(caption["verbatim"])),
             f"{label}.caption.words {caption['words']} does not match the quoted "
             f"caption ({len(words(caption['verbatim']))} words)")


def check_geometry(geometry: dict, families: set[str], label: str) -> None:
    need(isinstance(geometry, dict), f"{label}.geometry must be an object")
    for key in ("family", "panel_count", "panel_layout", "shared_axes", "legend",
                "colorbar", "three_d", "printed_numbers", "data_labels"):
        need(key in geometry, f"{label}.geometry missing {key}")
    need_enum(geometry["family"], families, f"{label}.geometry.family")
    need_int(geometry["panel_count"], f"{label}.geometry.panel_count", 1)
    need_enum(geometry["legend"], LEGENDS, f"{label}.geometry.legend")
    need_enum(geometry["three_d"], THREE_D, f"{label}.geometry.three_d")
    for key in ("shared_axes", "colorbar", "printed_numbers", "data_labels"):
        need(isinstance(geometry[key], bool), f"{label}.geometry.{key} must be bool")
    need(isinstance(geometry["panel_layout"], str), f"{label}.geometry.panel_layout "
         "must be a string like '1', '2x2', '2x2+1', 'column of 5'")


def check_table(table: dict, label: str) -> None:
    need(isinstance(table, dict), f"{label}.table must be an object")
    for key in ("rows", "cols", "header_rows", "rule_style", "zebra", "merged_cells",
                "diagonal_header", "units_in_header", "decimal_aligned", "numeric_cols",
                "text_cols", "width", "orientation", "continued", "note_sentence"):
        need(key in table, f"{label}.table missing {key}")
    need_int(table["rows"], f"{label}.table.rows", 1)
    need_int(table["cols"], f"{label}.table.cols", 1)
    need_int(table["header_rows"], f"{label}.table.header_rows", 1)
    need_int(table["numeric_cols"], f"{label}.table.numeric_cols")
    need_int(table["text_cols"], f"{label}.table.text_cols")
    need_enum(table["rule_style"], RULE_STYLES, f"{label}.table.rule_style")
    need_enum(table["width"], WIDTHS, f"{label}.table.width")
    need_enum(table["orientation"], ORIENTATIONS, f"{label}.table.orientation")
    for key in ("zebra", "merged_cells", "diagonal_header", "units_in_header",
                "decimal_aligned", "continued"):
        need(isinstance(table[key], bool), f"{label}.table.{key} must be bool")
