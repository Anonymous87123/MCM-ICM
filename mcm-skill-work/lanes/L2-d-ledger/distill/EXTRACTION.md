# EXTRACTION — L2-d text-extraction defects

Append-only register of defects in the extracted text layer, found while packing. One row per
pid/page/block. Page values are the chapter page range from the pack header; block values are
layout block numbers as cited in the pack.

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
| P-D-2018-82504-6cc63169 | 5-13 | 43, 45 | ligature loss (hyphenation variant) | block 43 opens mid-word `ar-eas`, block 45 opens `least 5%…`; the split is page-break hyphenation, not ligature stripping, and it breaks quotes at the unit boundary |

No D pack in the first 33 documents fi/fl/ff stripping. Absence here means not seen, not absent —
the D lane was read without the same word-level scan the E lane got.

## watermark splice

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-D-2018-73156-1a30e830 | 6-20 | 43, 54, 63, 76, 95, 118, 129, 130, 170, 177 | watermark splice | Taobao shop line mid-sentence in every one; quotes must be cut before and after |
| P-D-2018-78826-ed3ee7b7 | 4-16 | 29, 33, 38 (twice), 75, 79, 83, 86 | watermark splice | closes blocks; the cost formula is split 78/79 and its symbols never resolve |
| P-D-2018-80386-b757100d | 5-19 | 24-30, 33, 38-43, 45-49, 58-60, 68, 74-75 (twice), 77, 89-90, 95-98, 101, 110-111, 113 | watermark splice | worst in the lane; block 68 interrupts an assumption mid-sentence |
| P-D-2018-82504-6cc63169 | 5-13 | 43, 55, 63, 64 | watermark splice | reaches the Figure 2 caption (55) and the Table 2 body (63), so a caption-keyed figure census can be fooled |
| P-D-2018-81402-e1ca1921 | 5-11 | 29, 39, 41, 48, 54, 64, 74 and six more | watermark splice | 13 of 42 units; always appended at the tail |
| P-D-2020-2002526-23eb8c8d | 4-10 | 23, 28, 40, 49, 56, 66 | watermark splice | appended after the sentence, so the sentence survives but the block continues |
| P-D-2020-2003723-28f692ff | 5-8 | 35, 40, 43, 46, 49 | watermark splice | tails only; captions are separate blocks, so captions stay clean |
| P-D-2020-2006782-8d6d48b4 | 4-11 | 62, 50, 73, 82, 104, 109 | watermark splice | block 62 is spliced between two clauses and leaves a stray `2` |
| P-D-2020-2013245-e4e7ae08 | 4-11 | 47, 51, 52, 79 | watermark splice | block 52 splices `It is the same as` into the watermark and then into the Figure 5 caption |
| P-D-2020-2015044-db9655c7 | 5-10 | 106, 107 | watermark splice | caption and watermark injected between the two halves of one sentence |
| P-D-2020-2022868-71331b90 | 4-12 | 32, 41, 50, 62, 89, 99, 111 | watermark splice | harmless for quoting, but marks where a block really ends |
| P-D-2021-2100112-1b2d1f1c | 5-17 | 60+ spans across the chapter | watermark splice | four different advertisement strings; `微信公众号：数学模型` separates `max max max k (ECk)` from `F−Scorei` inside equations (17)-(18) and splits Table 2 rows |

## PUA math glyphs

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-D-2020-2002526-23eb8c8d | 4-10 | every display block | PUA math glyphs | `𝐶𝑑𝑤= 6. 70(809:8;)< 0` and `1LMNOP QR S&R&OTOPU`; subscripts flatten (`𝑝𝑖B`, `𝑡𝑝<`); no display block quotable |
| P-D-2018-78826-ed3ee7b7 | 4-16 | 78, 79 | PUA math glyphs | cost-formula symbols `u =߮`, `∗u+ ∗ߛ+ ߠi ∗ܮi` unrecoverable; only the fact of a formula survives |
| P-D-2020-2013140-d02fd0c3 | 5-10 | 4 numbered formulas | PUA math glyphs | all four are inequality systems on player coordinates and all four are text-layer unreadable |

## Outside the three classes (flagged, not merged)

- **flattened tables** — cell-level quoting impossible, row labels detached from values. Rows:
  P-D-2020-2013140-d02fd0c3 blocks 78, 81; P-D-2020-2022868-71331b90 Tables 2-4;
  P-D-2021-2100112-1b2d1f1c Table 2 (follower count pulled ahead of the name).
- **caption merged into body** — a figure caption sits in the same block as the sentence that cites
  it, so a quote cannot end at the sentence. Rows: P-D-2018-82504-6cc63169 55;
  P-D-2020-2013245-e4e7ae08 52; P-D-2020-2015044-db9655c7 106-107.

## Quoting convention (set by the pack audit of positions 1-33)

A handoff quote is page text with four permitted regularisations and nothing else:

1. End-of-line hyphenation is kept as printed (`real- life`, `ar-eas`), never silently rejoined.
2. Ligature glyphs are spelled out (`ﬁ` → `fi`), because the extracted glyph is not what a reader types.
3. Watermark, advertisement, table-cell, citation and dropped-symbol intrusions are elided with `…`.
4. A quote may stop at the end of its block; the stop is marked with `…`.

Anything else — a changed word, a dropped word, an added gloss — is a defect: fix the pack, or add a row
below. Rows added by the audit:

| pid | page | block | class | what it breaks |
|---|---|---|---|---|
| P-D-2016-42220-7261f9d3 | 4-12 | 50 | math symbols dropped from prose | `we assume that λi and φm is constant` prints as `we assume that i and is constant … the m average level`; each symbol lands after the word it belongs to, so the sentence is not quotable in order |
| P-D-2017-67316-f37f83c8 | 4-10 | 43 | doubled math glyphs | `ssww 1 nn1 1 nn2 1 375 tt0 025 14` for `s√(1/n1+1/n2) = 1.375 ≤ t0.025(14)` |
| P-D-2017-67316-f37f83c8 | 4-10 | 55 | spline numbers inside words | `com0 015 plicated`, `ex0 010 ponential`, and `we 0 025 have ss dd` for `we have λs = µd` |
| P-D-2017-67316-f37f83c8 | 4-10 | 60 | doubled math glyphs | `(𝑀𝑀/𝐸𝐸𝑘𝑘/𝑐𝑐)` for `(M/Ek/c)`; every symbol is emitted twice |
| P-D-2017-67316-f37f83c8 | 4-10 | 75-81 | spline numbers inside words | `104 … 189 passengers`, `i e 1000`, `we as900 sume`; plot values sit inside the sentence |
| P-D-2018-81402-e1ca1921 | 5-11 | 37 | superscript split | `more than V 2 variables` for `|V|² variables`; the block also ends `linear program-`, continuing `ming model` in block 38 |
| P-D-2018-81402-e1ca1921 | 5-11 | 65 | words run together | `anexponential` and `analogywith`; the space is lost in extraction |
| P-D-2019-1922074-a699b77f | 4-11 | 201 | bullet glyphs lost | `• Some channels cannot pass. • Some staircase is not accessible`; bullets and their line breaks collapse into one block |
| P-D-2020-2006782-8d6d48b4 | 4-11 | 85 | page counter inside a word | the block ends `There-` and the next page starts `5 to fore`, so `Therefore` is unquotable |

Append new rows as they are found; do not renumber existing ones.
