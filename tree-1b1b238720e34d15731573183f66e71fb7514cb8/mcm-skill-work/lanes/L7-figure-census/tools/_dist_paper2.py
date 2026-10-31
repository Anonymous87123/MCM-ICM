"""Paper 2 distillation rows: every measured region read off its crop.

Paper A-7571 is the parametric-scan paper: one bat model, then one exhibit per sweep
(preference coefficient, mass, swing speed, cork length, rubber length, wall
thickness). That shape decides almost every field here, and it is why the table
families are all the same booktabs one-row strip.

Judgement calls the crops forced:

- Tables 6-10 and 13 are one-row booktabs strips that repeat the header "Length of
  cork 0 5 10 15 20". Each is a separate table (own number, own stub), not a fragment
  of one long table; the regions that really are page breaks (Table 2's tail, Table
  4's data rows, Table 10's v2 row, Table 12's wrapped label, Table 15's last rows)
  are excluded with a reason.
- Table 3 (p13) is the only framed table: dashed column separators inside a heavy
  double frame. Everything else is booktabs.
- Figure 1 is hand-drawn ink, not a diagram: no axes, no boxes, family "other".
- Figure 11 is a colour photograph of a sawn-open bat, the paper's only raster.
- No figure here is 3D and none carries a colour bar. Figure 6 (nine curves) is the
  only figure whose legend names more than three series.

Sentences are cut out of the text layer by span(), never retyped.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))

import schema  # noqa: E402

PID = "P-A-2010-7571-1ac2a627"
SKEL = LANE / ".proxy" / f"{PID}-skel.json"
CTX = LANE / ".proxy" / f"{PID}-ctx.json"


def span(page: int, start: str, end: str) -> str:
    for unit in schema.page_units(PID, page):
        i = unit.find(start)
        if i < 0:
            continue
        j = unit.find(end, i)
        if j < 0:
            continue
        return unit[i:j + len(end)]
    raise SystemExit(f"no span {start!r} .. {end!r} on page {page}")


def cap(page: int, number: int) -> str:
    """The caption line for one numbered exhibit.

    A page can carry a sentence that merely starts with "Figure 19 and Figure 20", so
    candidates naming a second exhibit are dropped and the shortest survivor wins.
    """
    ctx = json.loads(CTX.read_text(encoding="utf-8"))
    hits = [c["text"] for c in ctx["captions"]
            if c["page"] == page and c["number"] == number]
    clean = [h for h in hits if len(re.findall(r"(?:figure|table)", h, re.I)) == 1]
    pool = clean or hits
    if not pool:
        raise SystemExit(f"no caption {number} on page {page}")
    return min(pool, key=len)


def fig(fam, panels, layout, legend, printed, labels, pattern, first, count, read,
        lead=None, trail=None, position="below", units=False, vars_=0, cond=False,
        concl=False, note=""):
    return dict(fam=fam, panels=panels, layout=layout, legend=legend, cbar=False,
                printed=printed, labels=labels, position=position, units=units,
                vars=vars_, cond=cond, concl=concl, pattern=pattern, first=first,
                count=count, read=read, lead=lead, trail=trail, note=note)


FIG = {
    1: fig("other", 1, "1", "none", False, False, "none", None, 0, 0,
           note="hand-drawn ink illustration of a batter with swing arcs and a red "
                "pivot-point circle; no axes, no boxes"),
    2: fig("flowchart-or-schematic", 2, "1x2", "none", False, True, "as-shown-in", 7, 1, 0,
           lead=span(7, "The force analysis is shown as follows", "follows:"),
           note="free-body bat with F, M, d, c, CM and P points, two panels"),
    3: fig("flowchart-or-schematic", 2, "1x2", "none", False, True, "none", None, 0, 1,
           trail=span(8, "Since the acceleration at point O", "of accelerations"),
           note="bat and ball before and after collision, v1/w1 then v2/w2"),
    4: fig("flowchart-or-schematic", 1, "1", "none", False, True, "none", None, 0, 1,
           trail=span(10, "The mass of the bat can be calculated as:", "calculated as:"),
           note="L_cm, L1, L2, d, c, b dimension lines over a two-cylinder bat"),
    6: fig("line", 1, "1", "inside", True, False, "as-shown-in", 12, 1, 1,
           lead=span(12, "Using the Matlab software", "shown in Figure 5"),
           units=True, vars_=2, cond=True,
           note="three index curves over b/cm, boxed legend naming comfort index, "
                "velocity index and objective function"),
    9: fig("line", 1, "1", "inside", True, False, "parenthetical", 14, 1, 1,
           lead=span(14, "(shown in Figure 6)", "(shown in Figure 6)"),
           trail=span(14, "From Figure 6, we find", "relatively concentrated."),
           vars_=2, cond=True,
           note="nine marker series, one per preference coefficient 0.1-0.9, boxed "
                "legend upper right"),
    10: fig("line", 1, "1", "none", True, False, "figure-n-shows", 14, 1, 1,
            lead=span(14, "Figure 7 is used to show", "varies."),
            trail=span(15, "Locations of Sweet Spots vary", "length of 4cm"),
            vars_=2, concl=True,
            note="single rising curve of sweet-spot location against lambda"),
    11: fig("line", 1, "1", "none", True, False, "parenthetical", 15, 1, 1,
            lead=span(15, "(shown in Figure 8)", "(shown in Figure 8)"),
            trail=span(16, "This influence of it is so slight", "can be ignored."),
            vars_=2,
            note="near-linear curve with a slope break, b/cm against change rate of mass"),
    12: fig("line", 1, "1", "none", True, False, "none", 16, 1, 1,
            trail=span(16, "we can safely say", "stays stable"), vars_=2,
            note="straight rising line, exit velocity against change rate of mass"),
    14: fig("line", 1, "1", "inside", True, False, "as-shown-in", 17, 2, 1,
            lead=span(17, "The influence on the exit velocity:", "swing speed."),
            trail=span(18, "The location of the Sweet Spot stays stable",
                       "swing speed varies."),
            vars_=3, cond=True,
            note="three humped curves, legend -10% / 0 / +10% swing speed, boxed "
                 "upper right"),
    16: fig("photo-or-raster-image", 1, "1", "none", False, False, "none", None, 0, 0,
            note="colour photograph of a sawn-open Louisville Slugger bat on grass, "
                 "the only raster in the paper"),
    17: fig("flowchart-or-schematic", 1, "1", "none", False, True, "none", 19, 1, 1,
            trail=span(19, "Then, the mass of the corked bat decreases to:",
                       "decreases to:"),
            note="stepped-cylinder bat with L_cm, L1, L2, d, c, b, r, R and a dashed "
                 "cork cavity"),
    23: fig("line", 1, "1", "none", True, False, "none", 22, 1, 1,
            trail=span(23, "The exit speed of an uncorked bat", "decreases by 0.72%."),
            vars_=2,
            note="single descending curve, sweet-spot location against cork length"),
    24: fig("line", 1, "1", "none", True, False, "none", 23, 1, 1,
            trail=span(23, "The longer the cork is", "exit speed will be."),
            vars_=2, concl=True,
            note="single descending curve, exit speed against cork length"),
    26: fig("line", 1, "1", "none", True, False, "none", 24, 1, 1,
            trail=span(24, "The length from the most", "in an uncorked bat"),
            vars_=2, concl=True,
            note="curve dipping near x=15 then rising, comfortable hitting point"),
    27: fig("line", 1, "1", "none", True, False, "as-shown-in", 24, 2, 1,
            lead=span(24, "When x=0", "and Table 13:"), vars_=2,
            note="two near-flat lines marking the upper and lower sweet-zone limits; "
                 "no legend, the pair is identified by the caption"),
    29: fig("flowchart-or-schematic", 1, "1", "none", False, True, "direct", 26, 1, 1,
            lead=span(26, "We simplify the shape of an aluminum bat", "different diameters"),
            note="hollow-cylinder aluminum bat with L_cm, L1, L2, r, R and wall t"),
    30: fig("line", 1, "1", "inside", True, False, "as-shown-in", 27, 2, 1,
            lead=span(27, "We substitute the parameters", "and Table 14."),
            vars_=3, note="three peaking curves, boxed legend lower centre"),
    32: fig("line", 1, "1", "none", True, True, "as-shown-in", 29, 2, 1,
            lead=span(29, "Consider the length of Sweet Zone", "Figure 20:"),
            vars_=2, concl=True,
            note="inverted-U with a 0.85 cut-off line and arrowed labels 46.09 / 53.87, "
                 "wooden bat"),
    33: fig("line", 1, "1", "none", True, True, "as-shown-in", 29, 2, 1,
            lead=span(29, "Consider the length of Sweet Zone", "Figure 20:"),
            vars_=2, concl=True,
            note="same inverted-U shape as Figure 19, arrowed labels 43.95 / 52.77, "
                 "aluminum bat"),
    35: fig("line", 1, "1", "none", True, False, "none", 30, 2, 1,
            trail=span(31, "The location of Sweet Spot stays stable", "change of t."),
            vars_=2, concl=True,
            note="straight descending line, exit velocity against change of wall "
                 "thickness"),
}

TABLE = {
    5: dict(cappage=11, capnum=1, first=11, count=1, read=1,
            lead=span(11, "a set of data is shown as follows", "follows:"), trail=None,
            table=dict(rows=2, cols=7, header_rows=1, rule_style="booktabs", zebra=False,
                       merged_cells=False, diagonal_header=False, units_in_header=False,
                       decimal_aligned=True, numeric_cols=6, text_cols=1, width="full",
                       orientation="portrait", continued=False, note_sentence=""),
            note="two-line table: a header row of impact positions 12.7-25.4 under "
                 "'68.2-b', one row of e values under a dashed rule"),
    7: dict(cappage=12, capnum=2, first=12, count=1, read=1,
            lead=span(12, "Using the Matlab software", "Table 2"), trail=None,
            table=dict(rows=5, cols=5, header_rows=1, rule_style="booktabs", zebra=False,
                       merged_cells=False, diagonal_header=False, units_in_header=True,
                       decimal_aligned=True, numeric_cols=5, text_cols=0, width="full",
                       orientation="portrait", continued=True, note_sentence=""),
            note="b(cm), E_batter, E_ball, v2(cm/s), f; four data rows run onto p13"),
    8: dict(cappage=13, capnum=3, first=13, count=1, read=1,
            lead=span(13, "The contrast between hitting", "shown in Table 3."), trail=None,
            table=dict(rows=3, cols=4, header_rows=1, rule_style="vertical-rules",
                       zebra=False, merged_cells=False, diagonal_header=False,
                       units_in_header=True, decimal_aligned=False, numeric_cols=3,
                       text_cols=1, width="full", orientation="portrait", continued=False,
                       note_sentence=""),
            note="the paper's only framed table: heavy double frame with dashed "
                 "vertical column rules, sweet point against end of bat"),
    13: dict(cappage=16, capnum=4, first=16, count=1, read=1, lead=None,
             trail=span(17, "Hence, in order to obtain higher exit velocity", "heavier bat"),
             table=dict(rows=4, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=True,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=True, note_sentence=""),
             note="header band on p16, three data rows on p17, units in the header"),
    15: dict(cappage=18, capnum=5, first=18, count=1, read=1,
             lead=span(18, "The relation between swing speed", "shown in Table 5"),
             trail=None,
             table=dict(rows=4, cols=3, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=True,
                        decimal_aligned=False, numeric_cols=2, text_cols=1, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="swing speed change against exit speed, units written inside the "
                  "header cells"),
    18: dict(cappage=21, capnum=6, first=21, count=1, read=1,
             lead=span(21, "Mass of the bat:", "Mass of the bat:"), trail=None,
             table=dict(rows=2, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="one-row strip: stub 'Mass of bat' against cork length 0-20"),
    19: dict(cappage=21, capnum=7, first=21, count=1, read=1,
             lead=span(21, "Length from the center of mass to the pivot", "to the pivot"),
             trail=None,
             table=dict(rows=2, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="same strip layout as Table 6; stub wraps to three lines"),
    20: dict(cappage=21, capnum=8, first=21, count=1, read=1,
             lead=span(21, "Moment of inertia to the center of mass", "( J o )"),
             trail=None,
             table=dict(rows=2, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="same strip layout, stub is the italic symbol J_o"),
    21: dict(cappage=22, capnum=9, first=22, count=1, read=1, lead=None, trail=None,
             table=dict(rows=2, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="same strip layout, stub 'Swing speed'"),
    22: dict(cappage=22, capnum=10, first=22, count=1, read=1,
             lead=span(22, "Influence on the location of the Sweet Spot", "the Sweet Spot"),
             trail=span(23, "The exit speed of an uncorked bat", "decreases by 0.72%."),
             table=dict(rows=3, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=True, note_sentence=""),
             note="stub b on p22, stub v2 on p23 with the header repeated"),
    25: dict(cappage=23, capnum=12, first=23, count=1, read=1,
             lead=span(23, "Influence on the comfort index", "the comfort index"),
             trail=span(24, "It suggests that a batter", "closer to his hands"),
             table=dict(rows=2, cols=6, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=True, numeric_cols=5, text_cols=1, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="stub 'The most comfortable hitting point' wraps onto p24 where only "
                  "the wrapped label and the closing rule survive"),
    28: dict(cappage=25, capnum=13, first=24, count=1, read=1,
             lead=span(24, "When x=0", "and Table 13:"), trail=None,
             table=dict(rows=6, cols=4, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=False,
                        decimal_aligned=False, numeric_cols=4, text_cols=0, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="X against lower limit, upper limit and span of the sweet zone"),
    31: dict(cappage=28, capnum=14, first=27, count=1, read=1,
             lead=span(27, "We substitute the parameters", "and Table 14."), trail=None,
             table=dict(rows=4, cols=5, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=True,
                        decimal_aligned=True, numeric_cols=5, text_cols=0, width="full",
                        orientation="portrait", continued=False, note_sentence=""),
             note="the five columns of Table 2 again, units in the header"),
    34: dict(cappage=30, capnum=15, first=30, count=1, read=1,
             lead=span(30, "The sensitivity analysis of the wall thickness", "wall thickness"),
             trail=span(31, "The location of Sweet Spot stays stable", "change of t."),
             table=dict(rows=6, cols=4, header_rows=1, rule_style="booktabs", zebra=False,
                        merged_cells=False, diagonal_header=False, units_in_header=True,
                        decimal_aligned=True, numeric_cols=4, text_cols=0, width="full",
                        orientation="portrait", continued=True, note_sentence=""),
             note="three rows on p30, two tail rows and the closing rule on p31 with no "
                  "repeated header"),
}

# (page, bbox, reason, note): the page-break tails, keyed by the measured region
EXCLUDED = [
    (13, [83.9, 79.6, 510.8, 195.6], "split-across-pages",
     "final four data rows of Table 2; header and first row stand on p12"),
    (17, [83.9, 79.6, 510.8, 185.5], "split-across-pages",
     "three data rows of Table 4 whose header band is the p16-r3 region"),
    (23, [83.9, 79.6, 510.8, 174.6], "split-across-pages",
     "v2 row of Table 10 with its header repeated; the table's own region is on p22"),
    (24, [83.9, 79.6, 510.8, 115.0], "split-across-pages",
     "wrapped second line of the Table 12 stub plus its closing rule"),
    (31, [115.6, 82.0, 479.0, 139.2], "split-across-pages",
     "two tail rows and the closing rule of Table 15, header not repeated"),
]

RULES = [
    "参数扫描题的每个自变量单独一图，图名只给编号，变量名留给正文第一句 "
    "[caption.variables]",
    "曲线图的引出句把自变量和因变量一起写出来，再补一句 shown in Figure N 或括号回指 "
    "[mention.lead_pattern]",
    "同一自变量的兄弟图共享一套刻度，图内不写标题只写轴名，图注只写 Figure N "
    "[geometry.shared_axes]",
    "扫描表一律做成单行 booktabs 条带，表头重复写出自变量 0 5 10 15 20，纵向只放一个被"
    "扫的量 [table.rule_style]",
    "只有要跟另一对象对照时才加竖线框，普通数据表不加 [table.rule_style]",
    "单位进表头（b (cm)、v2 (cm/s)），单行条带表才把单位留在正文 [table"
    ".units_in_header]",
    "数值列按小数点对齐，整数刻度行居中，不整列右对齐 [table.decimal_aligned]",
    "表跨页时下一段把表头重写一遍，不写续表字样 [table.continued]",
    "机理图一律无刻度：只画尺寸字母、质心点和外力箭头 [geometry.printed_numbers]",
    "结论型附图把关键数值直接标在图上（46.09 / 53.87），正文不再复述这两个数 "
    "[geometry.data_labels]",
    "灵敏度小节先表后图：先给扫描表，再给同数据的曲线 [place.page_zone]",
    "题注全部在图下方且不超过一行；解释写进正文，不写进题注 [caption.concludes]",
]


def numbering_of(text: str) -> str:
    if not text:
        return "none"
    for pattern, label in (
            (r"^Figure\s+\d+\s*:", "Figure N:"), (r"^Figure\s+\d+\s*\.", "Figure N."),
            (r"^Figure\s+\d+(\s|$)", "Figure N"), (r"^Table\s+\d+\s*:", "Table N:"),
            (r"^Table\s+\d+\s*\.", "Table N."), (r"^Table\s+\d+(\s|$)", "Table N")):
        if re.match(pattern, text.strip()):
            return label
    return "none"


def caption_block(text: str, position: str, units: bool, vars_: int, cond: bool,
                  concl: bool) -> dict:
    parts = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    return {"verbatim": text, "numbering": numbering_of(text),
            "words": len(schema.words(text)), "sentences": max(1, len(parts)),
            "units": units, "variables": vars_ > 0, "variable_count": vars_,
            "conditions": cond, "concludes": concl, "voice": "none",
            "position": position}


def main() -> None:
    skel = json.loads(SKEL.read_text(encoding="utf-8"))
    by_order = {e["doc_order"]: e for e in skel}
    items, tables, excluded = [], [], []
    for order, entry in sorted(FIG.items()):
        base = by_order[order]
        number = int(re.search(r"(\d+)", base["caption_verbatim"]).group(1))
        ctext = cap(base["page"], number)
        style = [f"Figure {number}"]
        items.append({
            "page": base["page"], "bbox": base["bbox"], "family": entry["fam"],
            "confidence": "high", "panel_count": entry["panels"], "table": False,
            "caption_verbatim": ctext, "caption_source": "text-layer", "excluded": None,
            "other_note": entry["note"] if entry["fam"] == "other" else None,
            "note": entry["note"],
            "place": {"section_path": base["section_path"],
                      "section_numbered": base["section_numbered"],
                      "section_kind": base["section_kind"],
                      "doc_order": base["doc_order"], "page_order": base["page_order"],
                      "page_zone": base["page_zone"], "area_frac": base["area_frac"],
                      "solo_page": base["solo_page"]},
            "mention": {"first_page": entry["first"],
                        "lead_pages": None if entry["first"] is None
                        else base["page"] - entry["first"],
                        "style": style if entry["count"] else [],
                        "count": entry["count"],
                        "lead_sentence": entry["lead"] or "",
                        "trail_sentence": entry["trail"] or "",
                        "lead_pattern": entry["pattern"],
                        "read_sentences": entry["read"],
                        "gap_sentences": base["gap_auto"]},
            "caption": caption_block(ctext, entry["position"], entry["units"],
                                     entry["vars"], entry["cond"], entry["concl"]),
            "geometry": {"family": entry["fam"], "panel_count": entry["panels"],
                         "panel_layout": entry["layout"], "shared_axes": False,
                         "legend": entry["legend"], "colorbar": entry["cbar"],
                         "three_d": "no", "printed_numbers": entry["printed"],
                         "data_labels": entry["labels"]},
        })
    for order, entry in sorted(TABLE.items()):
        base = by_order[order]
        ctext = cap(entry["cappage"], entry["capnum"])
        num = re.search(r"(\d+)", ctext).group(1)
        tables.append({
            "page": base["page"], "bbox": base["bbox"], "family": "table-grid",
            "caption_verbatim": ctext, "caption_source": "text-layer",
            "note": entry["note"],
            "place": {"section_path": base["section_path"],
                      "section_numbered": base["section_numbered"],
                      "section_kind": base["section_kind"],
                      "doc_order": base["doc_order"], "page_order": base["page_order"],
                      "page_zone": base["page_zone"], "area_frac": base["area_frac"],
                      "solo_page": base["solo_page"]},
            "mention": {"first_page": entry["first"],
                        "lead_pages": None if entry["first"] is None
                        else base["page"] - entry["first"],
                        "style": [f"Table {num}"] if entry["count"] else [],
                        "count": entry["count"],
                        "lead_sentence": entry["lead"] or "",
                        "trail_sentence": entry["trail"] or "",
                        "lead_pattern": "direct" if entry["lead"] else "none",
                        "read_sentences": entry["read"],
                        "gap_sentences": base["gap_auto"]},
            "caption": caption_block(ctext, "above", False, 0, False, False),
            "table": dict(entry["table"]),
        })
    for page, bbox, reason, note in EXCLUDED:
        excluded.append({"page": page, "bbox": bbox, "reason": reason, "note": note})

    payload = {
        "paper": PID,
        "layout_sha256": json.loads(
            (LANE / "layout" / f"{PID}.json").read_text(encoding="utf-8"))["layout_sha256"],
        "items": items, "tables": tables, "excluded_regions": excluded,
        "rules": RULES,
        "note": "parametric-scan paper: min bare captions, booktabs strips, page-break "
                "tails excluded",
    }
    out = LANE / ".proxy" / f"{PID}-payload.json"
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"items {len(items)} tables {len(tables)} excluded {len(excluded)} -> {out}")
    for block in items + tables:
        for key in ("lead_sentence", "trail_sentence"):
            value = block["mention"][key]
            if value and len(schema.words(value)) > schema.MAX_QUOTE_WORDS:
                print("  over cap:", block["place"]["doc_order"], key,
                      len(schema.words(value)),
                      value[:70].encode("ascii", "replace").decode())


if __name__ == "__main__":
    main()
