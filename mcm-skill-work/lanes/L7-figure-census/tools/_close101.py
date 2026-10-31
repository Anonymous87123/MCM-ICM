"""Close paper 101 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-C-2016-50193-615bc62f"

ROW = (
    "| 101 | P-C-2016-50193-615bc62f | mcm-9a | closed 2026-10-24 sha 615bc62f "
    "layout 11a3c96834466368 (figures=7 tables=7 excluded=1 unaccounted=0; 24 pages, 15 measured "
    "regions over 9 of them, resolving into SEVEN FIGURE ROWS, SEVEN TABLE ROWS and ONE EXCLUSION - the "
    "second panel of a two-panel figure - with nothing unaccounted; FIGURE 2'S CAPTION IS AN UNFILLED "
    "TEMPLATE, 'Figure 2: general title.', and both its panels carry the IDENTICAL sublabel '(a)/(b) "
    "Grey Predicting for Future ROI', so neither panel names its school, neither axis is named, and in "
    "panel (b) the observed point at 2012 sits at 0.026 while the fitted curve passes 0.043 there "
    "before forecasting to 2024; TABLE 6 CARRIES TABLE 1'S CAPTION WORD FOR WORD - 'Table 6: Missing "
    "data columns' over a list of fourteen institutions, three of which are Johnson Wales campuses - "
    "with no header row and an unlabelled rank and UNITID column; FIGURE 5 IS A PRINTED GRID NUMBERED "
    "AS A FIGURE, fifteen schools against 2016-2020 under 'Investment in year i' with a foot row 'sum of "
    "the money in the year' THAT IS OFF BY A FACTOR OF TEN (the 2016 column's printed values sum to "
    "about 100.3 million while its foot cell reads 10000000) and the five foot cells sum to "
    "100,000,000 against the 1,000,000,000 the model says it distributes; THE TWO SENSITIVITY CURVES "
    "DISAGREE ABOUT ONE QUANTITY - Figure 6 caps max return at 5.5 x 10^7 and flattens completely past "
    "a risk of 0.85, Figure 7 peaks at 1.75 x 10^8 at twelve schools and declines, and no sentence "
    "reconciles them, while the peak is read off as validating a constraint that already excludes "
    "everything outside 10 to 30; FIGURE 1 DRAWS THE ROI SYSTEM AS A NETWORK IN THREE REGISTERS - eight "
    "weighted arrows labelled w1 to w8 feed three sums but the Input branch runs through an EMPTY CIRCLE "
    "with no sum sign and the urgency edge into the final sum is labelled a^-1 rather than w - and its "
    "label 'Enhance' is defined by no equation in the paper; FIGURES 3 AND 4 CANNOT BE READ WITHOUT "
    "TABLE 6, since both label their fourteen categories with bare UNITIDs, and the pie's own "
    "percentages sum to 96 while the single risk bar of school 446604 stands at 2.26 against every other "
    "value on the same axis below 0.95; TABLES 1 AND 2 ARE ONE SHAPE TWICE - two side-by-side blocks of "
    "'Number | Variable Name', four physical columns, the header wording repeated, no rule between body "
    "rows and no outer edge rule - and Table 1 mixes two registers in one list while Table 2 is entirely "
    "raw, still carrying the literal mask 'XXXXX' in two entries; TABLES 4 AND 5 PRINT NO HEADER ROW AT "
    "ALL (header_rows held at the schema floor of 1 and the deviation stated in each note), Table 4 is "
    "captioned 'constant' although ROI_i and r_i vary per school, and Table 5's y_i gloss defines zero "
    "twice and one not at all ('not the the prize list' against 'not in the recommendation list'); Table "
    "3's cluster sizes are 27, 5, 1151, 1499 and 11 with no total and no statement that 'Size' counts "
    "schools; Table 7 indexes four policies as bare 1 to 4 with a dash in the fourth gap cell; six "
    "figure rows are named by a sentence but only four by number, Figure 1 as 'a picture' and Figure 2 "
    "as 'figures', Figure 5 by none, and Tables 4 to 7 by none; families table-grid 7, line 3, bar 1, "
    "node-link-network 1, other 1, table-as-figure 1) |"
)

READ = (
    "| 101 | P-C-2016-50193-615bc62f | 24 | 15 | 7 | 7 | closed, `check.py` layout identical, "
    "unaccounted 0; 15 measured regions over 9 of 24 pages resolving into 7 figure rows, 7 tables and 1 "
    "exclusion (the second panel of a two-panel figure); Figure 2's caption is the unfilled placeholder "
    "'Figure 2: general title.' and both panels share the sublabel 'Grey Predicting for Future ROI'; "
    "Table 6 reuses Table 1's caption over a list of fourteen institutions; Figure 5 is a printed "
    "five-year allocation grid numbered as a figure whose foot row is a tenth of the values above it and "
    "whose total is a tenth of the stated budget; Figures 6 and 7 disagree by a factor of three about "
    "one maximand; Figure 1 is a weighted network with an empty sum node and one a^-1 edge; Figures 3 "
    "and 4 label their categories with bare UNITIDs taken from Table 6, and the pie's percentages sum to "
    "96; Tables 4 and 5 print no header row and hold header_rows at the schema floor 1; Tables 4 to 7 "
    "and Figure 5 are named by no sentence |"
)

prefix = f"| 101 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 101 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
