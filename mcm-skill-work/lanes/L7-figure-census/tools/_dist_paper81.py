"""Hand census of P-C-2015-33900-7f8065e8 (Team 33900, 20 pages, 13 measured regions).

Twelve exhibit rows plus one excluded fragment. The paper numbers eleven figures and four
tables; eleven figures own a region and one of the four tables does, so three printed grids are
declared as a gap.

   p4  r1  Table 1   table-grid             the symbol table, three rules and two group headers
   p6  r1  Fig.1     flowchart-or-schematic the ICM org chart, boxes joined by connectors
   p6  r2  (excluded) -                     Figure 1's own key box, a fragment of the same art
   p7  r1  Fig.2     node-link-network      the 150-node personnel relationship graph
   p8  r1  Fig.3     node-link-network      the directed org graph, node size = LeaderRank
   p10 r1  Fig.4     flowchart-or-schematic the three-tier AHP hierarchy
   p13 r1  Fig.5     scatter                turnover intention at month 6 and month 8
   p14 r1  Fig.6     bar                    stacked monthly productivity, three levels
   p14 r2  Fig.7     line                   turnover intention and average productivity, dual axis
   p15 r1  Fig.8     line                   recruiting and training cost, dual axis
   p15 r2  Fig.9     line                   worker count under three churn rates
   p16 r1  Fig.10    bar                    stacked productivity after the promotion rule
   p17 r1  Fig.11    flowchart-or-schematic the multiplex picture: Network H over Network C

Declared gap: Table 2 (p12, a two-row unruled grid of service-time requirements), Table 3
(p16, an unruled four-row sensitivity grid) and Table 4 (p17, the same grid with another
parameter) return no measured region.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-C-2015-33900-7f8065e8"
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

DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


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


def caption(verbatim: str, numbering: str = "Figure N.", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


# ---------------------------------------------------------------- section paths
# Each label is an indexed heading or a printed line. On four rows the governing heading sits on
# the previous page, and on three more the heading for the NEXT section prints below the picture.
SEC_22 = ["2 Assumptions and Notations", "2.2 Notations"]
SEC_313 = ["3 The Human Capital Network Model", "3.1 Assigning Employees to Offices",
           "3.1.3 Optimization Using Genetic Algorithm"]
SEC_321 = ["3 The Human Capital Network Model", "3.2 Building The Human Capital Network",
           "3.2.1 Building The Network of Personnel Relationship"]
SEC_322 = ["3 The Human Capital Network Model", "3.2 Building The Human Capital Network",
           "3.2.2 Building the Organizational Network"]
SEC_334 = ["3.3 Evaluating Turnover Intention of Employee", "3.3.4 Evaluation using AHP]"]
SEC_5 = ["5 Simulation Results and Analysis"]
SEC_7 = ["7 Improvements using Multi-layered Networks"]

ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "single",
           legend: str = "none", numbers: bool = True, labels: bool = False,
           three_d: str = "no", colorbar: bool = False, source: str = "text-layer",
           shared_axes: bool = False, note: str = "", other_note: str = "",
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
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, numbering),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": colorbar,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, cap_text: str, mention: dict, kind: str, path: list[str], *,
          rows: int, cols: int, numeric_cols: int, text_cols: int, rule_style: str,
          width: str, header_rows: int = 1, units_in_header: bool = False,
          note: str = "", note_sentence: str = "", source: str = "text-layer") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source,
        "note": note,
        "place": place(page, reg, kind, path),
        "mention": mention,
        "caption": caption(cap_text, "Table N.", "above"),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule_style, "zebra": False, "merged_cells": False,
                  "diagonal_header": False, "units_in_header": units_in_header,
                  "decimal_aligned": False, "numeric_cols": numeric_cols,
                  "text_cols": text_cols, "width": width, "orientation": "portrait",
                  "continued": False, "note_sentence": note_sentence},
    })


# ---------------------------------------------------------------- 2.2 the symbol table
table(4, 1, q("Table 1. Notations (in the order of model)", 4),
      cited(4, 4, ["Table 1"], 1,
            "We use a list of symbols (cf. Table 1) for simplification of expression."),
      "model", SEC_22, rows=13, cols=3, numeric_cols=0, text_cols=3, rule_style="booktabs",
      width="full", note=(
          "Three full-width rules at 199.3, 218.5 and 414.5 pt across 473.0 pt, no vertical, and "
          "two more short rules at 300.3 and 332.6 pt which are the fraction bars inside the two "
          "formula cells, not row separators. Eleven symbol rows in three columns, plus TWO "
          "centred group headers inside the body - 'Human Capital Network Model' at 222.5 pt and "
          "'The Second Model' at 372.3 pt - which carry no symbol, no definition and no note and "
          "are centred across all three columns without being marked as merged cells "
          "[table.merged_cells]."),
      note_sentence="We use a list of symbols (cf. Table 1) for simplification of expression.")

# ---------------------------------------------------------------- 3.x the drawn figures
figure(6, 1, "flowchart-or-schematic",
       q("Figure 1. Organizational structure of ICM with all the employees assigned. Each block "
         "represents an office (without *) or two divisions (with * and thicker border). Bold "
         "text is abbreviation of positions(SM for Senior Manager etc.). Blocks with the same "
         "color and style share same constitute. Some blocks (Manager Offices and Branch Offices) "
         "are replaced by legend symbols for simplification.", 6), "Figure N.",
       cited(5, 6, ["Figure 1"], 1,
             "We can see from Figure 1 that the algorithm not only assigned offices according to "
             "staff hierarchy"),
       "model", SEC_313, labels=True, note=(
           "A four-tier box-and-connector org chart: CEO at the top, seven division heads under "
           "it, a row of PRODUCT* boxes, six DIRECTOR boxes with their own sub-boxes and a row of "
           "hatched boxes at the bottom. Colour carries meaning that no legend on the page "
           "explains in words: CEO and VP are red-framed, the six other heads green-framed, one "
           "DIRECTOR blue-framed and the rest black. The bottom row is hatched and EMPTY - nine "
           "manager and branch boxes carry only a fill pattern, their staffing moved into the key "
           "box on the next region [place.section_path]."))
figure(7, 1, "node-link-network",
       q("Figure 2. Personnel Relationship Network of ICM. The color denotes office hierarchy. "
         "Small clusters of offices and three types of edges are labeled. Some edges are omitted "
         "for conciseness.", 7), "Figure N.",
       cited(6, 7, ["Figure 2"], 1, "The graph G is illustrated in Figure 2."),
       "model", SEC_321, legend="inside", labels=True, note=(
           "About 150 nodes drawn as circles joined by thin edges, with five colours keyed by "
           "level in a boxed legend at upper right - red top-level, yellow mid-top, green "
           "mid-level, blue mid-bottom, purple bottom-level. Three edge classes are lettered into "
           "the picture with arrows ('Links within an office/division', 'Links between office "
           "heads', 'Inter-hierarchy links') and five individual nodes are circled and named "
           "(Director 2, Branch L, Internet, VP, CEO). No axes, no numbers: the 1709 vector paths "
           "in the region are all node outlines and edges."))
figure(8, 1, "node-link-network",
       q("Figure 3. Organizational Network of ICM. The color denotes office level. The size of "
         "the node denotes the LeaderRank Value. Note that the LeaderRank Value of Production "
         "Manager is higher than that of VP despite of their hierarchical relations.", 8),
       "Figure N.", cited(7, 8, ["Figure 3"], 1, "Graph g is a directed graph (cf. Figure 3)."),
       "model", SEC_322, legend="inside", labels=True, note=(
           "The same five-colour level key as Figure 2, but the graph is now a directed radial "
           "layout - CEO at the centre right with Production Manager and VP as hubs, department "
           "names radiating out and arrowheads on the edges. Node size encodes LeaderRank, which "
           "the caption flags as the interesting result: Production Manager's node is larger than "
           "VP's although VP sits higher. No axes and no numbers."))
figure(10, 1, "flowchart-or-schematic",
       q("Figure 4. The AHP hierarchy for determine employee’s turnover intention.", 10),
       "Figure N.",
       cited(10, 10, ["Figure 4"], 1,
             "Our AHP hierarchy for this evaluation is illustrated in Figure 4."),
       "model", SEC_334, labels=True, note=(
           "Three tiers of plain rectangles - the goal 'Turnover Intention (T)', four criteria "
           "C1 to C4, and the alternatives Employee1, Employee2, Employee3 and an ellipsis box - "
           "joined by straight lines with no arrowheads. No colour, no shading, no numbers. The "
           "one region in the paper with a single vertical rule inside it (x=259.2), which is an "
           "edge of the C2 box rather than a table rule [place.area_frac]."))
figure(13, 1, "scatter",
       q("Figure 5. Propagation of turnover intention over the Personnel Relationship Network. "
         "Observation of Turnover Intention of (a) a certain time and (b) two months later. "
         "Turnover propagation is clearly illustrated. It can also be observed that the turnover "
         "rate is higher in mid-level positions.", 13), "Figure N.",
       cited(13, 13, ["Figure 5", "Figure 5, 6"], 1,
             "according to the similarity of nodes (cf. Figure 5, 6)"),
       "model", SEC_5, panels=2, layout="1x2", legend="inside", shared_axes=True, colorbar=True,
       note=(
           "Two square panels side by side, (a) month = 6 and (b) month = 8, each about 150 open "
           "circles in the same coordinates -0.2 to 1.2 on both axes - with a grey 'turnover "
           "intention' scale bar inside each panel. The two panels are lettered (a) and (b) inside "
           "the picture and captioned in words under the axes, and a long arrow leaves the panel "
           "title 'relatively high turnover rate in mid-level positions' on the left and points "
           "into both panels, so a single annotation spans the pair."))
figure(14, 1, "bar",
       q("Figure 6. Task 2.1", 14), "Figure N.",
       cited(13, 14, ["Figure 6", "Figure 5, 6"], 1,
             "according to the similarity of nodes (cf. Figure 5, 6)"),
       "model", SEC_5, legend="inside", labels=True, note=(
           "Twenty-four stacked bars, one per month, in three salmon, green and blue segments for "
           "Senior Mangers, Middle Managers and Employees, on a grey panel with white gridlines "
           "and a boxed legend inside. The caption is the whole caption: 'Figure 6. Task 2.1'. "
           "The legend misspells 'Mangers', the same typo as Figure 10's legend and Figure 10's "
           "caption line, and the caption is a task number with no description of the exhibit "
           "[caption.verbatim]."))
figure(14, 2, "line",
       q("Figure 7. Task 2.2", 14), "Figure N.",
       cited(13, 14, ["Figure 7"], 1,
             "The average turn over intention of different levels of positions are shown in "
             "Figure 7, which is a main factor of productivity."),
       "model", SEC_5, legend="inside", labels=True, note=(
           "Four series on one grey panel with a dual y axis: three turnover-intention curves for "
           "Employees, Middle Managers and Senior Managers read off the left axis "
           "'Turnover Intention' 0.0-0.8, and the red Average Productivity curve read off the "
           "right axis 'Productivity (avg)' 0.0-0.6. The dual axis is the point of the exhibit - "
           "two different quantities on one month scale - and the prose says so explicitly "
           "('with the average productivity shown with the right y-axis'). Caption is again only "
           "a task number, 'Task 2.2'."))
figure(15, 1, "line",
       q("Figure 8. Task 3", 15), "Figure N.",
       cited(14, 15, ["Figure 8"], 1,
             "The recruiting costs of ICM in terms of σ shown in Figure 8 varies randomly"),
       "model", SEC_5, legend="inside", labels=True, note=(
           "Two cost curves on one grey panel with a dual y axis: the jagged blue Relative "
           "Recruiting Cost series on the left axis 0.0-2.0 and the smooth red Relative Training "
           "Cost series on the right axis 0-8. The jagged-versus-smooth contrast is the argument "
           "in the prose (poisson recruits against a deterministic training function), and the "
           "picture carries no annotation saying so. Caption is 'Task 3' and nothing else."))
figure(15, 2, "line",
       q("Figure 9. Task 4", 15), "Figure N.",
       cited(15, 15, ["Figure 9"], 1, "The total number of workers are shown in Figure 9"),
       "model", SEC_5, legend="inside", labels=True, note=(
           "Three curves of worker count against month, keyed '35% Churn Rate', '25% Churn Rate' "
           "and '18% Churn Rate' in a legend inside the grey panel, on a single y axis 160-320. "
           "The 18 per cent series is the comparison the prose asks for. Caption is 'Task 4' and "
           "nothing else."))
figure(16, 1, "bar",
       q("Figure 10. Task 5", 16), "Figure N.",
       cited(15, 16, ["Figure 10"], 1,
             "Figure 10 shows the overall productivity of different levels of positions."),
       "model", SEC_5, legend="inside", labels=True, note=(
           "The same 24-month stacked bar construction as Figure 6 - salmon, green and blue "
           "segments, same legend, same grey panel, same 'Senior Mangers' typo - but after the "
           "promotion rule runs, so the top of the stack is flatter and the blue base thinner. "
           "Two rows in one paper built from the identical template, distinguished only by the "
           "caption text 'Task 2.1' against 'Task 5' [geometry.panel_count]."))
figure(17, 1, "flowchart-or-schematic",
       q("Figure 11. Task 6", 17), "Figure N.",
       cited(17, 17, ["Figure 11"], 1,
             "We consider Network H and Network C (cf. Figure 11), which respectively"),
       "model", SEC_7, panels=2, layout="stacked planes", legend="inside", numbers=False,
       three_d="isometric", note=(
           "Two tilted parallelograms stacked one above the other - 'Network H' on top, "
           "'Network C' below - each carrying the same handful of labelled nodes (EE3, ES5, ES7, "
           "IS1, JM6, EE34, SM1) as coloured circles joined by solid edges, with dashed vertical "
           "lines tying each node to its counterpart on the other plane. That pairing is the whole "
           "argument: the two networks share their nodes and differ in their edges, which is what "
           "makes the multiplex point. FOUR RULES AND SEVEN VERTICALS sit inside the region at "
           "112 pt wide - they are the edges of the two slab frames, not a table grid, so this "
           "region must not be read as a printed table [kind]."))

# ---------------------------------------------------------------- the excluded fragment
EXCLUDED.append({
    "page": 6,
    "bbox": REG[(6, 2)],
    "reason": "fragment-of-other",
    "note": ("Figure 1's key box, cut off as its own region: a bordered rectangle holding two "
             "swatch-and-text pairs, green hatch 'Manager Offices*' over 'JM AC IS EE*4' and blue "
             "hatch 'Branch Offices*' over 'ES IE*6'. It is the legend that the Figure 1 caption "
             "promises ('Some blocks (Manager Offices and Branch Offices) are replaced by legend "
             "symbols for simplification'), it sits 8 pt under the chart, and it has no caption, "
             "no number and no title of its own."),
    "confidence": "high",
})

# ---------------------------------------------------------------- rules and note
RULES: list[str] = [
    "Families: line x3, flowchart-or-schematic x3, bar x2, node-link-network x2, scatter x1, "
    "table-grid x1, over twelve rows from thirteen measured regions plus one excluded fragment "
    "[geometry.family].",
    "The excluded region is Figure 1's key box on p6, a bordered box of two hatch swatches and "
    "their staffing that the Figure 1 caption explicitly describes as a legend substitution. It "
    "returns as its own measured region because it is separated from the chart by 8 pt of white, "
    "so it is declared excluded rather than counted as a thirteenth exhibit "
    "[place.area_frac].",
    "The three chart families are not interchangeable here. Figures 2 and 3 are the only "
    "node-link rows - hundreds of nodes in one frame with no axes - while Figures 1, 4 and 11 are "
    "schematic diagrams with a handful of labelled boxes on connectors. Figure 11 is the crossover "
    "case: it holds six nodes drawn as circles, but it is a two-plane construction diagram with no "
    "graph statistics, so it is recorded as a schematic with two panels [geometry.panel_count].",
    "Six captions say nothing. Figures 6 to 11 are captioned 'Task 2.1', 'Task 2.2', 'Task 3', "
    "'Task 4', 'Task 5' and 'Task 6' - a task number with no noun in it. The four figures before "
    "them carry two to four descriptive sentences each, so the paper's captioning collapses "
    "exactly at the point where the exhibits move from structure diagrams to simulation output "
    "[caption.words].",
    "Two of the line rows use a DUAL y axis, and that is the exhibit's argument rather than a "
    "styling choice: Figure 7 puts turnover intention on the left and average productivity on the "
    "right, and the prose justifies reading the second axis; Figure 8 puts a jagged poisson "
    "recruiting cost on one axis against a smooth deterministic training cost on the other. No "
    "legend key says which axis belongs to which series, so the colour of the axis title is the "
    "only cue [geometry.legend].",
    "Figures 6 and 10 are the same stacked-bar template twice - same three colours, same legend "
    "position, same grey panel, same 'Senior Mangers' typo - with the promotion rule the only "
    "difference. They are therefore one row each, not one row with two panels, because they print "
    "four pages apart and carry different task numbers [geometry.panel_count].",
    "Only Figure 5 has more than one panel among the charts, and its two panels are lettered (a) "
    "and (b) inside the picture with their own grey turnover-intention scale bars, on identical "
    "axes, and a single arrowed annotation crosses from outside into both [geometry.shared_axes].",
    "THREE PRINTED GRIDS ARE MISSING AND THAT IS DECLARED, NOT PATCHED: Table 2 on p12 (two rows, "
    "six level headers across and the service-time requirements under them, no rules at all), "
    "Table 3 on p16 (caption at 487.5 pt, four numeric rows to 574.6 pt, no rules) and Table 4 on "
    "p17 (caption at 87.1 pt, the same four rows, no rules). All three carry a caption in the "
    "text layer and Table 2 is cited three times, so their absence is a measurer result, not a "
    "judgement about what they are [place.area_frac].",
    "TABLE 4 REPEATS TABLE 3 NUMBER FOR NUMBER. The sigma sweep on p16 prints 2.314 / 2.083 / "
    "2.250, 0.378 / 0.353 / 0.374, 3.378 / 3.372 / 3.741 and 35.16 / 38.33 / 37.00, and the mu "
    "sweep on p17 prints the same twelve values in the same order under a caption that promises a "
    "different parameter. The prose reads the second one as an independent confirmation "
    "('comparing the two tests the conclusions are basically the same'), so the paper's second "
    "sensitivity result is a copy of its first [caption.verbatim].",
    "Section paths follow the last heading printed above each region, which on four rows is on the "
    "previous page: Table 1 under 2.2 on p4, Figure 1 under 3.1.3 on p5, Figure 2 under 3.2.1 on "
    "p6, Figure 3 under 3.2.2 on p7. On three more rows the heading for the NEXT section prints "
    "below the picture - 3.2 and 3.2.1 on p6 sit at 355.4 and 432.8 pt under a chart that ends at "
    "214.5 pt, and 3.3 on p8 sits at 385.0 pt under a chart that ends at 313.2 pt - so a naive "
    "nearest-heading pass files all three in the wrong section [place.section_path].",
    "Citation is complete but thin: eleven of the twelve rows are named in prose and none is "
    "never named, yet only Figure 1 is named from a page other than its own or the one before, and "
    "no exhibit is named twice. Figures 5 and 6 share a single pointer, 'cf. Figure 5, 6', which "
    "is the only place the paper cites two exhibits at once [mention.count].",
    "Area runs from 0.013 for the excluded key box to 0.274 for Figure 2, a factor of twenty-one, "
    "and the largest row is the personnel network - the one exhibit whose every point is data "
    "rather than layout [place.area_frac].",
]

NOTE = (
    "Paper 81, Team 33900, a 2015 paper that models the human capital network of an imaginary "
    "company called ICM - 370 employees assigned to offices by a genetic algorithm, a personnel "
    "relationship graph, a directed organisational graph, AHP scoring of turnover intention, and "
    "then a two-year simulation of churn, promotion, recruitment and productivity. Twenty pages, "
    "thirteen measured regions on ten pages: twelve exhibit rows and one excluded fragment. The "
    "paper numbers eleven figures and four tables.\n\n"
    "What the exhibits are. Three structural diagrams (the org chart, the AHP hierarchy and the "
    "multiplex picture), two node-link graphs of the same company at two different resolutions "
    "(personnel relationship and organisational), one two-panel scatter of turnover intention at "
    "month 6 against month 8, two stacked-bar records of monthly productivity, and three line "
    "charts of the simulation - turnover intention against average productivity on a dual axis, "
    "the two cost curves on another dual axis, and worker count under three churn rates. The "
    "symbol table is the only grid with a measured region.\n\n"
    "The finding worth carrying out of this paper is Table 4. It prints the same twelve numbers as "
    "Table 3 - 2.314, 2.083, 2.250 for the promoted count, 0.378, 0.353, 0.374 for productivity, "
    "3.378, 3.372, 3.741 for senior-manager productivity, 35.16, 38.33, 37.00 for middle-manager "
    "count - under a caption that promises a different parameter sweep, and the prose then reads "
    "the second as independent confirmation of the first. Neither grid has a measured region, so "
    "both are declared as a gap; the fact that they are the same table survives only because the "
    "page text was read.\n\n"
    "The second finding is a caption collapse. Figures 1 to 5 carry five, four, three, one and "
    "four sentences of description; Figures 6 to 11 carry a task number and nothing else - 'Task "
    "2.1', 'Task 2.2', 'Task 3', 'Task 4', 'Task 5', 'Task 6'. The three charts that actually need "
    "explaining, the two dual-axis plots and the churn comparison, are the ones captioned with two "
    "words.\n\n"
    "The third is the excluded region: Figure 1's legend is drawn as a separate bordered box 8 pt "
    "below the chart, so the measurer returns it as its own region. It is declared a fragment of "
    "Figure 1 and excluded by reason, not deleted.\n\n"
    "On the text side, three grids print with no rules at all - Table 2, Table 3 and Table 4 - "
    "which is the unruled-grid blind spot this lane keeps meeting. Section attribution needed hand "
    "work on seven rows: four sit under a heading printed on the previous page and three sit ABOVE "
    "the heading of the section the nearest-heading pass would assign them to, because 3.2, 3.2.1 "
    "and 3.3 all print below the pictures on pp6 and 8."
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

out = PROXY / "pc81-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
