"""Hand pass for P-B-2014-30680-9f0c0d05 (a 2014 B paper that builds one directed game network per
season, ranks teams by eigenvector centrality, then optimises a coach-skill matrix with Powell's
method to name the five best college coaches of the last century), 21 PDF pages.

Nine measured regions over nine pages, all accounted for: five figure rows, four tables, no
refusals.

    page    region   what it is
    2       r1       unnumbered force-directed network picture, no caption
    3       r1       the top five per sport, 4 columns over five ranks
    10      r1       Figure 1, the 2009-2010 basketball network, vector
    12      r1       eigenvector centrality against the AP and USA Today polls, ten ranks
    13      r1       Figure 2, the 2012-2013 basketball network, raster
    14      r1       Figure 3, the density for mismatched players
    15      r1       Figure 4, the density for evenly matched players
    17      r1       Powell's method top three for 1962, 2000 and 2005
    18      r1       the definitive top five per sport with career values

No grid in this paper carries a number or a caption. The pages run two designs: the magazine
spread on pages 2 and 3 is Cambria on a 433.1 pt measure with its rules drawn as hairline filled
rectangles, the body is LaTeX on a 343.7 pt measure with stroked rules. All four grids are
complete closed grids - a rule under every row, including under the header, and a vertical
between every column - so `vertical-rules`, never booktabs. The page-2 picture and the page-13
picture are raster screenshots of the same force-directed layout; only the page-10 drawing is
vector, 612 circles and 4792 cubic Bezier edges.

Usage: python -I tools/_dist_paper63.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2014-30680-9f0c0d05"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for _pg in LAYOUT["pages"]:
    for _i, _r in enumerate(sorted(_pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(_pg["page"], _i)] = _r["bbox"]
        KIND[(_pg["page"], _i)] = _r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

for _key, _bbox in REG.items():
    _ctx = CTXREG.get(_key)
    if _ctx is None or max(abs(a - b) for a, b in zip(_ctx["bbox"], _bbox)) > 0.5:
        raise SystemExit(f"region numbering disagrees with the context dump at {_key}")

# The heading pass is polluted here in a way the section paths cannot survive: nine of the 49
# heading records are rows of the poll table ('1 Duke Kansas Kansas', '9 Kentucky Duke West
# Virginia'), and the nearest-heading rule hands three regions the wrong section - the Figure 2
# page gets '6 Separating the Coach Effect', the heading printed BELOW the picture, and the
# Figure 4 page gets '6.2 Margin of Win Probability', the heading printed 200 pt below it. Every
# path below is the printed label of the heading that actually governs the region, and every one
# is present in the text layer, so all of them carry section_numbered true.
SUMMARY = "未编号标题 Summary"
DEGREE = "5.2.1 Degree Centrality"
EIGEN = "5.2.3 Eigenvector Centrality"
COACHSKILL = "6.1 When is Coach Skill Important?"
POWELL = "6.3.3 Powell’s Method"
TOPCOACHES = "7.1 Top Coaches of the Last 100 Years"

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def place(page: int, reg: int, path: list[str], kind: str, numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(path),
        "section_numbered": numbered,
        "section_kind": kind,
        "doc_order": DOC_ORDER,
        "page_order": c["region"],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def none_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def cited(first_page: int, page: int, style: list[str], count: int, lead: str,
          trail: str = "", read: int = 1, gap: int | None = None) -> dict:
    """A by-number citation the text layer prints; check_mention re-quotes both sentences."""
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": schema.norm(lead),
            "trail_sentence": schema.norm(trail), "lead_pattern": "as-shown-in",
            "read_sentences": read, "gap_sentences": gap}


def caption(verbatim: str, numbering: str = "none", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)), "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap: str, numbering: str, mention: dict,
           path: list[str], kind: str, *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           source: str = "text-layer", numbered: bool = True, position: str = "below",
           note: str = "", other_note: str = "") -> None:
    word = q(cap, page) if (cap and source == "text-layer") else schema.norm(cap)
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": word,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, path, "model" if numbered else "abstract", numbered),
        "mention": mention,
        "caption": caption(word, numbering, position),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": False, "legend": legend, "colorbar": False,
                     "three_d": "no", "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, rows: int, cols: int, path: list[str], kind: str,
          note_sentence: str, note: str, *, numeric: int = 1, numbered: bool = True,
          width: str = "full", zebra: bool = False, merged: bool = False,
          decimal: bool = False, header_rows: int = 1, continued: bool = False,
          mention: dict | None = None) -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": "",
        "caption_source": "none",
        "note": note,
        "place": place(page, reg, path, kind, numbered),
        "mention": mention or none_mention(),
        "caption": caption("", "none", "below"),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": "vertical-rules", "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": False, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued, "note_sentence": schema.norm(note_sentence)},
    })


# ---------------------------------------------------------------- the magazine spread, pages 2-3
figure(2, 1, "node-link-network",
       "", "none", none_mention(), [SUMMARY], "raster", numbered=False, source="none",
       note="unnumbered: the popular-essay page introduces it with 'The resulting drawing will "
            "look something like this:' and prints no number and no caption under it. A single "
            "embedded greyscale PNG, 2480 by 2105 px at 862 dpi on the page, node size standing "
            "for team rank as the prose says ('the best teams have the biggest circles drawn'). "
            "Speckled and washed out - a screen grab of a slide, not a plot exported for print")

table(3, 1, 6, 4, [SUMMARY], "abstract", "These coaches are:",
      "the lane's first table on a magazine spread: Cambria 12 pt, header not bold although the "
      "capitalised single words read as bold, rules drawn as 0.5 pt filled rectangles rather than "
      "strokes, 4 columns over five ranks, 443.6 pt wide against the spread's 433.1 pt measure so "
      "it overhangs the text block by 5.5 pt each side. Unnumbered and uncaptioned, introduced by "
      "'These coaches are:'. The same five names print again, in the same order, on page 18",
      numbered=False)

# ---------------------------------------------------------------- section 5, the team model
figure(10, 1, "node-link-network",
       "Figure 1: A complete network for the 2009-2010 NCAA Div. I basketball season. Each node "
       "represents a team, and each edge represents a game between the two teams. Note that, since "
       "teams play other teams in their conference most often, many teams have clustered into one "
       "of the 32 NCAA Div.1 Conferences.",
       "Figure N:", none_mention(), [DEGREE], "vector",
       note="the only vector network in the paper: 612 open circles of 2.65 pt nominal diameter "
            "and 4792 cubic Bezier edges in 60 % grey, force-directed, no arrowheads, no labels, "
            "no frame, no axes. Placed at the head of the page it continues 5.2.1, above the "
            "5.2.2 heading, so it illustrates degree centrality rather than the metric named "
            "below it. Cited by number nowhere - the section reaches it by position only")

table(12, 1, 11, 4, [EIGEN], "model",
      "Below is a table of top ranks from eigenvector centrality compared to the AP and USA Today polls",
      "LaTeX grid, CMBX10 bold header over CMR10 body, the cells that agree with a poll set in "
      "CMTI10 italic exactly as the prose promises ('The italicized entries are ones that appear "
      "in the top ten of both eigenvector centrality ranking and one of the AP and USA Today "
      "polls'). 336.0 pt against the 343.7 pt measure, so inset 4 pt each side. Unnumbered and "
      "uncaptioned; the write-up calls it 'a table of top ranks' and reads it back as 'the table "
      "above'. One numeric column (Rank), three name columns, no decimal alignment to speak of")

figure(13, 1, "node-link-network",
       "Figure 2: A complete network for the 2012-2013 NCAA Div. I Men’s Basketball season. The "
       "size and darkness of each nodes represents its relative eigenvector centrality value. "
       "Again, note the clustering of teams into NCAA conferences.",
       "Figure N:", none_mention(), [EIGEN], "raster",
       note="raster, 841 blobs at threshold, node diameter 1-6 pt, edges straight grey hairlines, "
            "greyscale only, no axes or frame. The caption contradicts the sentence that "
            "introduces it one page earlier, which promises 'the eigenvector centrality values "
            "for all games played in the 2010-2011 NCAA Division I Mens Football tournament'; the "
            "caption says 2012-2013 basketball. Cited by number nowhere")

# ---------------------------------------------------------------- section 6, the coach effect
figure(14, 1, "line",
       "Figure 3: A has a high chance of winning when its players are more skilled.",
       "Figure N:",
       cited(14, 14, ["Figure 3"], 1,
             "We can draw a plot approximating the probability of winning by a certain margin, "
             "which is shown in Figure 3."),
       [COACHSKILL], "vector",
       note="one indigo density curve, #3F3D99 stroke over a #D8D8EA fill, 749 path segments, on "
            "open L-axes: no ticks, no tick values, no scale, no gridlines, no legend, no frame. "
            "The vertical line is an origin line 32.6 pt left of the peak and is unlabelled. Both "
            "axis titles fall outside the measured box - 'Probability' above the top edge, "
            "'Margin of Win' past the right edge at the axis terminus - at a 5-6 pt cap height, "
            "so a crop of the region alone holds neither of them")

figure(15, 1, "line",
       "Figure 4: Neither A nor B are more likely to win when player skills are the same (if "
       "player skill is the only factor considered).",
       "Figure N:",
       cited(15, 15, ["Figure 4"], 1,
             "the Gaussian curve looks like the one shown in Figure 4."),
       [COACHSKILL], "vector",
       note="the same drawing style as Figure 3, 690 path segments, same indigo stroke and "
            "periwinkle fill, but the peak sits on the origin line, which is the whole point of "
            "the pair. Same unlabelled axes and the same out-of-box axis titles. The lead sentence "
            "crosses the page turn from 14, so the quoted fragment opens mid-sentence. The caption "
            "sentence that sends the reader here also crosses the break")

# ---------------------------------------------------------------- sections 6.3.3 and 7.1
table(17, 1, 4, 4, [POWELL], "model",
      "The table above shows the results of running",
      "LaTeX grid, 4 columns over three ranks, 263.8 pt against the 343.7 pt measure (77 %) and "
      "centred on the page. Header is the three years, 1962, 2000 and 2005, and the body cells are "
      "coach names. Unnumbered and uncaptioned: the only reference is the trailing sentence 'The "
      "table above shows the results of running Powell's method until the probability function "
      "shown in Equation 6 is optimized, for three widely separated arbitrary years.'")

table(18, 1, 6, 4, [TOPCOACHES], "result",
      "we arrived at the following table",
      "LaTeX grid, 4 columns over five ranks, 382.3 pt against the 343.7 pt measure (111 %), "
      "left-aligned to the margin and so overrunning the right text edge by 39.8 pt into the "
      "margin. Each cell carries a name and a career value behind a hyphen. Unnumbered and "
      "uncaptioned, introduced by 'we arrived at the following table' and called definitive in "
      "the sentence before it. Three cells drop the leading zero ('.23', '.21', '.17') against "
      "eleven that keep it, so the value column is neither decimal-aligned nor consistently set")

# ---------------------------------------------------------------- payload
RULES = [
    "an unnumbered picture is still an exhibit when the prose points at it and nothing else "
    "fills the page slot, so the page-2 network is a figure row whose numbering is none and whose "
    "caption source is none [caption.numbering]",
    "a grid whose rules close every cell - a rule under each row and a vertical between each "
    "column - is vertical-rules, not booktabs and not boxed, even when the outer box is no "
    "heavier than the interior [table.rule_style]",
    "a table with no number and no caption line still needs a place, and its section comes from "
    "the heading that governs the page, not from the nearest heading above the box [place.section_path]",
    "rows counts every printed row including the header: four columns over five ranks is 6 by 4, "
    "not 5 by 4 [table.rows]",
    "a spread typeset in Cambria and a body typeset in LaTeX can print the same grid design two "
    "pages apart; the rule style is a property of the drawing, not of the typesetter [table.cols]",
    "the numeric column count follows the content of the body cells: a poll table whose body is "
    "club names has one numeric column, the rank stub, however many figures the caption mentions "
    "[table.numeric_cols]",
    "a value column that opens '.23' in three cells and '0.23' in eleven is not decimal-aligned, "
    "whatever the column looks like at a glance [table.decimal_aligned]",
    "width is measured against the local text measure: 443.6 pt is 102 % of the 433.1 pt magazine "
    "measure but 129 % of the 343.7 pt body measure, and both are full [table.width]",
    "the nearest heading is not always above the box - on the Figure 2 page the governing section "
    "is the one printed above the art, and the heading below it belongs to the next section "
    "[place.section_kind]",
    "a figure reached only by position counts as uncited: no printed number means count 0 and "
    "lead_pages null, and the prose pointer goes into the note [mention.count]",
    "when the prose sends the reader to a figure by name of the form 'is shown in Figure 3', the "
    "lead pattern is as-shown-in, and the quoted sentence must survive the page turn intact "
    "[mention.lead_sentence]",
    "a caption that contradicts the sentence which introduces it is recorded as printed and the "
    "contradiction goes in the item note; the census does not repair the paper [caption.verbatim]",
    "an axis title set at the axis terminus, outside the measured box, belongs to the figure but "
    "not to the region, so the note has to say where it prints [caption.position]",
    "printed_numbers is about the axes: a density curve with no ticks and no scale prints no "
    "numbers even though its caption argues about a shift [geometry.printed_numbers]",
    "a force-directed network with no labels and no legend is still node-link-network, raster or "
    "vector [geometry.family]",
    "two panels printed as two numbered figures are two rows with panel_count 1, and a note that "
    "names their mate [geometry.panel_count]",
]

NOTE = (
    "Nine measured regions over nine of twenty-one pages, all accounted for, no refusals. Four of "
    "the nine are tables and not one of them carries a number or a caption: page 3 prints 'These "
    "coaches are:', page 12 'Below is a table of top ranks from eigenvector centrality compared to "
    "the AP and USA Today polls', page 17 'The table above shows the results of running Powell's "
    "method', page 18 'we arrived at the following table'. The four printed figures all run the "
    "'Figure N:' numbering on the caption line with no punctuation after the number. "
    "\n\n"
    "Unmeasured, declared rather than invented: (1) the two-circle arrow sketch on page 2, an "
    "image of 388 by 24 px placed at 198.0-414.0 by 353.6-367.4 pt inside the paragraph that "
    "explains how to draw one game - an in-body diagram, too small for the layout pass to box, and "
    "not an exhibit; (2) the inline 'A -> B -> C' chain on page 12, which is typeset in running "
    "prose and has no box; (3) display equations (1) to (9), which print as text and fraction "
    "rules, none of them a measured region. "
    "\n\n"
    "Defects recorded, not corrected: Figure 2's caption names the 2012-2013 basketball season "
    "while the sentence that introduces it one page earlier names the 2010-2011 football "
    "tournament; both density figures print A-axis titles outside the drawing's own box, "
    "'Probability' above the top edge and 'Margin of Win' past the right edge at the axis "
    "terminus, at a 5-6 pt cap height, and neither carries a scale, so the shift the captions "
    "argue about cannot be read off them; page 18 drops the leading zero in three career values; "
    "the page-3 header is not bold although the capitalised words read as if it were. The prose "
    "typos stand as printed: 'each nodes', 'infl uene', 'equalivalent', 'initalizing', "
    "'appearences', 'Krzyzewsky', 'three three outstanding coaches'."
)

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT["layout_sha256"],
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc63-payload.json"
out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
