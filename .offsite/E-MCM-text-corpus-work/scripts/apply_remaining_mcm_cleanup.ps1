$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$root = 'F:\MCM'
$audit = 'E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5'
$plan = Get-Content -LiteralPath (Join-Path $audit 'f-delete-plan.json') -Raw -Encoding UTF8 | ConvertFrom-Json
if ($plan.root -ne $root -or $plan.files.Count -ne 6571 -or $plan.logical_bytes_planned -ne 1329367403) { throw 'Unexpected approved inventory' }
function Assert-SafePath([string]$path) {
    $full = [IO.Path]::GetFullPath($path)
    if (-not $full.StartsWith($root+'\',[StringComparison]::OrdinalIgnoreCase)) { throw "Outside MCM: $path" }
    $item = Get-Item -LiteralPath $full -Force
    while ($null -ne $item -and $item.FullName -ne 'F:\') {
        if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw "Reparse point: $($item.FullName)" }
        if ($item -is [IO.FileInfo]) { $item = $item.Directory } else { $item = $item.Parent }
    }
}
$tracked = @{}
git -c core.quotepath=false -C $root ls-files | ForEach-Object { $tracked[$_.ToLowerInvariant()] = $true }
if ($LASTEXITCODE -ne 0) { throw 'Tracked-file inventory failed' }
$before = Get-Content -LiteralPath (Join-Path $audit 'preservation-before.json') -Encoding UTF8 -Raw | ConvertFrom-Json
$protected = @{}
$before.bindings.PSObject.Properties | ForEach-Object { $protected[$_.Name.ToLowerInvariant()] = $true }
$total = 0L
foreach ($row in $plan.files) {
    $path = Join-Path $root $row.path
    Assert-SafePath $path
    if ($row.tracked -or $tracked.ContainsKey($row.path.ToLowerInvariant()) -or $protected.ContainsKey($path.ToLowerInvariant())) { throw "Protected input: $path" }
    $item = Get-Item -LiteralPath $path -Force
    if ($item.Length -ne $row.bytes -or (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant() -ne $row.sha256) { throw "Source changed: $path" }
    if ($row.retained_copy) {
        Assert-SafePath $row.retained_copy
        if (-not $row.retained_copy.StartsWith($root+'\mcm-skill-work\artifacts\papers\',[StringComparison]::OrdinalIgnoreCase)) { throw 'Invalid retained copy' }
        if ((Get-FileHash -LiteralPath $row.retained_copy -Algorithm SHA256).Hash.ToLowerInvariant() -ne $row.sha256) { throw "Retained copy changed: $path" }
    } elseif ($row.reason -ne 'untracked regenerable Python/pytest cache') { throw 'Not disposable' }
    $total += $item.Length
}
if ($total -ne $plan.logical_bytes_planned) { throw 'Byte inventory differs' }
$freeBefore = ([IO.DriveInfo]::new('F')).AvailableFreeSpace
$journalPath = Join-Path $audit 'f-removal-journal.tsv'
$stream = [IO.StreamWriter]::new([IO.FileStream]::new($journalPath,[IO.FileMode]::CreateNew),[Text.UTF8Encoding]::new($false))
$removed = 0
try {
    $stream.WriteLine("state`tpath`tsha256`tbytes")
    foreach ($row in $plan.files) {
        $path = Join-Path $root $row.path
        $stream.WriteLine("PREPARE`t$path`t$($row.sha256)`t$($row.bytes)"); $stream.Flush()
        Remove-Item -LiteralPath $path -Force -ErrorAction Stop
        if (Test-Path -LiteralPath $path) { throw "Not removed: $path" }
        $stream.WriteLine("REMOVED`t$path`t$($row.sha256)`t$($row.bytes)"); $stream.Flush()
        $removed++
        if ($removed % 1000 -eq 0) { Write-Output "Removed $removed / $($plan.files.Count) verified duplicates/cache files" }
    }
    foreach ($group in $plan.directories) {
        $dirs = @(Get-ChildItem -LiteralPath $group.path -Directory -Recurse -Force | Sort-Object { $_.FullName.Length } -Descending)
        foreach ($d in $dirs) { if (@(Get-ChildItem -LiteralPath $d.FullName -Force).Count -eq 0) { Remove-Item -LiteralPath $d.FullName -Force } }
        if (@(Get-ChildItem -LiteralPath $group.path -Force).Count -eq 0) { Remove-Item -LiteralPath $group.path -Force }
        $parent = [IO.Path]::GetDirectoryName($group.path)
        if ((Test-Path -LiteralPath $parent) -and @(Get-ChildItem -LiteralPath $parent -Force).Count -eq 0) { Remove-Item -LiteralPath $parent -Force }
    }
} finally { $stream.Dispose() }
$result = [pscustomobject]@{RemovedFiles=$removed;RemovedLogicalBytes=$total;RedundantPaperTrees=$plan.directories.Count;FreeBefore=$freeBefore;FreeAfter=([IO.DriveInfo]::new('F')).AvailableFreeSpace}
$result | ConvertTo-Json | Out-File -LiteralPath (Join-Path $audit 'f-removal-completed.json') -Encoding UTF8
$result | ConvertTo-Json
