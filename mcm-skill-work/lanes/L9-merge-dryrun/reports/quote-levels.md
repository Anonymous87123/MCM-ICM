# Per-row quote levels for the merged projection

One row per dedupe key of `reports/rows.jsonl`: 41,088 rows in the order (type, paper, chapter_index, group_index), each carrying the level its quotation achieved and the evidence that level rests on. The level is re-derived from the owning lane's records and layout by running the L7 ladder of `tools/quote_blocks.py` again, rung for rung, on the block the generator quoted; it is not copied from the census, so the comparison below is a real second opinion on the same rows.

## Rows per lane

| lane | rows here | L7 census rows | difference |
|---|---|---|---|
| A | 3,232 | 3,232 | +0 |
| B | 10,333 | 10,333 | +0 |
| C | 10,397 | 10,397 | +0 |
| D | 5,308 | 5,308 | +0 |
| E | 5,024 | 5,024 | +0 |
| F | 6,794 | 6,794 | +0 |
| total | 41,088 | 41,088 | +0 |

A carries 3,232 rows whose quote lives in the lane record itself, so it has no ladder level and is reported as `in-record`; the five census files cover B to F only. Every lane matches its census file row for row, so there is no difference left to explain: the C and D quote files were regenerated after the census was first written - C lost seven duplicate claims and D one - and the census files were rebuilt with them, which is why the repair no longer shows as an offset here. Nothing is missing at the join: `quote_shortfall` in `stats.json` is 0.

## Level distribution

| level | A | B | C | D | E | F | all |
|---|---|---|---|---|---|---|---|
| exact | 0 | 7,950 | 8,325 | 4,806 | 4,555 | 5,906 | 31,542 |
| nfkc | 0 | 850 | 814 | 9 | 14 | 28 | 1,715 |
| squeezed | 0 | 486 | 435 | 138 | 93 | 218 | 1,370 |
| span | 0 | 551 | 428 | 225 | 226 | 362 | 1,792 |
| gapped | 0 | 143 | 117 | 57 | 52 | 124 | 493 |
| ocr-only | 0 | 4 | 0 | 0 | 0 | 0 | 4 |
| no-text-layer | 0 | 68 | 0 | 0 | 0 | 0 | 68 |
| text-gap | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| unverified | 0 | 281 | 181 | 73 | 84 | 154 | 773 |
| layout-only | 0 | 0 | 97 | 0 | 0 | 0 | 97 |
| in-record | 3,232 | 0 | 0 | 0 | 0 | 0 | 3,232 |
| total | 3,232 | 10,333 | 10,397 | 5,308 | 5,024 | 6,794 | 41,088 |

## Level by evidence class

| level | front-matter | prose | references | structural | all |
|---|---|---|---|---|---|
| exact | 72 | 31,045 | 292 | 133 | 31,542 |
| nfkc | 3 | 1,700 | 0 | 12 | 1,715 |
| squeezed | 0 | 1,358 | 2 | 10 | 1,370 |
| span | 0 | 1,773 | 6 | 13 | 1,792 |
| gapped | 1 | 488 | 0 | 4 | 493 |
| ocr-only | 0 | 4 | 0 | 0 | 4 |
| no-text-layer | 0 | 68 | 0 | 0 | 68 |
| text-gap | 0 | 2 | 0 | 0 | 2 |
| unverified | 0 | 749 | 19 | 5 | 773 |
| layout-only | 0 | 95 | 2 | 0 | 97 |
| in-record | 0 | 3,232 | 0 | 0 | 3,232 |
| total | 76 | 40,514 | 321 | 177 | 41,088 |

`references` and `structural` rows are quotations of bibliography entries, headings and display lines: the ladder cannot verify a symbol run, so those rows are `unverified` by nature and are not defects. `front-matter` rows are B's 76 excluded title rows, quoted but held out of the merge stream.

## Four separately reported counts

| count | A | B | C | D | E | F | all |
|---|---|---|---|---|---|---|---|
| no-text-layer | 0 | 68 | 0 | 0 | 0 | 0 | 68 |
| ocr-only | 0 | 4 | 0 | 0 | 0 | 0 | 4 |
| unverified | 0 | 281 | 181 | 73 | 84 | 154 | 773 |
| layout-only | 0 | 0 | 97 | 0 | 0 | 0 | 97 |

`no-text-layer` is a subset of what the ladder calls `ocr-only`, not a fifth bucket: the rows are those whose block sits on a printed page whose text file is empty, and the ladder's own label for them is `ocr-only` because the layout came off the page image. Here they are lifted out - 68 rows - and the remaining 4 keep the ladder label. The two counts therefore add to the ladder's 72, which is exactly the 72 the census records for B to F once the C and D repairs are taken off. `unverified` and `layout-only` overlap neither: the first is a non-prose block in a paper that has text somewhere, the second is a paper with no extracted text at all.

## Reconciliation with the census

Census cells against the recomputation, lane by lane. A dash means the level does not occur in that lane.

| level | B here | B census | C here | C census | D here | D census | E here | E census | F here | F census |
|---|---|---|---|---|---|---|---|---|---|---|
| exact | 7,950 | 7,950 | 8,325 | 8,325 | 4,806 | 4,806 | 4,555 | 4,555 | 5,906 | 5,906 |
| nfkc | 850 | 850 | 814 | 814 | 9 | 9 | 14 | 14 | 28 | 28 |
| squeezed | 486 | 486 | 435 | 435 | 138 | 138 | 93 | 93 | 218 | 218 |
| span | 551 | 555 | 428 | 430 | 225 | 226 | 226 | 228 | 362 | 365 |
| gapped | 143 | 140 | 117 | 115 | 57 | 57 | 52 | 51 | 124 | 121 |
| ocr-only | 4 | 72 | 0 | - | 0 | - | 0 | - | 0 | - |
| no-text-layer | 68 | - | 0 | - | 0 | - | 0 | - | 0 | - |
| text-gap | 0 | - | 0 | - | 0 | - | 0 | - | 2 | 2 |
| unverified | 281 | 280 | 181 | 181 | 73 | 72 | 84 | 83 | 154 | 154 |
| layout-only | 0 | - | 97 | 97 | 0 | - | 0 | - | 0 | - |
| rows | 10,333 | 10,333 | 10,397 | 10,397 | 5,308 | 5,308 | 5,024 | 5,024 | 6,794 | 6,794 |

Reading of the differences, with the count that carries each one:

- The top rungs reproduce the census cell for cell. `exact` agrees in all five lanes at 7,950 / 8,325 / 4,806 / 4,555 / 5,906; `nfkc` agrees in all five lanes at 850 / 814 / 9 / 14 / 28; `squeezed` agrees in all five lanes at 486 / 435 / 138 / 93 / 218. No cell in those three rungs differs, so the C and D duplicate-row repair the census once carried as an offset no longer shows at this rung.
- The bottom rungs - `span`, `gapped`, `unverified` - agree in total per lane: B 975 against 975, C 726 against 726, D 355 against 355, E 362 against 362, F 640 against 640, so 12 rows leave `span` in net and none leaves the three-rung family; a row that travels the other way is counted on both sides, so the physical number of moves is higher than that net and is not claimed here. The movement has one mechanism: the recomputation takes the longest run of at least eight words the token index can match and rejects that run when it holds no real words, so a block whose longest run is a numerals or glyph run (`, , , ,` or `m m m m m m`) fails `span` here and is labelled `gapped` or `unverified` further down the ladder, while the generator's substring probe had found a prose or table head in the same block. The rows are the same rows and the quotation is the same quotation; only the sentence-failure label moves. The glue pattern (`themodel`) is not this mechanism: it belongs to the quote-mismatch family below, where the two runs stop on different sentences.
- `ocr-only` plus `no-text-layer` sums to 72 against the census's 72 across B to F (B 72 against 72), so the two counts land on the same total and no row is missing from that bucket. Both sides label the same four rows `ocr-only` on pages that do carry text and the same sixty-eight `no-text-layer` rows on pages whose text file is empty, so there is no split row left to name. No lane has a `text-gap` cell except F, where both sides report 2.

## Quotation cross-check

For the 37,856 B to F rows the recomputation also reproduces the quote itself, not just its level, and compares it with the string stored in the L7 file. The strings agree on all but 247 rows, 0.65 percent, and those split three ways. 205 still carry the stored sentence byte for byte inside the block the ladder quoted, so the two runs stopped at different points of one paragraph. 41 carry it once ligatures and math glyphs are normalised - a printed `ﬁ` against the text layer's `fi`, and doubled italic letters such as `XXiiii` for `X_i` - so the sentence is there and only its characters differ. 1 match no block the group covers at all, which is what a quote file regenerated after a record rewrite leaves behind. Every one of the three is named by paper, chapter, group and both lengths in `residue-mismatches.jsonl`. Independently of that check, the 37,856 stored quote hashes were re-verified against the L7 files line by line: 0 mismatches, 0 dangling references, so every row's `quote_sha256` still names the string in its source file.

## Leftover quote rows and stale references

0 quote rows in the L7 files are cited by no row of the projection, and 0 rows cite a line their quote file no longer has. Both are zero after the C and D files were regenerated, which is the point: the quote layer and the record layer now agree on every lane, so the projection needs no subtraction to be squared against them.

