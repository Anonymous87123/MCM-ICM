# Remaining F:/MCM cleanup — 2026-10-31

## Outcome and stopping boundary

F: had 117,797,564,416 bytes free at this pass's baseline and
124,478,001,152 bytes at final measurement: an observed increase of
6,680,436,736 bytes (6.22 GiB). Other F: activity can change volume free space.

F:/MCM now contains 132,781 files / 26,821,527,414 logical bytes (24.98 GiB).
The unique-file, compression-aware data-size estimate is 19,863,996,334 bytes
(18.50 GiB). This estimate uses GetCompressedFileSize once per NTFS file identity;
it excludes directory/MFT overhead and uncompressed cluster slack. Subdirectory
estimates must not be added together because some retained files share storage.

No further large deletion candidate was established as safe. Stop here rather
than deleting unique/different historical evidence, live reader dependencies,
original PDFs, paused figure assets or Git history merely to reduce folder size.

## Applied operations

- Removed 6,571 untracked duplicate/cache files, 1,329,367,403 logical bytes.
  Ninety closed-paper temporary extraction trees were fully byte-identical to
  retained official paper files. Every target and retained copy passed full
  SHA-256 checks. Untracked regenerable Python/pytest caches were also removed;
  tracked cache files, frozen runtime files and paused-lane caches were retained.
- Kept 142 extraction groups with unique/different bytes. Kept the earlier
  explicit keep-list and paths mentioned in transaction history.
- Losslessly NTFS-compressed 9,520 unique generated-text files / 10,633 paths,
  retaining the paths and their SHA-256 hashes: reported data-size reduction
  4,123,652,351 bytes. A supplemental pass verified 1,426 more files and reduced
  reported data size by 219,500,086 bytes. No SQLite, Git pack, source PDF,
  active reader receipt or image was compressed by these passes.
- Shared storage for 2,521 byte-identical closed-paper PNG scratch copies with
  their retained official rasters. All existing paths remain and an independent
  full hash/NTFS-identity pass verified all 2,521 pairs. Duplicate data shared:
  1,120,638,634 bytes. These are immutable historical rasters: NEVER modify an
  existing shared file in place; produce new corrections at new paths.

Deletion, compression and sharing figures describe different effects. Do not
sum logical folder reductions with physical recovery from earlier cleanup passes.

All 6,571 file deletions finished before a PowerShell Split-Path parameter-set
error affected empty-directory finalization. The finalizer checked the complete
removal journal and retained-file hashes, then finished empty-directory cleanup;
no missing file was recreated or deletion plan blindly rerun.

## Preservation and machine evidence

`preservation-after.json` passes with no errors:

- 604 original source PDFs;
- 2,619 protected historical inputs;
- 2,505 reader files;
- 5,739 total unique protected bindings;
- 870 retained native/v16 structured-paper document hashes and available SQLite
  hash bindings.

Evidence files in this directory:

- `inventory.jsonl`, `inventory-summary.json` — complete pre-cleanup path inventory;
- `f-delete-plan.json`, `f-removal-journal.tsv`, `f-removal-completed.json`;
- `ntfs-compression-plan.json`, `ntfs-compression-journal.jsonl`,
  `ntfs-compression-completed.json` and the corresponding supplemental directory;
- `closed-raster-sharing-plan.json`, `closed-raster-sharing-journal.tsv`,
  `closed-raster-sharing-completed.json`;
- `preservation-before.json`, `preservation-after.json`, `final-storage.json`.

## E: scratch remains BLOCKED — not completed

The tool execution policy rejected this turn's normal guarded Remove-Item
operation before it executed. No alternate command/tool/script was used to
bypass that denial. A subsequent read-only check confirmed that all eight
stopped partial-archive files remain, exactly 4,327,197,427 bytes (4.33 GB):

| File | Bytes |
| --- | ---: |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v1/obsolete.tar.gz | 615490852 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v1/manifest.jsonl.gz | 7887490 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v2/obsolete.tar.gz | 1146039920 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v2/manifest.jsonl.gz | 12124090 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v3/obsolete.tar.gz | 494905513 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v3/manifest.jsonl.gz | 5418787 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v4/obsolete.tar.gz | 2026321137 |
| E:/MCM-text-corpus-work/archives/F-MCM-obsolete-generations-20261031-v4/manifest.jsonl.gz | 19009638 |

The user explicitly approved deleting these exact files. If removing them
manually in File Explorer, delete only these eight files, not their parent
directories: v4 contains the required inventories, 113 retained manifests and
preservation reports. Do not claim these partial archives are complete backups.

## Retained data and recurrence prevention

- F: native-20261029-v1 and reader-required reflow-20261030-v16 remain.
- E: v46/v48/v49 and actual reader receipts remain unchanged.
- Git count-objects reports zero garbage and zero prune-packable objects; Git
  history/packs were not pruned or rewritten.
- No other project/process was stopped. F:/CUMCM OCR was left alone.
- No new full corpus/package generation, paper-learning receipt, formula/figure
  distillation, transaction, progress completion or skill installation occurred.
- Keep the storage budget preflight. Before resuming long construction loops,
  implement incremental immutable-content reuse and bounded retention; do not
  relocate unbounded full-copy generation to E:.
