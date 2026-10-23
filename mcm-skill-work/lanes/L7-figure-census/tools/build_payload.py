"""Assemble a record payload from a hand-written spec plus the measured context dump.

Everything that can be measured is measured here, so the spec only carries what a
human or a crop has to decide: the family, the geometry and table readings, the
caption flags, and which text-layer line is quoted as the lead and trail sentence.

Measured here: bbox, area_frac, page_zone, solo_page and the heading path (copied from
`.proxy/<pid>-ctx.json`); doc_order and page_order (reading order over the exhibits);
caption words, sentences and numbering; `lead_pages`; and the lead/trail quotes, which
are sliced out of the raw page text so ligatures and typographic quotes survive — the
substring test in `schema.check_quote` compares characters, not words.

Spec shape (one file per paper, `<pid>-spec.json`):

  {"paper": pid,
   "note": "...",
   "exhibits": [{"page": 5, "region": 1, "kind": "table",
                 "caption": "Table 1: Notations used in this paper",
                 "caption_flags": {"units": false, "variables": false, "variable_count": 0,
                                   "conditions": false, "concludes": false,
                                   "voice": "none", "position": "above"},
                 "table": {"rows": 6, ...}, "note": "...",
                 "mention": {"first_page": 5, "style": ["Table 1"], "pattern": "direct",
                             "lead": [5, "The key mathematical notations"],
                             "trail": [5, "Table 1: Notations used"],
                             "read_sentences": 1, "gap_sentences": null}}],
   "excluded": [{"page": 24, "region": 1, "reason": "background", "note": "..."}],
   "rules": ["... [caption.numbering]", ...]}

Usage:
  python -I lanes/L7-figure-census/tools/build_payload.py <pid> <spec.json> [out.json]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PROXY = LANE / ".proxy"
PAPERS = LANE.parents[1] / "artifacts" / "papers"
MAX_WORDS = 25
TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9'.,%/()-]*")

NUMBERING = (
    (re.compile(r"^FIGURE\s+\d+"), "FIGURE N"),
    (re.compile(r"^Figure\s+\d+:"), "Figure N:"),
    (re.compile(r"^Figure\s+\d+\."), "Figure N."),
    (re.compile(r"^Figure\s+\d+"), "Figure N"),
    (re.compile(r"^Fig\.\s*\d+"), "Fig. N"),
    (re.compile(r"^Table\s+\d+:"), "Table N:"),
    (re.compile(r"^Table\s+\d+\."), "Table N."),
    (re.compile(r"^TABLE\s+\d+"), "TABLE N"),
    (re.compile(r"^Table\s+\d+"), "Table N"),
)


def word_list(text: str) -> list[str]:
    return TOKEN.findall(text)


def sentence_count(text: str) -> int:
    body = re.sub(r"^(Figure|Table)\s+\d+\s*[.:]?", "", text).strip()
    parts = [p for p in re.split(r"(?<=[.!?])\s+", body) if p.strip()]
    return max(1, len(parts))


def numbering_of(text: str) -> str:
    for pattern, name in NUMBERING:
        if pattern.match(text.strip()):
            return name
    return "none"


def raw_lines(pid: str, page: int) -> list[str]:
    """Untouched text-layer lines of one page, stripped, empties dropped."""
    path = PAPERS / pid / "text" / "pages" / f"page-{page:04d}.txt"
    if not path.exists():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]


def pick_line(pid: str, page: int, prefix: str, label: str, nth: int | None = None) -> str:
    """The raw line on `page` starting with `prefix` (nth=None: it must be unique)."""
    hits = [ln for ln in raw_lines(pid, page) if ln.startswith(prefix)]
    if not hits:
        raise SystemExit(f"{label}: no line on page {page} starts with {prefix!r}")
    if len(hits) > 1 and nth is None:
        raise SystemExit(f"{label}: {len(hits)} lines on page {page} start with "
                         f"{prefix!r}; pass an occurrence index")
    if nth is not None and nth >= len(hits):
        raise SystemExit(f"{label}: page {page} has {len(hits)} line(s) starting with "
                         f"{prefix!r}, occurrence {nth} does not exist")
    return hits[nth]


def trim(text: str) -> str:
    """Cut a quote to the word limit at a word boundary, right end only."""
    spans = list(TOKEN.finditer(text))
    if len(spans) <= MAX_WORDS:
        return text
    return text[:spans[MAX_WORDS - 1].end()].rstrip(" ,;:-")


def quoted(pid: str, spec, label: str) -> str:
    """A quote from one page, given as [page, prefix, nth?] or a list of those.

    Several pieces are joined with a space, which is what `schema.norm` does to the
    page text, so a sentence that wraps across lines still matches character for
    character.
    """
    pieces = spec if isinstance(spec[0], list) else [spec]
    parts = []
    for piece in pieces:
        page, prefix = piece[0], piece[1]
        nth = piece[2] if len(piece) > 2 else 0
        parts.append(pick_line(pid, page, prefix, label, nth))
    return trim(" ".join(parts))


def resolve_caption(pid: str, spec, page: int, label: str) -> str:
    """A caption given either as a literal string or as page/prefix selectors.

    Either way the result is checked against the text layer of the pages it claims to
    come from, because `record.py` will only accept it as a verbatim substring.
    """
    if spec in (None, ""):
        return ""
    if isinstance(spec, str):
        text, pages = spec, [page - 1, page, page + 1]
    else:
        pieces = [spec] if isinstance(spec[0], int) else spec
        text = quoted(pid, pieces, label)
        pages = sorted({p for piece in pieces for p in (piece[0] - 1, piece[0], piece[0] + 1)})
    doubled = " ".join(text.split())
    if not any(doubled in norm_page(pid, p) for p in pages if p >= 1):
        raise SystemExit(f"{label}: caption not found verbatim on pages {pages}: "
                         f"{text[:70]!r}")
    return text


def norm_page(pid: str, page: int) -> str:
    path = PAPERS / pid / "text" / "pages" / f"page-{page:04d}.txt"
    if not path.exists():
        return ""
    return " ".join(path.read_text(encoding="utf-8", errors="replace").split())


def region(ctx: dict, page: int, index: int) -> dict:
    for r in ctx["regions"]:
        if r["page"] == page and r["region"] == index:
            return r
    raise SystemExit(f"no measured region p{page} r{index} in the context dump")


def build(pid: str, spec: dict, layout: dict, ctx: dict) -> dict:
    exhibits = list(spec["exhibits"])
    order = sorted(exhibits, key=lambda e: (e["page"], region(ctx, e["page"], e["region"])["bbox"][1],
                                            region(ctx, e["page"], e["region"])["bbox"][0]))
    doc_order = {id(e): i for i, e in enumerate(order, 1)}
    page_seen: dict[int, int] = {}

    items, tables = [], []
    for e in exhibits:
        r = region(ctx, e["page"], e["region"])
        page_seen[e["page"]] = page_seen.get(e["page"], 0) + 1
        caption = resolve_caption(pid, e.get("caption"), e["page"], f"p{e['page']} caption")
        flags = e["caption_flags"]
        caption_block = {
            "verbatim": caption,
            "numbering": e.get("numbering") or numbering_of(caption),
            "words": len(word_list(caption)),
            "sentences": sentence_count(caption) if caption else 0,
            "units": flags["units"],
            "variables": flags["variable_count"] > 0,
            "variable_count": flags["variable_count"],
            "conditions": flags["conditions"],
            "concludes": flags["concludes"],
            "voice": flags["voice"],
            "position": flags["position"],
        }
        mention_spec = e["mention"]
        first = mention_spec.get("first_page")
        lead = quoted(pid, mention_spec["lead"], "lead") if mention_spec.get("lead") else ""
        trail = quoted(pid, mention_spec["trail"], "trail") if mention_spec.get("trail") else ""
        mention_block = {
            "first_page": first,
            "lead_pages": None if first is None else e["page"] - first,
            "style": list(mention_spec["style"]),
            "count": mention_spec["count"],
            "lead_sentence": lead,
            "trail_sentence": trail,
            "lead_pattern": mention_spec["pattern"],
            "read_sentences": mention_spec.get("read_sentences", 1),
            "gap_sentences": mention_spec.get("gap_sentences"),
        }
        override = e.get("place", {})
        place_block = {
            "section_path": override.get("section_path", r["section_path"]),
            "section_numbered": override.get("section_numbered", r["section_numbered"]),
            "section_kind": override.get("section_kind", r["section_kind"]),
            "doc_order": doc_order[id(e)],
            "page_order": page_seen[e["page"]],
            "page_zone": r["page_zone"],
            "area_frac": r["area_frac"],
            "solo_page": r["solo_page"],
        }
        entry = {"page": e["page"], "bbox": r["bbox"], "caption": caption_block,
                 "caption_source": e.get("caption_source", "text-layer" if caption else "none"),
                 "caption_verbatim": caption, "mention": mention_block,
                 "place": place_block, "note": e.get("note", "")}
        if e["kind"] == "item":
            entry["family"] = e["family"]
            entry["confidence"] = e["confidence"]
            entry["panel_count"] = e["panel_count"]
            entry["other_note"] = e.get("other_note")
            entry["geometry"] = {
                "family": e["family"], "panel_count": e["panel_count"],
                "panel_layout": e["panel_layout"], "shared_axes": e["shared_axes"],
                "legend": e["legend"], "colorbar": e["colorbar"],
                "three_d": e["three_d"], "printed_numbers": e["printed_numbers"],
                "data_labels": e["data_labels"],
            }
            entry["table"] = False
            entry["excluded"] = None
            items.append(entry)
        else:
            entry["family"] = "table-grid"
            entry["table"] = dict(e["table"])
            entry["table"].setdefault("note_sentence", "")
            tables.append(entry)

    excluded = []
    for x in spec.get("excluded", []):
        r = region(ctx, x["page"], x["region"])
        excluded.append({"page": x["page"], "bbox": r["bbox"],
                         "reason": x["reason"], "note": x["note"]})

    return {
        "paper": pid,
        "layout_sha256": layout["layout_sha256"],
        "note": spec.get("note", ""),
        "items": items,
        "tables": tables,
        "excluded_regions": excluded,
        "rules": spec.get("rules", []),
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        raise SystemExit("usage: build_payload.py <pid> <spec.json> [out.json]")
    pid, spec_path = argv[0], Path(argv[1])
    out = Path(argv[2]) if len(argv) > 2 else PROXY / f"{pid}-payload.json"
    layout = json.loads((LANE / "layout" / f"{pid}.json").read_text(encoding="utf-8"))
    ctx = json.loads((PROXY / f"{pid}-ctx.json").read_text(encoding="utf-8"))
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    if spec.get("paper") != pid:
        raise SystemExit(f"spec paper {spec.get('paper')!r} does not match {pid}")

    payload = build(pid, spec, layout, ctx)
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(payload['items'])} items, {len(payload['tables'])} tables, "
          f"{len(payload['excluded_regions'])} excluded -> {out}")
    for bucket in ("items", "tables"):
        for n, e in enumerate(payload[bucket], 1):
            m = e["mention"]
            print(f"  {bucket[:-1]} {n:2d} p{e['page']:<2d} doc={e['place']['doc_order']:<2d} "
                  f"first={m['first_page']} gap={m['lead_pages']} "
                  f"lead={len(word_list(m['lead_sentence']))}w trail={len(word_list(m['trail_sentence']))}w")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
