"""Hand census of P-B-2015-36178-d0225ad0 (Team 36178, 20 pages, 11 measured regions).

Eleven measured regions over nine of the twenty pages: ten figure rows and one refusal. The
paper prints seven numbered figures, Figures 1 to 7, and all seven own a measured region; the
other three rows are the unnumbered pictures of the closing press release on pp19-20, which
carry italic captions of their own but never a figure number. The paper prints no tables.

   p1  r1  refused - the summary sheet's cover form
   p5  r1  Fig.1   three search patterns sketched by hand
   p7  r1  Fig.2   ocean-current vector field over a satellite frame
   p8  r1  Fig.3   flight legs against the turn distance
   p9  r1  Fig.4   end locations, left turns only
   p9  r2  Fig.5   the full end-location set
   p11 r1  Fig.6   one leg of a search path, with its labels
   p14 r1  Fig.7   the algorithm comparison as a scatter
   p19 r1  press release, the full range of end locations
   p20 r1  press release, the two search patterns
   p20 r2  press release, the current field over debris

Ten figure rows and one refusal, no tables and nothing unresolved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2015-36178-d0225ad0"
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

# 595.32 x 841.92 pt page; the text block runs x 90.6 to 521.5, so the measure is 430.9 pt
MEASURE = 430.9
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def cap(page: int, prefix: str, tail: str) -> str:
    """Take the caption verbatim out of the layer: from its number to its last printed word."""
    text = schema.page_text(PID, page)
    start = text.find(prefix)
    if start < 0:
        raise KeyError((page, prefix))
    end = text.find(tail, start)
    if end < 0:
        raise KeyError((page, tail))
    return schema.norm(text[start:end + len(tail)])


def pct(span: float) -> str:
    return f"{span / MEASURE * 100:.1f}"


def place(page: int, reg: int, kind: str, path: list[str], numbered: bool = True) -> dict:
    global DOC_ORDER
    DOC_ORDER += 1
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
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
          pattern: str = "direct") -> dict:
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": q(lead, first_page),
            "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": 1, "gap_sentences": None}


def caption(verbatim: str, numbering: str = "Figure N:", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


# ---------------------------------------------------------------- section paths
def hlabel(page: int, number: str) -> str:
    """Printed label of a heading, taken from the ctx index by page and number.

    The index repeats small numbers - 1 and 2 and 4 each occur at several depths - so a lookup
    keyed on the number alone would return the wrong heading.
    """
    for h in CTX["headings"]:
        if h["page"] == page and h["number"] == number:
            return h["label"]
    raise KeyError((page, number))


SEC_HYP = [hlabel(5, "3"), hlabel(5, "3.1")]
SEC_PLANE = [hlabel(5, "4"), hlabel(5, "4.1"), hlabel(7, "4.1.3")]
SEC_AREA = [hlabel(5, "4"), hlabel(8, "4.2")]
SEC_LEG = [hlabel(5, "4"), hlabel(10, "4.5"), hlabel(11, "4.5.1")]
SEC_PICK = [hlabel(13, "5"), hlabel(13, "5.2"), hlabel(14, "5.2.2")]
# The closing spread prints a two-line title in an italic display face and no number.
SEC_PRESS = ["未编号标题 Addressing the Press Regarding the Plan for Future Searches"]


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", numbered: bool = True,
           note: str = "", other_note: str = "", shared_axes: bool = False,
           confidence: str = "high") -> None:
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
        "place": place(page, reg, kind, path, numbered),
        "mention": mention,
        "caption": caption(cap_text, numbering),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "reason": reason,
        "note": note,
    })


excluded(1, 1, "not-an-exhibit",
         ("The summary sheet's cover form: the Team Control Number and Problem Chosen rows with "
          "their boxes at the head of page 1, above the title block. No artwork, no number and "
          "no caption; the abstract's own text prints below it as live text."))

# ---------------------------------------------------------------- the seven printed figures
figure(5, 1, "flowchart-or-schematic",
       cap(5, "Figure 1: Some", "rectangular area."), "Figure N:",
       cited(5, 5, ["Figure 1"], 3, "illustrated in Figure 1."),
       "assumption", SEC_HYP, panels=3, layout="row of 3", labels=True, note=(
           "Three hand-drawn sketches on the same rectangle: a boustrophedon of parallel strips "
           "with the turn at the end of each, a diagonal sweep, and an inward spiral. The paper "
           "uses them as the set of ideas it then narrows down, and names Figure 1 three times "
           "in the prose on this page."))
figure(7, 1, "map-or-plan-view",
       cap(7, "Figure 2: A vector", "moving an object[21]"), "Figure N:", none_mention(),
       "model", SEC_PLANE, numbers=True, note=(
           "A dark satellite frame of open ocean with the current field drawn over it as cyan "
           "arrows and one white line traced across the picture, the grid position 65.20 E, "
           "43.23 S burnt into the image in yellow. The caption cites reference [21] and prints "
           "no full stop at all, which is why the verbatim stops at the bracket."))
figure(8, 1, "flowchart-or-schematic",
       cap(8, "Figure 3: The more", "the turn ends."), "Figure N:",
       cited(8, 8, ["Figure 3"], 1, "Figure 3 demonstrates"),
       "model", SEC_AREA, labels=True, note=(
           "Flight legs struck from one point, each ending on its own arc, labelled 5.30, 23.33, "
           "27.5, 31.66, 35.83 and 40 NM: the more the aircraft turns, the shorter the distance "
           "left to fly. The drawing carries the numbers, not an axis."))
figure(9, 1, "scatter",
       cap(9, "Figure 4: The possible", "the airplane’s turn radius."), "Figure N:",
       cited(8, 9, ["Figure 4"], 1, "in Figure 4"),
       "model", SEC_AREA, numbers=True, note=(
           "A blue cloud of candidate end points shaped as a single dome over the origin, with "
           "the turn radius drawn as a small grey circle inside it, on axes ticked at 20 and 40 "
           "over a frame running about -40 to 40. The left-only case: the cloud leans to one "
           "side of the vertical axis. Caption is two sentences, the second naming the circle."))
figure(9, 2, "scatter",
       cap(9, "Figure 5: The full", "example plane."), "Figure N:",
       cited(8, 9, ["Figure 5"], 1, "we get the result in Figure 5."),
       "model", SEC_AREA, numbers=True, note=(
           "The same construction mirrored, so the domino of end points is now two-lobed and "
           "symmetric about the vertical axis, with the turn-radius circle still drawn at the "
           "centre. Same axes and same frame as Figure 4, printed directly below it, and the two "
           "boxes are the paper's only stacked pair."))
figure(11, 1, "flowchart-or-schematic",
       cap(11, "Figure 6: A visual", "Search and Rescue Manual )"), "Figure N:",
       cited(11, 11, ["Figure 6"], 1,
             "(See Figure 6 for a visual representation of this terminology.)",
             "parenthetical"),
       "model", SEC_LEG, labels=True, note=(
           "One leg of a search path drawn as two long parallel straights joined by a rounded "
           "180-degree turn, with the track space S, the leg length L, the crossleg straightaway "
           "and the turn diameter all lettered on the art. The caption credits the United States "
           "National Search and Rescue Supplement and closes on a spaced-out bracket, so the "
           "verbatim keeps that bracket."))
figure(14, 1, "scatter",
       cap(14, "Figure 7: A visual", "higher wind speeds."), "Figure N:",
       cited(13, 14, ["Figure 7"], 1,
             "Figure 7 gives a visual representation of the results from the latter two search "
             "methods."),
       "result", SEC_PICK, numbers=True, note=(
           "The one plotted result in the paper: hundreds of points, red for the diagonal "
           "algorithm and blue for the optimised parallel search, rising in bands as the search "
           "index runs right, with ticks at 50, 100 and 150 across and 200 to 800 up. No axis "
           "titles are drawn in the art - the caption supplies both - and the caption also "
           "explains what the right-hand end of the axis means. Its own word 'di↵erent' carries "
           "the ligature the text layer holds, and 'meth- ods' is hyphenated mid-word in the "
           "caption itself."))

# ---------------------------------------------------------------- the press release spread
# These three carry italic captions typeset under the picture but no figure number, and the
# text layer prints every space in each caption as a dollar sign, so all three are typed from
# the crop rather than quoted.
figure(19, 1, "line",
       "The full range of end locations that the plane could have crashed at", "none",
       none_mention(), "other", SEC_PRESS, numbered=False, source="typed-from-crop",
       numbers=True, confidence="medium", note=(
           "The end-location plot redrawn for the letter: a blue circle about the origin with an "
           "inner figure-eight loop of marked points and two small grey circles, on axes ticked "
           "at 20 and 40 and nothing else. It restates the content of Figures 4 and 5 without "
           "referring to them, and its caption is a bare noun phrase, not a sentence. Recorded "
           "as line rather than scatter because the visible marks are the two closed curves; "
           "the point cloud of Figures 4 and 5 is not visible here, which is why the confidence "
           "is only medium."))
figure(20, 1, "flowchart-or-schematic",
       "The different search patterns", "none", none_mention(), "other", SEC_PRESS,
       numbered=False, source="typed-from-crop", panels=2, layout="row of 2", labels=True,
       note=(
           "Two boxed drawings side by side, both in the same frame: on the left the parallel "
           "pattern as a boustrophedon of horizontal strips with the turns at the ends, on the "
           "right the diagonal pattern as zigzag tracks. Same family in both panels, so a panel "
           "count of two and not a composite. The caption is four words and no full stop."))
figure(20, 2, "map-or-plan-view",
       "A vector field showing how ocean currents move debris", "none", none_mention(),
       "other", SEC_PRESS, numbered=False, source="typed-from-crop", numbers=True, note=(
           "The current field again, this time over a photographic sea surface: cyan arrows in "
           "the water, one white track line across the frame and the coordinate string 65.20 E, "
           "43.23 S in yellow at the top left. It is the press-release restatement of Figure 2, "
           "with a caption written for the letter and no reference number."))

# ---------------------------------------------------------------- rules and note
RULES: list[str] = [
    "Families split four ways and the count is small enough to state: four flowchart-or-"
    "schematic drawings, three scatters, two map-or-plan-view frames and one line plot, ten "
    "rows in all. Only one exhibit in the paper - Figure 7 - is a plotted result; the rest are "
    "the geometry the model is argued with [geometry.family].",
    "Two rows hold more than one panel and neither is a composite: Figure 1 is three hand-drawn "
    "patterns in a row and the press release's search-pattern picture is two boxed drawings in "
    "a row, and in both cases the panels are the same family, so each is one row with its panel "
    "count and its layout recorded [geometry.panel_count].",
    "The two map-or-plan-view rows are the only exhibits whose frame is geographic rather than "
    "cartesian: Figure 2 and the press release's current-field picture both show satellite sea "
    "surface with the current field drawn over it and a coordinate string in the corner. The "
    "probability plots of Figures 4, 5 and 7 are cartesian scatter frames in arbitrary units "
    "and are recorded as scatter, not as maps [geometry.family].",
    "Every caption in the paper prints BELOW its artwork, the seven numbered ones and the three "
    "italic letter captions alike, and nothing in the paper prints above [caption.position].",
    "Numbering is 'Figure N:' for the seven printed figures, including Figure 2 whose caption "
    "carries no full stop at all and stops on its reference bracket. The three pictures on "
    "pp19-20 print no figure number anywhere - they are the press release's own pictures - so "
    "they are recorded with numbering 'none' and their captions typed from the crop "
    "[caption.numbering].",
    "The letter's captions are unquotable from the text layer: page 19 prints 'The$full$range$"
    "of$end$locations$that$the$plane$could$have$crashed$at$' and page 20 prints 'The$different$"
    "search$patterns$' and 'A$vector$field$showing$how$ocean$currents$move$debris1$', every "
    "space rendered as a dollar sign because the letter's face has no space glyph in the "
    "subset. That is why all three are typed from the crop [caption.verbatim].",
    "Citation is uneven: Figure 1 is named three times on p5, Figures 3, 4 and 5 are each named "
    "once on p8 although the art of 4 and 5 prints on p9, Figure 6 is named once inside a "
    "parenthesis on p11, and Figure 7 is named once on p13 for art on p14. Figure 2 is never "
    "named in prose at all [mention.count].",
    "Three exhibits lead their section by a page and one trails: Figures 4 and 5 are cited on "
    "p8 and print on p9, Figure 7 is cited on p13 and prints on p14, while Figure 6 is cited "
    "and printed on the same page. Two of the paper's own sentences point at a figure that is "
    "not on the page they print on [mention.lead_pages].",
    "Section paths are taken by hand from the printed headings because the index is unreliable "
    "on this paper: it returns 'Modeling a generic downed plane using parameters' and "
    "'Modeling a generic search plane using parameters' as headings numbered 1, and the five "
    "aircraft of p6 as headings numbered 1 to 5, and it never returns a label for subsection "
    "4.1.3's parent chain in the right order. Each path here is the chain of printed labels "
    "with matching numbers and pages [place.section_path].",
    "The closing spread has no numbered heading at all - pages 19 and 20 print an italic "
    "two-line title, 'Addressing the Press Regarding the Plan for Future Searches', and no "
    "number - so the three rows there carry section_numbered false and the title behind the "
    "未编号标题 prefix [place.section_path].",
    "Area does not separate exhibits from furniture here either. The refusal on p1 is 0.236 of "
    "the page, larger than any figure in the paper, because the cover form spans the full text "
    "measure at the top of the sheet; the ten figure rows run from 0.072 to 0.184 [place.area_frac].",
    "Nothing in this paper is a printed table. The word Table never once appears in the text "
    "layer across all twenty pages, so the table list is empty and the family distribution "
    "carries no table-grid [geometry.family].",
]

NOTE = (
    "Paper 76, Team 36178, a 2015 paper on locating and then searching for an aircraft lost "
    "over water. Eleven measured regions over nine of the twenty pages: ten figure rows and one "
    "refusal, nothing unaccounted for and nothing unresolved. The paper prints seven numbered "
    "figures and all seven are here; the other three rows are the unnumbered pictures of the "
    "closing press release. It prints no tables at all, and the word Table never occurs in its "
    "text layer.\n\n"
    "What the exhibits are. Four drawings carry the geometry: Figure 1's three hand-drawn search "
    "patterns, Figure 3's flight legs against the turn distance, Figure 6's labelled leg of a "
    "search path, and the letter's two-panel picture of the parallel and diagonal patterns. "
    "Three scatters carry the end-location sets of Figures 4 and 5 and the algorithm comparison "
    "of Figure 7, which is the paper's only plotted result and the only exhibit with a data "
    "series in it. Two maps carry the ocean current field - Figure 2 in the body and the same "
    "field again on the letter's last page - and one line plot on p19 redraws the end-location "
    "geometry for the letter.\n\n"
    "The refusal is the summary sheet's cover form, which spans the full text measure at the top "
    "of page 1 and measures larger than any real exhibit in the paper. It is a registration "
    "block: team number, problem chosen, and the blank lines the contest leaves for its own "
    "entries.\n\n"
    "What is unusual here is the text layer. The letter on pp19-20 is set in a face whose subset "
    "has no space glyph, so every space in its three captions reaches the layer as a dollar "
    "sign, and its coordinate annotation reaches the layer as replacement characters. Nothing "
    "in that spread can be quoted, so all three captions are typed from the crops. The letter "
    "also repeats the paper's own results without cross-referencing them: its end-location "
    "picture is Figures 4 and 5 drawn again, and its current-field picture is Figure 2 drawn "
    "again, neither carrying a number or a reference back.\n\n"
    "Two smaller defects are worth recording. Figure 2's caption has no full stop - the verbatim "
    "stops on its reference bracket because that is where the printed caption stops - and "
    "Figure 6's caption closes on a spaced-out parenthesis, so its verbatim keeps the gap. The "
    "heading index is a third: it reads the five aircraft of p6 as headings numbered 1 to 5 and "
    "both modelling subsections as heading 1, so every section path in this record was taken "
    "from the printed labels by hand rather than from the ctx chain.\n\n"
    "Citation is thin and mostly deictic, except for Figure 1, which the prose on p5 names three "
    "times in one page. Figures 4 and 5 are announced a page before they print and Figure 7 a "
    "page before it prints, which is the only forward-lead behaviour in the paper."
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

out = PROXY / "pc76-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
