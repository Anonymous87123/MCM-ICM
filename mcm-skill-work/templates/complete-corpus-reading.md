# Complete-section corpus reading

The canonical layer contains source-linked ordered blocks and printed section
hierarchy. Continuous chapter Markdown and SQLite are derived views, not a new
collection of selected quotations. Every corpus generation is immutable.

Each paper in generations that declare `author_view_policy` also offers
`papers/PAPER_ID/author.md`: one continuous view identical to the complete
`all_author_text` selection, followed by a single export newline. Source comments
and page furniture do not interrupt its paragraphs. `author.source-map.json`
binds its bytes to `document.json` and records every included block's exact
character offsets, original section and physical pages. Offsets use Unicode code
points. Checked cross-page paragraph links remain continuous; unreviewed links
remain visible as unresolved defects. `full.md` separately preserves all source
blocks and their classification. Neither Markdown view certifies source fidelity.
Use the reader's batch/acknowledgement chain for exhaustive-reading requests;
opening a Markdown file alone does not advance a receipt or prove it was read.

## Commands

From the skill directory:

```text
python scripts/corpus_reader.py sections
python scripts/corpus_reader.py queries
python scripts/corpus_reader.py start --section abstract --scope all --mode exhaustive --run-dir reading-runs/abstract-001
python scripts/corpus_reader.py next --run-dir reading-runs/abstract-001
python scripts/corpus_reader.py ack --run-dir reading-runs/abstract-001 --completion-marker MARKER --observations observations.json
python scripts/corpus_reader.py status --run-dir reading-runs/abstract-001
python scripts/corpus_reader.py resume --run-dir reading-runs/abstract-001
python scripts/corpus_reader.py start --section all_author_text --scope all --mode exhaustive --run-dir reading-runs/all-author-001
python scripts/corpus_reader.py coverage --run-dir reading-runs/abstract-001 --run-dir reading-runs/all-author-001 --report all-chapter-coverage.json
```

`--scope all` is the default; explicit A-F/year filters are supported. Abstract,
Summary, Summary Sheet and 摘要 share the abstract role. For an exact printed
heading use `start --section "PRINTED TITLE" --title ...`. All matching sections
and their descendants are read in document order, without duplication. A missing
heading is not proof a section is absent. Unknown/unverified content stays visible
in coverage and blocks strict completion.

For author-section queries, descendant Contents, References and AI disclosure
subtrees are excluded even if a pending heading hierarchy nests them under the
requested chapter. This is role-based exclusion, not deletion of sentences that
mention references or AI. Explicitly requesting those non-author roles or printed
titles still returns their separately preserved material.

Use `queries` for problem restatement, problem analysis, assumptions, notation,
explicit tasks1–4, modeling/solution, sensitivity/validation and improvement/evaluation
families. Each returns every matching section and descendant, in original order.
Task queries require printed Task/Problem/Question labels; a chapter numbered3 is
not automatically Problem3. Unmapped or missing headings remain unresolved and
need source mapping, rather than substituting a few readable paragraphs.

`all_author_text` traverses all author sections, including unknown-role sections,
subchapters and appendices. It excludes separately marked Contents, References,
AI disclosure and non-prose furniture/captions/title/keywords. Those source blocks
remain in the database. The coverage report unions acknowledged character ranges
by source block across runs, so overlapping parent/child queries count once and
abstract reading cannot stand in for unread body chapters. Pending batches count
as delivered only. The final release requires all chapters of all435 papers,
not just the abstract checkpoint.

An observations file is a JSON array with exactly one record per paper delivered
in the current batch:

```json
[
  {
    "paper_id": "PAPER_ID_FROM_BATCH",
    "block_ids": ["BLOCK_ID_FROM_BATCH"],
    "observation": "Your substantive observation about the text actually read."
  }
]
```

Do not generate these records in a loop merely to advance the cursor. For stylistic
reading, discuss the paragraph progression, method/result link, claim boundary,
wording and distinctive or contrary choices. Count one paper as one supporting
paper, however many sentences it contributes. The goal is shared mechanisms and
variation, not copying source sentences or forcing every paper into one template.

## Delivery and acknowledgement

`next` replays the same pending batch until acknowledged. Its completion marker
is the final field, so tool truncation is detectable. The acknowledged cursor
advances only after observations and delivered-source references validate. Long
sections continue at exact character offsets; concatenating chunks reconstructs
the complete selected text including separators. Corpus changes invalidate old
cursors. A different dataset requires a new reading run.

Every newly started run also binds the query-policy SHA-256. A policy change
refuses resume under the changed rule. A corpus whose frozen query implementation
differs from the reader blocks strict start until a new immutable generation is
built. An explicitly unverified preview may label that mismatch, but cannot be a
final reading acceptance. Never patch a saved session/receipt to bypass the check.

Use a fresh context when needed. Carry the dataset ID, run directory, confirmed
cursor, and observations forward; do not replace unread chapters with summaries.
The final synthesis may use the accumulated observations, but full originals
remain available for direct comparison. This is serial exhaustive reading, not
one impossible unlimited-context request.

## Readiness

Machine extraction, source verification and AI processing are separate statuses.
The draft preview flag never clears source defects. `full_read_acceptance` can be
true only when the requested scope was entirely processed and every section is
source-verified or backed by a whole-document verified-absence review. Source
completeness itself also requires the corpus validator's separate fidelity audit.
Do not equate a structural integrity pass with source completeness.

Text-only corpus work does not close legacy full-paper transactions, install a
skill, validate equations, or resume figure distillation.
