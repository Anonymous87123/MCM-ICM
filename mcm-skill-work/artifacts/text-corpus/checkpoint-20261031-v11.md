# Complete text corpus checkpoint — 2026-10-31, v11

Goal remains ACTIVE. Preserve v10 and all older checkpoints, data generations,
failed drafts, packages, source PDFs, installed skills and legacy history.
No agents, cleanup, deletion, installation or legacy closure occurred.

## Accepted current generation

`reflow-20261031-v27`, dataset
`1a11dcf028e3d6a4475d142170b1481c30fc7b804d9abced2ba62772f03c3bf8`.
`integrity-reflow-20261031-v27.json`: structural PASS/errors0,435 papers,
11,552 physical pages,954,866 source lines,292,140 blocks,18,509 candidate
sections,435 continuous author views,9 verified section boundaries and2,619
protected legacy preimages checked. Source completeness FALSE; zero whole-paper
source acceptance. Abstract selections:6 verified,421 present-unverified,
6 verified-absent,2 empty unresolved(q11/q169).

V27 only resolves seven source-checked stale wrap flags: six in q114 and one in
q116. All435 abstract AND all-author text hashes remain identical to acceptedv26;
all other defect counts/statuses remain unchanged. q116 abstract is now verified;
q114 still has an open page1cross-engine review. Hyphen flags9747→9740. Do not
clear q114's other flags or count either paper as whole-source accepted.

## Guarded literal repair and validation

`scripts/source_text_repairs.py` adds explicit `resolve_hyphen_join_review`.
It requires prior literal operations in the SAME proof, their exact operation
chain digest, exact ordered source-line identities, eligible author block kind,
unchanged before/after text hashes and no remaining internal/terminal broken
hyphen fragment. It must be the final operation for the block, resolves exactly
one matching existing defect/flag and leaves every other issue untouched.
Final validation rejects changed text/line IDs/review digest/flag/defect evidence.
Old literal-only proofs still retain their old unresolved flag; no automatic
blanket clearance is added.

Five new meaningful tests cover real compound retention, replay, old-proof
behavior, unresolved fragments, invalid chain/line/operation/duplicate evidence,
and later mutation. Relevant99tests PASS. Full `pytest -q tests`:344 PASS;
`unittest discover -s tests -q`:342 PASS. The mistaken unbounded root pytest
collection was interrupted(session69520,exit1,no test result); it is not a test
failure and was replaced by the correctly scoped full test run. No tests remain
running.

Source-specific stager DONE/PASS:
`scripts/stage_q114_q116_wrap_resolutions.py`. Create-only proofs:
`reviews/20261031/q114-summary-word-repairs-v2.json` SHA256
`0795c4817d15859b40a5941e9082e166ef2f880fd8dfae8a0b886176314b1dc1`;
`q116-summary-word-repairs-v2.json` SHA256
`fdecb13f3aa7a0b844e4372b4e8cee608740041fdbe8fa6b2cb114acb5805a7b`.
`q114-q116-wrap-resolution-preflight-v1.json` binds all unchanged prose/source IDs
and other open defects. Full prospective `span-origin-flow-full-20261031-v21.json`
PASS435/11552/954866,Contents352unchanged,0errors/0review replay conflicts.
`scripts/build_text_corpus_v27.py` completed normally(session66892exit0) and froze
its exact inputs/implementation in `build-request-reflow-20261031-v27.json` and
the new generation. Do not rerun create-only staging/build outputs.

## Transport and separate preview package

`transport-runtime-v27-20261031-v1/`: exact frozen reader/query/text/transport
implementation checked against accepted build request. Reader/query semantics
are unchanged; source-repair code is separately frozen in corpus inputs.
`reader-transport-reconstruction-20261031-v27-v1.json` DONE/PASS(session54003exit0):
abstract/all-author selections each cover435 targets,1,311,958/20,100,561 characters,
438/5,876 batches and40/535 resume replays, exact byte reconstruction within
6000-token/32768-byte caps. It creates ZERO AI reading receipts and proves no
source completeness or comprehension.

New separate package DONE/PASS(session83908exit0):
`artifacts/skill-packages/text-corpus-preview-20261031-v14/mcm-icm-master-skill`,
23,833 files, datasetv27, explicitly PREVIEW. Source and copied audits pass.
`package-smoke-v14-20261031/report.json` DONE/PASS: unrelatedcwdC:\Users\Lenovo,
default relative attachment435targets, missing DB fails closed, pending batch
replays identically,0AIacks/full-read acceptanceFALSE. Installed base
`C:\Users\Lenovo\.claude\skills\mcm-icm-master-skill` unchanged.
All previous packages/runtimes remain intact. No live tool processes remain.

## Actual reading, still frozen oldv16

Run `reading-runs/abstract-preview-20261030-v16`, ID
`541d2520dc494e22a4ae952bd718d398`, dataset
`7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65`.
Resume ONLY the original frozen packagedpreviewv8 reader with oldv16corpus;
never use mutable/v27reader or silently transfer completion to a new dataset.

-235 acknowledgements000000–000234; cursorpaper_index235/char0; no pending batch.
 Nextq236NOTrequested.227 nonempty candidates fully processed,6 existing absences
 accounted for,2 empty unresolved.4 source-verified-and-processed in this old run.
-This continuation actually read35 additional candidate papers(q201–235) in38
 batches000197–000234. Longq207/q208/q214read both delivered parts before being
 marked whole. No automatic acknowledgement loop or language cards were used.
-New source issues include q207page2title/control/date leakage; q208two complete
 Summary regions repeated across1–2(do not deduplicate without source proof);
 q214marketing letter and a flattened recommendation object mixed into abstract;
 widespread keyword tails/watermarks, sentence breaks, word wraps and joined
 punctuation. Every delivered candidate text was read, including contamination.
-Reading observations retain method failures, rejected variables, uncertainty,
 conditional comparisons, separate metric definitions/horizons and different
 policy actions. Author technical/spelling claims are not silently corrected.
-`reviews/20261031/reading-source-issues-v16-through-q235-v1.json`:235receipt
 bindings validated,507 raw historical explicit issue observations/198papers,
 two prior observation corrections preserved/validated. This is NOTa live
 unresolved defect total. Throughq230snapshot495/193also retained. Original
 receipts and batches unchanged; snapshots add no AI processing receipts.

## Source/layout work and image guard

This context used8JPEGs/3,005,868bytes: q11overviews10–13andq169overviews01–04,
one per tool call, each<450000bytes. NOmore images before context compaction.
Formula verification and figure/table interpretation remain PAUSED.

-q11 `P-A-2012-14990-e2428f0d`: all42native pages had already been read; this
 continuation completes visual heading/layout coverage1–42. New bounded findings
 `reviews/20261031/q011-pages31-42-layout-findings-v1.json` cover final12pages.
 Editor letter on38is preserved as separate correspondence, not abstract.
-`scripts/stage_q011_absence_review.py` DONE/PASSexit0: exact42page/native/layout
 coverage, inspected JPEG hashes, all prepared native/raster/proxy hashes,
 independent strictUTF8pdftotextzeroAbstract/Summaryoccurrences,604-record and
 local filename alternative-copy check. Only same42-page PDF exists locally.
 Create-only `q011-whole-source-layout-findings-v1.json` and
 `q011-abstract-absence-v1.json`,109portable evidence files, source-local absence
 STAGED ONLY. Not applied tov27; q11there remains unresolved. It does not approve
 all prose, chapters or external source completeness. All older pending-image
 findings remain preserved rather than rewritten.
-q169 `P-C-2011-8882-54492a1f`: coverage now physical1–15. New
 `q169-pages4-15-layout-findings-v1.json` covers12pages with exact JPEG bindings
 PASS. Remaining overviews05–08cover16–27, not viewed. No abstract absence yet.
 Earlier all27native prose census remains valid; do not repeat it.
-New disk-only source bundles from acceptedv27, native/PDF/hash-bound:
 `q207-summary-title-pages-v1` pages1–3,
 `q208-repeated-summary-pages-v1` pages1–3,
 `q214-summary-letter-pages-v1` pages1–3. All nine JPEGs prepared, NOTvisually
 inspected or counted as image transfers/source acceptance. No formula/figure
 learning. Priorq195pages1–3/q198pages1–4/q137pages1–2/q93opening bundles remain
 prepared/unread as previously recorded.

## Next concrete work

After compaction: q169remaining4overviews, then source-bound absence proof if
appropriate; combine with stagedq11absence in a new immutable generation after
the required exact preflight/replay. Do not use currentv27wrap-only build as a
waiver for new proofs. Then repair individualq93/q137/q110Introduction and
q195/q198/q207/q208/q214summary/letter/title/duplicate boundaries, preserving all
author prose and separate letters. Actual abstract traversal resumes atq236using
frozenv8reader/oldv16. All remaining author chapters and source fidelity require
their own full acceptance; current structural/transport passes do not finish
the user goal. Continue autonomously; do not request already-given permissions.
