"""Hand census of P-A-2015-40764-20552f34 (Team 40764, 25 pages, 29 measured regions).

Twenty-nine regions over fifteen pages, all accounted for: ten figure regions and nineteen
table regions, no exclusions. The paper prints twenty-one tables, so two printed grids have no
measured region of their own - Tables 6 and 7 on p8 - and that gap is declared in the note
rather than invented here.

   p3  r1  Fig.1   the eight-state transition cartoon
   p3  r2  Table 1 state transition rates, 2 columns
   p5  r1  Table 2 stochastic parameters, 2 columns
   p6  r1  Table 3 stochastic vs deterministic advantages
   p7  r1  Table 4 live population statistics, 4 columns
   p7  r2  Table 5 population parameters, 4 columns
   p8  r1  Table 8 WHO data for 5 February 2015, 4 columns
   p9  r1  Table 9 appropriate parameter values, 6 columns
   p10 r1  Table 10 validation results, 9 columns, two-level header
   p10 r2  Fig.2   left panel
   p10 r3  Fig.2   right panel
   p10 r4  Fig.2   lower wide panel
   p11 r1  Table 11 stochastic vs deterministic comparison, 7 columns
   p11 r2  Fig.3   infected over time
   p13 r1  Table 12 projection at current treatment
   p14 r1  Table 13
   p14 r2  Table 14
   p14 r3  Table 15
   p14 r4  Table 16
   p14 r5  Table 17
   p15 r1  Table 18
   p15 r2  Table 19
   p15 r3  Table 20
   p16 r1  Fig.4   short-term reduction, scatter
   p16 r2  Fig.5   medium-term reduction, scatter
   p17 r1  Fig.6   left part
   p17 r2  Fig.6   right part
   p19 r1  Table 21 fixed points, with the case list under it
   p22 r1  Fig.7   extension cartoon

Ten figure rows, nineteen table rows, nothing excluded and nothing unresolved.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2015-40764-20552f34"
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

# 595.32 x 841.92 pt page, text block x 56.7 to 538.6, so the measure is 481.9 pt
MEASURE = 481.9
DOC_ORDER = 0


def q(text: str, page: int) -> str:
    """Refuse to record a quote that the text layer of that page does not print."""
    if schema.norm(text) not in schema.page_text(PID, page):
        raise KeyError((page, text[:70]))
    return schema.norm(text)


def qp(text: str, pages: list[int]) -> str:
    """Same guard, for a sentence that may print on a neighbouring page."""
    for page in pages:
        if schema.norm(text) in schema.page_text(PID, page):
            return schema.norm(text)
    raise KeyError((pages, text[:70]))


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
          pattern: str = "direct", read: int = 1, gap: int | None = None,
          trail: str = "") -> dict:
    pages = sorted({page - 1, page, page + 1, first_page - 1, first_page, first_page + 1})
    return {"first_page": first_page, "lead_pages": page - first_page, "style": list(style),
            "count": count, "lead_sentence": qp(lead, pages) if lead else "",
            "trail_sentence": qp(trail, pages) if trail else "", "lead_pattern": pattern,
            "read_sentences": read, "gap_sentences": gap}


def caption(verbatim: str, numbering: str = "none", position: str = "below") -> dict:
    return {"verbatim": verbatim, "numbering": numbering,
            "words": len(schema.words(verbatim)),
            "sentences": verbatim.count(". ") + (1 if verbatim else 0),
            "units": False, "variables": False, "variable_count": 0,
            "conditions": False, "concludes": False, "voice": "none",
            "position": position}


ITEMS: list[dict] = []
TABLES: list[dict] = []
EXCLUDED: list[dict] = []


def figure(page: int, reg: int, family: str, cap_text: str, numbering: str, mention: dict,
           kind: str, path: list[str], *, panels: int = 1, layout: str = "1",
           legend: str = "none", numbers: bool = False, labels: bool = False,
           three_d: str = "no", source: str = "text-layer", numbered: bool = True,
           position: str = "below", note: str = "", other_note: str = "",
           shared_axes: bool = False, confidence: str = "high") -> None:
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
        "caption": caption(cap_text, numbering, position),
        "geometry": {"family": family, "panel_count": panels, "panel_layout": layout,
                     "shared_axes": shared_axes, "legend": legend, "colorbar": False,
                     "three_d": three_d, "printed_numbers": numbers, "data_labels": labels},
    })


def table(page: int, reg: int, rows: int, cols: int, kind: str, path: list[str],
          note_sentence: str, note: str, *, rule: str = "booktabs", numeric: int = 1,
          header_rows: int = 1, numbered: bool = True, width: str = "full",
          zebra: bool = False, merged: bool = False, decimal: bool = False,
          diagonal: bool = False, continued: bool = False, cap_text: str = "",
          numbering: str = "Table N:", position: str = "above",
          mention: dict | None = None, source: str = "text-layer") -> None:
    TABLES.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "caption_verbatim": cap_text,
        "caption_source": source if cap_text else "none",
        "note": note,
        "place": place(page, reg, kind, path, numbered),
        "mention": mention or none_mention(),
        "caption": caption(cap_text, numbering if cap_text else "none", position),
        "table": {"rows": rows, "cols": cols, "header_rows": header_rows,
                  "rule_style": rule, "zebra": zebra, "merged_cells": merged,
                  "diagonal_header": diagonal, "units_in_header": False,
                  "decimal_aligned": decimal, "numeric_cols": numeric,
                  "text_cols": cols - numeric, "width": width, "orientation": "portrait",
                  "continued": continued,
                  "note_sentence": qp(note_sentence, [page - 1, page, page + 1]) if note_sentence else ""},
    })


def excluded(page: int, reg: int, reason: str, note: str) -> None:
    EXCLUDED.append({
        "page": page,
        "bbox": REG[(page, reg)],
        "kind": KIND[(page, reg)],
        "reason": reason,
        "note": note,
    })


# ---------------------------------------------------------------- section paths
SEC_INTRO = ["1.1 Problem Approach", "1.1.1 Assumptions"]
SEC_STOCH = ["2 Mathematical Models", "2.1 Stochastic Model"]
SEC_CMP = ["2 Mathematical Models", "2.3 Comparison of Models"]
SEC_PARAMS = ["3 Results - Predicting the Spread of Ebola", "3.1 Model Parameters"]
# 3.1.4 prints its own Greek in a private-use glyph, so the accepted spelling carries the
# alphabetic characters the text layer does hold; 3.1.2 does not, and stops at its parent.
SEC_STATES = ["3.1 Model Parameters", "3.1.4 α, β, γ"]
SEC_VALID = ["3 Results - Predicting the Spread of Ebola", "3.2 Validation",
             "3.2.1 Stochastic Model"]
SEC_DET = ["3.2 Validation", "3.2.2 Deterministic Model"]
SEC_SENS = ["4 Results - Predicting the Effect of Improved Treatment", "4.2 Sensitivity Analysis",
            "4.2.1 Stochastic Model"]
SEC_SENSDET = ["4.2 Sensitivity Analysis", "4.2.2 Deterministic Model"]
SEC_CONCL = ["5 Summary of Mathematical Modelling", "5.3 Conclusion"]

# ---------------------------------------------------------------- state cartoon and the first grids
figure(3, 1, "flowchart-or-schematic",
       cap(3, "Figure 1: Possible", "in an Ebola outbreak"), "Figure N:",
       cited(3, 3, ["Figure 1"], 1, "All possible state transitions are illustrated in Figure 1."),
       "assumption", SEC_INTRO, numbers=True, labels=True, note=(
           "Four state boxes - Healthy (Vulnerable), Infected, Healthy (Immune) and Death - with "
           "Birth drawn as an inflow above the first, joined by eight numbered transitions that "
           "the prose says are each assigned one rate parameter. The numbers are the only text the "
           "diagram carries besides the state names; the four rate symbols themselves print as "
           "bare glyphs beside the arrows and are defined only in Table 1, 100 pt below the art on "
           "the same page. Caption below, outside the drawing."))

table(3, 2, 6, 2, "assumption", SEC_INTRO,
      "A list of these parameters is provided in Table 1.",
      ("Header 'Parameter | Description' in bold, a rule above it, a heavy rule under it and a "
       "rule at the bottom, no vertical rule and no side frame, no shading. Six body rows, one per "
       "transition symbol alpha through epsilon, each description a rate in units per day. The "
       "gamma row's description drops the comma the phi row carries, which is the only difference "
       "in punctuation across the six."),
      rule="booktabs", numeric=0, width="full",
      cap_text=cap(3, "Table 1: State", "in the general Ebola model"),
      mention=cited(3, 3, ["Table 1"], 1,
                    "A list of these parameters is provided in Table 1."))
table(5, 1, 5, 2, "model", SEC_STOCH,
      "Definitions of parameters required for the stochastic model are given in Table 2.",
      ("Same two-column shape as Table 1 and the same three horizontal rules with no vertical "
       "rule: n, dt, P_n, I_n and H_n against their descriptions, dt given as a fraction of one "
       "day. This is the grid that the running prose cites before the deterministic model is "
       "introduced, and it is the only grid in the paper whose header cell is the bare word "
       "'Parameter' with nothing else in it."),
      rule="booktabs", numeric=0, width="full",
      cap_text=cap(5, "Table 2: Parameters", "stochastic model"),
      mention=cited(5, 5, ["Table 2"], 1,
                    "Definitions of parameters required for the stochastic model are given in "
                    "Table 2."))
table(6, 1, 4, 2, "model", SEC_CMP,
      "Table 3 compares the relative strengths of the stochastic and deterministic models.",
      ("Header 'Stochastic | Deterministic', rules above the header, under it and at the bottom, "
       "no vertical rule, no shading: four body rows of advantages. The fourth row has text in "
       "the stochastic column only - the deterministic cell is left blank with no dash and no "
       "em rule - so the grid's own four-versus-three imbalance reads as a value that went "
       "missing."),
      rule="booktabs", numeric=0, width="full",
      cap_text=cap(6, "Table 3: Unique", "stochastic and deterministic models"),
      mention=cited(6, 6, ["Table 3"], 1,
                    "Table 3 compares the relative strengths of the stochastic and deterministic "
                    "models."))
table(7, 1, 4, 4, "model", SEC_PARAMS,
      "Table 4 gives this data for the three relevant countries on 5 February 2015.",
      ("Header Country / Population / Birth Rate [ppl d-1] / Death Rate [ppl d-1] over three "
       "country rows and an 'Overall' row that is set bold and given its own rule above, so the "
       "grid has four horizontal rules and no vertical rule. The Overall population prints "
       "23,436,196 while its three rows add to 23,435,196, out by exactly one thousand; the two "
       "rate columns do add up. The two rate headers print 'ppld-1' with no space between the "
       "unit and the exponent, and the source named in the caption, CountryMeters, is not a "
       "health agency."),
      rule="booktabs", numeric=3, width="full",
      cap_text=cap(7, "Table 4: Live", "(CountryMeters 2015)"),
      mention=cited(7, 7, ["Table 4"], 2,
                    "Table 4 gives this data for the three relevant countries on 5 February 2015."))
table(7, 2, 4, 4, "model", SEC_PARAMS,
      "(6) Performing these operations gives the results in Table 5.",
      ("Country / epsilon / phi / Initial Population over three country rows and a bold Overall "
       "row separated by its own rule. Horizontal rules only, no vertical rule, no shading. The "
       "two symbols are the whole header - no word, no unit and no definition - and the reader has "
       "to carry their meaning down from Table 1 two pages earlier, where they are named in "
       "Table 1's description column rather than in a heading."),
      rule="booktabs", numeric=3, width="half",
      cap_text=cap(7, "Table 5: Population", "use in the model"),
      mention=cited(7, 7, ["Table 5"], 1,
                    "(6) Performing these operations gives the results in Table 5."))
table(8, 1, 4, 4, "result", SEC_STATES,
      "This data is given in Table 8.",
      ("Country / Total Cases / Total Deaths / Mortality Rate over three countries and a bold "
       "Overall row with its own rule above; four horizontal rules, no vertical rule, no shading. "
       "Every rate checks against its own row and the Overall rate checks against the column "
       "totals, but the header never says the mortality rate is a bare fraction - 0.65204 prints "
       "with no percent sign and no unit, so it reads as six hundred times a percentage."),
      rule="booktabs", numeric=3, width="half",
      cap_text=cap(8, "Table 8: WHO", "(World Health Organisation 2015a)"),
      mention=cited(8, 8, ["Table 8"], 2,
                    "This data is given in Table 8."))
table(9, 1, 4, 6, "model", SEC_STATES,
      "The parameters shown in Table 9 result in suitable estimates of the final death and case "
      "counts post-simulation.",
      ("Country / K / T / alpha / beta / gamma over three countries and an Overall row, with "
       "only three rules on the page - above the header, under the header and at the bottom - so "
       "the Overall row is not separated the way Tables 4, 5 and 8 separate theirs. No vertical "
       "rule and no shading; five of the six headers are bare italic symbols with no unit and no "
       "definition. The Overall row cannot be an aggregate of the rows above it: overall alpha "
       "5.0992e-10 and overall beta 8.2775e-3 both fall outside the range of the three country "
       "values, which is a typo in one exponent rather than a rule the reader can recover."),
      rule="booktabs", numeric=5, width="half",
      cap_text=cap(9, "Table 9: Appropriate", "values of parameters"),
      mention=cited(9, 9, ["Table 9"], 3,
                    "The parameters shown in Table 9 result in suitable estimates of the final "
                    "death and case counts post-simulation."))

table(10, 1, 4, 9, "result", SEC_VALID,
      "Results are presented in Table 10.",
      ("Country / C_M / sigma_C / D_M / sigma_D / C_W / D_W / |C_M - C_W| / sigma_C / "
       "|D_M - D_W| / sigma_D over three countries and an Overall row, with thin internal "
       "dividers after the country stub, after each sigma column and before and between the two "
       "ratio columns; the left and right edges stay open. The last two headers are written as "
       "stacked fractions rather than as a second header level. The Overall row is not the sum of "
       "the three countries in the two model-count columns - 22,557 against 22,614 cases and "
       "9,041 against 8,990 deaths - while the same row's WHO columns do add exactly, and its "
       "sigma_C of 150 is smaller than Sierra Leone's own 159."),
      rule="vertical-rules", numeric=8, width="full",
      cap_text=cap(10, "Table 10: Results", "validate the model"),
      mention=cited(10, 10, ["Table 10"], 1, "Results are presented in Table 10."))
table(11, 1, 4, 7, "result", SEC_DET,
      "Table 11 shows the results for February 5 2015 of simulating the deterministic model with "
      "the parameters in Section 3.1.",
      ("Country / I_S / I_D / H_S / H_D / P_S / P_D over three countries and an Overall row, with "
       "internal dividers after the stub, after the two infected columns, after the two healthy "
       "columns and before the population pair; open left and right. The single-letter S and D "
       "subscripts are never expanded anywhere on the page. The Overall row contradicts every one "
       "of the six columns it closes - 7,690 against 7,127 infected, 5,820 against 6,490 healthy, "
       "and populations that differ in the thousands - so the reader cannot tell which of the two "
       "readings the paper stands behind."),
      rule="vertical-rules", numeric=6, width="half",
      cap_text=cap(11, "Table 11: Comparison", "February 5 2015"),
      mention=cited(11, 11, ["Table 11"], 1,
                    "Table 11 shows the results for February 5 2015 of simulating the "
                    "deterministic model with the parameters in Section 3.1."))
for _page, _reg, _num, _rows, _cap_tail, _first, _sentence, _note in (
    (13, 1, 12, 3, "(new cases and new deaths)", 13,
     "These results are presented in Table 12.",
     ("Country / C / D under a spanning row of 6 Months, 1 Year and 2 Years - two header rows, "
      "two internal dividers between the three time groups, a bottom rule and no top rule, so the "
      "grid begins on a bare header row. The six leaf headers are the identical strings C and D "
      "three times, so which C belongs to which year can only be read by column position, and "
      "neither letter is expanded anywhere in the paper.")),
    (14, 1, 13, 3, "decreased by 10%", 13,
     "The results are given in Table 13 and Table 14 respectively.",
     ("Same seven-column two-level shape as Table 12, same two dividers and same missing top rule. "
      "All eighteen cells are negative and not one of them carries a minus sign, so the reader "
      "has to know from the prose that every entry is a loss. C and D are again the only column "
      "label, with no unit and no expansion.")),
    (14, 2, 14, 3, "K = 0.", 13,
     "The results are given in Table 13 and Table 14 respectively.",
     ("Seventh column pair for the same three countries, the previous table continued as a second "
      "grid rather than as more rows: the two are cited in one sentence on p13, 'The results are "
      "given in Table 13 and Table 14 respectively.', and the reader has to take the pair together. "
      "Same dividers, same missing top rule, same unexpanded C and D.")),
    (14, 3, 15, 3, "decreased by 10%", 14,
     "Average simulation results are given in Table 15, Table 16 and Table 17 respectively.",
     ("Same seven columns and same missing top rule. The signing is inconsistent inside a single "
      "row: Sierra Leone prints '-10  +25', one explicit minus and one explicit plus, while the "
      "Liberia C column runs +18, +146, -25 across the three time points, so the sign convention "
      "changes from cell to cell rather than from table to table.")),
    (14, 4, 16, 3, "rate to 30% in all regions", 14,
     "Average simulation results are given in Table 15, Table 16 and Table 17 respectively.",
     ("Same seven columns, same missing top rule. Sierra Leone's death column reads -3, -147, "
      "-178 while its case column reads +75 and then a two-digit figure, so the two paired "
      "columns are on scales four orders of magnitude apart and the grid offers no unit to say "
      "so.")),
    (14, 5, 17, 3, "rate to 15% in all regions", 14,
     "Average simulation results are given in Table 15, Table 16 and Table 17 respectively.",
     ("Same seven columns, same missing top rule. Guinea's case and death columns diverge inside "
      "one row - -15 against -1,109, Liberia -43 against -1,196 - which is the pattern the "
      "medicine sensitivity produces throughout, and nothing in the header explains why the death "
      "column moves two orders harder than the case column.")),
    (15, 1, 18, 3, "population in two years", 15,
     "Simulating the stochastic model with these parameters gives results shown in Table 18, "
     "Table 19, and Table 20.",
     ("First of the three vaccine grids: same seven columns, same two-level header with the span "
      "row 6 Months / 1 Year / 2 Years, same missing top rule. Sierra Leone's death column at six "
      "months is the one cell in the paper that improves - '+25' - and it prints with a plus sign "
      "while its neighbours carry none.")),
    (15, 2, 19, 3, "population in two years", 15,
     "Simulating the stochastic model with these parameters gives results shown in Table 18, "
     "Table 19, and Table 20.",
     ("Second vaccine grid, ten per cent stronger than Table 18, identical shape and identical "
      "faults - no top rule, unexpanded C and D, no units. Internally consistent, which is worth "
      "recording on this paper because Tables 10, 11 and 21 are not.")),
    (15, 3, 20, 3, "population in two years", 15,
     "Simulating the stochastic model with these parameters gives results shown in Table 18, "
     "Table 19, and Table 20.",
     ("Third vaccine grid at fifty per cent, identical shape and identical faults. The three "
      "tables are cited in one sentence and are the only place the paper shows the vaccine "
      "scaling monotonically - every value in Table 20 is a larger loss than the matching value "
      "in Table 19.")),
):
    # The sentence that cites Tables 13 and 14 prints on p13, one page above the grid, and a note
    # sentence is only valid on its own page or the next, so those two rows carry none.
    _note_sentence = _sentence if _page == _first else ""
    table(_page, _reg, _rows, 7, "result", SEC_SENS, _note_sentence, _note,
          rule="vertical-rules", numeric=6, header_rows=2, width="half",
          cap_text=cap(_page, f"Table {_num}:", _cap_tail),
          mention=cited(_first, _page, ["Table %d" % _num], 1, _sentence))
table(19, 1, 8, 4, "model", SEC_SENSDET,
      "",
      ("Case / Steady state / Conditions / Description over eight cases, a rule above the header, "
       "one under it, one under every case row and a closing rule at the bottom, and no vertical "
       "rule anywhere - the only booktabs grid after Table 9. The steady-state column carries "
       "three equations per row in cases 1, 2 and 3 and a three-line fraction stack in case 8, "
       "whose H_n expression breaks across two display lines and ends the first line on a bare "
       "'+'. Case 5's condition 'gamma = -beta' contradicts its own description, which argues from "
       "the non-negativity of the parameters that beta = gamma = 0, and cases 4 and 6 carry the "
       "identical condition epsilon = phi with different conclusions. The same measured box holds "
       "the numbered case list that follows the grid - six items, each opening with a state "
       "equation such as 'In = 0 None' - which is why this region is 463.8 pt tall."),
      rule="booktabs", numeric=0, width="full",
      cap_text=cap(19, "Table 21: Fixed", "deterministic model"),
      mention=cited(18, 19, ["Table 21"], 1, "These are summarised in Table 21."))

figure(22, 1, "flowchart-or-schematic",
       cap(22, "Figure 7: A", "general model"), "Figure N:",
       cited(22, 22, ["Figure 7"], 1,
             "The state transition diagram would look like Figure 7."),
       "other", SEC_CONCL, numbers=False, labels=True, note=(
           "The p3 transition cartoon drawn again with ten numbered transitions where Figure 1 "
           "carries eight, and with no rate symbol printed against any of them - the extension is "
           "argued in the prose and never priced in the figure, so a reader cannot tell which of "
           "the ten arrows are new. State names are vector text (Birth, Healthy (Vulnerable), and "
           "so on) as in Figure 1. Caption below the art, and the next heading, '5.3 Conclusion', "
           "is welded onto the caption line in the text layer."))

_cap_fig2 = cap(10, "Figure 2: Comparison", "death count in each region")
_cap_fig3 = cap(11, "Figure 3: Comparison", "deterministic and stochastic models")
_cap_fig4 = cap(16, "Figure 4: Net", "treatment methods")
_cap_fig5 = cap(16, "Figure 5: Net", "treatment methods")
_cap_fig6 = cap(17, "Figure 6: Long", "of the overall virus")
_lead45 = ("The resulting short-term (six months) and medium-term (two years) plots are shown in "
           "Figure 4 and Figure 5 respectively.")

figure(10, 2, "line", _cap_fig2, "Figure N:",
       cited(10, 10, ["Figure 2"], 2, "Examples are provided in Figure 2."),
       "test", SEC_VALID, legend="inside", numbers=True, labels=True, note=(
           "Panel (a), Guinea, under a subcaption printed below the axes. WHO and the simulation "
           "bundle: the WHO series is heavy black crosses with no connecting line, the eight "
           "simulation runs are thin coloured polylines, and the legend inside the top left pairs "
           "the cross key with 'WHO' and the line key with 'Simulations', so here the keys do "
           "match the marks. The y axis runs 1,100 to 2,100 with no zero and the WHO crosses stop "
           "near day 84 while the lines run on to day 88. This panel is one of three measured "
           "boxes that carry one figure; the caption prints once, under the bottom row."))
figure(10, 3, "line", _cap_fig2, "Figure N:",
       cited(10, 10, ["Figure 2"], 2, "Examples are provided in Figure 2."),
       "test", SEC_VALID, legend="inside", numbers=True, labels=True, note=(
           "Panel (b), Liberia, drawn beside (a) at the same height. Same two mark types, same "
           "inside legend, same truncated y axis (2,800 to 3,800, no zero) and the same "
           "simulation run structure in eight colours; the WHO crosses again stop before the "
           "axis end. Run identity is carried by colour alone."))
figure(10, 4, "line", _cap_fig2, "Figure N:",
       cited(10, 10, ["Figure 2"], 2, "Examples are provided in Figure 2."),
       "test", SEC_VALID, panels=2, layout="1x2", legend="inside", numbers=True, labels=True,
       note=(
           "Two panels in one measured box: (c) Sierra Leone and (d) Overall, side by side under "
           "the row above, each with its own inside legend and its own truncated y axis (1,000 to "
           "3,500 and 5,000 to 9,500). Over roughly day 35 to 55 the WHO crosses sit clearly above "
           "the whole simulation bundle in (c) and (d) - the same divergence the prose calls a "
           "reasonably good track. The box's top edge also catches the subcaptions of (a) and (b), "
           "which is why a crop of it looks like it repeats panels that are not inside it. "
           "Caption below this row only, so the three measured boxes share one caption."))
figure(11, 2, "line", _cap_fig3, "Figure N:",
       cited(11, 11, ["Figure 3"], 2,
             "An example of this is illustrated in Figure 3."),
       "test", SEC_VALID, legend="inside", numbers=True, labels=True, note=(
           "One axes: about ten thin coloured stochastic replicates against one thick black "
           "deterministic trajectory, no markers, and two separate legend boxes in opposite "
           "corners - 'Stochastic' top right and 'Deterministic' bottom left - when one box would "
           "have done. The y axis is labelled with the bare state symbol 'In' rather than with the "
           "quantity the caption promises, and it runs 7,500 to 9,000 with no zero, so the "
           "fluctuation the caption attributes to the stochastic runs is all that a reader can "
           "measure. Every series stops at day 85 inside a 90-day axis."))
figure(16, 1, "scatter", _cap_fig4, "Figure N:",
       cited(15, 16, ["Figure 4"], 2, _lead45),
       "sensitivity", SEC_SENS, legend="inside", numbers=True, labels=True, note=(
           "Marker-only scatter, not a line plot: net six-month reduction in deaths against "
           "percentage increase in treatment, treatment type in the marker shape and country in "
           "the colour. The trap is the legend - the three country keys are drawn as short "
           "coloured line segments although no line is plotted anywhere, while the three "
           "treatment keys use the real marker glyphs, so a reader hunting for the green curve "
           "finds nothing to find. The black dashed reference line that crosses the field has no "
           "legend entry at all and is the only line in the panel. Markers at the origin sit on "
           "the x spine and are half clipped by it."))
figure(16, 2, "scatter", _cap_fig5, "Figure N:",
       cited(15, 16, ["Figure 5"], 2, _lead45),
       "sensitivity", SEC_SENS, legend="inside", numbers=True, labels=True, note=(
           "The two-year version of Figure 4 at four times the vertical scale, same marks, same "
           "inside legend and the same country-keys-drawn-as-lines flaw. The dashed reference "
           "line runs off the top of the axes at about 93 per cent treatment and is simply clipped "
           "there, so the panel hides the value it is drawing. Origin cluster sits on the spine "
           "again."))
figure(17, 1, "line", _cap_fig6, "Figure N:",
       cited(17, 17, ["Figure 6"], 1, "Results are shown in Figure 6."),
       "sensitivity", SEC_SENSDET, numbers=True, labels=True, note=(
           "Panel (a), infected, the left of three panels on one row; the identifier is the "
           "subcaption '(a) Infected' printed under the axes, so the panel has no title above it. "
           "One thick black sawtooth that grows and then rises away. The y label is the bare "
           "symbol I_n with a x10^5 multiplier at the top left and the x label 'Time [d]' carries "
           "a x10^4 multiplier, which puts the run at 60,000 days - about 164 years - and the "
           "plotted quantities far above the 7,690 infected that Table 11 reports. No legend."))
figure(17, 2, "line", _cap_fig6, "Figure N:",
       cited(17, 17, ["Figure 6"], 1, "Results are shown in Figure 6."),
       "sensitivity", SEC_SENSDET, panels=2, layout="1x2", numbers=True, labels=True, note=(
           "Two more panels in one measured box: (b) Immune in green rising to a plateau and (c) "
           "Vulnerable in red decaying to a constant, each with its subcaption under the axes and "
           "no legend. The three panels of Figure 6 are not comparable: the y multipliers differ "
           "per panel (10^5, 10^7, 10^7), (c) starts its axis at 2.2x10^7 with no zero while (a) "
           "and (b) start at zero, and (b)'s 1.8x10^8 immune people is roughly eight times the "
           "whole population the paper builds its model on. Panel widths are equal within one per "
           "cent, so the two-box split is the measurer's, not the author's."))

# PLACEHOLDER-FIGURES

RULES: list[str] = [
    "Width is measured against this paper's own 481.9 pt measure, and only six of the nineteen "
    "grids clear 75 per cent of it - Table 1 at 100.5, Table 2 at 75.8, Table 3 at 80.6, Table 4 "
    "at 81.1, Table 10 at 84.6 and Table 21 at 102.3 - while Table 11 at 73.2 is the widest that "
    "does not, and the ten sensitivity grids run from 58.6 to 65.6 [table.width].",
    "Rule style is read literally and splits the paper in two: nine grids are booktabs (Tables 1 "
    "to 5, 8, 9 and 21), ten are vertical-rules (Tables 10 to 20), none is boxed, and not one "
    "carries shading - the fill scan found no filled rectangle inside any of the nineteen regions, "
    "so zebra is false throughout [table.rule_style].",
    "Header depth is not what the geometry hints at: Tables 12 to 20 print two header rows, a "
    "span row of 6 Months / 1 Year / 2 Years over a leaf row in which the strings C and D repeat "
    "six times, while Table 10's two ratio columns are stacked fractions inside a single header "
    "row and Table 11's S and D subscripts are single letters [table.header_rows].",
    "Rows counts body rows only, never a header: Table 1 has six, Tables 2 to 5, 8, 9, 10 and 11 "
    "have four each, Tables 12 to 20 have three each because none of the sensitivity grids has an "
    "Overall row, and Table 21 has eight cases [table.rows].",
    "Two printed grids have no measured region at all. Tables 6 and 7 print on p8 with rules of "
    "their own - Table 6 at y=160.6, 174.6, 215.6 and 229.6 across 239.2 pt, Table 7 at y=464.1, "
    "478.0, 519.1 and 533.0 across 179.5 pt - and the measurer returned no region for either, so "
    "this census carries nineteen of the paper's twenty-one tables and declares the gap here "
    "instead of inventing rows or geometry for the missing two [place.page_order].",
    "Two measured boxes hold more than one panel, and the split is the measurer's, not the "
    "author's: p10 r4 holds panels (c) and (d) of Figure 2 and p17 r2 holds (b) and (c) of "
    "Figure 6, each recorded as one row with a panel count of two, while the three panels of "
    "Figure 6 are equal in width within one per cent [geometry.panel_count].",
    "Caption sides split without exception: all nineteen grids print their caption above the grid "
    "and all ten figure regions print theirs below the art. Where one figure spans several "
    "measured boxes the single caption is recorded on every box of that figure, because the paper "
    "numbers seven figures over ten boxes and no box carries a caption of its own [caption.position].",
    "Every caption on this paper uses the colon form, 'Table 12:' and 'Figure 2:', with no "
    "exception in twenty-nine captions, so numbering is uniform here where the papers before it "
    "in this lane were not [caption.numbering].",
    "Citation practice runs in groups: fifteen of the nineteen grids are cited once, Table 8 is "
    "cited twice, Table 9 three times, and three runs of grids are cited by one sentence apiece - "
    "'Table 13 and Table 14 respectively', 'Table 15, Table 16 and Table 17 respectively', "
    "'Table 18, Table 19, and Table 20'. Figures 4 and 5 are named on p15 for art that prints on "
    "p16, which is the only one-page "
    "forward lead in the paper; Table 21 is named on p18 for a grid printed on p19 [mention.lead_pages].",
    "Section paths follow the printed heading, not the index: heading 3.1.2 prints as an epsilon "
    "and a phi whose epsilon reaches the text layer as the private-use character 0x0f, so there is "
    "no spellable form of that label and the two p7 grids stop at '3.1 Model Parameters'; "
    "3.1.1, 3.1.4 and 5.3 are used even though the heading pass missed all three, since each is a "
    "printed line of the layer [place.section_path].",
    "The heading pass also invented ten headings out of table content - nine copies of '6 Months 1 "
    "Year 2 Years', one per sensitivity grid, plus '2000 Simulations 3700 Simulations' from "
    "Figure 2's legends, '1500 Liberia', '1000 Medical Services' and '500 Vaccine' from Figure 4's "
    "axis and legend, and '1 In = 0 None' from the case list under Table 21 - and those invented "
    "labels were the ctx section_path of ten regions, all replaced by hand here [place.section_path].",
    "Note sentences are quoted from the sentence that introduces the grid, and three of them do "
    "duty for three rows each, which is why Table 12 and Tables 13 to 20 share their introductory "
    "wording rather than each having its own [table.note_sentence].",
    "Area separates nothing on this paper. The largest region is the p19 box at 0.456 of the page, "
    "but that box is Table 21 plus the six-item case list printed under it, and the smallest is a "
    "0.039 sensitivity grid; between those extremes the eighteen grids of pp7-19 all fall in a "
    "0.039 to 0.057 band, so no threshold would have found the two missing tables [place.area_frac].",
    "Families come out of the page and not out of a label rule: nineteen table-grids, six line "
    "panels across Figures 2, 3 and 6, two scatter panels in Figures 4 and 5, and the two "
    "transition cartoons of Figures 1 and 7 [geometry.family].",
]

NOTE = (
    "Paper 74, Team 40764. Twenty-nine measured regions over fifteen of the twenty-five pages, all "
    "twenty-nine accounted for: ten figure regions, nineteen table regions, no exclusions at all "
    "and nothing left unresolved. That clean arithmetic hides the paper's one real gap - it prints "
    "twenty-one tables and the census carries nineteen, because Tables 6 and 7 print on p8 with "
    "rules of their own and produced no measured region. The gap is declared rather than filled.\n\n"
    "What the exhibits are. Six line panels carry Figure 2's four comparisons over three measured "
    "boxes, Figure 3's stochastic-against-deterministic overlay and Figure 6's three-panel "
    "long-term run over two boxes. Two scatter panels carry Figures 4 and 5. Two schematics carry "
    "the transition cartoons of Figures 1 and 7. Nineteen grids carry the rest: five parameter "
    "lists, three WHO data tables, two validation grids and nine sensitivity grids that are the "
    "same seven-column shape printed nine times.\n\n"
    "The tables fail in ways that matter to a reader. Table 4's Overall population reads 23,436,196 "
    "while its three country rows add to 23,435,196 - out by exactly one thousand - and only the "
    "rate columns add up. Table 9's Overall row cannot be an aggregate of anything: overall alpha "
    "5.0992e-10 and overall beta 8.2775e-3 both fall outside the range of the three country values "
    "above them, and the row is not even separated by a rule the way Tables 4, 5 and 8 separate "
    "theirs. Table 10's Overall row contradicts its own model columns (22,557 against 22,614 cases, "
    "9,041 against 8,990 deaths) while its WHO columns add exactly, and its overall sigma_C of 150 "
    "is smaller than Sierra Leone's 159. Table 11's Overall row contradicts all six of the columns "
    "it closes. In Table 3 the fourth row leaves the deterministic cell blank with no dash and no "
    "em rule, so an imbalance reads as a missing value. Table 8's mortality rate prints as a bare "
    "fraction with no unit, and Table 21 states case 5 as 'gamma = -beta' and then argues in the "
    "same cell from the non-negativity of the parameters that both are zero, gives cases 4 and 6 "
    "the same condition with different conclusions, and breaks its case-8 expression across two "
    "lines ending the first on a bare plus sign.\n\n"
    "The nine sensitivity grids carry a structural fault in common: none of them prints a top rule. "
    "Each begins on a bare span row of 6 Months / 1 Year / 2 Years with the leaf row under it "
    "reading only C, D, C, D, C, D, so the two column meanings are never expanded anywhere in the "
    "paper and the three time groups can only be told apart by the two internal dividers. The "
    "signing is inconsistent inside single rows - Sierra Leone prints '-10  +25' in Table 15, one "
    "explicit minus beside one explicit plus - and the case and death columns of one row differ by "
    "two to four orders of magnitude with no unit to say so.\n\n"
    "The figures are worse behaved than the tables. Figure 1 draws four state boxes and eight "
    "numbered transitions and leaves every rate symbol to Table 1, 100 pt below on the same page. "
    "Figure 2 is four panels - Guinea, Liberia, Sierra Leone and Overall - laid out over three "
    "measured boxes, with the bottom two sharing a box; in the Sierra Leone and Overall panels the "
    "WHO crosses sit clearly above the whole simulation bundle for about twenty days, which is the "
    "divergence the prose calls a reasonably good track, and every panel truncates its y axis below "
    "zero. Figure 3 puts two separate legends in opposite corners for one axes and labels its "
    "vertical axis with the bare state symbol 'In' instead of the quantity its caption promises. "
    "Figures 4 and 5 are the sharpest trap on the paper: they plot markers only, yet their three "
    "country legend keys are drawn as short coloured line segments, the actual line on the page is "
    "an unexplained black dashed reference with no legend entry, and in Figure 5 that line runs off "
    "the top of the axes and is clipped. Figure 6's three panels cannot be compared with one "
    "another - the y multipliers differ per panel, the third starts at 2.2x10^7 with no zero while "
    "the first two start at zero, and the second panel's 1.8x10^8 immune people is roughly eight "
    "times the whole population the model is built on. Figure 7 repeats the transition cartoon with "
    "ten numbered transitions where Figure 1 has eight, and prints no rate against any of them.\n\n"
    "The heading layer is the worst part of the machine. The pass that builds the section index "
    "harvested ten headings out of table content: nine copies of '6 Months 1 Year 2 Years', one per "
    "sensitivity grid, plus '2000 Simulations 3700 Simulations' from Figure 2's inside legends, "
    "'1500 Liberia', '1000 Medical Services' and '500 Vaccine' from Figure 4's axis and legend, and "
    "'1 In = 0 None' from the case list under Table 21. Those were the section_path of ten of the "
    "twenty-nine regions and all ten were replaced by hand from the printed headings. In the other "
    "direction the pass missed 3.1.1, 3.1.4 and 5.3, and it could never have indexed 3.1.2 at all, "
    "because that heading's epsilon reaches the text layer as the private-use character 0x0f and no "
    "spelling of the label matches it.\n\n"
    "Citation practice is grouped rather than per exhibit. Fifteen of the nineteen grids are cited "
    "once, Table 8 twice, Table 9 three times, and three runs of grids share one sentence apiece. "
    "Figures 4 and 5 are named a page before they print. Table 21 is named a page before it prints "
    "and then named again on the page after, so the paper's most complicated grid is its "
    "best-cited exhibit. The two grids it prints without giving the measurer anything to measure "
    "fare unevenly in the prose as well: Table 6 gets the six words 'This data is given in Table "
    "6.' and Table 7 is never named in the prose at all."
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
out = PROXY / "pc74-payload.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"payload: {len(ITEMS)} figures, {len(TABLES)} tables, {len(EXCLUDED)} excluded -> {out}")
