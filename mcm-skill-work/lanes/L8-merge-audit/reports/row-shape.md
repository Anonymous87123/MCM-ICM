# Row shape — one row per group, and the gaps that stop two lanes

Machine source: `reports/recount.json` (same snapshot as `deltas.md`). Counts in the
tables come from `tools/audit.py`; none are typed by hand.

## 1. The two input shapes

**Chapter shape — B, C, D, E, F.** One file per paper, a list of chapter rows:

```
{"chapter": str, "heading": str|null, "pages": [start, end],
 "groups": [[block_n, ...], ...], "jobs": [str, ...], "note": str}
```

`groups[i]` is one printed unit (one or more layout paragraphs glued by OCR or by a
heading at the block tail); `jobs[i]` is that unit's function. `block_n` is the
layout's 1-based paragraph number. The file is the only row source; `jobs-<lane>.jsonl`
restates the same rows with derived evidence (`units`, `evidence`, `stored_count`,
`literal_blocks`) and is never a second source of truth.

**Block shape — A.** One file per paper, a list of chapter rows whose blocks are
already flat and already carry the quote:

```
{"paper": str, "chapter": str,
 "blocks": [{"block_index": int, "job": str, "quote": str, "page": int}, ...]}
```

`block_index` here is a 0-based ordinal **inside the chapter**, not the layout
paragraph number: it restarts at 0 in every chapter (`P-A-2011-11199-cfe6d809` has
one chapter at 0-8 and another at 0-56). A has no `layout/`, no `heading`, no
`note`, no declared `pages`; the page of a block is the only page evidence.

**Quote files.** `quotes-a.jsonl` and L7's `quotes-{b,c,d}.jsonl` both emit one row
per group:

```
{"paper": str, "chapter": str, "block_index": int, "job": str, "quote": str, "page": int}
```

The field name `block_index` is misleading: in B/C/D it is the group's 0-based
ordinal within the chapter (verified: `P-B-2025-2503268-228e0ec5` chapter
`algorithm` has 20 quote rows at 0-19 and the record's groups start at layout block
132). It is not the layout block number and cannot be joined to `layout/`. A's
quote rows use A's own 0-based block ordinal, so there the two meanings coincide.

## 2. Unified merge row

One row per group, fields and provenance:

| field | type | provenance | notes |
|---|---|---|---|
| `paper` | str | record filename stem | equal across all six lanes |
| `type` | `A`-`F` | lane | |
| `chapter` | str | record `chapter` | verbatim, never renamed |
| `chapter_normalized` | str\|null | alias map in `deltas.md` §3 | 14-value vocabulary, `null` for front matter and unruled labels |
| `chapter_index` | int | 1-based print order inside the paper | required: F repeats labels up to 11 times per paper |
| `group_index` | int | 1-based print order inside the chapter | matches the quote row's `block_index + 1` |
| `block_index` | int | first block of the group | layout paragraph `n` for B-F; A's record ordinal, basis recorded |
| `block_index_basis` | str | `layout-paragraph-n` \| `record-ordinal-0` | A only uses the second |
| `blocks` | int[] | record `groups[i]` | the measured blocks glued into this unit |
| `job` | str | record `jobs[i]` | raw, may be `ext:claim` or carry `+close:` |
| `base_job` | str | `job.split("+close:")[0]` minus `ext:` | one of the 13 |
| `close_job` | str\|null | text after `+close:` | one of the 13, else null |
| `quote` | str\|null | A record `blocks[i].quote`, B-D L7 quote row | null for E/F |
| `quote_level` | enum | L7 `match_levels`; A `in-record`; E/F `missing` | see §4 |
| `page` | int\|null | A quote row / L7 quote row | page of the quoted sentence |
| `pages_declared` | [int,int]\|null | record `pages` | A has none |
| `pages_coded` | [int,int] | min/max page of `blocks` from `layout/` | A takes min/max of block pages |
| `heading` | str\|null | record `heading` | A has none |
| `evidence_class` | `prose` \| `structural` \| `references` \| `front-matter` | chapter label + `deltas.md` §3 | `title` rows are dropped, not emitted |
| `source_record` | str | lane path | |
| `source_quote_row` | int\|null | 1-based line in the quote file | null for E/F |

Ordering: `(type, paper, chapter_index, group_index)`.
Dedupe key: `(paper, chapter_index, group_index)`.

Why not the obvious alternatives:

- `(paper, chapter, group_index)` collides in F: 48 papers, 276 extra rows, e.g.
  `P-F-2022-2209952-fcd31d6e` stores `model-establishment` 11 times.
- `(paper, block_index)` collides inside papers with duplicate block references
  (C 23 blocks, D 3) and is meaningless across the two block-index bases.
- `(paper, chapter, block_index)` collides the same way in the quote layer only if
  the quote file were keyed by layout block; it is keyed by ordinal, so it is
  unique today but stops being a join key the moment duplicates are fixed.

## 3. A rows vs B/C/D rows, field by field

| field | A (`records-a`) | B/C/D (`records` + L7 quotes) | E/F (`records` only) |
|---|---|---|---|
| chapter / heading | chapter only | chapter + heading | chapter + heading |
| groups | implicit, one block per group | explicit lists of block indices | explicit lists of block indices |
| jobs | per block | per group | per group |
| quote | inline in record | separate quote file, one row per group | none |
| quote verification level | none (`in-record`) | exact / nfkc / squeezed / span / run / gapped / layout-only / ocr-only / unverified | none |
| block index basis | 0-based per chapter | string `n` from layout, 1-based | same as B |
| pages | per block only | declared `[start,end]` per chapter | declared `[start,end]` per chapter |
| note | absent | present, carries the delta sentence | present |
| jobs JSONL | absent | present, restates the records | present |

Consequence: A rows need a synthetic `chapter_index`/`group_index` (from list order)
and a `pages_declared = null`; B/C/D rows need the quote joined by
`(paper, chapter, group_index)`; E/F rows carry `quote = null` and
`quote_level = missing`.

## 4. Quote-level distribution

From L7 `reports/coverage.json` and the A file. Levels are per row, not per paper.

| level | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| exact | — | 7,917 | 8,300 | 4,119 | — | — |
| nfkc | — | 849 | 813 | 9 | — | — |
| squeezed | — | 490 | 432 | 122 | — | — |
| span | — | 597 | 465 | 153 | — | — |
| run (gapped) | — | 192 | 149 | 59 | — | — |
| layout-only | — | — | 97 | — | — | — |
| ocr-only | — | 72 | — | — | — | — |
| unverified | — | 216 | 148 | 45 | — | — |
| in-record (A, no ladder) | 3,232 | — | — | — | — | — |
| missing (no quote layer) | — | — | — | — | 5,024 | 6,794 |
| **rows** | **3,232** | **10,333** | **10,404** | **4,507** | **5,024** | **6,794** |

`unverified` (409 rows over B/C/D) and `layout-only` (C 97) are the rows whose quote
does not appear verbatim in the extracted text; they are the rows a downstream
consumer must treat as unverified evidence rather than as a quotation of the paper.
E and F contribute no quote rows at all, so every one of their 11,818 rows is a gap
until a quote pass runs.

## 5. E lane — gap per paper

No quote layer. Missing rows = the paper's group count, because every group needs a
quote row and none exists. Lane total: 60 papers, 5,024 rows.

| # | paper | missing rows |
|---|---|---|
| 1 | `P-E-2016-43443-82025ab9` | 73 |
| 2 | `P-E-2016-49630-af20ebac` | 124 |
| 3 | `P-E-2016-52831-df9e4468` | 74 |
| 4 | `P-E-2016-52849-d6e64df0` | 67 |
| 5 | `P-E-2016-53494-99855cf8` | 87 |
| 6 | `P-E-2017-61502-f0a50d47` | 81 |
| 7 | `P-E-2017-65123-e36461ec` | 138 |
| 8 | `P-E-2017-67171-0a99e096` | 95 |
| 9 | `P-E-2017-68242-753e0037` | 108 |
| 10 | `P-E-2017-71672-f2a1a712` | 92 |
| 11 | `P-E-2018-72968-5f2ee223` | 136 |
| 12 | `P-E-2018-73119-79c4dde3` | 85 |
| 13 | `P-E-2018-74971-2b1f503a` | 111 |
| 14 | `P-E-2018-78511-395a90c3` | 141 |
| 15 | `P-E-2018-88902-cefa4db9` | 151 |
| 16 | `P-E-2018-89499-90bc677f` | 90 |
| 17 | `P-E-2018-93840-dffa6997` | 94 |
| 18 | `P-E-2019-1902029-f44b44ca` | 111 |
| 19 | `P-E-2019-1902054-4ff1f32f` | 73 |
| 20 | `P-E-2019-1902917-3fb00373` | 130 |
| 21 | `P-E-2019-1903455-a52f7980` | 130 |
| 22 | `P-E-2019-1916129-cfc06e89` | 109 |
| 23 | `P-E-2020-2008521-e040e3b4` | 135 |
| 24 | `P-E-2020-2010035-cf1cc4f2` | 140 |
| 25 | `P-E-2020-2016287-6ed5334f` | 147 |
| 26 | `P-E-2020-2017963-104327a3` | 108 |
| 27 | `P-E-2020-2021103-996a6655` | 145 |
| 28 | `P-E-2021-2102057-3e6906e7` | 41 |
| 29 | `P-E-2021-2113869-a6c9c257` | 34 |
| 30 | `P-E-2021-2119031-7da0a6d0` | 36 |
| 31 | `P-E-2021-2119893-783934c9` | 43 |
| 32 | `P-E-2021-2122175-f3669e48` | 38 |
| 33 | `P-E-2022-2202171-2ac7357e` | 60 |
| 34 | `P-E-2022-2202666-f7b82c76` | 61 |
| 35 | `P-E-2022-2202838-75410db9` | 67 |
| 36 | `P-E-2022-2203489-75977cc9` | 68 |
| 37 | `P-E-2022-2209336-b759712b` | 66 |
| 38 | `P-E-2022-2216618-127926c7` | 70 |
| 39 | `P-E-2022-2218144-2f85ee8c` | 57 |
| 40 | `P-E-2022-2220714-2e6b46c5` | 67 |
| 41 | `P-E-2022-2223269-9c9b5216` | 71 |
| 42 | `P-E-2022-2223495-07272032` | 72 |
| 43 | `P-E-2023-2301428-46c8d86f` | 74 |
| 44 | `P-E-2023-2305598-54437939` | 74 |
| 45 | `P-E-2023-2307336-5797f8da` | 67 |
| 46 | `P-E-2023-2308000-0f85170c` | 67 |
| 47 | `P-E-2023-2312411-513d8bc7` | 66 |
| 48 | `P-E-2023-2314354-42336b14` | 72 |
| 49 | `P-E-2023-2314817-3fbab10f` | 69 |
| 50 | `P-E-2023-2320131-a457a41e` | 65 |
| 51 | `P-E-2024-2400860-84b8e466` | 83 |
| 52 | `P-E-2024-2401102-4ea16839` | 88 |
| 53 | `P-E-2024-2407414-773ebad2` | 83 |
| 54 | `P-E-2024-2410578-d7df14d8` | 73 |
| 55 | `P-E-2024-2410889-763393c4` | 57 |
| 56 | `P-E-2024-2413552-a32915be` | 56 |
| 57 | `P-E-2025-2502355-f89a99dc` | 61 |
| 58 | `P-E-2025-2508861-c97e23e1` | 62 |
| 59 | `P-E-2025-2515136-5dd4cae6` | 46 |
| 60 | `P-E-2025-2517273-98509d3b` | 35 |

## 6. F lane — gap per paper

No quote layer. Lane total: 48 papers, 6,794 rows.

| # | paper | missing rows |
|---|---|---|
| 1 | `P-F-2016-43181-88427331` | 107 |
| 2 | `P-F-2016-44348-d3da2a69` | 130 |
| 3 | `P-F-2016-46634-153dc78f` | 100 |
| 4 | `P-F-2017-64486-62f12f04` | 138 |
| 5 | `P-F-2017-68940-3e5f9c47` | 129 |
| 6 | `P-F-2017-72197-93a3c66b` | 85 |
| 7 | `P-F-2017-72283-776dd1c3` | 149 |
| 8 | `P-F-2018-83744-386b67db` | 146 |
| 9 | `P-F-2018-87280-fa7e05e4` | 176 |
| 10 | `P-F-2018-88508-de947611` | 162 |
| 11 | `P-F-2018-93036-caae279b` | 153 |
| 12 | `P-F-2019-1904381-2a09d2c8` | 131 |
| 13 | `P-F-2019-1905127-b4a0bea2` | 112 |
| 14 | `P-F-2019-1916375-d9b69c90` | 143 |
| 15 | `P-F-2019-1916704-dd8d036e` | 147 |
| 16 | `P-F-2020-2005623-fc75252e` | 118 |
| 17 | `P-F-2020-2006291-c876ce05` | 128 |
| 18 | `P-F-2020-2009139-c2e6c7af` | 179 |
| 19 | `P-F-2020-2013233-f7fd24e3` | 151 |
| 20 | `P-F-2020-2013733-073f48f7` | 94 |
| 21 | `P-F-2020-2013772-594465e5` | 151 |
| 22 | `P-F-2021-2102185-018cbd61` | 104 |
| 23 | `P-F-2021-2103649-5f40ae4f` | 198 |
| 24 | `P-F-2021-2106074-d0b37839` | 153 |
| 25 | `P-F-2021-2109443-9398701f` | 170 |
| 26 | `P-F-2021-2122374-0c765494` | 144 |
| 27 | `P-F-2021-2123945-e8b5b6e5` | 179 |
| 28 | `P-F-2022-2204803-b65fac0e` | 140 |
| 29 | `P-F-2022-2208238-5a8ba6a9` | 122 |
| 30 | `P-F-2022-2209952-fcd31d6e` | 146 |
| 31 | `P-F-2022-2211240-e209939c` | 138 |
| 32 | `P-F-2022-2218577-d61b87f7` | 123 |
| 33 | `P-F-2022-2220722-8f8dab63` | 153 |
| 34 | `P-F-2022-2224021-25b6c5d5` | 159 |
| 35 | `P-F-2023-2305794-7917e986` | 172 |
| 36 | `P-F-2023-2311258-7008e4b0` | 160 |
| 37 | `P-F-2023-2311517-83b94523` | 174 |
| 38 | `P-F-2023-2315018-a355e166` | 178 |
| 39 | `P-F-2024-2409949-da56f15f` | 141 |
| 40 | `P-F-2024-2413565-15e84639` | 187 |
| 41 | `P-F-2024-2417340-491a7b05` | 178 |
| 42 | `P-F-2024-2422054-7c8f8bf5` | 136 |
| 43 | `P-F-2024-2426941-d347a3c2` | 179 |
| 44 | `P-F-2025-2504223-019dfa54` | 116 |
| 45 | `P-F-2025-2507789-8d9181d0` | 130 |
| 46 | `P-F-2025-2513705-f78c7aca` | 119 |
| 47 | `P-F-2025-2517199-1033f2d4` | 61 |
| 48 | `P-F-2025-2521039-b7738f88` | 105 |

Both gap tables recount exactly: E 5,024 and F 6,794, equal to their group totals in
`recount.json` → `lanes.E.groups` and `lanes.F.groups`.
