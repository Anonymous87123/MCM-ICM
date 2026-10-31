# EXTRACTION — L5-e text-extraction defects

Append-only register of defects in the extracted text layer, found while packing. One row per
pid/page/block. Page values are the chapter page range from the pack header unless the pack pins a
single page; block values are layout block numbers, unit numbers where the pack counts units only.

Purpose: a failed quotation test with a row here is a documented extraction reason. A failure with
no row here is a defect in the paper or in the pack and must be treated as such.

## Class key

| class | effect on quoting |
|---|---|
| ligature loss | breaks exact-match quoting on prose (` rst`, `coe cient`, `in uential`) |
| watermark splice | breaks quoting inside displays and mid-sentence; worst where a formula should be |
| PUA math glyphs | displays unrecoverable while prose stays clean — invalidates the page for displays, not for prose |

## ligature loss

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-E-2018-78511-395a90c3 | 4-13 | 47-130 | ligature loss | ~200 words damaged: ` rst`, `in uential`, `re ect`, `bene t-type`, `coe cient`, ` eld`. Any quote containing fi/fl/ff is broken. |
| P-E-2018-74971-2b1f503a | 5-11 | whole chapter | ligature loss | same fi/fl/ff stripping; verbatim quotes must avoid those words |
| P-E-2018-88902-cefa4db9 | 6-16 | 77-174 | ligature loss | same; prose quotes break on the same word class |
| P-E-2018-73119-79c4dde3 | 7-14 | 167-174 | ligature loss | same |
| P-E-2018-89499-90bc677f | 4-9 | 22-58 | ligature loss | same, plus caption text appended to sentences |
| P-E-2018-93840-dffa6997 | 2-4 | 14-27 | ligature loss | ` rst de ne`, `in uenced`, `uctuations`, `di erent`, ` nally` |
| P-E-2019-1916129-cfc06e89 | 4-14 | 33-130 | ligature loss (hyphenation variant) | page-break hyphens retained inside words: `coefﬁcie`, `re- gion`, `nation- wide`; ligature glyphs themselves survive |

## watermark splice

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-E-2018-72968-5f2ee223 | 6-17 | 95 and six further blocks | watermark splice | Taobao line inside sentences and inside displays; 7 units affected |
| P-E-2018-73119-79c4dde3 | 7-14 | 170-174 | watermark splice | advertisement used as punctuation between clauses |
| P-E-2018-74971-2b1f503a | 5-11 | units 10, 14, 19, 28, 35 | watermark splice | interrupts formulas |
| P-E-2018-78511-395a90c3 | 4-13 | 58, 82, 89-90, 109, 110-112 | watermark splice | splits sentences mid-clause (`…under safety and society` / `proportional to…`) |
| P-E-2018-88902-cefa4db9 | 6-16 | 77, 87-89, 96-98, 110-111, 129-130, 139, 148-149, 160, 172 | watermark splice | cuts quotes, lists and formulas; splits numbered list item 3 away from items 1-2 |
| P-E-2018-89499-90bc677f | 4-9 | 23-24, 49 | watermark splice | cuts a definition and the entropy step 3 |
| P-E-2018-93840-dffa6997 | 2-4 | 15, 22-23 | watermark splice | advertisement plus running header `Team # 93840 Page 3 of 19` close unit 2; advertisement mid-sentence in unit 7 |
| P-E-2019-1902029-f44b44ca | 6-10 | 56-108 | watermark splice | none found — recorded as a clean chapter for contrast |
| P-E-2019-1903455-a52f7980 | 11-16 | 94, 111, 124-127, 137, 140-141 | watermark splice | opens a figure caption, truncates a clause, lands inside eq (19) |
| P-E-2020-2008521-e040e3b4 | 5-10 | 48, 59-60, 70-72, 83, 104-105 | watermark splice | opens and closes units; unit 17 is the watermark plus two headings and no prose |
| P-E-2020-2010035-cf1cc4f2 | 5-14 | 43, 71, 94, 99, 111, 121 | watermark splice | cuts the Table 1 announcement; six units affected |
| P-E-2020-2016287-6ed5334f | 4-14 | 57-59, 73, 122-124, 147-149, 170-171, 182-185, 196-197, 208-209, 221, 235 | watermark splice | ten units; splits clauses across the insertion |
| P-E-2020-2017963-104327a3 | 5-12 | 64-65, 99-100, 116, 128, 133 | watermark splice | five units; the Table 2 column of block 83 is interleaved with the indicator sentence so a quote cannot end at the table edge |
| P-E-2020-2021103-996a6655 | 4-8 | 28, 48, 63, 73 | watermark splice | appended at block tails; block 63 adds the 2.2.2 heading after the watermark |
| P-E-2021-2102057-3e6906e7 | 6-14 | 65, 85-86, 90, 99, 125, 141, 166, 172, 183-184, 189 | watermark splice | three variants, twice repeated back to back; lands between the terms of eqs (14) and (21) |
| P-E-2021-2113869-a6c9c257 | 5-15 | 42, 52, 62-74 group, 99 | watermark splice | four variants; block 52 puts the advertisement on the same line as a pseudocode step |
| P-E-2021-2119031-7da0a6d0 | 7-15 | 58, 62, 88, 105-106, 124, 129, 137, 149, 157, 166-167 | watermark splice | three variants; block 157 buries the 7 Indicator Definition heading behind one |
| P-E-2021-2119893-783934c9 | 4-15 | 40, 83, 90, 92, 99, 110, 134, 141 | watermark splice | stacked two and three at unit openings; block 99 is the three strings plus the 3.2.1 heading and no prose |
| P-E-2021-2122175-f3669e48 | 5-15 | 85, 99, 106, 111, 118, 123, 134, 166 | watermark splice | appended at block tails; block 118's weighting step 1 ends inside the advertisement |

## PUA math glyphs

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-E-2016-53494-99855cf8 | 3-14 | all display blocks | PUA math glyphs | every equation unreadable (`஽ ൌ ൌ ݋ݓ௥௘௡௘௪௔௕௟௘`); `EQ_TAGS` empty; prose clean |
| P-E-2018-89499-90bc677f | 4-9 | 44-56 | PUA math glyphs | `X, i, j, m, n` print as `"#`, `>`, `<`; the six-step entropy chain exists as words with no symbols |
| P-E-2018-88902-cefa4db9 | 6-16 | 129-160 | PUA math glyphs | probabilistic notation lost inside the factor and entropy displays |

## Outside the three classes (flagged, not merged)

- **math-token drop** — displays unrecoverable, no PUA bytes: Greek letters, subscripts, summation
  limits and braces vanish, leaving punctuation. Same quoting consequence as PUA glyphs, different
  mechanism. Rows: P-E-2019-1903455-a52f7980 p14-15 blocks 115-134 (eqs 16-21);
  P-E-2020-2008521-e040e3b4 p5-10 blocks 43, 47, 50, 54, 63, 82, 104-105 (all 12 relations);
  P-E-2020-2016287-6ed5334f p4-14 eqs (1), (2), (5), (7), (8);
  P-E-2021-2119031-7da0a6d0 p7-15 blocks 63-82, 89-93, 102-112, 133-144, 160-162, 175-177
  (a bullet form: the symbol goes and `represents the region ’s total plantation production in
  month .` is all that survives, so prose is quotable and the bullet corpus is not);
  P-E-2022-2202838-75410db9 p5-17 blocks 58-141 (whole chapter: `we take .` also loses the IPCC
  constant values, so the calibrated coefficients are not recoverable); P-E-2021-2122175-f3669e48
  p9-14 blocks 138-148 (the display and its symbol list both go, leaving `are the coefficients of the
  variables.` on its own line, so only the prose survives).
- **flattened tables** — cell-level quoting impossible, row labels detached from values. Rows:
  P-E-2019-1916129-cfc06e89 p6-10 Tables 3-9; P-E-2020-2010035-cf1cc4f2 p8-11 Tables 2-3;
  P-E-2020-2016287-6ed5334f p10-13 Tables 2-7; P-E-2019-1902917-3fb00373 p11-12 Table 2;
  P-E-2020-2017963-104327a3 p10-11 Tables 3-4 (Table 4 repeats `PMC12` in the `PMC22` column);
  P-E-2021-2119031-7da0a6d0 p8 Table 2 (calorie and ratio pairs printed as one run);
  P-E-2021-2119893-783934c9 p9-10 Tables 1-2 (both captioned "The weights of Basic Food Systems
  indicators", both flattened into one run, so the 24 weights cannot be paired with their indicators);
  P-E-2022-2202666-f7b82c76 p12-14 the ten-class table (six factor columns as one numeric run with the
  class numbers floating mid-row); P-E-2022-2203489-75977cc9 p6 Table 2 (growth rates survive, the
  species-count column does not) and p8 Table 3 (the density, ratio and life columns have no header).
- **doubled math glyphs** — every mathematical character is emitted twice, so `Pb(t)` prints as
  `𝑃𝑃𝑃𝑃(𝑡𝑡)` and `NDVI` as `𝑁𝑁𝑁𝑁𝑁𝑁𝑁𝑁`; prose is clean, every display and every symbol in a where-line
  needs manual de-duplication before it can be read. Row: P-E-2022-2203489-75977cc9 p5-16 blocks
  66-195 (whole chapter).
- **bare-tag displays** — the equation body is gone and the printed tag survives alone. `EQ_TAGS`
  therefore overstates what the chapter prints. Rows: P-E-2021-2119031-7da0a6d0 p10-14 blocks 88,
  113, 117, 174 (`(6)`, `(7)`, `(9)` each in a block by themselves). Related: P-E-2020-2021103-996a6655
  p6-7 carries stray tags `0, 1, 2, 3, 51` and no numbering in prose; P-E-2021-2102057-3e6906e7 tags
  `(9)` and `(10)` at the end of their where-lines rather than beside the display;
  P-E-2021-2122175-f3669e48 p9-14 tags 1-7 with none printed, so the tag list describes a chapter of
  prose only; P-E-2022-2202838-75410db9 p5-17 tags 1-31 with no body surviving in any block.
- **formula split across units** — a display's two halves land in units that do not touch, so neither
  half can be quoted as the definition. Rows: P-E-2020-2021103-996a6655 p6 blocks 60/61 (the two
  `Ppolicy` branches, three blocks apart); P-E-2021-2102057-3e6906e7 p12-13 blocks 191/192 (eq (21)
  continues at the first block of the next unit).

## Quoting convention (set by the pack audit of positions 1-36)

A handoff quote is page text with four permitted regularisations and nothing else:

1. End-of-line hyphenation is kept as printed (`real- life`, `decreas- ing`), never silently rejoined.
2. Ligature glyphs are spelled out (`ﬁ` → `fi`), because the extracted glyph is not what a reader types.
3. Watermark, advertisement, table-cell, citation and dropped-symbol intrusions are elided with `…`.
4. A quote may stop at the end of its block; the stop is marked with `…`.

Anything else — a changed word, a dropped word, an added gloss — is a defect: fix the pack, or add a row
below. Rows added by the audit:

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-E-2016-43443-82025ab9 | 10 | 124-125 | display scattered into prose | the EWR identity prints as `WSI = withdrawals MAR withdrawals EWR = MAR −withdrawals 1 WSI −1 = population population`, so it is described in the pack, not quoted |
| P-E-2018-74971-2b1f503a | 7-8 | 81 | watermark splice | `the extreme weather` / advertisement / `disasters mainly embodies` — the sentence is split across two blocks by the Taobao line |
| P-E-2018-89499-90bc677f | 8 | 28-29 | watermark splice | block 28 ends `correspond to stress`, the advertisement fills the gap, block 29 opens `indicators, status indicators…` |
| P-E-2019-1903455-a52f7980 | 8 | 115-117 | doubled math glyphs | `some space u u v v M R Y R`, `uY 1,2,3, ,b`; the notation sentence cannot be quoted without a marked gap |
| P-E-2020-2017963-104327a3 | 6-11 | 76 | watermark splice | `The maximum capacity of the environment` + advertisement + `to bear the toxic gases…` |
| P-E-2022-2202171-2ac7357e | 6-12 | 90-93 | math symbols dropped from prose | the deforestation-intensity sentence loses `r` and `≤`, and the `E = r/2` display arrives with its symbols gone |

Append new rows as they are found; do not renumber existing ones.
