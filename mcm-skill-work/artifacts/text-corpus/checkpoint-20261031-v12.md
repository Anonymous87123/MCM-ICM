# Complete text corpus checkpoint — 2026-10-31, v12

Goal ACTIVE. Preserve every earlier checkpoint, corpus, failed draft, source PDF,
package, installed skill and legacy history. No cleanup/deletion/revert, live
installation, legacy closure or new agents. Formula verification and figure/table
interpretation remain paused; images/OCR only recover prose and layout.

## Accepted corpus and transport

Current ACCEPTED generation `reflow-20261031-v29`, dataset
`2c90dfb4340b067f261e4a9d1b1f491c5de326f5746db602bca6773aad13e824`.
`integrity-reflow-20261031-v29.json`: structural PASS/errors0,435 papers,
11,552 physical pages,954,866 source lines,292,074 blocks,18,508 sections,
435 continuous author views,10 verified section boundaries,2,619 protected
legacy preimages checked. Abstracts:7 verified,420 present-unverified,
8 source-local verified-absent,0 empty unresolved. Source completeness FALSE;
zero whole-paper source acceptance.42,145 open machine flags overlap and are
not42,145 independently proven text errors.

V28 applied q11/q169 whole-source local abstract absence and restored q236's
intact78-character Apriori prose line falsely classified as a caption(+80chars
including separator). All434other abstract/all-author hashes unchanged.
V29 restored q137's complete five-paragraph2638-character Summary and five exact
discretionary breaks. Laterq137author text and all434other papers unchanged.
Hyphen flags9736;section-boundary flags18498. q137 proof was staged againstv27;
thev29driver explicitly proves only scope_id differs inq137betweenv27/v28,
binds eachscope_id to its frozen scope and preserves both full document hashes.
V28buildsession20764 andv29buildsession68482 completed normally/exit0.

Full prospectivev22/v23 PASS. V29transport report
`reader-transport-reconstruction-20261031-v29-v1.json` DONE/PASS(session14255):
435abstract/all-author targets each;1,312,004/20,100,607 characters;
438/5,876batches;40/535resume replays;byte exact/budget pass. Used immutable
`transport-runtime-v28-20261031-v1/scripts`, whose four hashes matchv29's frozen
build. ZEROAIreceipts/source acceptance. Reader/query behavior unchanged.

Latest completed separate package is still
`artifacts/skill-packages/text-corpus-preview-20261031-v15/mcm-icm-master-skill`,
24,016files/datasetv28/PREVIEW. Its copied audit and
`package-smoke-v15-20261031/report.json` pass: unrelatedcwd, relative attachment,
missing DB fails closed, pending batch replay exact,0acks. Installed base unchanged.
V29has no separate package yet; prefer package the next acceptedv30if appropriate.

## ACTIVE JOB — do not restart

`session_id45911`: `python -X utf8 scripts/build_text_corpus_v30.py` is running.
Last output reachesq300. Candidate `reflow-20261031-v30` is NOT ACCEPTED until
normal exit and `integrity-reflow-20261031-v30.json` exists with all guards passed.
Do not edit core/driver while running. Preserve any failed candidate; do not
rerun create-only build blindly. Other sessions listed above are complete.

V30adds ONLYq256's source-checked complete three-paragraph Summary. Request
freezes every prior proof/OCRinput, exact prospective audit/implementation,
scope-onlyv28→v29q256binding transfer, local before/after defect counters,
all434other abstract/all-author text/status hashes and all laterq256author prose.
No blanket defect clearance or whole-source approval. Check final guard results.

## q256 complete local restoration staged

`P-C-2025-2501869-dbf7e00e`,25pages,PDFSHA
`dbf7e00e8159524369ff310c63f1dfba4c4cad9bf60219528e029faba92eacb1`,
rawSHA`df25bd2db136453da646fa68c3c017c3e77df5995b6424bc474e4d35f0479d93`.
All three bounded opening JPEGs and page1native author text actually read.
Page1Summary has3paragraphs; ordinary introduction in Question2 was falsely
classified a heading, omitting the rest ofQuestion2and allQuestion3. Page2is OCR
Contents/promotion;page3starts actualIntroduction.687tiny margin m glyphs are
retained together as furniture, not deleted or interpreted as formulae.

`scripts/stage_q256_summary_restoration.py` DONE/PASS. Preview actually read:
3433chars/SHA`015376f13d1b34c3acb8af5f5e3472e6c98fce06ab8c5052654bc2899ae09fee`.
Three paragraphs/every source line accounted exactly once/four exact wraps,
two paragraph wrap flags resolved. Correct two-stage compound retained.
Proofs in `reviews/20261031/`:
-`q256-summary-layout-v1.json` SHA
`3ba90221b73fcb3980fc89e9b67dd383c9e86df543f174cb6950e6d006958072`;
-`q256-summary-word-repairs-v1.json` SHA
`e3ef2e0a2dde4656e9ba6e0c01f02fa500823da8e288756e3e89a299a9a227a6`;
-`q256-summary-source-review-v1.json` SHA
`53e143d7b7e49828ee4766f431fd5c34d6994a7d89b34ec44646bcf6990e6941`.
Preflight/preview/findings/native diagnosis retained. First stager attempt failed
before any output because automatic microtext exclusion removed reviewed IDs.

Small core fix `scripts/text_corpus.py`: explicit source-reviewed groups precede
generic microtext exclusion. Unreviewed behavior unchanged. Source-reviewed
furniture stays in declared groups. New `tests/test_reviewed_microtext.py`2tests;
full scoped pytest346PASS/unittest344PASS. Exact result in
`source-layout-microtext-tests-20261031-v1.json`. Core SHA
`442502056bb0d339ecf3348b406cf8d4260d49ee67329950f0c6309ef29aa82f`.
Full prospectivev24PASS435/11552/954866,Contents352unchanged,0errors/0replayconflicts.

## q248 staged; q244 next individual restoration

q248 `P-C-2024-2406176-bd7757f9`: both opening JPEGs and every page1native line
actually read. Five author paragraphs; native9line6 observations. must precede
line7 The significance on the same printed baseline. Existing flow interleaved
them. Keep source wording base on and inline mathematical glyphs unchanged.
`stage_q248_summary_restoration.py` DONE/PASS;3296-character preview actually read,
SHA`c58e60d76c0ad86a3b41e909ffa34e3e0e8a7d310b763b7fe9c4c9600c8444d1`.
One exact cap-/tures repair; full keyword tail separated; later author text and
all source IDs unchanged. Staged againstv29, NOT yet applied to accepted corpus.
Proof hashes:layout`1e7a91a286180b0e158ef86a326c2436261af1903bd42754f9a553f353b322ed`;
word-repairs`fa1a61a4ab5b5247113a469f93f4b94b6092e8b35492efb829154f7ee0758da1`;
source-review`b18a6984b1ba542e08fe0bc4063633b5da3240baba1e21b84f1d2a1ff6280824`.

q244 `P-C-2024-2401298-07d37078`: both opening JPEGs AND all page1native lines
now actually read. `q244-opening-layout-findings-v1.json` preserves earlier visual
findings(native pending at writing); new native read happened afterward.
Exactly7author paragraphs native10–16;formnative2–6;two-line papertitlenative7/8;
Summarynative9;two-line Keywordsnative17;watermark/promotionnative0/1/18–21.
Inline Performance Metrics/Momentum Existence/Prediction/Predictive Analysis/
Coaching Strategies(Memo) labels belong inside Summary, not separate chapters
or an actual memo. Preserve fails-to-reject randomness/not overwhelmingly
conclusive despite assertive title/closing. Nine author discretionary breaks:
mod-/eling,Wimble-/don,instanta-/neous,com-/petition,dif-/ferences,
synthesiz-/ing,com-/petitive,rigor-/ous,appli-/cable. Keywords Perfor-/mance is
stored separately. NO q244repair proof or source approval staged yet.

q236 full paragraph continuity still pending despite its accepted bounded line
classification repair. Do not drop/rebind its existing proof without exact
transfer. Other prepared but unread bundles q93,q195,q198,q207,q208,q214 remain.
q110intro andq96remainingbody also pending as previously recorded.

## Actual reading remains frozen OLDv16

Run`reading-runs/abstract-preview-20261030-v16`,ID
`541d2520dc494e22a4ae952bd718d398`,dataset
`7ccbf227d7b1409eae38fb9744f1d2a4fbc46c0b4e9ab7a0cc33224e78106f65`.
Resume ONLY original packagedpreviewv8reader with oldv16corpus; never silently
transfer receipts to newer data.263acks000000–000262,throughq263,cursor263/0,
255nonempty candidates processed,6old verified absences,2old empty unresolved,
4old sourceverified-and-processed. NO pendingbatch;nextq264NOTrequested.
No autoackloop. New observations000258–000262 include form/keyword contamination,
same-page word/paragraph seams and exact metric/causal/scope limitations.
q263source callsMalaysia a first-medalist candidate; keep author wording separate
from extraction errors rather than silently fact-correcting it.

Latest issue snapshot throughq261:591rawhistorical explicit issues/224papers,
2observation corrections validated. NOTlive unresolved count. q262/q263receipts
are newer than this snapshot; refresh later. Older snapshots/receipts preserved.

## Image guard and next steps

This context used7individual JPEGs/2,317,107bytes:q2561–3,q2481–2,q2441–2.
At most ONE more proxy before compaction; never exceed8or4MiB. No original PNG
was transmitted. Future full-page proxies≤450000bytes,one per tool call.

Poll45911; ifv30passes, freeze exact new runtime and verify transport, then
separatePREVIEWpackage/smoke. Finishq244source-bound native restoration and
combine with stagedq248in next immutable generation after full prospective
replay; do not editv30inputs mid-build. Continue actual readingq264onoldv16and
record each fully delivered batch before acknowledging. User goal requires all
chapters/all papers/source fidelity, not only all abstracts or machine passes.
