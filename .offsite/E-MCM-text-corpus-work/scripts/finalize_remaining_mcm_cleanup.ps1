$ErrorActionPreference = 'Stop'
$root = 'F:\MCM'
$audit = 'E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5'
$plan = Get-Content -LiteralPath (Join-Path $audit 'f-delete-plan.json') -Encoding UTF8 -Raw | ConvertFrom-Json
$records = @(Get-Content -LiteralPath (Join-Path $audit 'f-removal-journal.tsv') -Encoding UTF8 | Where-Object { $_.StartsWith("REMOVED`t") })
if ($records.Count -ne $plan.files.Count) { throw 'Incomplete removal journal; do not finalize' }
foreach ($row in $plan.files) {
    if (Test-Path -LiteralPath (Join-Path $root $row.path)) { throw "Planned file still exists: $($row.path)" }
    if ($row.retained_copy -and (Get-FileHash -LiteralPath $row.retained_copy -Algorithm SHA256).Hash.ToLowerInvariant() -ne $row.sha256) { throw 'Retained counterpart mismatch' }
}
function Remove-EmptyTree([string]$path) {
    $full = [IO.Path]::GetFullPath($path)
    if (-not $full.StartsWith('F:\MCM\mcm-skill-work\tmp\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Outside scratch root' }
    if (-not (Test-Path -LiteralPath $full)) { return }
    $item = Get-Item -LiteralPath $full -Force
    if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw 'Reparse point' }
    foreach ($child in @(Get-ChildItem -LiteralPath $full -Directory -Force)) { Remove-EmptyTree $child.FullName }
    if (@(Get-ChildItem -LiteralPath $full -Force).Count -eq 0) { Remove-Item -LiteralPath $full -Force }
}
foreach ($group in $plan.directories) {
    Remove-EmptyTree $group.path
    $parent = [IO.Path]::GetDirectoryName($group.path)
    if ((Test-Path -LiteralPath $parent) -and @(Get-ChildItem -LiteralPath $parent -Force).Count -eq 0) { Remove-EmptyTree $parent }
}
$result = [pscustomobject]@{RemovedFiles=$records.Count;RemovedLogicalBytes=$plan.logical_bytes_planned;RedundantPaperTrees=$plan.directories.Count;FreeAtCompletion=([IO.DriveInfo]::new('F')).AvailableFreeSpace;RecoveredFrom='All file deletions finished; fixed PowerShell Split-Path parameter-set error in empty-directory finalization'}
$result | ConvertTo-Json | Out-File -LiteralPath (Join-Path $audit 'f-removal-completed.json') -Encoding UTF8
$result | ConvertTo-Json
