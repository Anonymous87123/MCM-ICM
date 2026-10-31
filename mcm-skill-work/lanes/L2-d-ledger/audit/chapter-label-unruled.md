# D lane — chapter labels with no ruling (left blocked)

These are the 70 rows L9 blocks as `chapter-label-unruled`. They are listed here, not
resolved: a chapter label is a vocabulary ruling and belongs to the user, so no label was
renamed, aliased or merged from this lane. The duplicate-block repair changed none of
them.

Determined by applying L9's own classifier to the current 55 D records: a label that is
absent from `CHAPTERS_14`, `ALIASES`, `STRUCTURAL` and `FRONT_MATTER` and present in
`UNRULED` in `lanes/L9-merge-dryrun/tools/build_rows.py` blocks its rows.

| label | blocked rows | paper | printed chapter |
|---|---|---|---|
| `recommendations` | 24 | P-D-2020-2003723-28f692ff | the recommendation chapter |
| `gcn-evidence` | 9 | P-D-2021-2101855-c4682962 | the graph-convolution evidence chapter |
| `cultural-analysis` | 8 | P-D-2017-67316-f37f83c8 | the cultural-norms chapter |
| `technology-impact` | 7 | P-D-2018-82504-6cc63169 | the technology-impact chapter |
| `our-work` | 7 | P-D-2019-1900007-65267201 | the Our Work chapter |
| `advice` | 5 | P-D-2020-2015044-db9655c7 | the advice chapter |
| `future-considerations` | 5 | P-D-2020-2022868-71331b90 | the future-considerations chapter |
| `illustration` | 4 | P-D-2018-82794-47f05792 | the illustration chapter |
| `heavy-trucks` | 1 | P-D-2018-82794-47f05792 | the heavy-truck chapter |
| **total** | **70** | 9 papers | |

The count matches `stats.json` exactly (`chapter-label-unruled: 70`), so no D row is
blocked for a reason missing from this table.

What a ruling would have to decide, if the user wants these merged rather than blocked:

* `our-work` is the one label here that duplicates a chapter other papers print as a
  subsection of `introduction`; D papers also use `problem-restatement` and
  `problem-analysis`, which L8 already aliased into `introduction`, so `our-work` is the
  only sibling left unruled;
* `recommendations` and `advice` are both closing-advice chapters and would have to be
  ruled either separately or as one label;
* `future-considerations` and `future-improvements` name the same move, and
  `future-improvements` is already aliased to `strengths-limitations`, so leaving one
  aliased and the other unruled is an inconsistency only the ruling can settle;
* `cultural-analysis`, `technology-impact`, `illustration`, `heavy-trucks` and
  `gcn-evidence` are paper-specific chapters with no counterpart anywhere in the fourteen,
  so they cannot be aliased without inventing a target.
