"""Hand census of P-B-2015-39173-b8260835 (Team 39173, 32 pages, 18 measured regions).

Eighteen measured regions over fourteen of the thirty-two pages, every one an exhibit: eighteen
figure rows, no refusal and no printed table. The paper prints thirteen numbered figures and
each of the thirteen owns a region; the other five rows are unnumbered pictures carrying no
caption at all.

   p6  r1  Fig.1   flowchart-or-schematic search cone with the IFP arrow and sigma-x
   p7  r1  Fig.2   flowchart-or-schematic the SAN x 6 search region matrix
   p8  r1  Fig.3   flowchart-or-schematic one region referenced to the IFP
   p13 r1  Fig.4   line                  f(G) at x=yi=0.5
   p13 r2  Fig.5   line                  POD(theta)
   p14 r1  Fig.6   line                  POD(G)
   p14 r2  Fig.7   line                  POD(hs)
   p15 r1  Fig.8   line                  POD(hs) against the plane count
   p16 r1  none    map-or-plan-view      the Boston to Lisbon route on a satellite basemap
   p17 r1  none    line                  the PDF for distance to casualty
   p18 r1  Fig.9   surface-or-3D         the joint density function
   p19 r1  Fig.10  bar                   POC for the search regions, drawn in 3-D
   p19 r2  Fig.11  table-as-figure       the POC allocated to every region, as a ruled table
   p21 r1  Fig.12  line                  the search path this model produces
   p22 r1  Fig.13  line                  the same path without the adjacency restriction
   p23 r1  none    table-as-figure       the Shifted Coords spreadsheet block
   p26 r1  none    table-as-figure       the INPUTS and Probabilities blocks
   p26 r2  none    table-as-figure       the Extended Calculation Information block

Eighteen figure rows, no tables and no refusals; nothing unresolved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2015-39173-b8260835"
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

# 595.28 x 841.89 pt page; the text block runs x 102.9 to 520.0, so the measure is 417.1 pt
MEASURE = 417.1
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


def place(page: int, reg: int, kind: str, path: list[str]) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
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


def cited(first_page: int, page: int, style: list[str], count: int, lead: str) -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": "direct",
            "read_sentences": 1, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": "below"}


# ---------------------------------------------------------------- section paths
# The heading index drops section 3 entirely - its title is set at the foot of p16 and the index
# reads the pages after it as 2.6.2 Weaknesses - and it never returns 2.1.2, so the Fig.3 row
# would inherit 2.1.1. Every path here is either the indexed label or the printed line itself,
# cut where the page breaks the heading.
SEC_211 = [q("2 Model", 3),
           q("2.1 Constructing Probabilities of Containment", 3),
           q("2.1.1 Partitioning Search Region Through Model Dis-", 6)]
SEC_212 = [q("2 Model", 3),
           q("2.1 Constructing Probabilities of Containment", 3),
           q("2.1.2 Finding Latitude and Longitude Coordinates for", 8)]
SEC_25 = [q("2 Model", 3), q("2.5 Sensitivity Analysis", 12)]
SEC_262 = [q("2 Model", 3), q("2.6 Strengths and Weaknesses of Our Model", 15),
           q("2.6.2 Weaknesses", 16)]
SEC_3 = [q("3 Working Example: Flight ABCD to Lisbon, Portugal", 16)]
SEC_7 = [q("7 Appendix B", 26)]


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "single",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", shared_axes: bool = False,
           note: str = "", other_note: str = "", confidence: str = "high") -> None:
    ITEMS.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": confidence,
        "other_note": other_note,
        "panel_count": panels,
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, numbering),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


# ---------------------------------------------------------------- 2.1 the model's geometry
figure(6, 1, "flowchart-or-schematic",
       q("Figure 1: One standard deviation is calculated to be the distance from the IFP where "
         "a plane gliding", 6), "Figure N:",
       cited(16, 6, ["Figure 1"], 1, "Refer to Figure 1."),
       "model", SEC_211, labels=True, note=(
           "A black-outlined search cone hanging from the flight path, the IFP arrow run down "
           "from the apex to the top edge, a dashed offset line on the right and a small angle "
           "mark at the apex lettered theta; sigma-x, G and h are lettered on the art and never "
           "on an axis. The caption is a sentence and a half, and its second sentence is the only "
           "place the paper states the standard deviation used throughout [geometry.family]."))
figure(7, 1, "flowchart-or-schematic",
       q("Figure 2: The discretization method is modeled by the above SAN ×6 search region "
         "matrix.", 7), "Figure N:", none_mention(), "model", SEC_211, labels=True,
       note=(
           "The same cone seen from above as a five-column, four-row matrix of cells, a red line "
           "down the middle marking the IFP, sigma tick labels along the bottom edge and two "
           "bracketed recurrence formulas printed outside the right edge. It is the drawing that "
           "defines the N x 6 partition the rest of the paper counts in [geometry.family]."))
figure(8, 1, "flowchart-or-schematic",
       q("Figure 3: The location of a given ru×l = (l, u) in reference to an IFP and σx", 8),
       "Figure N:", none_mention(), "model", SEC_212, labels=True, note=(
           "A grid of empty cells with one cell picked out in pale blue and arrowed to its "
           "formula, the IFP line in red, a brace under the bottom row lettered sigma-x. The "
           "captions of this row and the row above it are the paper's only two naming the "
           "partition coordinates [geometry.family]."))

# ---------------------------------------------------------------- 2.5 the sensitivity sweep
figure(13, 1, "line",
       q("Figure 4: f (G) where (x, yI ) = (0.5, 0.5) exemplifies the curvature of f (G) and "
         "f (θ) regardless of the x and yI values", 13), "Figure N:",
       cited(14, 13, ["Figure 4"], 1,
             "Figure 4 illustrates that when h"),
       "sensitivity", SEC_25, note=(
           "One thin decaying curve read off two rulers, from about 6e-5 at the left down to "
           "5e-6 by x=50, with no axis titles and no legend. The prose sentence that refers to "
           "it sits on the next page and reaches the layer with the subscript glyph broken, so "
           "the quote recorded here stops where the layer breaks [geometry.family]."))
figure(13, 2, "line",
       q("Figure 5: P OD(θ) where θ is in radians", 13), "Figure N:", none_mention(),
       "sensitivity", SEC_25, note=(
           "A monotone decreasing curve from 1.0 near the left end to 0.2 at x=1.5, the axes "
           "ticked and unlabelled. Same frame as Figure 4 and printed below it on the same page "
           "[geometry.family]."))
figure(14, 1, "line",
       q("Figure 6: P OD(G)", 14), "Figure N:", none_mention(), "sensitivity", SEC_25,
       note=(
           "A decreasing curve from 1.0 down to 0.1 by x=50 on ticked but untitled axes. The "
           "caption is four words and never says what G is; the paragraph below supplies it "
           "[geometry.family]."))
figure(14, 2, "line",
       q("Figure 7: P OD(hs ) where 0 ≤ hs <", 14), "Figure N:", none_mention(),
       "sensitivity", SEC_25, note=(
           "A curve falling from 0.44 to zero at x=4 on ruler-ticked axes. The printed caption "
           "stops mid-condition - 'where 0 <= hs <' with no upper bound, the glyph reaching the "
           "layer as a control character - so the verbatim stops where the paper's own caption "
           "stops [caption.verbatim]."))
figure(15, 1, "line",
       q("Figure 8: P OD(hs ) where n ∈ N", 15), "Figure N:", none_mention(),
       "sensitivity", SEC_25, note=(
           "The mirror case: a concave curve rising from the origin and flattening near 0.9 by "
           "x=20, the plane count n varied instead of the altitude. Last row of the sensitivity "
           "sweep, which is four plots deep by now [geometry.family]."))

# ---------------------------------------------------------------- 2.6 and the worked example
figure(16, 1, "map-or-plan-view",
       "", "none", none_mention(), "other", SEC_262, labels=True, source="none", note=(
           "A satellite basemap of the North Atlantic with the great-circle route drawn as a "
           "light blue line between pin markers at Boston and Lleida and a readout box over the "
           "water giving 8 h 15 min and 5,186 miles. It is a screenshot, not a drawn figure, and "
           "it carries no caption and no number anywhere on the page [caption.verbatim]."))
figure(17, 1, "line", "", "none", none_mention(), "solution", SEC_3, labels=True,
       source="none", note=(
           "A density curve for the distance to the casualty, decaying from 0.0018 toward zero "
           "by 1700 miles, the only plot in the paper whose axes are both titled and the only "
           "one with a title set inside its own plot area ('PDF for Distance to Casualty'). No "
           "number, no caption [caption.verbatim]."))
figure(18, 1, "surface-or-3D",
       q("Figure 9: The joint density function is shown above, indicating the locations in "
         "which the POC is largest, and locations where the POC is smallest", 18), "Figure N:",
       none_mention(), "solution", SEC_3, labels=True, note=(
           "A perspective surface over the (x, y1) plane, mesh over pastel fill, a single tall "
           "ridge falling away along y1, z ticked at 0, 5e-6 and 1e-5. The caption is one long "
           "sentence with no full stop and points back at the picture with 'shown above' "
           "[geometry.family]."))
figure(19, 1, "bar",
       q("Figure 10: The graph above represents the discretized POC of Flight ABCD", 19),
       "Figure N:", none_mention(), "solution", SEC_3, labels=True,
       three_d="perspective-bars", note=(
           "Square prism bars on a flat tiled floor, stepping down across and back, coloured by "
           "height with no key, POC ticked 0 to 0.15 against N ticked 1 to 6. The one bar family "
           "row in the paper, and the only 3-D bar rendering in this census so far "
           "[geometry.three_d]."))
figure(19, 2, "table-as-figure",
       q("Figure 11: Map representation of POC allocated to each of the search regions", 19),
       "Figure N:", none_mention(), "solution", SEC_3, labels=True, note=(
           "The caption calls this a map representation and the pixels are a ruled table: seven "
           "columns under an italic title strip reading 'Probability of Containment for Search "
           "Regions', a row of decimal probabilities and a bottom row of sigma labels with an "
           "N-from-N column at the right. Recorded as table-as-figure because that is what the "
           "picture is; the caption is quoted as printed and the mismatch is left standing "
           "[caption.verbatim]."))
figure(21, 1, "line",
       q("Figure 12: The diagram above shows the search path produced by our al- gorithm and "
         "described by the output of the Mathematica code in Appendix C.", 21), "Figure N:",
       none_mention(), "solution", SEC_3, note=(
           "A square grid with heavier centre crosshairs overlaid by nested rounded search loops "
           "and straighter transit segments, an aircraft glyph in the top-right corner, no axis "
           "titles and no legend. The caption is hyphenated mid-word in its own subtitle "
           "[geometry.family]."))
figure(22, 1, "line",
       q("Figure 13: The diagram above shows the search path produced by an algo- rithm similar "
         "to ours but without requiring subsequent search regions to be adjacent.", 22),
       "Figure N:", none_mention(), "solution", SEC_3, note=(
           "The same grid and crosshairs as Figure 12 and the same aircraft glyph, but the tracks "
           "are denser and cross each other freely because adjacency is no longer required. The "
           "two rows are the paper's one controlled comparison, and its prose refers to them "
           "deictically as 'the two figures above' without a number [geometry.family]."))

# ---------------------------------------------------------------- the appendix spreadsheets
figure(23, 1, "table-as-figure", "", "none", none_mention(), "solution", SEC_3, labels=True,
       source="none", note=(
           "A spreadsheet-screenshot block headed 'Shifted Coords:', four columns under IFP, IFP, "
           "sigma, sigma with a 2, 2, 3, 3 sub-header, two rows of angular decimals. It sits at "
           "the top of p23, ahead of the sentence sending the reader to Appendix B, so it belongs "
           "to the worked example and not to the press-conference section that the region pass "
           "assigned it to [place.section_path]."))
figure(26, 1, "table-as-figure", "", "none", none_mention(), "other", SEC_7, labels=True,
       panels=2, layout="stacked", source="none", note=(
           "Two Excel blocks stacked in one picture: an INPUTS block of seven labelled rows with "
           "two degree columns, and a Probabilities block of six numbered rows against the three "
           "standard-deviation columns. Same family in both panels, so one row with a panel count "
           "of two [geometry.panel_count]."))
figure(26, 2, "table-as-figure", "", "none", none_mention(), "other", SEC_7, labels=True,
       source="none", note=(
           "The largest spreadsheet block in the paper: a titled 'Extended Calculation "
           "Information' frame holding a label/value column and four sub-tables of coordinates "
           "and probabilities, separated by internal rules, ending on a 'divide by 69' scaling "
           "step. It is the calculation the whole model runs on, preserved as a screenshot "
           "[geometry.family]."))

# ---------------------------------------------------------------- rules and note
RULES: list[str] = [
    "Families split six ways over eighteen rows: eight line plots, four table-as-figure blocks, "
    "three flowchart-or-schematic drawings, one map-or-plan-view frame, one surface-or-3D and one "
    "bar [geometry.family].",
    "The four table-as-figure rows are all preserved tables rather than drawn plots - three "
    "spreadsheet screenshots from the appendices and Figure 11, whose printed caption calls it a "
    "map representation while the picture is a seven-column probability table [geometry.family].",
    "Only one row is a 3-D rendering with bars, Figure 10, and it is recorded with "
    "three_d perspective-bars rather than with the surface rows [geometry.three_d].",
    "Two rows carry more than one panel and neither is a composite: the stacked INPUTS and "
    "Probabilities blocks on p26 are the same family twice, so one row with a panel count of two "
    "[geometry.panel_count].",
    "Every caption in the paper prints BELOW its artwork, the thirteen numbered ones alike "
    "[caption.position].",
    "Numbering is 'Figure N:' for the thirteen printed figures and 'none' for the five pictures "
    "that never receive a number - the route map on p16, the density curve on p17, and the three "
    "spreadsheet blocks on pp23 and 26 [caption.numbering].",
    "Caption fidelity is poor. Figure 7's caption stops mid-condition at 'where 0 <= hs <' with "
    "no bound, the glyph reaching the layer as a control character; Figure 1's censored fraction "
    "reaches the layer as spaced digits; Figure 12 and Figure 13 are hyphenated mid-word in their "
    "own subtitles. Each verbatim stops where the printed caption stops [caption.verbatim].",
    "Citation is the weakest part of the paper: ten of the thirteen numbered figures are never "
    "named in the prose at all. Figure 1 is named once on p16, ten pages after it prints; Figure "
    "4 once on p14, a page after it prints; Figure 11 once on p20, a page after it prints. "
    "Figures 12 and 13 are referred to only as 'the two figures above' [mention.count].",
    "Every one of the three named exhibits is cited after it prints - leads of -10, -1 and -1 - "
    "so not one clause in the paper forecasts an exhibit [mention.lead_pages].",
    "Section paths are rebuilt by hand. The heading index never returns section 3 - its title "
    "sits at the foot of p16 after the weaknesses prose, and the index reads pp17-22 as 2.6.2 "
    "Weaknesses - and it never returns 2.1.2, so the Figure 3 row would inherit 2.1.1. The path "
    "behind 3 Working Example is checked against the layer [place.section_path].",
    "Area separates the row kinds here: the smallest row is the Shifted Coords block at "
    f"{pct(REG[(23, 1)][3] - REG[(23, 1)][1])} percent of the measure and the largest is the "
    f"search-region matrix at {pct(REG[(7, 1)][3] - REG[(7, 1)][1])} percent, a factor of six "
    "between them [place.area_frac].",
    "Nothing in this paper is a printed table with a number, so the table list is empty; the word "
    "Table never once appears in the text layer, which is why the three spreadsheet blocks are "
    "figure rows [geometry.family].",
]


NOTE = (
    "Paper 78, Team 39173, a 2015 paper that builds a probability-of-containment model for a "
    "missing transoceanic flight and then runs it on Flight ABCD from Boston to Lisbon. Eighteen "
    "measured regions over fourteen of the thirty-two pages, every one of them an exhibit: "
    "eighteen figure rows, no refusal, no printed table and nothing unresolved. The paper prints "
    "thirteen numbered figures and all thirteen own a region; the other five rows are unnumbered "
    "pictures that carry no caption at all.\n\n"
    "What the exhibits are. Three drawings carry the geometry of the model - the search cone of "
    "Figure 1, the SAN x 6 matrix of Figure 2 and the single referenced cell of Figure 3 - and "
    "eight line plots carry the sensitivity sweep of Figures 4 to 8 and the two search paths of "
    "Figures 12 and 13. One surface, Figure 9, is the joint density the whole method integrates; "
    "one 3-D bar chart, Figure 10, is the discretised result; and four blocks are preserved "
    "tables. The five unnumbered pictures are the route map on p16, the density curve on p17 and "
    "the three Excel screenshots of pp23 and 26.\n\n"
    "The one caption that does not match its picture is Figure 11. The printed caption reads "
    "'Map representation of POC allocated to each of the search regions', which is what a "
    "reader would expect next to the 3-D bar chart above it, but the pixels are a ruled seven-"
    "column table titled 'Probability of Containment for Search Regions'. The record keeps the "
    "caption as printed and classifies the picture as table-as-figure rather than repairing "
    "either side.\n\n"
    "The worked example sits inside the region pass's blind spot. Section 3's heading is set at "
    "the very foot of p16, printed with its folio caught in the same line, and the heading index "
    "never sees it: it reads pp17-22 as 2.6.2 Weaknesses, which would file the joint density, the "
    "discretised POC, the allocation table and both search paths under a weaknesses paragraph. "
    "The 2.1.2 heading is missed too, so Figure 3 would inherit 2.1.1. Every path in this record "
    "was typed from the printed headings and the contents page.\n\n"
    "Caption and citation are both thin. Figure 7 stops mid-condition, Figure 1's censored "
    "fraction reaches the layer as spaced digits, and the two search-path captions are "
    "hyphenated mid-word. Ten of the thirteen numbered figures are never named in prose; the "
    "three that are get a single bare pointer each, and all three point backwards - Figure 1 from "
    "ten pages later. Not one sentence in the paper forecasts an exhibit."
)

payload = {
    "paper": PID,
    "layout_sha256": LAYOUT.get("layout_sha256") or LAYOUT.get("sha256", ""),
    "items": ITEMS,
    "tables": TABLES,
    "excluded_regions": EXCLUDED,
    "rules": RULES,
    "note": NOTE,
}

out = PROXY / "pc78-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
