# 2026-10-25 integrity repair — checkpoint, not final completion

User priority: repair existing debt first; content/language work may proceed; figure/chart distillation is paused. No source PDF, existing figure deliverable, previous transaction, or another session's draft was deleted. Temporary prospective history files created by this repair alone were removed after prospective validation. No images were transmitted.

## Completed corrective work

- 38 papers repaired through 38 append-only, present-time metadata transactions: `TX-000515-046318191719` through `TX-000552-c43ecd1213a0`.
- 49 staged paper/rule data files changed: 38 cards, five observation files, five audits, and the C rule catalogue, in addition to the prescribed history/progress/derived-report bookkeeping. All original changed-file bytes remain in `tmp/integrity-repair-20261025-v1/before/`; all 86 staged preimage hashes were rechecked with zero errors. The other 37 staged card proposals remain uninstalled and their live preimages unchanged.
- Restored 258 missing historical evidence IDs from exact local snapshots, preserving all newer observations and recording source paths, source SHA-256 and original schema values. This restores references; it is not new learning or proof of earlier manual review.
- Conservatively normalized 15 legacy proposals to unpromoted `seed` / `low`; the original values remain recorded. No rule was promoted because its field format was repaired.
- Every corrected target passed the four unchanged paper validators, including `--require-complete-visual-review`, plus the complete unittest suite, before its transaction. Metadata-only events contain no substantive language/model/visual counts and therefore do not inflate the rolling learning window.
- Final chain errors: 0. Latest-event artifact binding errors: 0. Rolling audit: pass. Latest hash: see the exact event in `history.jsonl`.
- Final regression replay after adding repair/snapshot safety tests: pytest 129/129; unittest 127/127; plan protocol pass. Test fixtures intentionally print negative-case validator output; the complete suites exit successfully. All 2,619 frozen audit input hashes were rechecked unchanged after the final tests.

The new scripts are `stage_integrity_repair.py` (create-only candidate and preimages), `commit_integrity_repair.py` (checked installation and prospective/live transaction protocol), and `audit_integrity_snapshot.py` (read-only all-paper replay). Existing validators and their gate requirements were not weakened.

## Counts must not be conflated

Frozen full-corpus replay: [integrity-audit-20261025-v1.json](integrity-audit-20261025-v1.json).

| Check | Result | Meaning |
|---|---:|---|
| Lifecycle rows labelled closed | 435 / 435 | Existing bookkeeping, not proof of completion |
| Derived protocol + learning-audit checks | 399 / 435 | Up from 361; 36 remaining metadata/audit debts |
| All four current paper gates | 368 / 435 | 67 fail; this check includes complete visual-review status |
| Both derived protocol and four paper gates | 334 / 435 | Still not an independent replay of all earlier manual reading |
| Papers lacking any history event | 37 | Includes 36 remaining protocol-debt papers; do not sum these counts |
| Papers lacking a native paper-closed event | 54 | Includes 17 older baseline/migration cases with other history; these are not the same as the 37 wholly unrecorded papers |

All language/model structural validators pass. One F paper fails 74 learning-audit checks because its 191-unit language inventory no longer matches the 61-unit card/audit. All 67 paper-artifact failures are listed in the JSON report: 66 papers have a non-complete visual-review enum (65 `pending`, one legacy `validated`); one of those D cards also has missing schema fields and a source-path mismatch. The remaining F failure is the count/audit inconsistency.

The 66 non-complete visual states are C2, D32, E31, F1. They have not been changed to `complete`. Existing visual outputs are retained and may be checked read-only for provenance; fresh figure reading/distillation is not authorized by this checkpoint.

## Root causes and unresolved work

1. Some older closing scripts directly set progress to closed without appending a transaction. For example, `tmp/q275-close.py` changes D2015 38727's progress but contains no transaction append. Do not backdate a reconstructed event.
2. Temporary queue-number filenames are not unique paper identities. `q275-close.py` refers to D2015 38727, while `q275-draft.json` and `q275_install.py` refer to C2025 2524070. Do not replay an installer based on its filename; verify embedded paper ID, source SHA and all artifact hashes.
3. Some historical rule references outlived overwritten observation inventories. The exact snapshots recovered here restore the IDs; they do not retroactively certify every original claim.
4. The lightweight derived report does not check all paper-card fields, full visual-review state or closure history. Use the full snapshot as a separate check, not the derived number alone.

37 missing-history papers and all 67 failing-gate papers are enumerated in the frozen JSON report. No historical event was modified or fabricated, and no unfinished paper was made complete by changing a counter.

## Language/content correction progressed without figure work

For `P-F-2022-2211240-e209939c`, the main agent read Summary, Introduction, then all remaining page text through p25. The live 191 units and old 61-unit stage were retained unchanged.

Fresh anti-copy replay on the 191 current original-example pairs fails 113 units (maximum shared run 20 words). The old 61-unit stage has source-copy/placeholder problems too, so it was not restored merely to pass the count check.

Prepared [16 source-backed mechanism candidates and 32 original examples](../staging/integrity-repair-20261025-v1/P-F-2022-2211240-e209939c/style-candidates.json), with a [source/paragraph/organisation correction note](../staging/integrity-repair-20261025-v1/P-F-2022-2211240-e209939c/REPAIR-NOTES.md). The candidates include conditional obstacle-to-method repair, explicit model handoffs, paired-extreme trade-offs, baseline/recovery/horizon comparisons, policy implementation registers, bounded sensitivity reporting and limitation-to-remedy chains.

All 32 new examples pass the existing 8-word anti-copy checker, maximum shared run 3 words. This is draft corrective evidence, not a promoted skill update or a formal completed G0–G8 transaction. Third-party quotations, reference entries, sentence counts masquerading as paragraphs, drifting page anchors and an omitted model-handoff sentence are explicitly identified for formal reconciliation. No zero-new-moves saturation result was invented.

## Next safe work

- Keep L7 paused; preserve its 260 completed records and all drafts.
- Resolve the earliest remaining paper's actual provenance and retain missing proof explicitly. If a present-time recovery is justified, validate it honestly rather than recreating an unproved historical closure.
- Reconcile the F language record/audit from the source-backed draft, preserving the 191/61 preimages and excluding borrowed language from positive evidence.
- Continue language/content correction; do not mark any visual-dependent final gate passed while the corresponding evidence remains pending.
- Rebuild and re-audit after further live changes. The JSON snapshot is frozen to its source hashes and becomes historical if any input changes.
