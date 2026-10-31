# MCM complete-text offsite backup

This snapshot includes working F-MCM files and the E: current v49, accepted v48, reader-required v46 databases, reading receipts, frozen runtimes and recovery evidence.

Files above100MiB are split under `.offsite/chunks/`; the local originals are unchanged. The SHA-256 manifest maps every original file to its exact bytes.

After cloning, verify without another data copy:

`python .offsite/restore_backup.py --checkout .`

Restore into a NEW directory (allow enough free disk):

`python .offsite/restore_backup.py --checkout . --restore-to X:/new-empty-path`

The tool creates F-MCM/ and E-MCM-text-corpus-work/ beneath that destination. It never overwrites existing files. NTFS compression/hardlink relationships are not restored.

The backup is public at the user's explicit request. Obsolete copies, caches/private runtime and interrupted archives are excluded. This is storage preservation, NOT proof that all source sections are correct or AI-read.

## Exact-byte checkout

On Windows, use a short destination and enable long paths. Example:

`git -c core.autocrlf=false -c core.longpaths=true clone https://github.com/Anonymous87123/MCM-ICM.git X:/mcm-backup`

The generated root `.gitattributes` disables newline conversion for this frozen backup. It is backup metadata, not a modification of the original F: files.

