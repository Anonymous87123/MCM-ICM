"""Validate one paper's census payload and write records/<pid>.json + notes/<pid>.md.

The payload is written by hand from the crops. This script never invents a family; it
only refuses payloads that break the vocabulary or leave a measured region unaccounted.

Usage:
  python -I lanes/L7-figure-census/tools/record.py <pid> --payload <file.json> [--force]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
LAYOUT = LANE / "layout"
RECORDS = LANE / "records"
NOTES = LANE / "notes"
PROXY = LANE / ".proxy"
sys.path.insert(0, str(Path(__file__).resolve().parent))

import schema  # noqa: E402

RULE_CITE = re.compile(r"\[([a-z_]+\.[a-z_]+)\]")

FAMILIES = {
    "line", "scatter", "bar", "histogram", "box-or-violin", "heatmap-or-contour",
    "surface-or-3D", "node-link-network", "flowchart-or-schematic", "map-or-plan-view",
    "photo-or-raster-image", "table-as-figure", "composite-panel", "other",
}
CONFIDENCE = {"high", "medium", "low"}
CAPTION_SOURCES = {"text-layer", "typed-from-crop", "none"}
REASONS = {"caption-background", "rule", "fragment-of-other", "duplicate",
           "background", "in-body-diagram", "not-an-exhibit", "split-across-pages"}


def fail(msg: str) -> None:
    raise SystemExit(f"record rejected: {msg}")


def region_key(page: int, bbox: list[float]) -> tuple:
    return (int(page),) + tuple(round(float(v), 1) for v in bbox)


def quote_pages(exhibit: dict) -> list[int]:
    """Pages a quoted lead/trail sentence may come from.

    Same page and its two neighbours, plus the page where the paper first names the
    exhibit: a lead sentence usually sits there when the figure is placed further on,
    and a trail sentence often lands there too when a later section re-reads the figure.
    """
    page = int(exhibit["page"])
    pages = {page - 1, page, page + 1}
    first = exhibit.get("mention", {}).get("first_page")
    if isinstance(first, int):
        pages |= {first - 1, first, first + 1}
    return sorted(p for p in pages if p >= 1)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pid")
    ap.add_argument("--payload", required=True)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args(argv)

    layout_path = LAYOUT / f"{args.pid}.json"
    if not layout_path.exists():
        fail(f"no layout for {args.pid}; run fig_extract.py layout first")
    ctx_path = PROXY / f"{args.pid}-ctx.json"
    if not ctx_path.exists():
        fail(f"no context dump for {args.pid}; run context_extract.py first")
    layout = json.loads(layout_path.read_text(encoding="utf-8"))
    ctx = json.loads(ctx_path.read_text(encoding="utf-8"))
    payload = json.loads(Path(args.payload).read_text(encoding="utf-8"))
    headings = ctx["headings"]

    if payload.get("paper") != args.pid:
        fail("payload paper does not match pid")
    if payload.get("layout_sha256") != layout["layout_sha256"]:
        fail("payload layout_sha256 does not match the measured layout; re-run fig_extract")

    measured = {region_key(pg["page"], r["bbox"])
                for pg in layout["pages"] for r in pg["regions"]}
    seen: set[tuple] = set()

    items = payload.get("items", [])
    for i, it in enumerate(items, 1):
        fam = it.get("family")
        if fam not in FAMILIES:
            fail(f"item {i}: family {fam!r} not in the closed vocabulary")
        if it.get("confidence") not in CONFIDENCE:
            fail(f"item {i}: confidence must be one of {sorted(CONFIDENCE)}")
        if not isinstance(it.get("panel_count"), int) or it["panel_count"] < 1:
            fail(f"item {i}: panel_count must be an int >= 1")
        src = it.get("caption_source", "text-layer")
        if src not in CAPTION_SOURCES:
            fail(f"item {i}: caption_source {src!r} invalid")
        if src != "none" and not (it.get("caption_verbatim") or "").strip():
            fail(f"item {i}: empty caption and caption_source is not 'none'")
        if "page" not in it or "bbox" not in it:
            fail(f"item {i}: page and bbox are required")
        key = region_key(it["page"], it["bbox"])
        if key not in measured:
            fail(f"item {i}: bbox {it['bbox']} on page {it['page']} is not a measured region")
        if key in seen:
            fail(f"item {i}: region counted twice")
        seen.add(key)
        if fam == "other" and not (it.get("other_note") or "").strip():
            fail(f"item {i}: family 'other' needs other_note")
        if fam == "composite-panel" and it["panel_count"] < 2:
            fail(f"item {i}: composite-panel needs panel_count >= 2")

        for block in ("place", "mention", "caption", "geometry"):
            if not isinstance(it.get(block), dict):
                fail(f"item {i}: missing {block} block")
        try:
            schema.check_place(it["place"], args.pid, headings, f"item {i}")
            schema.check_mention(it["mention"], args.pid, it["page"], f"item {i}",
                                 quote_pages(it))
            schema.check_caption(it["caption"], f"item {i}")
            schema.check_geometry(it["geometry"], FAMILIES, f"item {i}")
        except schema.Bad as exc:
            fail(str(exc))
        if it["geometry"]["family"] != fam:
            fail(f"item {i}: family {fam!r} disagrees with geometry.family "
                 f"{it['geometry']['family']!r}")
        if it["geometry"]["panel_count"] != it["panel_count"]:
            fail(f"item {i}: panel_count disagrees with geometry.panel_count")
        if it["caption"]["verbatim"] != (it.get("caption_verbatim") or ""):
            fail(f"item {i}: caption.verbatim must equal caption_verbatim")
        if src == "text-layer":
            try:
                schema.check_quote(it["caption"]["verbatim"], args.pid,
                                   [it["page"] - 1, it["page"], it["page"] + 1],
                                   f"item {i} caption", limit=None)
            except schema.Bad as exc:
                fail(str(exc))

    tables = payload.get("tables", [])
    for i, t in enumerate(tables, 1):
        if "page" not in t or "bbox" not in t:
            fail(f"table {i}: page and bbox are required")
        key = region_key(t["page"], t["bbox"])
        if key not in measured:
            fail(f"table {i}: bbox on page {t['page']} is not a measured region")
        if key in seen:
            fail(f"table {i}: region already counted as a figure item")
        seen.add(key)
        for block in ("place", "mention", "caption", "table"):
            if not isinstance(t.get(block), dict):
                fail(f"table {i}: missing {block} block")
        try:
            schema.check_place(t["place"], args.pid, headings, f"table {i}")
            schema.check_mention(t["mention"], args.pid, t["page"], f"table {i}",
                                 quote_pages(t))
            schema.check_caption(t["caption"], f"table {i}")
            schema.check_table(t["table"], f"table {i}")
            if t["table"]["note_sentence"]:
                schema.check_quote(t["table"]["note_sentence"], args.pid,
                                   [t["page"], t["page"] + 1], f"table {i} note")
            if (t.get("caption_source") or "text-layer") == "text-layer":
                schema.check_quote(t["caption"]["verbatim"], args.pid,
                                   [t["page"] - 1, t["page"], t["page"] + 1],
                                   f"table {i} caption", limit=None)
        except schema.Bad as exc:
            fail(str(exc))
        if t["caption"]["verbatim"] != (t.get("caption_verbatim") or ""):
            fail(f"table {i}: caption.verbatim must equal caption_verbatim")

    for i, ex in enumerate(payload.get("excluded_regions", []), 1):
        if ex.get("reason") not in REASONS:
            fail(f"excluded {i}: reason {ex.get('reason')!r} not allowed")
        key = region_key(ex["page"], ex["bbox"])
        if key not in measured:
            fail(f"excluded {i}: bbox on page {ex['page']} is not a measured region")
        if key in seen:
            fail(f"excluded {i}: region already counted")
        seen.add(key)

    rules = [r for r in payload.get("rules", []) if r.strip()]
    if not rules:
        fail("payload has no rules: notes/<pid>.md must state the distillation as "
             "rules, one per line, each citing the field it came from")
    field_paths = set()
    for bucket in (items, tables):
        for entry in bucket:
            for block, value in entry.items():
                if isinstance(value, dict):
                    field_paths |= {f"{block}.{k}" for k in value}
    for n, rule in enumerate(rules, 1):
        cited = RULE_CITE.findall(rule)
        if not cited:
            fail(f"rule {n} cites no field: append e.g. [caption.numbering]")
        for path in cited:
            if path not in field_paths:
                fail(f"rule {n} cites {path!r}, which no recorded exhibit carries")

    missing = measured - seen
    if missing and not args.force:
        listing = ", ".join(f"p{p}@{b[1]:.0f}" for p, *b in sorted(missing))
        fail(f"{len(missing)} measured region(s) unaccounted: {listing}. "
             "Account for each as item, table, or excluded_region, or pass --force.")

    record = {
        "paper": args.pid,
        "layout_sha256": layout["layout_sha256"],
        "census_version": 2,
        "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "page_count": layout["page_count"],
        "measured_regions": len(measured),
        "figure_items": len(items),
        "table_items": len(tables),
        "excluded_regions": len(payload.get("excluded_regions", [])),
        "unaccounted": len(missing),
        "items": items,
        "tables": tables,
        "excluded_regions": payload.get("excluded_regions", []),
        "family_counts": {},
        "rules": rules,
        "note": payload.get("note", ""),
    }
    counts: dict[str, int] = {}
    for it in items:
        counts[it["family"]] = counts.get(it["family"], 0) + 1
    if tables:
        counts["table-grid"] = len(tables)
    record["family_counts"] = dict(sorted(counts.items()))

    RECORDS.mkdir(parents=True, exist_ok=True)
    (RECORDS / f"{args.pid}.json").write_text(
        json.dumps(record, indent=1, sort_keys=True), encoding="utf-8")

    lines = [f"# {args.pid} — figure census", "",
             f"- layout sha `{layout['layout_sha256']}`, {layout['page_count']} pages, "
             f"{len(measured)} measured regions",
             f"- accounted: {len(items)} figures, {len(tables)} tables, "
             f"{len(record['excluded_regions'])} excluded, {len(missing)} unaccounted",
             f"- families: " + ", ".join(f"{k} {v}" for k, v in record["family_counts"].items()),
             ""]
    for n, it in enumerate(items, 1):
        lines.append(f"{n}. p{it['page']} **{it['family']}** conf={it['confidence']} "
                     f"panels={it['panel_count']}"
                     + (f" panel_of={it['is_panel_of']}" if it.get("is_panel_of") else ""))
        lines.append(f"   bbox {it['bbox']} ({'raster' if it.get('kind') == 'raster' else it.get('kind', '?')})")
        lines.append(f"   cap: {it.get('caption_verbatim', '')[:300]}")
        if it.get("note"):
            lines.append(f"   note: {it['note']}")
    if tables:
        lines += ["", "## tables"]
        for n, t in enumerate(tables, 1):
            lines.append(f"{n}. p{t['page']} table-grid bbox {t['bbox']}")
            lines.append(f"   cap: {t.get('caption_verbatim', '')[:300]}")
    if record["excluded_regions"]:
        lines += ["", "## excluded"]
        for ex in record["excluded_regions"]:
            lines.append(f"- p{ex['page']} {ex['reason']} bbox {ex['bbox']} {ex.get('note', '')}")
    if missing:
        lines += ["", f"## unaccounted ({len(missing)})", "forced, see README"]
    NOTES.mkdir(parents=True, exist_ok=True)
    inv = ["## distillation fields", ""]
    for bucket, name in ((items, "figure"), (tables, "table")):
        for n, e in enumerate(bucket, 1):
            p, g = e["place"], e.get("geometry", {})
            m, c = e["mention"], e["caption"]
            inv.append(f"{name} {n} p{e['page']}: "
                       f"sec={' > '.join(p['section_path'])} [{p['section_kind']}] "
                       f"zone={p['page_zone']} order={p['doc_order']}/{p['page_order']} "
                       f"area={p['area_frac']} solo={p['solo_page']}")
            inv.append(f"  family={g.get('family', 'table-grid')} "
                       f"panels={g.get('panel_count', 1)} layout={g.get('panel_layout', '-')} "
                       f"shared={g.get('shared_axes', '-')} legend={g.get('legend', '-')} "
                       f"cbar={g.get('colorbar', '-')} 3d={g.get('three_d', '-')} "
                       f"printed={g.get('printed_numbers', '-')}")
            inv.append(f"  mention: first={m['first_page']} lead={m['lead_pages']} "
                       f"count={m['count']} read={m['read_sentences']} "
                       f"gap={m['gap_sentences']} pattern={m['lead_pattern']} "
                       f"style={m['style']}")
            inv.append(f"  caption: {c['numbering']} words={c['words']} "
                       f"sent={c['sentences']} units={c['units']} vars={c['variable_count']} "
                       f"cond={c['conditions']} concl={c['concludes']} voice={c['voice']} "
                       f"pos={c['position']}")
            if e.get("table"):
                t = e["table"]
                inv.append(f"  table: {t['rows']}x{t['cols']} header={t['header_rows']} "
                           f"rules={t['rule_style']} zebra={t['zebra']} "
                           f"merged={t['merged_cells']} diag={t['diagonal_header']} "
                           f"units_hdr={t['units_in_header']} dec={t['decimal_aligned']} "
                           f"num={t['numeric_cols']} txt={t['text_cols']} "
                           f"width={t['width']} orient={t['orientation']} "
                           f"cont={t['continued']}")
            inv.append("")
    (NOTES / f"{args.pid}-inventory.md").write_text(
        "\n".join(lines + [""] + inv) + "\n", encoding="utf-8")
    (NOTES / f"{args.pid}.md").write_text(
        "\n".join([f"# {args.pid} — distilled rules", ""] + [f"- {r}" for r in rules]
                  + [""]), encoding="utf-8")

    print(f"{args.pid}: figures={len(items)} tables={len(tables)} "
          f"excluded={len(record['excluded_regions'])} unaccounted={len(missing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
