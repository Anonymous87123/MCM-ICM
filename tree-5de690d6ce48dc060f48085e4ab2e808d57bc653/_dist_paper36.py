"""Hand pass for P-B-2012-15417-df1dd905 (Big Long River scheduling, Java listing, 26 pp).

The geometry pass measures 12 regions over 10 pages, and eight of those regions are
typeset Java listings, not exhibits:

    p5-r1   generateSchedule() body, headed "Algorithm generateSchedule()."
    p7-r1   the tail of the same listing (lines 143-155) above the prose
    p9-r1   addBoats(int day) body
    p10-r1  reschedule(Boat boat) body
    p17-r1  the whole of Boat.java, the appendix listing
    p19-r1  the tail of Boat.java, cut by the footer
    p19-r2  the opening lines of River.java
    p26-r1  the tail of the driver listing, indented one space

All eight are excluded `not-an-exhibit`, the class paper 8 set for program listings: they
are ruled code blocks with no drawing on them.

The four remaining regions are the paper's four printed figures, one region each:

    Figure 1  p8-r1   table-shaped image, case 4: boat D finds no site
    Figure 2  p8-r2   the resolution: boat A is forced back
    Figure 3  p11-r1  "Graph of Magic Numbers"
    Figure 4  p13-r1  trips per year against the motor:oar ratio

Accounting: 4 figure items + 8 exclusions = 12 regions, unaccounted 0.

Figures 1 and 2 are two side-by-side raster images printed on the same baseline, each a
three-column grid (Site / Day k / Day k + 1) whose cells hold shaded raft glyphs and
printed cell text "Priority: n" and "Next desired site: n". They are one exhibit each,
because each image carries its own printed number: the two caption paragraphs run under
the pair, "Figure 1: …" under the left image and the wrapped "Figure 2: Resolution …"
under the right one. Drawn state grids with icons and no axes, so family
`flowchart-or-schematic`, the same call the lane made for paper 34's occupancy strips.

Family for the two plotted figures, read off page-band proxies:

* `scatter` is Figure 3: blue diamond markers only, grey gridlines, axis titles "Number of
  rescheduled trips" and "Number of Site (Y)", x ticks 28-56 and y ticks 0-45, no legend.
* `line` is Figure 4: blue diamond markers with a smooth fitted quadratic drawn through
  them, carrying the printed equation y = -26.173x^2 + 66.222x + 617.96 and R^2 = 0.9968
  inside the frame; axis titles "Number of Trips per Year" and "Ratio of Motor boats to
  Oar boats". A drawn curve is present, so the family is line and the markers are noted.

The heading index is useless here - it is full of code lines such as "87 Boat temp =
nextBoat;" - so the section paths are built from the paper's own unnumbered headings,
read off the text layer: "Representation of a Schedule", "Magic Numbers" and
"Error/Sensitivity Analysis".

Usage: python -I tools/_dist_paper36.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-B-2012-15417-df1dd905"
PROXY = LANE / ".proxy"
LAYOUT = json.loads((LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))
CTX = json.loads((PROXY / f"{PID}-ctx.json").read_text(encoding="utf-8"))

REG: dict[tuple[int, int], list[float]] = {}
KIND: dict[tuple[int, int], str] = {}
for pg in LAYOUT["pages"]:
    for i, r in enumerate(sorted(pg["regions"], key=lambda x: (x["bbox"][1], x["bbox"][0])), 1):
        REG[(pg["page"], i)] = r["bbox"]
        KIND[(pg["page"], i)] = r.get("kind", "vector")

CTXREG = {(r["page"], r["region"]): r for r in CTX["regions"]}

SCHED = "未编号标题 Representation of a Schedule"
MAGIC = "未编号标题 Magic Numbers"
SENS = "未编号标题 Error/Sensitivity Analysis"
KIND_OF = {SCHED: "other", MAGIC: "other", SENS: "sensitivity"}

PATH = {8: [SCHED], 11: [MAGIC], 13: [SENS]}

NULL_MENTION = {"first_page": None, "lead_pages": None, "style": [], "count": 0,
                "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
                "read_sentences": 0, "gap_sentences": None}

# accounted regions per page, counted first so doc_order stays monotonic
VENTION = {5: 1, 7: 1, 8: 2, 9: 1, 10: 1, 11: 1, 13: 1, 17: 1, 19: 2, 26: 1}

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []
PAGE_SEEN: dict[int, int] = {}


def ctext(page: int, start: str, stop: str | None = None) -> str:
    """The printed caption as the text layer carries it, cut at `start`..`stop`."""
    text = schema.page_text(PID, page)
    i = text.find(start)
    if i < 0:
        raise KeyError((page, start))
    cut = text[i:]
    if stop:
        j = cut.find(stop)
        if j < 0:
            raise KeyError((page, stop))
        cut = cut[:j]
    return cut.strip()


def place(page: int, reg: int) -> dict:
    PAGE_SEEN[page] = PAGE_SEEN.get(page, 0) + 1
    route = PATH[page]
    c = CTXREG[(page, reg)]
    return {
        "section_path": list(route),
        "section_numbered": False,
        "section_kind": KIND_OF[route[-1]],
        "doc_order": PAGE_SEEN[page] + sum(VENTION[p] for p in VENTION if p < page),
        "page_order": PAGE_SEEN[page],
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def caption_block(text: str) -> dict:
    return {
        "verbatim": text,
        "numbering": "Figure N:",
        "words": len(schema.words(text)),
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": "below",
    }


def figure(page: int, reg: int, family: str, caption: str, *, legend: str = "none",
           numbers: bool = True, labels: bool = False, mention: dict | None = None,
           note: str = "") -> None:
    ORDER.append((page, reg))
    blocking = dict(mention) if mention else dict(NULL_MENTION)
    if blocking["first_page"] is not None and blocking["lead_pages"] is None:
        blocking["lead_pages"] = page - blocking["first_page"]
    ITEMS[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": caption,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg),
        "mention": blocking,
        "caption": caption_block(caption),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": numbers,
            "data_labels": labels,
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def mention(first_page: int, style: list[str], lead: str, pattern: str,
            count: int = 1) -> dict:
    return {"first_page": first_page, "lead_pages": None, "style": style,
            "count": count, "lead_sentence": lead, "trail_sentence": "",
            "lead_pattern": pattern, "read_sentences": count, "gap_sentences": None}


STATEGRID = ("A raster image of a three-column grid headed 'Site', 'Day k' and 'Day k + 1' "
             "over the six site rows; each filled cell holds a shaded raft glyph and two "
             "printed lines, 'Priority: n' and 'Next desired site: n'. No axes, no scale, "
             "no legend: the grid is the drawing.")


def build() -> str:
    figure(8, 1, "flowchart-or-schematic",
           ctext(8, "Figure 1:", "Figure 2:"),
           numbers=False, labels=True,
           note="Case 4 drawn out: boat D sits in site 4 on day k with priority 4 and next "
                "desired site 6, site 6 is already held by boat A on day k + 1, and the "
                "stray glyph to the right of the grid is D locked out of the row. " +
                STATEGRID)
    figure(8, 2, "flowchart-or-schematic",
           ctext(8, "Figure 2:", "Once all boats have found"),
           numbers=False, labels=True,
           note="The resolution of case 4 on the same grid: boat A (priority 1) is forced "
                "back from site 6 to site 3 on day k + 1 while D takes site 4, so a "
                "higher-priority boat yields to keep the schedule legal. " + STATEGRID)
    figure(11, 1, "scatter",
           ctext(11, "Figure 3:", "At first it looked like jumbled data"),
           note="Rescheduling against campsite count: blue diamond markers only, no line, "
                "over light grey gridlines; two isolated points sit far above the rest near "
                "Y = 34-35 (30 and 39 rescheduled trips) and the remainder breaks into two "
                "low runs split at about Y = 42, which is the period-7 pattern the section "
                "names. Axis titles 'Number of rescheduled trips' 0-45 and 'Number of Site "
                "(Y)' 28-56. No legend.")
    figure(13, 1, "line",
           ctext(13, "Figure 4:", "Rowing more than 12 hours is not realistic"),
           labels=True,
           mention=mention(13, ["Figure 4"],
                           "As can be seen in Figure 4, the efficiency does increase.",
                           "parenthetical"),
           note="Trips per year against the motor:oar ratio: blue diamond markers with a "
                "smooth fitted quadratic drawn through them and the fit printed inside the "
                "frame, 'y = -26.173x^2+66.222x+617.96', 'R^2 = 0.9968'. Axis titles "
                "'Number of Trips per Year' 610-665 and 'Ratio of Motor boats to Oar boats' "
                "0-1.2, gridlines on both directions, no legend. The caption line runs into "
                "the paper's own prose and is quoted up to the sentence break.")

    excluded(5, 1, "not-an-exhibit",
             "typeset Java listing under a printed 'Algorithm generateSchedule().' title "
             "bar, 127 vector paths of code text and no drawing.")
    excluded(7, 1, "not-an-exhibit",
             "the tail of the same listing, lines 143-155 with their comments, above the "
             "prose that explains addBoats().")
    excluded(9, 1, "not-an-exhibit",
             "typeset Java listing of addBoats(int day), 112 vector paths of code text.")
    excluded(10, 1, "not-an-exhibit",
             "typeset Java listing of reschedule(Boat boat), 48 vector paths of code, "
             "quoted in the prose as the 'LinkedList implementation of reschedule()'.")
    excluded(17, 1, "not-an-exhibit",
             "the appendix listing Boat.java, a full page of code text under the printed "
             "line 'Appendix: Source Code'.")
    excluded(19, 1, "not-an-exhibit",
             "the tail of the appendix Boat.java listing, cut by the page footer, with the "
             "'River.java' title line of the next listing printed under it.")
    excluded(19, 2, "not-an-exhibit",
             "the opening lines of the appendix River.java listing (imports and class "
             "comment), 47 vector paths of code text.")
    excluded(26, 1, "not-an-exhibit",
             "the tail of the driver listing that closes the appendix, indented one space "
             "and without its own title bar.")

    rules = [
        "Eight of the twelve measured regions are typeset Java listings - p5, p7, p9, p10, "
        "p17, p19 twice and p26 - so they are excluded not-an-exhibit and the paper has four "
        "figure items [place.area_frac].",
        "Figures 1 and 2 are two side-by-side raster images on one baseline, each with its "
        "own printed number and its own caption paragraph under it [caption.verbatim].",
        "Figures 1 and 2 are drawn state grids with raft glyphs and printed cell text, no "
        "axes and no tick numbers, so they are flowchart-or-schematic with printed_numbers "
        "false and data_labels true [geometry.printed_numbers] [geometry.data_labels].",
        "Figure 3 is a marker-only plot with grey gridlines and no legend, so it is scatter "
        "[geometry.family].",
        "Figure 4 has a smooth fitted quadratic drawn through its markers and prints the fit "
        "and its R^2 inside the frame, so it is line and data_labels is true "
        "[geometry.family] [geometry.data_labels].",
        "Only Figure 4 is cited in running text ('As can be seen in Figure 4'), on the page "
        "that prints it; Figures 1-3 are read only through their captions "
        "[mention.lead_sentence].",
        "The heading index is made of code lines ('87 Boat temp = nextBoat;' and the like), "
        "so every section_path here is an unnumbered heading copied from the text layer and "
        "section_numbered is false [place.section_path].",
        "Figure 4's printed caption runs on into the paper's prose, so the quote stops at "
        "the sentence break before 'Rowing more than 12 hours is not realistic' "
        "[caption.words].",
    ]

    payload = {
        "paper": PID,
        "source": "F:/MCM/MCM-ICM-master/2012\u7f8e\u8d5b\u7279\u7b49\u5956/"
                  "B-15417-Outstanding.pdf",
        "pages": len(LAYOUT["pages"]),
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER],
        "tables": [],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": (
            "Twelve measured regions, twelve accounted: four figure items and eight "
            "exclusions. The paper prints exactly four numbered figures and all four are "
            "measured. The eight exclusions are typeset Java listings, one of them a whole "
            "appendix page (Boat.java) and one the tail of the next (River.java), which the "
            "layout pass measures as vector regions because their code text draws paths; "
            "paper 8 settled that a program listing is no exhibit. Declared gap: eight "
            "further pages carry code paths the layout pass leaves unmeasured (p6, p18, "
            "p20, p21, p22, p23, p24, p25), and those listing bodies are not counted "
            "anywhere; the appendix of source code runs from p17 to the end of the "
            "document."
        ),
    }
    out = PROXY / "pb36-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return (f"{out} items={len(payload['items'])} tables={len(payload['tables'])} "
            f"excluded={len(payload['excluded_regions'])}")


def main() -> int:
    print(build())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
