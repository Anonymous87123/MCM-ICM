"""Read-only validator for a recorded paper: every distillation field, every quote.

`record.py` refuses a payload at write time; this tool re-runs the same refusals on a
record already on disk, and instead of stopping at the first bad field it reports the
whole missing-key list for the paper, so a record that was written under an older shape
can be told apart from one that is simply wrong.

Checks, in the order `record.py` applies them: family in the closed vocabulary,
confidence, panel_count, caption_source, page/bbox present and measured, no region
counted twice, `other` and `composite-panel` rules, the four blocks present, then
`schema.check_place / check_mention / check_caption / check_geometry / check_table`
— which is where the verbatim-substring test, the heading-path test and the enum
vocabularies live — then the cross-block agreements and the rules-cite check. Nothing
here is reimplemented: the vocabulary comes from `record.FAMILIES`, the checks from
`schema`. The key tuples below mirror the loops inside those two modules; if `schema`
grows a key, the paper fails here with a `schema:` line rather than passing quietly.

Not checked here, because a validator cannot see ink: three_d, rule_style, zebra,
merged_cells are only decidable from the crop. The rules file records which crop each
one was read off; this tool only enforces that the value is in vocabulary.

Usage: python -I tools/validate_distill.py [pid ...]     (no pid = every record)
Exit 0 when every paper passes.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import record  # noqa: E402
import schema  # noqa: E402

PLACE_KEYS = ("section_path", "section_numbered", "section_kind", "doc_order",
              "page_order", "page_zone", "area_frac", "solo_page")
MENTION_KEYS = ("first_page", "lead_pages", "style", "count", "lead_sentence",
                "trail_sentence", "lead_pattern", "read_sentences", "gap_sentences")
CAPTION_KEYS = ("verbatim", "numbering", "words", "sentences", "units", "variables",
                "variable_count", "conditions", "concludes", "voice", "position")
GEOMETRY_KEYS = ("family", "panel_count", "panel_layout", "shared_axes", "legend",
                 "colorbar", "three_d", "printed_numbers", "data_labels")
TABLE_KEYS = ("rows", "cols", "header_rows", "rule_style", "zebra", "merged_cells",
              "diagonal_header", "units_in_header", "decimal_aligned", "numeric_cols",
              "text_cols", "width", "orientation", "continued", "note_sentence")
BLOCK_KEYS = {"place": PLACE_KEYS, "mention": MENTION_KEYS, "caption": CAPTION_KEYS,
              "geometry": GEOMETRY_KEYS, "table": TABLE_KEYS}


def missing_keys(block: dict, keys: tuple[str, ...]) -> list[str]:
    return [k for k in keys if k not in block]


def audit(pid: str) -> list[str]:
    """Every refusal `record.py` would raise on this paper's record, all of them."""
    bad: list[str] = []
    rec_path = LANE / "records" / f"{pid}.json"
    lay_path = LANE / "layout" / f"{pid}.json"
    ctx_path = LANE / ".proxy" / f"{pid}-ctx.json"
    if not rec_path.exists():
        return [f"no record at {rec_path.name}"]
    rec = json.loads(rec_path.read_text(encoding="utf-8"))
    headings = None
    if lay_path.exists():
        lay = json.loads(lay_path.read_text(encoding="utf-8"))
        measured = {record.region_key(pg["page"], r["bbox"])
                    for pg in lay["pages"] for r in pg["regions"]}
        if rec.get("layout_sha256") != lay.get("layout_sha256"):
            bad.append("layout_sha256 differs from layout/: re-run fig_extract on this paper")
    else:
        measured = None
        bad.append(f"no layout at layout/{pid}.json: regions, dup and unaccounted not checked")
    if ctx_path.exists():
        headings = json.loads(ctx_path.read_text(encoding="utf-8")).get("headings", [])
    else:
        bad.append(f"no context dump at .proxy/{pid}-ctx.json: heading path not checked")

    seen: set[tuple] = set()
    for label, bucket in (("item", rec.get("items", [])), ("table", rec.get("tables", []))):
        for i, e in enumerate(bucket, 1):
            tag = f"{label} {i} p{e.get('page')}"
            if "page" not in e or "bbox" not in e:
                bad.append(f"{tag}: page and bbox are required")
                continue
            if measured is not None:
                key = record.region_key(e["page"], e["bbox"])
                if key not in measured:
                    bad.append(f"{tag}: bbox not a measured region")
                if key in seen:
                    bad.append(f"{tag}: region counted twice")
                seen.add(key)
            if label == "item":
                fam = e.get("family")
                if fam not in record.FAMILIES:
                    bad.append(f"{tag}: family {fam!r} not in the closed vocabulary")
                if e.get("confidence") not in record.CONFIDENCE:
                    bad.append(f"{tag}: confidence {e.get('confidence')!r} invalid")
                if not isinstance(e.get("panel_count"), int) or e["panel_count"] < 1:
                    bad.append(f"{tag}: panel_count must be an int >= 1")
                if fam == "other" and not (e.get("other_note") or "").strip():
                    bad.append(f"{tag}: family 'other' needs other_note")
                if fam == "composite-panel" and isinstance(e.get("panel_count"), int) \
                        and e["panel_count"] < 2:
                    bad.append(f"{tag}: composite-panel needs panel_count >= 2")
                src = e.get("caption_source", "text-layer")
                if src not in record.CAPTION_SOURCES:
                    bad.append(f"{tag}: caption_source {src!r} invalid")
                if src != "none" and not (e.get("caption_verbatim") or "").strip():
                    bad.append(f"{tag}: empty caption and caption_source is not 'none'")
                if e.get("geometry", {}).get("family") != fam:
                    bad.append(f"{tag}: family {fam!r} disagrees with geometry.family "
                               f"{e.get('geometry', {}).get('family')!r}")
                if e.get("geometry", {}).get("panel_count") != e.get("panel_count"):
                    bad.append(f"{tag}: panel_count disagrees with geometry.panel_count")
                blocks = ("place", "mention", "caption", "geometry")
            else:
                blocks = ("place", "mention", "caption", "table")

            for block in blocks:
                value = e.get(block)
                if not isinstance(value, dict):
                    bad.append(f"{tag}: missing {block} block")
                    continue
                absent = missing_keys(value, BLOCK_KEYS[block])
                if absent:
                    bad.append(f"{tag}: {block} missing {', '.join(absent)}")

            if not all(isinstance(e.get(b), dict) for b in blocks):
                continue
            if e.get("caption", {}).get("verbatim") != (e.get("caption_verbatim") or ""):
                bad.append(f"{tag}: caption.verbatim must equal caption_verbatim")
            try:
                schema.check_place(e["place"], pid, headings or [], tag)
                schema.check_mention(e["mention"], pid, e["page"], tag,
                                     record.quote_pages(e))
                schema.check_caption(e["caption"], tag)
                if label == "item":
                    schema.check_geometry(e["geometry"], record.FAMILIES, tag)
                    if e.get("caption_source", "text-layer") == "text-layer":
                        schema.check_quote(e["caption"]["verbatim"], pid,
                                           [e["page"] - 1, e["page"], e["page"] + 1],
                                           f"{tag} caption", limit=None)
                else:
                    schema.check_table(e["table"], tag)
                    if e["table"]["note_sentence"]:
                        schema.check_quote(e["table"]["note_sentence"], pid,
                                           [e["page"], e["page"] + 1], f"{tag} note")
                    if (e.get("caption_source") or "text-layer") == "text-layer":
                        schema.check_quote(e["caption"]["verbatim"], pid,
                                           [e["page"] - 1, e["page"], e["page"] + 1],
                                           f"{tag} caption", limit=None)
            except schema.Bad as exc:
                bad.append(f"{tag}: schema: {exc}")

    for i, ex in enumerate(rec.get("excluded_regions", []), 1):
        if ex.get("reason") not in record.REASONS:
            bad.append(f"excluded {i}: reason {ex.get('reason')!r} not allowed")
        if measured is not None:
            key = record.region_key(ex["page"], ex["bbox"])
            if key not in measured:
                bad.append(f"excluded {i}: bbox not a measured region")
            if key in seen:
                bad.append(f"excluded {i}: region already counted")
            seen.add(key)

    rules = [r for r in rec.get("rules", []) if str(r).strip()]
    if not rules:
        bad.append("no rules: notes/<pid>.md must state the distillation as rules")
    field_paths: set[str] = set()
    for bucket in (rec.get("items", []), rec.get("tables", [])):
        for entry in bucket:
            for block, value in entry.items():
                if isinstance(value, dict):
                    field_paths |= {f"{block}.{k}" for k in value}
    for n, rule in enumerate(rules, 1):
        cited = record.RULE_CITE.findall(rule)
        if not cited:
            bad.append(f"rule {n}: cites no field")
        for path in cited:
            if path not in field_paths:
                bad.append(f"rule {n}: cites {path!r}, which no exhibit carries")

    if measured is not None:
        left = measured - seen
        if left:
            listing = ", ".join(f"p{p}@{b[1]:.0f}" for p, *b in sorted(left))
            bad.append(f"{len(left)} measured region(s) unaccounted: {listing}")
        if rec.get("unaccounted", 0) != len(left):
            bad.append(f"record says unaccounted={rec.get('unaccounted')}, recount is {len(left)}")
    return bad


def main(argv: list[str]) -> int:
    pids = argv or [p.stem for p in sorted((LANE / "records").glob("*.json"))]
    failed = 0
    for pid in pids:
        bad = audit(pid)
        if bad:
            failed += 1
            print(f"{pid}: FAIL ({len(bad)})")
            for line in bad:
                print(f"  {line}")
        else:
            print(f"{pid}: pass")
    print(f"\n{len(pids) - failed} pass, {failed} fail, {len(pids)} total")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main([a for a in sys.argv[1:] if not a.startswith("-")]))
