# F:/MCM obsolete-generation cleanup — completed

The user explicitly chose **manifests only, permanent deletion of old copies**.
Full recoverable archives were therefore stopped; there is no promise that old
generation payloads can be restored. Current data, originals and learning/reading
evidence were retained.

## Measured outcome

- Removed: 32 obsolete reflow generations and all 17 obsolete preview packages.
- Removed file count: 1,088,001; removed logical bytes: 119,124,749,322.
- F:/MCM after cleanup: 139,352 files / 28,150,893,422 bytes (26.22 GiB).
- Before size reconstructed from the unchanged remaining tree plus the exact
  removed inventory: 147,275,642,744 bytes (137.16 GiB), about 81% reduction.
- F: available at final measurement: 117,907,939,328 bytes (about 109.81 GiB).
- This pass observed 22,182,010,880 additional free bytes. Logical directory size
  dropped much more because the first cleanup had already physically deduplicated
  repeated hardlinked data. These two recovery figures must not be added twice.

Actual evidence: `removal-completed.json`, `removal-progress.tsv`,
`mcm-size-after.json`, `plan.json`, and `manifest-only-ready.json`.

## Preserved

- F: native extraction base: `text-corpus/native-20261029-v1`.
- F: v16 corpus required by the completed abstract reading session:
  `text-corpus/reflow-20261030-v16`.
- E: current v49, accepted v48, active v46 author-reading dataset and reader
  runtimes/source stages unchanged. No AI processing receipts were created.
- 604 original source PDFs, 2,619 protected historical inputs, 2,505 reader files,
  core history/progress/compliance and E: catalog/scope/SQLite bindings checked:
  5,739 preserved bindings all PASS.
- 870 retained native/v16 structured-paper documents checked against their
  frozen hashes: PASS. Their available SQLite hash bindings also pass.
- Git history, older paper-learning assets, staged evidence and temporary work
  were not indiscriminately deleted. F:/CUMCM and its active OCR job were untouched.

Proof: `preservation-before.json` and `preservation-after.json` (no errors).

## Retained manifests

`source-before.tsv` lists every removed file/directory with its relative path,
type, length and timestamp. `retained-manifests/` holds 113 compressed corpus
catalogs/scopes/package manifests, verified after compression. Their frozen
hashes and exact source paths are listed in `manifest-only-ready.json`.
These are inventories, not full payload backups. Do not recreate all old
directories merely to satisfy stale historical links.

## Largest remaining MCM components

| Component | Approx. logical GiB | Reason retained |
| --- | ---: | --- |
| mcm-skill-work/tmp | 7.52 | Existing staged/temporary evidence; not in the approved obsolete-generation list |
| .git | 5.79 | User repository/history; not pruned |
| artifacts/text-corpus | 5.16 | Two required F: bases plus OCR/source-review evidence and reader records |
| artifacts/papers | 4.47 | Prior paper extraction/learning assets |
| MCM-ICM-master | 1.59 | All original source PDFs |

The obsolete-preview directory now has zero child packages. Only native and v16
remain among the F: native/reflow generations.

## Explicit unresolved E: scratch cleanup

Execution policy rejected both attempted cleanup commands for this turn's
abandoned E: backup scratch. No alternate tool/command was used to bypass the
rejection. These **eight stopped, incomplete files still exist**, approximately
4,327,197,427 bytes (4.33 GB total):

- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v1/obsolete.tar.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v1/manifest.jsonl.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v2/obsolete.tar.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v2/manifest.jsonl.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v3/obsolete.tar.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v3/manifest.jsonl.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v4/obsolete.tar.gz`
- `E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v4/manifest.jsonl.gz`

These are not current paper data or a complete recoverable archive. They remain
a disclosed cleanup exception; do NOT claim the E: scratch was removed.

## Recurrence guard

No new full generations/packages on F:. The existing E: storage preflight must
be used with real allocation estimates, 2x headroom and a 20 GiB reserve. Before
resuming a long full-corpus build loop, implement incremental/immutable-content
reuse and bounded retention; moving unbounded full-copy generations to E: is
not a storage design fix. Frozen shared files must never be edited in place.

No paper-learning completion count, source-fidelity acceptance, formula review,
figure distillation, transaction history or skill installation was advanced.
