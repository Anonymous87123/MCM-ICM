"""Hand pass for P-B-2011-12114-03fd7440 (repeater coverage of a region, 28 pages).

Fifteen numbered figures, no tables. The geometry pass measured 31 regions: 28 are panel
bodies of numbered figures and 3 are program listings. Every family below was read off a
cropped page proxy.

What drives the record:

* Captions sit inline. This paper breaks every single convention the earlier papers followed:
  Figure 2's caption is printed to the right of a body line ("... we only    Figure 2: Circles
  of radii 40 and 10."), Figure 3's caption sits under two panels that each carry their own
  inline label, and Figure 10's caption is split across three indented lines with a hyphen
  break ("distribu- tion"). Captions are therefore typed from the text layer and each one is
  verified as a verbatim substring of its page.
* One figure is not measurable. Figure 1 on p6 is a text table of UK repeater channels with a
  caption line; the page carries three thin rules and no image block, so nothing passes the
  extractor's size filter and the figure stays unresolved.
* Program listings. Pages 14, 17 and 19 carry "Program 1-3" blocks with a ruled title bar and
  a block of parameter definitions, not figures. They are excluded as not-an-exhibit, the same
  class the lane carries for algorithm listings.
* Family split for the point clouds. Every coverage picture has unitless axes (-40..40 with no
  axis title), so the family is scatter; a plan view whose axes are titled in Miles is
  map-or-plan-view, and that distinction is what separates these figures from the placement
  maps of the two previous papers.

Usage: python -I tools/_dist_paper20.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2011-12114-03fd7440"
PROXY = LANE / ".proxy"
PAGES = LANE.parents[1] / "artifacts" / "papers" / PID / "text" / "pages"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}
MENTIONS = CTX["mentions"]

CORPUS = LANE.parents[2] / "MCM-ICM-master"
QUEUE = LANE / "queue.txt"
PDF = next(
    CORPUS.joinpath(*line.split()[2].split("/"))
    for line in QUEUE.read_text(encoding="utf-8").splitlines()
    if line.strip() and line.split()[1] == PID)

CAPTIONS: dict[int, tuple[int, str]] = {
    1: (6, "Figure 1: The number of repeaters which output at given frequencies in the UK.[10]"),
    2: (9, "Figure 2: Circles of radii 40 and 10."),
    3: (10, "Figure 3: Upper bound of 21 derived from hexagonal packing."),
    4: (11, "Figure 4: Signal range extends due to tropospheric interference."),
    5: (12, "Figure 5: Reflections of the signal can interfere or strengthen the direct wave."),
    6: (12, "Figure 6: Diffraction over surfaces can cause indirect paths to connect antennas."),
    7: (13, "Figure 7: The two types of considered user distributions with 1000 users."),
    8: (19, "Figure 8: Uniform distribution of 1000 users with 80%, 92%, and 100% coverage. "
            "The number of colors corresponds to the number of frequencies used."),
    9: (20, "Figure 9: Uniform distribution of 10,000 users with 80%, 92%, and 100% coverage."),
    10: (20, "Figure 10: Preferential distribu- tion of 10,000 users with 80% coverage."),
    11: (20, "Figure 11: Preferential distribution of 1000 users with 80%, 92%, and 100% "
             "coverage."),
    12: (21, "Figure 12: Uniform and preferential distributions of both 1, 000 and 10, 000 user "
             "population, looking at the covering and utility cases."),
    13: (22, "Figure 13: Preferential distribution of 10,000 users with 80%, 90%, and 98% "
             "utility ratios."),
    14: (22, "Figure 14: Preferential distribution of 1000 users with 90% and 98% utility "
             "ratios."),
    15: (25, "Figure 15: Here we shows the curvature of the Earth in our model as well as the "
             "curvature perturbed by mountains."),
}

HEADINGS: list[tuple[int, float, str, str, str]] = []


def load_headings() -> None:
    """Attach the printed y of each heading so a region is placed by position.

    The extracted index also carries the pseudo-headings of the program listings
    ("Function preferential attachment", "For each vertex v in G:"), which are filtered out
    here by keeping only numbered headings and the two unnumbered section titles.
    """
    import pymupdf

    doc = pymupdf.open(PDF)
    for h in CTX["headings"]:
        if h["page"] < 5:
            continue
        num, title = h["number"].strip(), h["title"].strip()
        if num and not re.match(r"^\d+(\.\d+)*$", num):
            continue
        if not num and title in ("References", "Background"):
            continue
        y = None
        for block in doc[h["page"] - 1].get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                text = schema.norm(" ".join(s["text"] for s in line["spans"]))
                if num and text.startswith(num):
                    y = line["bbox"][1]
                elif not num and schema.norm(title).lower() in text.lower():
                    y = line["bbox"][1]
        if y is not None:
            HEADINGS.append((h["page"], y, num, title, h["kind"]))
    doc.close()


def place_for(page: int, reg: int) -> dict:
    y0 = REG[(page, reg)][1]
    before = [h for h in HEADINGS if h[0] < page or (h[0] == page and h[1] <= y0)]
    if not before:
        raise SystemExit(f"no heading before p{page} r{reg}")
    _, _, num, title, kind = before[-1]
    path = [f"{h[2]} {h[3]}".strip() for h in before
            if h[2] and (h[2] == num or num.startswith(h[2] + "."))]
    if not num:
        path = [title]
    same = [k for k in ITEMS_ORDER if k[0] == page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": kind,
        "doc_order": 0,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


PROSE = re.compile(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}\s+[A-Za-z]{3,}")
AXIS_TICK = re.compile("−")
TABLE_CELL = re.compile(r"\d+\.\d+")
INLINE_CAPTION = re.compile(r"(Figure|Table)\s+\d+\s*[:.]")
RUNHEAD = re.compile(r"Control\s+#?\s*\d+\s+\d+\s*", re.I)


def lead_sentence(number: int) -> tuple[str, str]:
    pat = re.compile(r"[Ff]igure\s+" + str(number))
    for page in range(1, LAYOUT["page_count"] + 1):
        for unit in schema.page_units(PID, page):
            unit = RUNHEAD.sub("", unit)
            if not pat.search(unit) or INLINE_CAPTION.match(unit):
                continue
            hit = next((s for s in schema.sentences(unit)
                        if pat.search(s) and PROSE.search(s)
                        and AXIS_TICK.search(s) is None
                        and len(TABLE_CELL.findall(s)) < 3
                        and INLINE_CAPTION.search(s) is None
                        and re.match(r"^[A-Z“\"]", s) is not None
                        and s.count("(") < 2), "")
            if not hit:
                continue
            parts = hit.split()
            text = " ".join(parts[:schema.MAX_QUOTE_WORDS])
            while len(schema.words(text)) > schema.MAX_QUOTE_WORDS:
                parts = parts[:-1]
                text = " ".join(parts[:schema.MAX_QUOTE_WORDS])
            low = text.lower()
            if re.search(r"\(figure\s+\d+", low) or "(see figure" in low:
                pattern = "parenthetical"
            elif "as shown" in low:
                pattern = "as-shown-in"
            elif re.match(r"^figure\s+\d+\s+shows", low):
                pattern = "figure-n-shows"
            else:
                pattern = "direct"
            return text, pattern
    return "", "none"


def mention(number: int, page: int) -> dict:
    blank = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
             "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
             "read_sentences": 0, "gap_sentences": None}
    ms = [m for m in MENTIONS if m["number"] == number and m["kind"] == "figure"]
    if not ms:
        return blank
    first = min(m["page"] for m in ms)
    sent, pattern = lead_sentence(number)
    styles = sorted({m["spelling"] for m in ms if m["page"] == page})
    return {"first_page": first, "lead_pages": page - first,
            "style": styles or [f"Figure {number}"], "count": len(ms),
            "lead_sentence": sent, "trail_sentence": "", "lead_pattern": pattern,
            "read_sentences": 1 if sent else 0, "gap_sentences": abs(page - first)}


def caption_block(text: str) -> dict:
    m = re.match(r"^Figure\s+\d+([:.])?", text)
    numbering = "none"
    if m:
        numbering = {":": "Figure N:", ".": "Figure N."}.get(m.group(1) or "", "Figure N")
    vars_ = 1 if re.search(r"[A-Za-z]\s*[=~]", text) or "_" in text else 0
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": bool(re.search(r"\b(m|m/s|degree|degrees|%)\b", text)),
        "variables": vars_ > 0,
        "variable_count": vars_,
        "conditions": bool(re.search(r"\b(under|with|without|fixed|default|varying)\b", text)),
        "concludes": bool(re.search(r"\b(which|so that|therefore)\b", text)),
        "voice": "none",
        "position": "below",
    }


def figure(page: int, reg: int, number: int, family: str, conf: str, *,
           legend: str = "none", three_d: str = "no", labels: bool = False,
           note: str = "", position_below: bool = True) -> dict:
    cap_page, cap = CAPTIONS[number]
    assert cap_page == page, f"Figure {number} caption is on p{cap_page}, not p{page}"
    return {
        "page": page,
        "bbox": REG[(page, reg)],
        "family": family,
        "confidence": conf,
        "panel_count": 1,
        "caption_verbatim": cap,
        "caption_source": "text-layer",
        "note": note,
        "place": place_for(page, reg),
        "mention": mention(number, page),
        "caption": caption_block(cap),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": three_d,
            "printed_numbers": True,
            "data_labels": labels,
        },
    }


def excluded(page: int, reg: int, note: str) -> dict:
    return {"page": page, "bbox": REG[(page, reg)], "reason": "not-an-exhibit", "note": note}


ITEMS_ORDER: list[tuple[int, int]] = [
    (9, 1), (9, 2), (10, 1), (10, 2), (11, 1), (12, 1), (12, 2), (13, 1), (13, 2),
    (19, 2), (19, 3), (19, 4),
    (20, 1), (20, 2), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7),
    (21, 1), (21, 2),
    (22, 1), (22, 2), (22, 3), (22, 4), (22, 5),
    (25, 1), (25, 2),
]

ITEMS: list[dict] = []
EXCLUDED: list[dict] = []
RULES: list[str] = []

SCHEMATIC = "flowchart-or-schematic"
SCATTER = "scatter"


def build() -> str:
    load_headings()

    ITEMS.extend([
        figure(9, 1, 2, SCHEMATIC, "high",
               note="panel of Figure 2: one hatched circle, the repeater coverage of radius 10 "
                    "drawn inside the region of radius 40; pure construction, no axes and no "
                    "labels. Label 'Simple lower bound' prints above the pair"),

        figure(9, 2, 2, SCHEMATIC, "high",
               note="the other panel of Figure 2: sixteen hatched circles of radius 10 set on a "
                    "4x4 square lattice inside the same frame, showing that the area bound of 16 "
                    "repeaters cannot actually cover the disc; no axes, no labels"),

        figure(10, 1, 3, SCHEMATIC, "high",
               note="panel labelled 'Hexagonal lattice packing with circle radii 5 3.': a "
                    "pyramid-shaped stack of about two dozen hatched circles packed without "
                    "overlap, the packing that gives the upper bound of 21; the enclosing radius "
                    "40 circle is drawn as a faint arc through the stack"),

        figure(10, 2, 3, SCHEMATIC, "high",
               note="panel labelled 'Hexagonal lattice covering with circle radii 10.': the same "
                    "lattice with the radii expanded so neighbouring circles overlap into a "
                    "covering of the disc; caption for the pair prints below both panels"),

        figure(11, 1, 4, SCHEMATIC, "high",
               note="tropospheric interference: a long shallow arc with hatched wedges at each "
                    "end, a dashed ray running above the arc and a solid ray following it, plus an "
                    "arrow head to show the extended range; no axes, no labels, no legend"),

        figure(12, 1, 5, SCHEMATIC, "high",
               note="reflection: a wide horizontal beam profile with hatched end blocks, two "
                    "diagonal rays crossing down to the ground and back up, and an arrow along the "
                    "top edge for the direct wave; unlabelled line art"),

        figure(12, 2, 6, SCHEMATIC, "high",
               note="diffraction: a hill-shaped solid between two hatched pillars with a solid "
                    "arrow sweeping over the crest and a dashed arrow carrying on to the far "
                    "pillar, showing an indirect path over an obstruction; unlabelled line art"),

        figure(13, 1, 7, SCATTER, "high",
               note="panel of Figure 7: 1000 users drawn as small black dots on a unitless "
                    "-40..40 square, bounded by a light grey circle of radius 40 and a dotted grid; "
                    "the points fill the disc fairly evenly. No axis titles, no legend"),

        figure(13, 2, 7, SCATTER, "high",
               note="the preferential-attachment panel of Figure 7: the same frame and grid, but "
                    "the points gather into a dense core with satellite clumps, which is what makes "
                    "the two distributions distinguishable at a glance"),

        figure(19, 2, 8, SCATTER, "high",
               note="Figure 8, the 80% coverage panel: the uniform 1000-user cloud with filled "
                    "coverage discs laid over it, each disc coloured by the frequency it is assigned "
                    "and each holding its own cluster of users; about a dozen discs, spilling past "
                    "the boundary circle. No legend is printed on any of the three panels"),

        figure(19, 3, 8, SCATTER, "high",
               note="the 92% coverage panel: more discs than the 80% panel, five or six distinct "
                    "fills (red, blue, teal, yellow-green, magenta), heavier overlap, with the user "
                    "cloud showing between them"),

        figure(19, 4, 8, SCATTER, "high",
               note="the 100% coverage panel: about twenty discs, the densest of the three, so that "
                    "almost no user is left outside a disc; the discs run past the boundary circle "
                    "on every side"),

        figure(20, 1, 9, SCATTER, "high",
               note="Figure 9 first panel (80% coverage) for 10,000 uniform users: the point cloud "
                    "is an order of magnitude denser than Figure 8's, with twelve visible discs, "
                    "three red, four sky blue, four yellow-green and one purple"),

        figure(20, 2, 9, SCATTER, "high",
               note="Figure 9 second panel (92% coverage): about fourteen discs in red, green, sky "
                    "blue, yellow, magenta and navy, each centred on a dark knot of points"),

        figure(20, 3, 9, SCATTER, "high",
               note="Figure 9 third panel (100% coverage): the densest stipple in the paper, with "
                    "about twenty dark saturated discs under the point cloud; the discs are cut by "
                    "the frame on three sides"),

        figure(20, 4, 11, SCATTER, "high",
               note="Figure 11 first panel, preferential 1000 users at 80%: a sparse cloud of "
                    "tight knots with only six discs, three red, two green and one navy, and large "
                    "uncovered areas of the disc"),

        figure(20, 5, 11, SCATTER, "high",
               note="Figure 11 second panel (92%): ten discs, four red, three sky blue, two "
                    "yellow-green and one purple, several of them semi-transparent so the knots "
                    "show through"),

        figure(20, 6, 11, SCATTER, "high",
               note="Figure 11 third panel (100%): fifteen to seventeen discs over the clustered "
                    "points, red, yellow, magenta, green, navy and light blue, overflowing the "
                    "boundary circle at three sides"),

        figure(20, 7, 10, SCATTER, "high",
               note="Figure 10, the single 80%-coverage panel for 10,000 preferential users: nine "
                    "discs, three red, three green and three navy, each holding one of the dense "
                    "knots. This is the only figure on the page with one panel instead of three"),

        figure(21, 1, 12, "line", "high", legend="inside",
               note="panel (a) of Figure 12, the covering case: four series against 80-98% coverage "
                    "(1,000 uniform, 10,000 uniform, 1,000 preferential, 10,000 preferential), each "
                    "a line with vertical error bars at every sample, no markers; the boxed legend "
                    "sits inside the upper left and the printed title reads Repeater Effectiveness. "
                    "The x label is clipped at the region's bottom edge"),

        figure(21, 2, 12, "line", "high", legend="inside",
               note="panel (b) of Figure 12, the utility case: the same four series and the same "
                    "boxed legend, plotted against utility ratio 80-98%, with the curves rising "
                    "more steeply and the two preferential series crossing the uniform ones; title "
                    "and axis label are clipped at the region edges"),

        figure(22, 1, 13, SCATTER, "high",
               note="Figure 13 first panel, preferential 10,000 users at an 80% utility ratio: ten "
                    "visible discs, three red, three green, three sky blue and one purple, over a "
                    "dense black stipple"),

        figure(22, 2, 13, SCATTER, "high",
               note="Figure 13 second panel (90% utility): fifteen to seventeen discs, slate blue, "
                    "cyan, yellow, magenta, red, green and navy, with the heaviest stipple of the "
                    "three panels darkening the disc interiors"),

        figure(22, 3, 13, SCATTER, "high",
               note="Figure 13 third panel (98% utility): about twenty increasingly overlapping "
                    "discs spanning a wide colour range, so that the assignments overlap far more "
                    "than in the 80% panel"),

        figure(22, 4, 14, SCATTER, "high",
               note="Figure 14 first panel, preferential 1000 users at 90% utility: nine large "
                    "discs, red, light blue, green and purple, over a sparse point cloud"),

        figure(22, 5, 14, SCATTER, "high",
               note="Figure 14 second panel (98% utility): seventeen or eighteen mostly cyan, "
                    "navy, magenta and red discs, with the users sitting in tight local knots so "
                    "that most of the disc is empty"),

        figure(25, 1, 15, "surface-or-3D", "high", three_d="surface-mesh", legend="none",
               note="panel (a) of Figure 15: a wireframe surface mesh with a jet colour ramp over "
                    "two Miles axes, height axis 'Distance from Center of Earth (mi)' from 3958 to "
                    "3959.5, showing the smooth curvature of the Earth; no colour bar"),

        figure(25, 2, 15, "surface-or-3D", "high", three_d="surface-mesh", legend="none",
               note="panel (b) of Figure 15: the same mesh with terrain relief added, so the "
                    "surface is ragged at the border and carries ridges and pits; same axes and the "
                    "same jet ramp, still without a colour bar"),
    ])

    EXCLUDED.extend([
        excluded(14, 1, "'Program 1 Preferential Attachment Algorithm' listing: a ruled title bar "
                        "over a block of parameter definitions for the pseudo-code, not a figure or "
                        "a table"),
        excluded(17, 1, "'Program 2 Utility-Based Greedy Cover' listing, the same shape: title bar "
                        "and parameter definitions only"),
        excluded(19, 1, "'Program 3 Frequency Allocation Algorithm' listing, the same shape again, "
                        "printed above the Figure 8 panels on the same page"),
    ])

    RULES.extend([
        "a coverage picture on unitless -40..40 axes is scatter, while a plan view whose axes are "
        "titled in Miles is map-or-plan-view: the axis titles, not the marker type, decide between "
        "the two families [geometry.family]",

        "an outline construction (circles, hatched wedges, ray diagrams) is flowchart-or-schematic "
        "even when it carries no text at all, because it draws a mechanism rather than data "
        "[geometry.family] [geometry.data_labels]",

        "a caption printed inside a body line, or split over indented lines with a hyphen break, "
        "is quoted as printed and never reflowed: Figure 2's caption sits at the end of a prose "
        "line, Figure 10's breaks 'distribu- tion' across three lines [caption.verbatim] "
        "[caption.words]",

        "each panel of a multi-panel figure is measured as its own region and recorded as its own "
        "item sharing the figure's caption, so Figure 9 yields three items on p20 and Figure 13 "
        "three more on p22 [geometry.panel_count] [caption.verbatim]",

        "program listings in a ruled title bar are excluded as not-an-exhibit in the same class as "
        "algorithm listings, even where the listing is printed on a page that also carries figure "
        "panels [geometry.family]",
    ])

    return (
        "Fifteen numbered figures, no tables, across 28 pages. 31 measured regions resolve to 28 "
        "figure items and 3 excluded program listings with no leftovers; Figure 1 on p6 (a text "
        "table of UK repeater channels with only three thin rules and no image block) is "
        "unresolved because nothing passed the extractor's size filter. Seven items are "
        "schematics, seventeen are scatter pictures of users with coverage discs, two are line "
        "charts with error bars and two are 3D surface meshes."
    )


def main() -> int:
    note = build()
    order = 0
    merged = sorted(ITEMS + EXCLUDED, key=lambda it: (it["page"], it["bbox"][1]))
    for it in merged:
        order += 1
        if "place" in it:
            it["place"]["doc_order"] = order

    payload = {
        "paper": PID,
        "page_count": LAYOUT["page_count"],
        "layout_sha256": LAYOUT["layout_sha256"],
        "measured_regions": sum(len(pg["regions"]) for pg in LAYOUT["pages"]),
        "items": ITEMS,
        "tables": [],
        "excluded_regions": EXCLUDED,
        "rules": RULES,
        "note": note,
    }
    out = PROXY / "pb20-payload.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"items={len(ITEMS)} tables=0 excluded={len(EXCLUDED)} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
