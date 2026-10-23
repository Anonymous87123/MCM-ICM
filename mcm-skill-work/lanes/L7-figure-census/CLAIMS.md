# L7-figure-census — writer claims

One pid, one writer. Append-only: add a row when you start a paper, and do not edit or
delete anyone else's row. A row claims the paper while it is being worked; a closed paper
also has a `records/<pid>.json` on disk, which is the authority on whether it is done.

Queue order is `queue.txt`. Ranges below are a no-collision agreement, not a rule about
which papers may be recorded — anyone may claim the next free paper in their own range.

| queue # | pid | session | state |
|---|---|---|---|
| 1 | P-A-2010-6749-395f556a | closed before this agreement | closed |
| 2 | P-A-2010-7571-1ac2a627 | closed before this agreement | closed |
| 3 | P-A-2010-7586-ff69029f | closed before this agreement | closed |
| 4 | P-A-2010-7920-06d31c2b | closed before this agreement | closed |
| 5 | P-B-2010-7273-e234c9a6 | closed before this agreement | closed |
| 6 | P-B-2010-7507-24d34e5d | closed before this agreement | closed |
| 7 | P-B-2010-7947-b6007ae0 | closed before this agreement | closed |
| 8 | P-B-2010-8362-bd23db32 | closed before this agreement | closed |
| 9 | P-B-2010-8479-b934962b | closed before this agreement | closed |
| 10 | P-C-2010-6947-c5305f34 | closed before this agreement | closed |
| 11 | P-C-2010-7812-c2fa13fd | closed before this agreement | closed |
| 12 | P-C-2010-8048-a080a4e2 | closed before this agreement | closed |
| 13 | P-C-2010-8088-e7ab6731 | closed before this agreement | closed |
| 14 | P-A-2011-11199-cfe6d809 | closed before this agreement | closed |
| 15 | P-A-2011-12149-cb2b7105 | closed before this agreement | closed |
| 16 | P-A-2011-9159-41b0c737 | closed before this agreement | closed |
| 17 | P-A-2011-9582-99696cfc | mcm-9a | closed |
| 18 | P-B-2011-10496-de9286d6 | mcm-9a | closed |
| 19 | P-B-2011-11759-ee4be862 | mcm-9a | closed |
| 20 | P-B-2011-12114-03fd7440 | mcm-9a | closed |
| 21 | P-B-2011-9440-95f0fa40 | mcm-9a | closed |
| 22 | P-C-2011-10607-6ed4fd93 | mcm-9a | closed |
| 23 | P-C-2011-11325-4609137d | mcm-9a | closed |
| 24 | P-C-2011-11422-caf513f2 | mcm-9a | closed |
| 25 | P-C-2011-11893-6a9ea7d9 | mcm-9a | closed |
| 26 | P-C-2011-8882-54492a1f | mcm-9a | closed |
| 27 | P-C-2011-9089-838e50df | mcm-9a | closed |
| 28 | P-A-2011-9665-6560aced | mcm-9a | closed |
| 29 | P-A-2012-14297-5cb8073e | mcm-9a | closed |
| 121 | P-B-2017-68303-6c8a9ede | mcm-5e | closed |
| 122 | P-B-2017-69427-b04ae242 | mcm-5e | closed 2026-10-23 |
| 1 | P-A-2010-6749-395f556a | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 2 | P-A-2010-7571-1ac2a627 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 3 | P-A-2010-7586-ff69029f | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 4 | P-A-2010-7920-06d31c2b | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 5 | P-B-2010-7273-e234c9a6 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 6 | P-B-2010-7507-24d34e5d | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 7 | P-B-2010-7947-b6007ae0 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 8 | P-B-2010-8362-bd23db32 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 9 | P-B-2010-8479-b934962b | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 10 | P-C-2010-6947-c5305f34 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 11 | P-C-2010-7812-c2fa13fd | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 12 | P-C-2010-8048-a080a4e2 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 13 | P-C-2010-8088-e7ab6731 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 14 | P-A-2011-11199-cfe6d809 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 15 | P-A-2011-12149-cb2b7105 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 16 | P-A-2011-9159-41b0c737 | mcm-65 | rewriting 2026-10-23 (backfill exception) |
| 123 | P-B-2017-70174-8bf62421 | mcm-5e | closed 2026-10-23 |
| 124 | P-B-2017-70545-8e86fcfa | mcm-5e | closed 2026-10-23 |
| 125 | P-C-2017-55261-f877d0a0 | mcm-5e | closed 2026-10-23 |
| 126 | P-C-2017-55278-a011d0e2 | mcm-5e | closed 2026-10-23 |
| 127 | P-C-2017-55583-34388031 | mcm-5e | closed 2026-10-23 |
| 128 | P-C-2017-55585-278f2f68 | mcm-5e | closed 2026-10-23 |

## Ranges

| queue range | session | note |
|---|---|---|
| 18–120 | mcm-9a | sequential, one paper at a time, in `queue.txt` order |
| 101–120 | mcm-d0 | handed over 2026-10-23 by mcm-9a, who keeps 18–100; same conventions, no `Tbl.` normalisation |
| 121–277 | mcm-5e | agreed 2026-10-23; tail 260–277 handed to mcm-d0 the same day (see below) |
| 260–277 | mcm-d0 | reassigned 2026-10-23 from the tail of the mcm-5e range, at mcm-d0's request and granted by mcm-5e as the range owner, to keep one writer per paper; mcm-d0 claims each pid in this file before writing it |
| 278–435 | MCM4 | agreed 2026-10-23 |
| 278–435 | mcm-65 | reassigned 2026-10-23: no live session stood behind the MCM4 row above (the session its Status panel pointed at reports itself as `mcm-9a`, which holds 18–120 and has never worked 278–435); user confirmed the range was open and assigned it to mcm-65 |

## Backfill exception (queue #1–#16)

User-authorized 2026-10-23, for session mcm-65 only. The sixteen papers at queue #1–#16 were
closed before this agreement under a record shape that leaves `mention.lead_sentence`,
`mention.trail_sentence`, `mention.first_page` and `mention.count` empty on exhibits the text
layer does name, so those rows may be rewritten in place. Scope is exactly those sixteen pids:
`records/<pid>.json` and `notes/<pid>.md` may change, no pid outside #1–#16 is covered, and no
other session's row is edited or deleted. The closed-before-this-agreement rows above stand
otherwise unchanged, and this section is the standing record of why a closed row may move.

Deferred 2026-10-23 by user direction: queue #278 onward is worked first, so the sixteen rows
below stay `closed` and no #1–#16 record has been rewritten. Titles, for the record:
MCM4 = mcm-9a, MCM3-quizzical-cupcake = mcm-5e, MCM1 = mcm-65 (this session).

Overlap is not allowed: if a paper in your range already has a `records/` file, skip it —
someone finished it first. If you finish a paper whose row is already claimed by another
session, report it instead of writing the record.
| 279 | P-A-2022-2209466-5952dd05 | mcm-65 | closed 2026-10-23 |
| 280 | P-A-2022-2209812-101c692c | mcm-65 | closed 2026-10-23 |
| 281 | P-A-2022-2210307-63733813 | mcm-65 | closed 2026-10-23 |
| 420-435 | see queue.txt | mcm-d0 | claimed 2026-10-23 (handed over by mcm-65) |
| 282 | P-A-2022-2212245-8b85eeb2 | mcm-65 | closed 2026-10-23 |

## mcm-9a additions after the range table

| queue # | pid | session | state |
|---|---|---|---|
| 30 | P-A-2012-14990-e2428f0d | mcm-9a | closed 2026-10-23 |
| 31 | P-A-2012-15065-1cbc0cd9 | mcm-9a | closed 2026-10-23 |
| 32 | P-A-2012-16831-ec8f03fd | mcm-9a | closed 2026-10-23 |
| 33 | P-B-2012-13074-8fc549d2 | mcm-9a | closed 2026-10-23 |
| 34 | P-B-2012-13955-a0e5e63c | mcm-9a | closed 2026-10-23 |
| 35 | P-B-2012-15171-ce229936 | mcm-9a | closed 2026-10-23 |
| 36 | P-B-2012-15417-df1dd905 | mcm-9a | closed 2026-10-23 |
| 37 | P-B-2012-15420-8b46b980 | mcm-9a | closed 2026-10-23 |
| 38 | P-B-2012-15878-825774ea | mcm-9a | closed 2026-10-23 |
| 39 | P-C-2012-12218-14ded715 | mcm-9a | closed 2026-10-23 |
| 40 | P-C-2012-13215-607f0f06 | mcm-9a | closed 2026-10-23 sha cc7b22dd1ad2f5cf (figures=13 tables=2 excluded=0 unaccounted=0; 4 declared gaps p4/p8/p11/p15, Figure 4 split over a page turn, Figure 8 2x2) |
| 41 | P-C-2012-13855-8ff9127d | mcm-9a | closed 2026-10-23 sha 2d5c8b69cfc51caa (figures=1 tables=10 excluded=3 unaccounted=0; 3 declared gaps p11/p15/p19, three Algorithm boxes excluded `not-an-exhibit`) |
| 42 | P-C-2012-14531-6018365f | mcm-9a | closed 2026-10-23 sha 755c83b450ac5f3b (figures=7 tables=4 excluded=1 unaccounted=0; 1 declared gap p15 Table 4, p1 title block excluded `background`, text cites Table 1 as `Table 2.1`) |
| 43 | P-C-2012-15356-6b8f0a28 | mcm-9a | closed 2026-10-23 sha 16c5ea6e9e13f3c5 (figures=10 tables=5 excluded=0 unaccounted=0; two exhibits both numbered Figure 7 p15/p19, unnumbered p4 symbol glossary counted as a table, uncaptioned p12 chart beside Table 4, Tables 1 and 3 two blocks under one merged title row) |
| 44 | P-C-2012-16075-4bbf9219 | mcm-9a | closed 2026-10-23 sha a76ae0c93481fd35 (figures=13 tables=7 excluded=0 unaccounted=0; 2 declared gaps p5 Table 1 and p19 Table 8, Table 5 continued across p15/p16, Figure 3(a)/(b) and Figure 8 x3 recorded panel-level, Figure 6 `composite-panel`) |
| 45 | P-C-2012-17160-8b6c54d2 | mcm-9a | closed 2026-10-23 sha ae79b0e9b4cbc096 (figures=0 tables=9 excluded=1 unaccounted=0; no figures in the paper at all, appendix listing `A Complete Listing of Results` over p21-p23 has no caption and is recorded as three continued fragments 33+42+7 rows) |

## mcm-d0 claim log

One row per paper, written before the record, in the order worked.

| queue # | pid | session | state |
|---|---|---|---|
| 420 | P-C-2025-2521556-9f85362c | mcm-d0 | closed 2026-10-23 sha 0517e47ce0879bbf (figures=19 tables=3 excluded=10 unaccounted=0; 4 declared gaps p8/p23) |
| 421 | P-C-2025-2522820-7a254095 | mcm-d0 | closed 2026-10-23 sha 7c32c223c22651cc (figures=11 tables=14 excluded=10 unaccounted=0; 2 declared gaps p20/p22, p15 blank) |
| 422 | P-C-2025-2524070-816ac5d5 | mcm-d0 | closed 2026-10-23 sha 4c6ddb887912b624 (figures=18 tables=6 excluded=11 unaccounted=0; 2 declared gaps p6/p17, p11 uncaptioned raster, Table 5 region partial) |
| 423 | P-D-2025-2504188-db12259e | mcm-d0 | closed 2026-10-23 sha 39d843ee44888ed2 (figures=15 tables=2 excluded=18 unaccounted=0; no printed exhibit missing, Figure 5/Table 2 never printed, p25 one-page memo raster yields no region; re-recorded same day to the settled panel rule: Figures 2 and 12 print ONE number each, so each is one row plus a fragment-of-other region, was 17/16) |
| 424 | P-D-2025-2507692-249f88dd | mcm-d0 | closed 2026-10-23 sha bd1cbcf9f9364081 (figures=21 tables=1 excluded=10 unaccounted=0; 8 printed figures 12-16/22-24 unmeasured because p15/p17/p18 are single 1700x2200 rasters dropped by MAX_AREA_FRAC 0.85) |
| 425 | P-D-2025-2516219-17e4e820 | mcm-d0 | closed 2026-10-23 sha ebfdd65d337b2c3b (figures=12 tables=2 excluded=17 unaccounted=0; 3 printed exhibits unmeasured on page rasters: Table 3 on p11, Figure 8 and Table 4 on p18; one-number figures recorded as one row plus fragment-of-other) |
| 426 | P-D-2025-2519935-f07f7c47 | mcm-d0 | closed 2026-10-23 sha 0b509d26eb1e5f15 (figures=22 tables=0 excluded=10 unaccounted=0; 8 declared gaps: Figures 9/10/12 printed only on the p11/p14 page rasters, and all five printed tables 1-5 returned no region at all though Table 5 on p13 was not in the text layer either) |
| 427 | P-E-2025-2502355-f89a99dc | mcm-d0 | closed 2026-10-23 sha 50dc3e9b4d927384 (figures=12 tables=5 excluded=12 unaccounted=0; 5 declared gaps on the zero-text pages: Figure 3 p6, Figure 7 p11, Figure 14 + Table 6 p21, Figure 16 p24; Table 3 measurable only as the repeated header plus one row on p17, its caption and first header sit on p16 above the page turn; Figures 8 and 11 are one-number panels, right panel recorded fragment-of-other) |
| 428 | P-E-2025-2508861-c97e23e1 | mcm-d0 | closed 2026-10-23 sha 3dcb2d1faa5bfe46 (figures=15 tables=1 excluded=22 unaccounted=0; 6 declared gaps, all on five zero-text pages that are each one flat inline raster: Table 1 + Figure 4 on p6, Table 2 on p11, Figures 10/11 on p13, Figure 19 on p22; p2 is the contents page; Figure 9 is one printed number over two panels, right panel recorded fragment-of-other; p25 is a nine-region farmer leaflet with no printed number, p26/p27 return ruled appendix text frames) |
| 429 | P-E-2025-2515136-5dd4cae6 | mcm-d0 | closed 2026-10-23 sha 97fe46ca04be1f1b (figures=14 tables=1 excluded=16 unaccounted=0; prints 15 figures + 4 tables, 4 declared gaps - Table 1 and Table 2 p5 and Figure 6 p11 on zero-text full-page rasters, plus Table 3 p10 whose grid is set as aligned symbol/value pairs with no rules at all so the layout pass returns no region on a page whose text layer is complete; 7 one-number (a)/(b) pairs, each one row plus fragment-of-other, and on Figures 11 and 12 the extractor returns the RIGHT panel first; 9 watermark QR blocks excluded; p2 contents, p24 references, p25 uncaptioned farmer leaflet returns no region) |
| 430 | P-E-2025-2517273-98509d3b | mcm-d0 | closed 2026-10-23 sha 3deb87345f473ad6 (figures=15 tables=1 excluded=11 unaccounted=0; prints 16 figure captions over 15 numbers - Figure 11 used twice with different titles on p21 and p24 - and not one table number anywhere; Figure 1 prints on zero-text p3 so it is the single declared gap, the p6 notation sub-tables are a second gap for the same reason, and the only measured table is the uncaptioned whole-page parameter table on p7 with 37+24 data rows and no rules, split by the detector into a row plus a fragment-of-other; six 2x2 four-panel line grids, Figure 9 is the paper's only colour bar; 10 watermark QR blocks excluded) |
| 431 | P-F-2025-2504223-019dfa54 | mcm-d0 | closed 2026-10-23 sha f2efcca5afbcdb7e (figures=12 tables=3 excluded=10 unaccounted=0; 13 printed figure captions and 4 printed table captions, 3 declared gaps - Figure 8 on the zero-text p15 raster, Figure 11 on the zero-text p18 raster, and Table 4 p20 whose fit-index grid is plain text with only two rules so no region survives; Table 2 p8 is printed with a table number but holds a bordered pseudo-code listing with no columns or rows, recorded table-as-figure; Figure 4 is ONE caption over two separate complete t-SNE+bar blocks, the right half fragment-of-other; five 595x841 zero-text sheets p2/15/16/18/25, and p16 is where sections 6.2-6.4 and equations (19)-(20) live; p7 cites "the algorithm in Table 3" while the algorithm is printed as Table 2; 9 watermark QR blocks excluded, the p20 one widened to 133-590 by the Table 4 foot) |
| 283 | P-A-2022-2216547-e72f44f2 | mcm-65 | closed 2026-10-23 sha 2a8f1d4b1d109297 (figures=21 tables=3 excluded=6 unaccounted=0; gaps: p5/p14 header-band regions, 5 unindexed headings, leaflet p24/p25) |
| 129 | P-D-2017-55285-1835cc0b | mcm-5e | closed 2026-10-23 sha 428810f7e0c3a19c (figures=31 tables=2 excluded=17 unaccounted=0; appendix "7 Other figures" holds 7 uncited plates; re-recorded same day: Table 1 rows 26 -> 25 after a pixel count of the notation grid, both table captions re-confirmed above the grid) |
| 130 | P-D-2017-55295-9001b6d9 | mcm-5e | closed 2026-10-23 sha 6322432e926aec64 (figures=19 tables=5 excluded=2 unaccounted=0; Fig 18 is one captioned pair printed as two regions - left panel carries the row, right panel and its nested legend box are fragment-of-other) |
| 131 | P-D-2017-56632-67f41f43 | mcm-5e | closed 2026-10-23 sha a758969ad81cdb2d (figures=10 tables=0 excluded=18 unaccounted=0; 8 of the 10 figures are one printed number over two side-by-side panels - the right panel of each pair is fragment-of-other; 6 boxed Assumption blocks + the X/W/Y definition box + 2 boxed equations + the Algorithm 1 listing are excluded as text, not artwork) |
| 132 | P-D-2017-67316-f37f83c8 | mcm-5e | closed 2026-10-23 sha 806692b37dc08eb0 (figures=16 tables=3 excluded=23 unaccounted=0; 3 of the 16 "figures" are printed tables (Figs 10/13/14, family table-as-figure); Tables 1-4 have no measured region and are declared gaps; Fig 12 collage = 1 row + 6 fragments + 10 duplicates; 3 caption bands + 2 halves of the cross-page green-framed letter excluded) |
| 133 | P-D-2017-68942-f0b0893e | mcm-5e | closed 2026-10-23 sha 1cb30aa655278e30 (figures=12 tables=17 excluded=1 unaccounted=0; only exclusion is p1, the MCM summary sheet as one full-page raster - no fragmentation at all; all 17 tables fully boxed with vertical rules, none booktabs, none zebra; prose cites by wrong numbers: zone schematic called "Figure 4" x3, WTMD chart called "Figure 11", slow-traveller table called "Figure 15", section 8.1 prints an unresolved "Table ??" |
| 134 | P-E-2017-61502-f0a50d47 | mcm-5e | closed 2026-10-23 sha caa1e5e11fcdf75d (figures=4 tables=4 excluded=3 unaccounted=0; 11 measured regions = 8 exhibits + 3 exclusions; p1 right column reprints Fig 2.1 and Fig 4.1 with unnumbered four-word captions, both duplicate; p21 second box is a fragment of Table A-2, the one landscape exhibit; figures always captioned below, tables always above; every number printed with a trailing hyphen ("Figure 2.1-Process flow", "Table A-1-"); Table A-2 has no rules at all, held together by coloured banner strips; Table A-1 has an open body; one declared coverage gap - printed Table A-2 grid runs y=84.8-490.9 pt but detector boxes only its top 133 pt plus one mid-table box, so 165 pt of printed grid has no measured region) |

| 284 | P-B-2022-2200084-66b742a2 | mcm-65 | closed 2026-10-23 sha 8096c1a74459ea76 (figures=18 tables=3 excluded=4 unaccounted=0; gaps: 4 algorithm-listing regions p9/p16, p12 Sankey right edge clipped, doc_order flips side-by-side pairs) |
| 285 | P-B-2022-2202748-102f6d4c | mcm-65 | closed 2026-10-23 sha 186437f78feb4608 (figures=9 tables=7 excluded=4 unaccounted=0; gaps: Table 1 split p5-p6 measured on caption band only, algorithm listing p12 runs onto p13 unmeasured, p20 grid is a raster spreadsheet with no caption) |
| 286 | P-B-2022-2207864-75af6d15 | mcm-65 | closed 2026-10-23 sha 13f926d8fec487cd (figures=17 tables=10 excluded=33 unaccounted=0; gaps: 30 pasted formula images + p15 boxed math band excluded as in-body-diagram, p5 pies share one caption line so doc_order prints Fig 4 before Fig 3, uncaptioned p5 drought map, Table 4 merged equation row, six empty pages p1/p2/p16/p17/p23/p24) |
| 287 | P-B-2022-2211922-6aa59818 | mcm-65 | closed 2026-10-23 sha f8865319e5543ada (figures=13 tables=3 excluded=11 unaccounted=0; gaps: notation table p5-p6 printed with rules but returned as no region so declared not recorded, Fig 7 region 0.521 because inset+annotation box fall inside it, Fig 11 left doughnut labels sum past 100%, Fig 4 top panel y axis starts at -8,000,000, newsletter insert p20-p21 counts as art plus one unnumbered sketch, p24 code slab excluded, eight empty pages) |
| 288 | P-B-2022-2213970-3f0a69d2 | mcm-65 | closed 2026-10-23 sha 5a47eae92fb56f47 (figures=15 tables=5 excluded=9 unaccounted=0; gaps: heading pass missed 5.2/5.3/6.3 and the chapter-6 title so those paths come from printed lines and Table 5 starts at 6.3, Figure 5 caption split in half by body prose so typed-from-crop, Table 5 region starts below its printed header row, Table 3 prints no header row at all (symbol row counts as header), Figures 14/15 inside the unnumbered lay summary are the same embedded rasters as Figures 6/7, p20 cites figure 15a three pages early and never cites Figure 13, Figure 5 polar axis runs into negative day labels, eight empty pages) |
| 289 | P-B-2022-2228168-d50f161d | mcm-65 | closed 2026-10-23 sha 15b6dde86930552f (figures=12 tables=10 excluded=0 unaccounted=0; gaps: Table 1 printed on p7 with caption and 8x3 grid but returned no region so declared not recorded, Figure 9 printed twice (p20 objective trace, p24 drought map) with Figure 10 following in the same magazine column, p13 flowchart carries no number and no caption while the caption 'Figure 7 Water resource scheduling process' sits at the top of p14 over a line chart, heading pass missed 4.1.2 and invented '7 Dw,i' inside equation (14) so five paths were corrected against printed order, unnumbered notation grid at p5 has a genuine header row so is a table with caption_source none, Table4 transposed with an empty stub header, Table7 bare zeros plus 'arce-feet', Table9 detached decimals and a 100 with none, Table10 only the 75% column populated, magazine page is two-column so page_order puts the right-column map before the left-column photo, eleven empty pages) |
| 290 | P-C-2022-2200401-824b71b2 | mcm-65 | closed 2026-10-23 sha 8d948f75d0dc19a8 (figures=16 tables=5 excluded=1 unaccounted=0; gaps: zero table numbers and zero table captions in the whole paper - all five grids announced by sentence, three notation grids under bullet labels; Algorithm 1 listing has no cells so it is family 'other' not a grid; p4 framework chart, p13 indicator grid, p23 memo grid and both p25 appendix charts unnumbered with caption_source none; heading pass read the p7 pseudocode as five section headings and the paper prints no 5.1.3; Figure 6 caption sits at the top of p14 before the chapter-6 heading but its citation is a 5.3 bullet; only 3-D row is Figure 10 perspective-bars, no colour bar anywhere; p22 margin holds the COMAP wordmark, excluded not-an-exhibit; nine empty pages) |
| 291 | P-C-2022-2200688-b6248fa6 | mcm-65 | closed 2026-10-23 sha c7ae992a420ae0d8 (figures=13 tables=1 excluded=15 unaccounted=0; gaps: only one grid in the whole paper and it is the unnumbered p5 notation table - a full-text scan finds 'Table' nowhere else; 13 of 29 regions are sub-panels of a printed number (two stock photos inside Fig 2, the 2x2 cells of Fig 5, both cells of Fig 6, two panels of Fig 7, the star raster inside Fig 8, both panels of Fig 9) excluded as fragment-of-other; p14 prints Fig 7's caption twice interleaved word by word so that caption alone is typed-from-crop; Figure 1 is a borrowed BitcoinOnAir infographic with no citation number in the text; six rows never named by number and Fig 10's cross-reference is printed as 'shown in 5.3'; Fig 5 lead_pages -1 because its caption is on p12 and its citation on p13; only 3-D plate and only colour bar is Fig 12 surface-mesh; p23 draws 44 paths with no region - crop shows code glyph runs plus one orphan right-margin rule; p22 memorandum header block and p24 Appendix 1 code listing excluded not-an-exhibit; eight section paths corrected against the heading index; nine empty pages) |
| 292 | P-C-2022-2203120-59ecfcb7 | mcm-65 | claimed 2026-10-23 (in progress) |
| 135 | P-E-2017-65123-e36461ec | mcm-5e | closed 2026-10-23 sha 4de4f26d0cc6dc6d (`check.py` layout identical, unaccounted 0) |
| 136 | P-E-2017-67171-0a99e096 | mcm-5e | closed 2026-10-23 sha 8bd135835b51b0a3 (`check.py` layout identical, unaccounted 0) |
| 137 | P-E-2017-68242-753e0037 | mcm-5e | closed 2026-10-23 sha e11afce8ef3067fd (figures=10 tables=10 excluded=3 unaccounted=0; nine of ten figures are drawings - one three-circle Venn template used four times, two box-and-arrow schematics; captions never mix sides (figures below, tables above); numbering splinters four ways; Figure 2 and Figure 9 never cited by number; Figure 10 cited seven pages early; Table 8's Wellington block is a declared gap) |
| 138 | P-E-2017-71672-f2a1a712 | mcm-5e | closed 2026-10-23 sha 510acd3da7caab93 (figures=0 tables=5 excluded=0 unaccounted=0; first paper in the lane with an empty figure list - all five measured regions are tables; all five captions print BELOW their grid with the only numbering form 'Table N:'; all five boxed with a rule between every body row; four are one two-column Metric/Value template with an italic ruled-off L row, only Table 5 has a two-tier header, merges and decimal alignment; four of five print a page after their announcing sentence; p14 and p17 each lose one value in the text layer so the grids look misaligned but print clean) |
