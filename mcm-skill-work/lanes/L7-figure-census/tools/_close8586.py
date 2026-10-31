"""Close papers 85 and 86 in CLAIMS.md, the recovery file and the README progress table.

Paper 85's row was reverted a fourth time by a peer `git checkout HEAD -- CLAIMS.md`, so both rows
are rewritten here from scratch: an existing row with the same number and pid is replaced, never
duplicated.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]

ROW_85 = (
    "| 85 | P-D-2015-34985-c7be0d8b | mcm-9a | closed 2026-10-24 sha cf71e1c0e57d7da0 "
    "(figures=11 tables=3 excluded=0 unaccounted=0; 20 pages, 14 measured regions over 12 of them, "
    "nothing refused, because every region is a framed pasted chart or a ruled grid and this paper "
    "has none of the page-wide vector prose bands that wrecked 72 and 73; families line 2, "
    "map-or-plan-view 2, heatmap-or-contour 2, node-link-network 2, composite-panel 2, bar 1, "
    "table-grid 3; THE PAPER PRINTS NO NUMBERED TABLE AT ALL - 'Table' never appears in the text "
    "layer, and all three grids take their names from a title row inside the box or from the "
    "appendix heading above it; the summary sheet repeats Figure 6's function map unnumbered and "
    "uncited; Figure 5 is two measured regions under one caption, its (b) half subcaptioned "
    "'Trended' while the caption calls the seed 'biased'; caption glyph runs lose every space on "
    "pp7 and p12 so those two verbs are typed from the crops; Figure 2 has no y axis at all, "
    "Figure 8 prints each alpha twice with a mismatched swatch, Figure 9 has no axis titles or y "
    "numbers, and Figures 1 and 3 key their classes with 'Low'/'High' and no numbers; Figure 6's "
    "caption is set inside a sentence; four of nine figures never cited) |"
)

ROW_86 = (
    "| 86 | P-D-2015-35780-97fea85b | mcm-9a | closed 2026-10-24 sha 2d875a4dd64aa1a1 "
    "(figures=14 tables=6 excluded=1 unaccounted=0; 24 pages, 21 measured regions over 14 of them; "
    "families line 10, flowchart-or-schematic 3, heatmap-or-contour 1, table-grid 6; the one "
    "exclusion is the summary sheet's T1-T4/F1-F4 fill-in rules, one 0.77-area vector cluster "
    "because the form rules span the page; EIGHT OF THE FOURTEEN FIGURES ARE TWO-COLUMN PAIRS "
    "pasted as separate bitmaps (3+4 on p12, 5+6 on p13, 7-10 on p17, 11+12 on p18), so each half "
    "is its own region and its own row, and the text layer INTERLEAVES the two captions of every "
    "pair into one run ('Figure 3: Forecast on comprehensive Figure 4: The GE-Matrix for "
    "sustainability of performances of three countries three countries'), so all eight of those "
    "captions are typed from the crops; TABLE 2 IS A DECLARED GAP - it prints on p9 as a plain "
    "text grid with no rules at all, owns no measured region, and is the paper's most-cited grid "
    "(twice) while Table 1, which is drawn and measured, is cited never; Figure 14's caption "
    "promises a 'two dimensional concentration distribution under Gaussian model' and the art is a "
    "one-dimensional D_12-against-eta profile of about ten straight-interpolated points cusping to "
    "zero; Figure 13's y axis is titled only 'Item' and marks no perturbation the caption promises; "
    "Figures 7-10 are four panels on four different y windows (0.0260-0.0270, 0.022-0.032, "
    "0.0260-0.0270, 0.024-0.029) with inline end labels only, Figure 9 prints seven labels for at "
    "most six curves with two floating mid-plot, and Figure 7's y title reads 'Development "
    "Index(DJ)'; Figures 5 and 6 print a summing junction with no polarity on any input, so the "
    "feedback subtraction is invisible; Figure 2 shades nine blocks in four fills with no key and "
    "numbers them I-IX half a cell off the blocks they name; Table 5 prints 'Transferring the "
    "obtrusive industries to the industrial towns' twice at 0.13 and 0.19, Table 7 prints c1 as "
    "0.05 in all four periods and b3's row with no numbers, Table 1 prints 'Pullotion' and files "
    "the food-deficit indicator under Education, Table 3 loses the country names of ranks 4 and 10 "
    "out of their cells to the end of the text layer) |"
)

READ_85 = (
    "| 85 | P-D-2015-34985-c7be0d8b | 20 | 14 | 11 | 3 | closed, `check.py` layout identical, "
    "unaccounted 0; 14 measured regions over 12 of 20 pages = 11 figure rows + 3 grids, nothing "
    "refused; no numbered table exists - 'Table' never appears in the text layer and all three "
    "grids are named by an in-grid title row or the appendix heading; the summary sheet repeats "
    "Figure 6's function map unnumbered and uncited; Figure 5 is two regions under one caption, its "
    "(b) half subcaptioned 'Trended' while the caption calls the seed 'biased'; caption glyph runs "
    "lose every space on pp7 and p12 so those two verbs are typed from the crops; Figure 2 has no y "
    "axis at all, Figure 8 prints each alpha twice with a mismatched swatch, Figure 9 has no axis "
    "titles or y numbers, and Figures 1 and 3 key their classes with 'Low'/'High' and no numbers; "
    "four of nine figures never cited |"
)

READ_86 = (
    "| 86 | P-D-2015-35780-97fea85b | 24 | 21 | 14 | 6 | closed, `check.py` layout identical, "
    "unaccounted 0; 21 measured regions over 14 of 24 pages = 14 figure rows + 6 grids + 1 exclusion "
    "(the summary sheet's fill-in rules, one 0.77-area vector cluster); eight of the fourteen "
    "figures are two-column pairs pasted as separate bitmaps so each half is its own row, and the "
    "text layer interleaves every pair's two captions into one run, so those eight captions are "
    "typed from the crops; Table 2 is a declared gap - printed on p9 as a plain text grid with no "
    "rules, no measured region, and cited twice while Table 1, drawn and measured, is cited never; "
    "Figure 14's caption promises a 2-D Gaussian concentration distribution and the art is a 1-D "
    "cusp; Figure 13's y axis is titled only 'Item'; Figures 7-10 sit on four different y windows "
    "with inline end labels only, Figure 9 prints seven labels for at most six curves, Figure 7's y "
    "title reads 'DJ'; Table 5 prints one activity twice with two scores, Table 7 gives c1 a "
    "constant 0.05 and b3 no numbers at all |"
)


def upsert(path: Path, prefix: str, row: str) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(row)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    return len(kept)


claims = LANE / "CLAIMS.md"
recovery = LANE / "CLAIMS-rows-mcm-9a.md"
for number, pid, row in ((85, "P-D-2015-34985-c7be0d8b", ROW_85),
                         (86, "P-D-2015-35780-97fea85b", ROW_86)):
    prefix = f"| {number} | {pid} |"
    print("claims rows", upsert(claims, prefix, row))
    print("recovery rows", upsert(recovery, prefix, row))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
for number, pid, read in ((85, "P-D-2015-34985-c7be0d8b", READ_85),
                          (86, "P-D-2015-35780-97fea85b", READ_86)):
    rows = [line for line in rows if not line.startswith(f"| {number} | {pid} |")]
    idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
    rows.insert(idx, read)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("readme rows", len(rows))
