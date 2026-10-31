# Complete text corpus checkpoint — 2026-10-29, v2

## Current truth and authority

The approved full plan remains ACTIVE and unfinished. This checkpoint supersedes
v1's pointers/counts, not its preserved evidence. No full-paper learning closure,
legacy transaction append, installed-skill replacement or non-text review is claimed.

- Current canonical candidate: `reflow-20261029-v8/`.
- Dataset: `dd5596d0901ef048423949ce57864aa095f1a6aa8ec34a793443e4178bb32d9c`.
- All 435 eligible PDFs / 11,552 physical pages extracted and source-hash checked.
- Structural integrity: pass, zero errors, including source PDFs and 2,619 frozen
  legacy inputs. All 954,866 raw source lines have one retained owner or an explicit
  exclusion. This is accounting, NOT proof that all prose is correctly recovered.
- 291,545 typed blocks / 19,496 section CANDIDATES, not verified paragraph counts.
- 427 nonempty abstract candidates, 8 empty unresolved, 0 verified absent.
- Four abstracts have source/paragraph/boundary verification applied (q1–q4).
  Zero complete papers have whole-source acceptance.
- `integrity-reflow-20261029-v8.json`: `source_completeness_accepted: false`.

## Changes completed since v1

1. Added literal source transcription (`scripts/source_text_repairs.py`) with exact
   pre/post text hashes, short explicit replacements/counts, source/raw bindings,
   checked pages, portable evidence and independent validator replay. q2's quotes
   and two visible prose glyphs repaired without polishing author sentences.
2. Opening date, team labels, competition form fields/instructions, oversized titles
   and sparse title covers are retained but separated from default author prose.
   q3's date and q4's form/title no longer contaminate abstract output. q5's team/date
   are no longer counted as an abstract. Sparse-cover rules explicitly protect short
   real abstracts. All machine classifications still require source review.
3. Native PDF blocks no longer dictate paragraph breaks. Added hanging-bullet and
   indented-paragraph tests; q7 now has six main paragraphs plus three list items,
   rather than line-sized fragments, and its following title cover is excluded.
4. Recombine number/title fragments on the same baseline and native block, while
   preserving both original line IDs. q6's next-chapter `1` no longer leaks into abstract.
5. Recognize split ICM Summary/Sheet banners and competition printing instructions,
   restoring q191/q274's previously misclassified abstract prose as candidates.
6. Recognize singular `Content` and spaced dot leaders. The diagnostic number of
   abstracts containing possible directory entries fell from 29 (v7) to 4 (v8).
7. Cross-engine warnings can resolve ONLY by exact whole-page text equality after
   whitespace and alphabetic presentation-ligature expansion. The proof is replayed
   by validation. 564 such diagnostics resolved; canonical author text is unchanged.
8. Reader status now separates complete delivery from processed receipts and refuses
   mutated pending batches or previously processed documents. Old cursors still fail
   against different dataset IDs; there is no automatic migration or acknowledgement.
9. Preview packaging recursively retains review/transcription evidence, validates the
   copied corpus and supports relative data paths. Existing installations are untouched.

## OCR: complete evidence generation, NOT source acceptance

`ocr-empty-frontier-20261029-v1/queue.json` freezes all 49 affected papers / 219
native-empty pages, in original queue order. The resumable worker preserves failed
attempts, validates completed evidence and never changes canonical data in place.

- 219/219 pages completed, 14,628 detected lines, no zero-line OCR result.
- 988 lines score below .95. Scores are diagnostic, not correctness guarantees.
- All 219 pages are integrated as unverified candidates into v6–v8, alongside the
  four earlier opening-page OCR recoveries (223 OCR pages awaiting source review).
- Native originals, OCR boxes/confidence, model/source/file hashes are retained.
- Original renderings stay local; no full PNG or remote OCR request was used.
- q11's cover OCR is separately retained, NOT used as a fake abstract.

## Exhaustive reading evidence

Latest actual field-test run is **v7**, not v8:
`reading-runs/abstract-preview-20261029-v7/`.

- Run ID: `d5264108eda04d0dad9998843e589e68`.
- Seven acknowledged batches; queue positions 1–9 accounted for.
- Eight nonempty candidate abstract queries fully delivered and processed; q5 is
  unresolved/empty, NOT an abstract read. Four were source-verified and processed.
- Cursor: paper_index=9, char_offset=0; no pending batch. Next would be q10 ON v7.
- Actual observations are under `reading-observations/abstract-preview-20261029-v7-*`.
- Frozen status: `reading-status-20261029-v7-at-q009.json`.
- q9's complete preview included wrongly absorbed physical-page2–3 directory text.
  Both pieces were actually read and the defect recorded; v8 repairs that boundary.
- Do NOT reuse this cursor against v8. No v8 actual-reading run has been started.
  These counts demonstrate the reader and discovery workflow, not all-abstract acceptance.
- Previous v3/v4/v5 runs and all their receipts remain preserved. Never sum repeated
  readings across generations into a unique-paper completion count.

## Whole-scope unresolved inventory

`section-candidate-audit-20261029-v8.json` records all 435 papers with source/document
bindings, per-paper findings and open flags, not a selection of good samples.

- Eight empty abstract queries: q5, q11, q94, q162, q165, q167, q169, q170.
  Covers/Contents/direct Introduction are not proof of whole-source absence.
  Search source pages and alternative copies before verified-absence promotion.
- Four possible directory contaminations remain: q20, q176, q277, q343.
- 92 possible same-page abstract envelope exclusions. Some may be true following
  sections; do not automatically import all sibling text or mark them resolved.
- Source-boundary pending19,492; hyphen joins9,681; private-use glyphs5,442;
  cross-page joins5,097; cross-engine differences1,850; Contents-page checks334;
  margin microtext251; OCR source checks223; column order90; malformed Unicode15.
  These 42,475 review flags overlap and are NOT 42,475 proven prose errors.
- q6 still has `deter- mine` and requires a logged line-end word repair; preserve
  the author's differing Runga-Kutta/Runge Kutta spellings, do not silently polish.
- Formula correctness and figure/chart interpretation remain PAUSED. Retain their
  source location and adjacent explanations, do not force non-text review to clear flags.

## Tests, packages and protection

- Latest pytest `tests -q`: 235 passed.
- Latest unittest `discover -s tests -q`: 233 passed.
- Plan protocol validation: pass, zero errors. No legacy history/progress modified.
- New regression cases cover untitled summaries, all-Introduction traversal,
  long exact reconstruction/resume, duplicate parent/child matches, whole-source
  absence proof, OCR frontier resume/tampering, literal repair replay, pre/post
  source mutations, metadata leakage, split headings, paragraph continuity and
  directory/abstract envelope diagnostics. Synthetic test acknowledgements are
  explicitly synthetic, not real-paper AI reading.
- Old unscoped tmp q221 tests previously failed historical-preimage expectations;
  those artifacts/tests remain preserved, not fixed/deleted for a green result.
- v7 preview: `../skill-packages/text-corpus-preview-20261029-v4/mcm-icm-master-skill/`;
  standalone reader works from an unrelated cwd; skill validator passes. 49 installed
  skill files were rehashed unchanged.
- v8 preview target: `../skill-packages/text-corpus-preview-20261029-v5/mcm-icm-master-skill/`.
  Packaging finished:22,398 payload files plus manifest; copied-corpus structural
  validation and skill metadata validation pass. The standalone reader works from
  the unrelated D: project cwd and reports427 nonempty abstract candidates/8 empty.
  All49 installed-skill preimages were rechecked unchanged. This remains a preview,
  never an accepted release or an installation.
- No new subagents, no old-file cleanup/deletion. All native/reflow/prototype/OCR
  generations, source reviews (including superseded q3/q4 staging), installed skill,
  source PDFs and pre-existing dirty/deleted user states were preserved.
- Five bounded JPEG proxies were viewed this context, one per call, total1,171,636
  bytes. No whole session JSONL/base64, image batching or original full PNG output.

## Next safe work

1. The v8 preview is validated as a runnable draft. Keep the installed version unchanged;
   do not repeat packaging or completed OCR/whole-source extraction without a new reason.
2. Fix the four remaining possible directory contaminations and inspect all 92
   possible omissions in deterministic paper order. Review source page prose and
   boundaries, not graphs or formulas. Preserve uncertainty explicitly.
3. Resolve the eight empty abstract cases against complete source/alternate copies;
   verified absence is allowed only with whole-document source coverage.
4. Apply exact literal/paragraph/source-boundary reviews in a new immutable batch,
   not a copied full generation per isolated typo. Continue using all review guards.
5. On the accepted stable generation, start a NEW exhaustive abstract run and actually
   read/observe/ack every deliverable; do not migrate old cursors or auto-generate receipts.
6. Continue Introduction/all substantive author prose and appendices, all defects,
   final source acceptance and strict skill packaging. Never reduce the final objective
   to an OCR pass, 427 abstract candidates, a working preview, or this checkpoint.
