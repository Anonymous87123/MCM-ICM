# L7 — verbatim quote backfill for the B, C, D, E and F job ledgers

## Why this lane exists

L6 (`lanes/L6-a-evidence`) gave every coded A block one verbatim quote, so that the A
rows can be merged into `artifacts/paragraph-ledger.jsonl` with evidence attached. The
B, C, D, E and F lanes were coded the same way as A but carry only block indices and job
labels: their records have `chapter / heading / pages / groups / jobs / note`, and no
quote. This lane produces the missing quote layer for those five lanes, in the same row
shape as L6, so that the merge session has one uniform input.

E and F were backfilled after the B/C/D pass: both are closed lanes (E 60 papers, F 48),
so their row counts are final, while B, C and D are still being coded by their owners and
their numbers move between runs.

This lane reads everything and writes only `lanes/L7-quote-backfill/**`.

## Inputs (read only)

| path | use |
| --- | --- |
| `lanes/L4-b-ledger/records/*.json` | B denominator: chapter records, `groups`, `jobs` |
| `lanes/L3-c-ledger/records/*.json` | C denominator |
| `lanes/L2-d-ledger/records/*.json` | D denominator |
| `lanes/L5-e-ledger/records/*.json` | E denominator |
| `lanes/L1-f-structure/records/*.json` | F denominator |
| `lanes/L{4,3,2,5,1}-*/layout/<pid>.json` | measured blocks: `paragraphs[].n`, `.text`, `.pages`, `.kind` |
| `artifacts/papers/<pid>/text/full.txt` | verification text, whitespace-folded |
| `artifacts/papers/<pid>/pages.jsonl`, `extraction.json` | fallback verification text when `full.txt` is absent |

`.skipped.json` files are not part of any denominator.

## Output

| file | content |
| --- | --- |
| `quotes-{b,c,d,e,f}.jsonl` | one line per coded group: `{paper, chapter, chapter_index, block_index, job, quote, page}`, ordered by paper, then chapter order in the record, then `block_index` |
| `reports/levels-<lane>.json` | census written by the generator: ladder level of every row, verification source, heading and display rows |
| `reports/coverage.json` | machine recount: rows per lane, shortfall against the records, empty quotes, short quotes, duplicate `(paper, chapter, block_index)`, label census outside the 13-job vocabulary |
| `reports/coverage.md` | the same, human-readable |
| `reports/spot-check-<lane>.md` | the hand sample required by step 4, one row per sampled quote with its ladder level and a `clean` / `suspect` mark |

`chapter_index` is the chapter's position inside its paper (0-based, record order). It
exists because F repeats a chapter label inside one paper — 672 chapter rows but only 389
distinct `(paper, chapter)` labels — so the label alone cannot key a row. The uniqueness
key for every lane is `(paper, chapter_index, chapter, block_index)`; `coverage.py` counts
duplicates on that key.

## Denominator

Measured on 2026-10-23 from the lane records themselves; B, C and D are still growing, so
their rows are a checkpoint, not a constant. E and F are closed lanes, so their rows are
final. `tools/coverage.py` recomputes every number and prints the current values.

| lane | papers | chapter records | coded groups = quote rows | blocks inside those groups |
| --- | --- | --- | --- | --- |
| B | 76 | 1,068 | 10,333 | 18,115 |
| C | 112 | 1,112 | 10,397 | 24,724 |
| D | 55 | 598 | 5,308 | 10,240 |
| E | 60 | 662 | 5,024 | 15,596 |
| F | 48 | 672 | 6,794 | 10,713 |
| total | 351 | 4,112 | 37,856 | 79,388 |

Re-run `tools/coverage.py` before quoting these numbers: the owners of B, C and D keep
adding papers, and the quote files were regenerated at the checkpoint above.

Three C papers have no staged `text/` tree. `P-C-2021-2123823-dddc6e65` still keeps its
extraction in a correction workspace, so its 167 rows verify there. `P-C-2023-2307166-ec54f9ce`
and `P-C-2023-2307946-61b646ed` keep no extracted text anywhere in their artifact
directory, only derived records; their 97 rows are emitted from the layout and marked
`layout-only` in the coverage report rather than silently dropped.

## Quote rule

1. A quote is a **verbatim span of the group's first block**, taken from the lane's own
   measured `layout/<pid>.json` paragraph text, never rewritten. It is the opening
   sentence wherever that sentence verifies.
2. Sentence end = `.` `!` `?` followed by whitespace and a capital, a quote or a digit;
   a `:` or `;` does not end a quote.
3. Verification ladder, in order, each accepting the first candidate that hits the
   extracted text: exact folded match, then NFKC match (collapses `fi`/`fl` ligatures),
   then whitespace-squeezed match (absorbs line and column breaks), then the **longest
   contiguous span of at least 8 words** that matches, then the **longest in-order run of
   at least 8 words with at most 8 foreign words between consecutive quoted words, where
   up to 3 block words that the text layer never carried (a doubled math glyph such as
   `jjth` for `jth`) may drop out of the run**. The
   last step exists because a two-column table extracts as its two columns interleaved
   word by word, so one cell's sentence never survives contiguously while all of its
   words survive in order. Every step still quotes words exactly as the layout emits them.
   A `span` or `gapped` match that carries fewer than two distinct words of three letters
   or more is discarded, because a run of single-letter tokens (`m m m m …` from a matrix)
   or of digits verifies and still says nothing; the block then falls through to the label
   its content deserves.
4. A block that carries prose and yields no hit at any ladder step is a hard error: the
   tool exits non-zero and names the paper, chapter and block. Prose means at least 12
   plain words, at least 70 percent plain words among all tokens, at least half of those
   lowercase, and at least one sentence terminator. Anything else — a `display` block, a
   notation table, an equation — is quoted as-is and counted as `unverified`, because no
   reading order exists in which symbol soup and the extracted text agree. Measured limit of
   that label: of the 13,516 non-prose first blocks in these lanes, only 8 have **none** of
   their plain words anywhere in the paper's text (B 6, E 1, F 1), so `unverified` almost
   always means "present, order unverifiable" rather than "absent from the text layer". A
   paper whose equations are embedded images would show up as a cluster of absent blocks, and
   no lane here does.
5. A paper with no extracted text anywhere in its artifact directory is quoted from the
   layout alone and counted as `layout-only`. A paper whose layout was read from page
   images (`extractor: ocr_layout`) may hold prose the text layer never captured; on such
   a paper a prose block that fails the four contiguous steps is quoted from the layout and
   counted as `ocr-only` **before** the `gapped` step is tried, because a gapped run there
   stitches words from elsewhere in the text into a string that reads like a quotation and
   is not one. A paper that does have a text layer can still drop whole paragraphs, so a
   prose block that fails every contiguous step on such a paper is quoted from the layout
   and counted as `text-gap`, but only when the paper's own text layer is shown gappy —
   at least three body blocks with no eight-word span anywhere. Without that evidence a
   prose block still aborts the lane. All three levels are emitted so the merge session
   sees the gap, never dropped.
6. If the first block is a `heading` or `display` block, the heading or caption text is
   the quote; the kind is recorded in the coverage report so a reviewer can see how many
   rows lean on a heading or a caption.
7. Every row records its ladder step in `reports/levels-<lane>.json` (`exact`, `nfkc`,
   `squeezed`, `span`, `gapped`, `unverified`, `layout-only`, `ocr-only`, `text-gap`), so
   the merge session can decide whether the partial-match rows need a second read.
8. The uploader watermark (`微信号`, `关注数学模型`, `MATHmodels`, `获取更多资讯`) is printed as
   three widely spaced lines, so the layout emits it as its own block and it can land as a
   group's first block. When the first block holds nothing but the stamp, the quote is taken
   from the first block of the same group that carries the paper's own text; when the stamp
   is glued to the head of an otherwise real block, it is trimmed off the head. Both moves
   keep the quote a verbatim span of a block. A stamp that sits **inside** a `span` or
   `gapped` run is left alone and counted, because cutting it there would tear a hole in a
   run whose whole claim is that the words are in order: 120 rows over 61 papers, none of
   them at the start of their quote.

### 与最初目标口径的差异

目标写成"B 68 / 9,280、C 96 / 9,787、D 34 / 2,914，合计 21,981"。本轮执行期间 B、C、D
三个车道的属主继续加篇，实测已是 350 篇 / 37,748 组（含 E、F 两车道），因此行数只能对
"当前 records"成立，不能对目标里的冻结值成立。按实测收口：本页数字与 `tools/coverage.py`
的输出一致，车道再增篇时重跑该命令即可，不用改口径。

E、F 是关道，行数可写死：E 5,024、F 6,794，两者合计 11,818 行是本轮补证的全部目标。

### 粒度原则

存储单元是一份决策记录，不是页面地图（"stored units are a decision log, not a page map"）。
本车道不读 stored 字段做定位：行的位置来自 record 的 `groups`（`groups[i][0]` 是 1 起的
段落号），文本来自该车道 `layout/paragraphs[n-1]`，页号来自该段落的 `pages[0]`。
`content_counts` 之类的排版统计从不参与定位，所以排版计数出错不会移动任何一行引文。

### 验收判据（可复算，取代冻结条数）

冻结的行数判据无法成立：B/C/D 属主在执行期间持续加篇，行数随 records 增长。本车道以
下面三条为准，全部由命令输出判定，不写死数字。

1. 逐车道 `quote_blocks.py <lane>` 退出码 0，无硬错误。散文块在五级回退（exact / nfkc /
   squeezed / span / gapped）全不命中时才是硬错误；非散文块计 `unverified`，无文本论文计
   `layout-only`，图像读取布局计 `ocr-only`，文本层整段缺失的论文计 `text-gap`。
2. `coverage.py` 输出每车道 `rows == coded_groups`（短差 0）、`empty 0`、`dup 0`
   （键为 `paper / chapter_index / chapter / block_index`）。
3. 每车道抽检 30 条，`reports/spot-check-<lane>.md` 重抽，结论写入
   `reports/spot-check-review.md`。

`tools/coverage.py` 打印的行即为判据，README 表格只是某个时点的快照。

## Label handling

B and C use labels outside the 13-job vocabulary: `claim`, `ext:context`, `ext:claim`,
and compound labels such as `interpret+close:handoff`. This lane does **not** rewrite
them. Each row keeps the label exactly as the owning lane wrote it, and the coverage
report prints a second census with the normalised base (`x+close:y` -> `x`, `ext:z` ->
`z`) plus a list of every label that does not fall inside the 13-job taxonomy. Whether
`claim` becomes `interpret` is a vocabulary decision for the merge session, not for this
lane.

## Reproduction

```bash
cd mcm-skill-work
python -I -X utf8 lanes/L7-quote-backfill/tools/quote_blocks.py B
python -I -X utf8 lanes/L7-quote-backfill/tools/quote_blocks.py C
python -I -X utf8 lanes/L7-quote-backfill/tools/quote_blocks.py D
python -I -X utf8 lanes/L7-quote-backfill/tools/quote_blocks.py E
python -I -X utf8 lanes/L7-quote-backfill/tools/quote_blocks.py F
python -I -X utf8 lanes/L7-quote-backfill/tools/coverage.py
python -I -X utf8 lanes/L7-quote-backfill/tools/spot_check.py B
python -I -X utf8 lanes/L7-quote-backfill/tools/spot_check.py C
python -I -X utf8 lanes/L7-quote-backfill/tools/spot_check.py D
python -I -X utf8 lanes/L7-quote-backfill/tools/spot_check.py E
python -I -X utf8 lanes/L7-quote-backfill/tools/spot_check.py F
```

`quote_blocks.py` writes one quote file and its level census per lane and fails loudly on
any prose block it cannot verify. `coverage.py` recounts rows against the records and
rewrites `reports/coverage.json` and `reports/coverage.md`. `spot_check.py` redraws the
hand sample for one lane into `reports/spot-check-<lane>.md`.

## Progress

| step | state |
| --- | --- |
| generator, five lanes, zero hard errors | done |
| quotes rows against the records | B 10,333 / C 10,397 / D 5,308 / E 5,024 / F 6,794, shortfall 0, empty 0, duplicate 0 |
| E and F backfill (closed lanes, final counts) | done: E 5,024, F 6,794, 11,818 rows |
| hand sample, 30 rows per lane | done, `reports/spot-check-{b,c,d,e,f}.md`, verdict in `reports/spot-check-review.md` (150 of 150 verbatim, 15 / 10 / 10 / 10 / 7 flagged as non-sentence opens) |
| coverage report and one-command recount | done, `tools/coverage.py` |
