"""Hand pass for P-C-2011-8882-54492a1f (EV/HEV in France, USA and China, 27 pages).

Fifty-four measured regions: forty-one rasters and thirteen vector blocks. The rasters
are the paper's whole illustration: one export per panel, with a printed label line of the
form "Figure 2 Figure 3 Figure 4" under each row of three, so a multi-panel figure has no
per-panel caption of its own and each panel is recorded as its own item carrying its own
label. That keeps the lane's convention that items are measured layout blocks.

Families and table shapes below were read off the cropped page proxies, one crop per
reading, never from the text layer alone.

Usage: python -I tools/_dist_paper26.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2011-8882-54492a1f"
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
MENTIONS = CTX["mentions"]

INTRO = "1 Introduction"
SIM = "4 Simulation of Quantities of CV, EV and HEV"
INC = "4.1 Increase of Number of Total Vehicles"
GROWTH = "4.2 Growth of Quantities of CV, EV and HEV"
ENERGY = "5 Energy Demand and Supply from/for EV and HEV"
OFFPEAK = "5.2 Off-Peak Charging Supply for EV and HEV"
EXTRA = "5.3 Extra Energy Supply for EV/HEV and Its Optimization"
ENVIRON = "6 Environmental, Economic, Social and Health"
FOSSIL = "6.1 EV/HEV Consumes Less Fossil Fuels"
COST = "6.2 Driving EV and HEV Costs Less"
JOBS = "6.3 New Vehicle Industry Provides More Job Opportunities"
INVEST = "6.4 Invest in New Vehicle Industry is Rewarding"
POLLUTE = "6.5 EV/HEV Reduce Pollutions and Do Good for Health"
CONCL = "7 Conclusion"

KIND_OF = {INTRO: "introduction", SIM: "solution", INC: "solution",
           GROWTH: "solution", ENERGY: "solution", OFFPEAK: "solution",
           EXTRA: "solution", ENVIRON: "result", FOSSIL: "result", COST: "result",
           JOBS: "result", INVEST: "result", POLLUTE: "result", CONCL: "evaluation"}


def path_for(page: int, reg: int) -> list[str]:
    """Section path by the heading the region actually sits under, not the last heading
    the ctx dump saw on the page. p25 is the case: its three Fig. 22 panels are printed
    above the '7 Conclusion' heading and the two world figures below it."""
    if page == 2:
        return [INTRO]
    if page in (4, 5):
        return [SIM, INC]
    if page == 6:
        return [SIM, GROWTH]
    if page == 8:
        return [ENERGY]
    if page in (9, 10, 11):
        return [ENERGY, OFFPEAK]
    if page in (13, 14):
        return [ENERGY, EXTRA]
    # Pages 16-19 all sit under 6.1: the '6.2' heading is printed below the p19 mini
    # table and Fig. 18, not above them, so those two blocks belong to 6.1.
    if page in (16, 17, 18, 19):
        return [ENVIRON, FOSSIL]
    # Page 20 carries the end of 6.2 above its own '6.3' heading, page 24 carries Fig. 21
    # above its '6.5' heading, and page 25 carries the Fig. 22 panels above '7 Conclusion'.
    if page == 20:
        return [ENVIRON, COST]
    if page == 21:
        return [ENVIRON, JOBS]
    if page in (23, 24):
        return [ENVIRON, INVEST]
    if page == 25:
        return [ENVIRON, POLLUTE] if reg <= 3 else [CONCL]
    return [CONCL]

ORDER: list[tuple[int, int]] = []
ITEMS: dict[tuple[int, int], dict] = {}
TABLES: dict[tuple[int, int], dict] = {}
EXCLUDED: list[dict] = []


def place(page: int, reg: int, order: int) -> dict:
    path = path_for(page, reg)
    c = CTXREG[(page, reg)]
    same = [k for k in ORDER if k[0] == page]
    return {
        "section_path": path,
        "section_numbered": True,
        "section_kind": KIND_OF[path[-1]],
        "doc_order": order,
        "page_order": same.index((page, reg)) + 1,
        "page_zone": c["page_zone"],
        "area_frac": c["area_frac"],
        "solo_page": c["solo_page"],
    }


def null_mention() -> dict:
    return {"first_page": None, "lead_pages": None, "style": [], "count": 0,
            "lead_sentence": "", "trail_sentence": "", "lead_pattern": "none",
            "read_sentences": 0, "gap_sentences": None}


def snippet(page: int, token: str, *, before: int = 6, after: int = 12) -> str:
    text = schema.norm(schema.page_text(PID, page))
    at = text.index(schema.norm(token))
    cut = text.rfind(". ", 0, at)
    start = cut + 2 if cut != -1 else 0
    tail = text.find(". ", at)
    end = tail + 1 if tail != -1 else len(text)
    window = text[start:end].split()
    where = schema.norm(text[start:at]).split()
    lo = max(0, len(where) - before)
    hi = min(len(window), len(where) + len(schema.norm(token).split()) + after)
    return " ".join(window[lo:hi])


def pattern_of(sentence: str) -> str:
    low = sentence.lower()
    if "refer to" in low:
        return "direct"
    if "shown" in low or "shown in" in low:
        return "as-shown-in"
    if re.search(r"\b(shows|depicts|pictures|illustrates)\b", low):
        return "figure-n-shows"
    return "direct"


def figure_mention(page: int, number: int) -> dict:
    hits = [m for m in MENTIONS if m["kind"].startswith("fig") and m["number"] == number]
    if not hits:
        return null_mention()
    first = hits[0]["page"]
    return {
        "first_page": first,
        "lead_pages": page - first,
        "style": sorted({m["spelling"] for m in hits}),
        "count": len(hits),
        "lead_sentence": snippet(first, f"Figure {number}"),
        "trail_sentence": "",
        "lead_pattern": pattern_of(hits[0]["sentence"]),
        "read_sentences": len(hits),
        "gap_sentences": None,
    }


def table_mention() -> dict:
    """Only Tables 1-12 exist and each is named once in the sentence just above it; the
    label itself is the caption, so no reference is resolved here."""
    return null_mention()


def caption_block(text: str, numbering: str) -> dict:
    return {
        "verbatim": text,
        "numbering": numbering,
        "words": len(schema.words(text)) if text else 0,
        "sentences": len(schema.sentences(text)) if text else 0,
        "units": False,
        "variables": False,
        "variable_count": 0,
        "conditions": False,
        "concludes": False,
        "voice": "none",
        "position": "below",
    }


def figure(page: int, reg: int, number: int, family: str, text: str, *,
           numbering: str = "Figure N.", legend: str = "none", printed: bool = True,
           labels: bool = False, other_note: str = "", note: str = "") -> None:
    ORDER.append((page, reg))
    item = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "family": family,
        "confidence": "high",
        "panel_count": 1,
        "caption_verbatim": text,
        "caption_source": "text-layer",
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": figure_mention(page, number),
        "caption": caption_block(text, numbering),
        "geometry": {
            "family": family,
            "panel_count": 1,
            "panel_layout": "1",
            "shared_axes": False,
            "legend": legend,
            "colorbar": False,
            "three_d": "no",
            "printed_numbers": printed,
            "data_labels": labels,
        },
    }
    if other_note:
        item["other_note"] = other_note
    ITEMS[(page, reg)] = item


def table(page: int, reg: int, rows: int, cols: int, *, header: int = 1,
          numeric: int = 0, text_cols: int = 0, units: bool = False,
          label: str = "", note: str = "") -> None:
    ORDER.append((page, reg))
    source = "text-layer" if label else "none"
    numbering = "Table N." if label else "none"
    TABLES[(page, reg)] = {
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": label,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, len(ORDER)),
        "mention": table_mention(),
        "caption": caption_block(label, numbering),
        "table": {
            "rows": rows,
            "cols": cols,
            "header_rows": header,
            "rule_style": "vertical-rules",
            "zebra": False,
            "merged_cells": False,
            "diagonal_header": False,
            "units_in_header": units,
            "decimal_aligned": False,
            "numeric_cols": numeric,
            "text_cols": text_cols,
            "width": "full",
            "orientation": "portrait",
            "continued": False,
            "note_sentence": "",
        },
    }


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({"page": page, "bbox": REG[(page, reg)], "reason": reason,
                     "note": note})


def build() -> str:
    # Every family and every legend below was read off that region's own crop, one
    # crop per reading. Panel order inside a printed figure runs left to right in the
    # page's three-column layout, which is why the region numbers are not sequential.
    ROWS = [
        (2, 1, 1, "flowchart-or-schematic", "Figure 1. Formation of our paper",
         {"numbering": "Figure N.", "printed": False,
          "note": "Three labelled aspect bands feed three model boxes; line art, no axes."}),
        # p6: left France = Fig. 2, middle USA = Fig. 3, right China = Fig. 4.
        (6, 2, 2, "line", "Figure 2", {"numbering": "Figure N"}),
        (6, 3, 3, "line", "Figure 3", {"numbering": "Figure N"}),
        (6, 1, 4, "line", "Figure 4", {"numbering": "Figure N"}),
        # p8: left France = Fig. 5, middle USA = Fig. 6, right China = Fig. 7.
        (8, 2, 5, "line", "Figure 5", {"numbering": "Figure N", "legend": "inside"}),
        (8, 3, 6, "line", "Figure 6", {"numbering": "Figure N", "legend": "inside"}),
        (8, 1, 7, "line", "Figure 7", {"numbering": "Figure N", "legend": "inside"}),
        # Fig. 8 is printed at the foot of p9 but its caption sits at the head of p10.
        (9, 1, 8, "line", "Figure 8. Electricity Supply in 24-hour-circle",
         {"legend": "inside",
          "note": "Vector clock-face demand curve with peak and off-peak bands."}),
        (9, 2, 8, "photo-or-raster-image", "Figure 8. Electricity Supply in 24-hour-circle",
         {"printed": False,
          "note": "Screenshot of a demand-versus-time chart from mpoweruk.com, dropped in "
                  "beside the drawn curve as part of the same printed figure."}),
        # p10: left France = Fig. 9, middle USA = Fig. 10, right China = Fig. 11.
        (10, 2, 9, "line", "Figure 9", {"numbering": "Figure N"}),
        (10, 4, 10, "line", "Figure 10", {"numbering": "Figure N"}),
        (10, 3, 11, "line", "Figure 11", {"numbering": "Figure N"}),
        # p13: left France, middle USA, right China, all panels of Fig. 12.
        (13, 3, 12, "line",
         "Figure 12. Amount and type of electricity generation to meet energy demand "
         "from EV/HEV in France, USA and China", {"legend": "inside"}),
        (13, 4, 12, "line",
         "Figure 12. Amount and type of electricity generation to meet energy demand "
         "from EV/HEV in France, USA and China", {"legend": "inside"}),
        (13, 2, 12, "line",
         "Figure 12. Amount and type of electricity generation to meet energy demand "
         "from EV/HEV in France, USA and China", {"legend": "inside"}),
        # p14: Fig. 13, three bar panels, caption clipped at 'in France, USA and'.
        (14, 1, 13, "bar",
         "Figure 13. New power stations needed to be constructed in a five-year circle "
         "in France, USA and", {"note": "France panel, eleven five-year columns."}),
        (14, 2, 13, "bar",
         "Figure 13. New power stations needed to be constructed in a five-year circle "
         "in France, USA and", {"note": "USA panel, eleven five-year columns."}),
        (14, 3, 13, "bar",
         "Figure 13. New power stations needed to be constructed in a five-year circle "
         "in France, USA and", {"note": "China panel, eleven five-year columns."}),
        # p17: left France = Fig. 14, middle USA = Fig. 15, right China = Fig. 16.
        (17, 2, 14, "line", "Figure 14. CO2 emission in France", {}),
        (17, 1, 15, "line", "Figure 15. CO2 emission in USA", {}),
        (17, 3, 16, "line", "Figure 16. CO2 emission in China", {}),
        # p18: left France, middle USA, right China, panels of Fig. 17.
        (18, 2, 17, "line", "Figure 17. Oil saved by EV/HEV in France, USA and China",
         {"legend": "inside"}),
        (18, 3, 17, "line", "Figure 17. Oil saved by EV/HEV in France, USA and China",
         {"legend": "inside"}),
        (18, 1, 17, "line", "Figure 17. Oil saved by EV/HEV in France, USA and China",
         {"legend": "inside"}),
        (19, 2, 18, "line", "Figure 18. Oil saved in the world", {"legend": "inside"}),
        # p21: left USA, middle China, right France, panels of Fig. 19.
        (21, 4, 19, "line",
         "Figure 19. New job positions provided by new industries in France, USA and "
         "China.", {}),
        (21, 2, 19, "line",
         "Figure 19. New job positions provided by new industries in France, USA and "
         "China.", {}),
        (21, 3, 19, "line",
         "Figure 19. New job positions provided by new industries in France, USA and "
         "China.", {}),
        # p23: left France, middle USA, right China, panels of Fig. 20.
        (23, 4, 20, "line", "Figure 20. Investment for EV/HEV in France, USA and China",
         {}),
        (23, 2, 20, "line", "Figure 20. Investment for EV/HEV in France, USA and China",
         {}),
        (23, 3, 20, "line", "Figure 20. Investment for EV/HEV in France, USA and China",
         {}),
        # p24: left France, middle USA, right China, panels of Fig. 21.
        (24, 3, 21, "line",
         "Figure 21. Monetary output of new industries in France, USA and China", {}),
        (24, 1, 21, "line",
         "Figure 21. Monetary output of new industries in France, USA and China", {}),
        (24, 2, 21, "line",
         "Figure 21. Monetary output of new industries in France, USA and China", {}),
        # p25: Fig. 22 above '7 Conclusion', then the two world figures below it.
        (25, 1, 22, "line", "Figure 22. Nitrogen Generation in France, USA and China", {}),
        (25, 3, 22, "line", "Figure 22. Nitrogen Generation in France, USA and China", {}),
        (25, 2, 22, "line", "Figure 22. Nitrogen Generation in France, USA and China", {}),
        (25, 4, 23, "line", "Figure 23 World’s CO2 emission",
         {"numbering": "Figure N", "legend": "inside"}),
        (25, 5, 24, "line", "Figure 24 World’s new job positions",
         {"numbering": "Figure N", "legend": "inside"}),
        (26, 1, 25, "line", "Figure 25 World’s monetary reward",
         {"numbering": "Figure N", "legend": "inside"}),
        (26, 2, 26, "line", "Figure 26 World’s nitrogen production",
         {"numbering": "Figure N", "legend": "inside"}),
    ]
    for page, reg, number, family, text, kw in ROWS:
        figure(page, reg, number, family, text, **kw)

    TAB = [
        (4, 1, 4, 3, "Table 1. Features of CV, EV and HEV",
         {"numeric": 1, "text_cols": 2}),
        (5, 1, 4, 7,
         "Table 2. Quantities of total vehicle in France, USA and China from 2005 to 2010",
         {"numeric": 6, "text_cols": 1, "units": True}),
        # The page prints the label as 'Tabel 3.'; the typo is kept in the quote.
        (5, 2, 3, 4, "Tabel 3. Values of coefficients in logistic mode acquired by fitting",
         {"numeric": 3, "text_cols": 1,
          "note": "Printed label misspells 'Table' as 'Tabel'."}),
        (10, 1, 2, 4, "Table 4. Annual Electricity Generation in France, USA and China",
         {"numeric": 3, "text_cols": 1}),
        (11, 1, 2, 4, "Table 5. Electricity needed to be generated for EV/HEV",
         {"numeric": 3, "text_cols": 1}),
        (11, 2, 3, 4, "Table 6. Number of EV/HEV supported by off-peak charging",
         {"numeric": 3, "text_cols": 1}),
        (13, 1, 4, 11, "Table 7. Values of coefficients in (8) and (9)",
         {"numeric": 10, "text_cols": 1, "units": True}),
        (16, 1, 4, 4, "Table 8. Information related with CO2 intensity",
         {"numeric": 3, "text_cols": 1}),
        (16, 2, 4, 4, "Table 9. CO2 consumption of CV, EV and HEV in France, USA and China",
         {"numeric": 3, "text_cols": 1}),
        # Unlabelled parameter block in the body of p19; counted as a table, no caption.
        (19, 1, 2, 3, "", {"numeric": 3,
                           "note": "Unlabelled r1 r2 r3 parameter block; the printed label "
                                   "is absent, so the caption source is none."}),
        (20, 1, 4, 4, "Table 10. Cost and Saving of driving CV, EV and HEV",
         {"numeric": 3, "text_cols": 1}),
        (21, 1, 4, 6, "Table 11. Coefficients", {"numeric": 5, "text_cols": 1}),
        (23, 1, 4, 5, "Table 12. Data needed for (16)", {"numeric": 4, "text_cols": 1}),
    ]
    for page, reg, nrows, ncols, label, kw in TAB:
        table(page, reg, nrows, ncols, label=label, **kw)

    rules = [
        "The panels of one printed figure share one label line, printed as a run "
        "('Figure 2 Figure 3 Figure 4', 'Figure 5. Figure 6.'), so each panel's caption "
        "quotes its own label out of that run [caption.verbatim].",
        "Each panel is its own measured layout block and is recorded as its own item "
        "with panel_count 1, which is why 26 printed figure numbers become 41 items "
        "[geometry.panel_count].",
        "Family follows the ink: the Fig. 13 panels on p14 are drawn as columns and are "
        "recorded as bar, every other plotted block is a connected series and is "
        "recorded as line [geometry.family].",
        "The Fig. 1 block is line art with boxed nodes and arrows, not a plot, so it is "
        "recorded as flowchart-or-schematic and its printed_numbers is false "
        "[geometry.printed_numbers].",
        "The right-hand p9 block is a raster screenshot of a web chart rather than "
        "vector ink, so it is recorded as photo-or-raster-image [geometry.family].",
        "Fig. 8 is drawn at the foot of p9 while its caption is printed at the head of "
        "p10; the caption quote is still verbatim on the neighbouring page "
        "[caption.position].",
        "Series are labelled by inline arrows inside the axes on Figs. 5-8, 12, 17, 18 "
        "and 23-26, so those blocks carry legend inside; the one-series blocks on p6, "
        "p10, p14, p17, p21, p23, p24 and the Fig. 22 panels carry none "
        "[geometry.legend].",
        "The Fig. 13 caption is clipped by the page gutter after 'in France, USA and', "
        "so the verbatim caption ends there [caption.verbatim].",
        "Table 3's printed label reads 'Tabel 3.'; the quote keeps the typo and the "
        "numbering field uses the nearest closed-enum member, 'Table N.' "
        "[caption.numbering].",
        "The p19 block prints three parameter values with no label of any kind, so it "
        "is recorded as a table with an empty verbatim and caption_source none "
        "[caption.numbering].",
        "Every ruled block in this paper uses vertical rules only, with a shaded header "
        "band and no zebra striping [table.rule_style].",
        "Table 7 is the one wide block: eleven columns, ten of them numeric, so it is "
        "recorded as full width in portrait [table.cols].",
        "Units are printed inside the stub cells of Tables 4, 5, 7-10, not in the header "
        "row, so units_in_header is false there [table.units_in_header].",
        "Figs. 10, 11 and 24 are named only inside a run of numbers ('Figure 9, 10 and "
        "11', 'Figure 23, 24, 25, 26'), which the mention reader resolves for the first "
        "number only, so those items carry a null mention with count 0 [mention.count].",
        "The p19 mini table and Fig. 18 are printed above the '6.2' heading, so they are "
        "filed under 6.1 rather than under the heading nearest the foot of the page "
        "[place.section_path].",
    ]
    note = (
        "Twenty-six printed figure numbers become forty-one items because twelve of them "
        "are three-panel figures whose panels are separate exports, and Fig. 8 carries a "
        "dropped-in screenshot beside its drawn curve. Twelve printed table numbers plus "
        "one unlabelled parameter block on p19 make thirteen tables, so the measured 54 "
        "regions split 41 + 13 with nothing excluded. Two tool blind spots are recorded "
        "here rather than fixed mid-queue: context_extract.py resolves only the first "
        "number in a run ('Figure 9, 10 and 11'), so Figs. 10, 11 and 24 have no mention, "
        "and its path_for() takes the last heading the page carries, which files the p19 "
        "table and Fig. 18 under 6.2 and Fig. 21 under 6.5 although both are printed "
        "above those headings; the section paths written here follow the printed order. "
        "The Fig. 13 caption is clipped by the gutter after 'in France, USA and', and "
        "Table 3's label is printed as 'Tabel 3.'."
    )
    payload = {
        "paper": PID,
        "layout_sha256": LAYOUT["layout_sha256"],
        "items": [ITEMS[k] for k in ORDER if k in ITEMS],
        "tables": [TABLES[k] for k in ORDER if k in TABLES],
        "excluded_regions": EXCLUDED,
        "rules": rules,
        "note": note,
    }
    out = PROXY / "pc26-payload.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    return str(out)


def main() -> int:
    path = build()
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    print(f"payload {path}: {len(payload['items'])} figures, "
          f"{len(payload['tables'])} tables, {len(payload['excluded_regions'])} excluded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
