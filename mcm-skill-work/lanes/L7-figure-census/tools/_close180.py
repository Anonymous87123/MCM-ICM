"""Close paper 180 in CLAIMS.md, the recovery file and the README progress table."""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

LANE = Path(__file__).resolve().parents[1]
PID = "P-E-2019-1902029-f44b44ca"

ROW = (
    "| 180 | P-E-2019-1902029-f44b44ca | mcm-9a | closed 2026-10-24 sha f44b44ca "
    "layout d85eb24d3f03559c (figures=23 tables=2 excluded=0 unaccounted=0; 28 pages, running header "
    "'Team # 1902029 Page N of 25', 25 measured regions over 16 pages and every one an exhibit, so 23 "
    "figure rows + 2 table rows with nothing refused; THE CENSUS IS MOSTLY TABLES - eleven figure rows "
    "are printed grids carrying a figure number (Figure 2 a fourteen-column coefficient grid with two "
    "header bands, Figure 3 fourteen provinces by nine columns, Figure 6 a six-band classification strip "
    "ruled only by colour fills, Figure 10 one row of seven values, and the whole appendix block Figures "
    "17-23), and a twelfth figure, Figure 16, is CAPTIONED 'The table of Different ecosystem importance "
    "levels' over a six-series line chart; ONLY TWO OF THE 25 REGIONS ARE LIVE TEXT - Table 1 (p5) and "
    "Table 2 (p14) are three-path vectors and every other region is a single-path raster, so 23 exhibits "
    "including all seven appendix tables were pasted in as images; ONE QUANTITY PRINTS IN FOUR UNIT "
    "SYSTEMS ('Billion yuan' in Figure 3's caption, '*10^8 Yuan' on Figure 4's axes, '10^4 yuan/hm^2' on "
    "Figure 5's ordinate against 'yuan/km2' in the prose that reads it, 'Million Yuan' in Figure 19, "
    "'ESV/10^12 Yuan' in Figure 15 with the exponent set as a caret); ARITHMETIC WHERE THE PAPER HOLDS - "
    "Figure 3 is exact to the last digit on all fourteen rows (six land-type cells summing to the printed "
    "ESV, cultivated contribution = cultivated cell over that sum) and Figure 6 files all fourteen "
    "provinces into the band their Figure 5 value falls in, and Figure 14's two in-plot annotations "
    "77388 and 639 (10^8 Yuan) are Jiangsu's GDP from Figure 7's table and its ESV from Figure 3 - AND "
    "WHERE IT FAILS: Figure 17 prints a 0.79 change where 30.49 against 29.71 gives 0.78 (and 2.65% "
    "where the cells give 2.63%), Figure 18's unused-land rate of 2.65% is Figure 17's LAND-AREA rate "
    "while its own cells give 2.78% and its Total column misses its row sums by 0.02 at 2014 and 2015, "
    "Figure 19's direct-value change is -6.713 where the endpoints give -6.712, Figure 22's 2009 column "
    "sums to 9888.22 against a printed total of 9843.22 (a 45.00 shortfall) and its ecological-cost "
    "column to 31.99 against 32.03 with the Other Land entry left out of its own total, and the two "
    "sensitivity grids do not close (Figure 20 sums to 1.31, Figure 23 to 0.997) although both are "
    "called CS; Figure 22's total falls 32.03 in a unit the table never prints, against the prose's "
    "'323,300 yuan'; Figure 7's bars plot GDP while its caption names the ecological service capacity per "
    "unit GDP, which exists only as an unplotted row beneath the bars, so the plate's ranking is the "
    "inverse of the text's, and its two legend swatches are the same blue; Figure 13's legend names three "
    "series and draws four (GDP(ΔA2/A2) printed twice, no ESV(ΔA2/A2)); Figures 5 and 7 have no usable "
    "ordinate (Figure 5 has no ticks at all and its bars are thin white stems on a light field); Figures "
    "11 and 12 are cost-benefit sketches with no tick, number or unit on either axis, (a) marking "
    "equilibria A and B and (b) marking only A on a different line; Figure 9 is the only radar map in the "
    "census, an eight-step radial scale that skips 0.98 and marks no ring at 1.00; REGION ORDER IS NOT "
    "READING ORDER - p15's Figure 9 sits in region 1 and Figure 8 in region 2, and p20's Figures 13/14 "
    "are likewise exchanged, both settled from the crop; seven of the twenty-three figure rows (17-23) "
    "sit in an appendix block with no prose near them; families table-as-figure 11, line 5, "
    "flowchart-or-schematic 3, bar 2, scatter 1, other 1 (radar), table-grid 2) |"
)

READ = (
    "| 180 | P-E-2019-1902029-f44b44ca | 28 | 25 | 23 | 2 | closed, `check.py` layout identical, "
    "unaccounted 0; 25 measured regions over 16 of 28 pages resolving into 23 figure rows and 2 table "
    "rows; eleven figure rows are printed grids (Figures 2, 3, 6, 10, 17-23) and Figure 16 is captioned "
    "'The table of…' over a line chart; only Table 1 and Table 2 are live vectors, the other 23 regions "
    "are pasted rasters; one quantity printed as Billion yuan, *10^8 Yuan, 10^4 yuan/hm^2, yuan/km2, "
    "Million Yuan and ESV/10^12 Yuan; Figure 3 sums exactly and Figure 6 agrees with Figure 5 while "
    "Figure 22's 2009 column misses its total by 45.00 and Figures 20/23 sum to 1.31 and 0.997; Figure "
    "7's bars plot GDP not ESC/GDP; Figures 13's legend names three series and draws four; p15 and p20 "
    "region order is swapped against reading order |"
)

prefix = f"| 180 | {PID} |"
for name in ("CLAIMS.md", "CLAIMS-rows-mcm-9a.md"):
    path = LANE / name
    lines = path.read_text(encoding="utf-8").splitlines()
    kept = [line for line in lines if not line.startswith(prefix)]
    kept.append(ROW)
    path.write_text("\n".join(kept) + "\n", encoding="utf-8", newline="\n")
    print(name, "rows", len(kept))

readme = LANE / "README.md"
rows = readme.read_text(encoding="utf-8").splitlines()
rows = [line for line in rows if not line.startswith(f"| 180 | {PID} |")]
idx = next(i for i, line in enumerate(rows) if line.startswith("| 121 |"))
rows.insert(idx, READ)
readme.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
print("README rows", len(rows))
