$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
$archive='E:\MCM-text-corpus-work\archives\F-MCM-obsolete-generations-20261031-v4'
$base='F:\MCM\mcm-skill-work\artifacts\'
$plan=Get-Content -LiteralPath (Join-Path $archive 'plan.json') -Encoding UTF8 -Raw | ConvertFrom-Json
$verified=Get-Content -LiteralPath (Join-Path $archive 'manifest-only-ready.json') -Encoding UTF8 -Raw | ConvertFrom-Json
if ($verified.policy -ne 'user-approved-permanent-deletion-manifests-only') {throw 'Explicit manifest-only retention policy required.'}
if ($verified.files -ne 1088001 -or $verified.logical_bytes -ne 119124749322) {throw 'Unexpected target corpus size/count.'}
foreach($binding in @(@{Name='plan.json';Hash=$verified.plan_sha256},@{Name='source-before.tsv';Hash=$verified.source_index_sha256})) {
    $actual=(Get-FileHash -LiteralPath (Join-Path $archive $binding.Name) -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $binding.Hash) {throw ('Verified archive binding changed: '+$binding.Name)}
}
if (@($plan.roots).Count -ne 49 -or @(Compare-Object @($plan.roots) @($verified.roots)).Count -ne 0) {throw 'Exactly 49 inventoried target directories required.'}
$targets=@()
foreach($target in $plan.roots) {
    $absolute=[System.IO.Path]::GetFullPath($target)
    if (-not $absolute.StartsWith($base,[System.StringComparison]::OrdinalIgnoreCase)) {throw ('Outside artifact root: '+$absolute)}
    $relative=$absolute.Substring($base.Length)
    $allowed=($relative -match '^text-corpus\\reflow-202610(?:29|30|31)-v\d+$') -or ($relative -match '^skill-packages\\text-corpus-preview-202610(?:29|30|31)-v\d+$')
    if (-not $allowed -or $relative -eq 'text-corpus\reflow-20261030-v16') {throw ('Not an approved obsolete generation: '+$absolute)}
    $item=Get-Item -LiteralPath $absolute -Force
    if (-not $item.PSIsContainer) {throw 'Target is not a directory.'}
    $ancestor=[System.IO.DirectoryInfo]::new($absolute)
    while($null -ne $ancestor) {
        if (($ancestor.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {throw ('Refuse reparse ancestor: '+$ancestor.FullName)}
        $ancestor=$ancestor.Parent
    }
    $resolved=(Resolve-Path -LiteralPath $absolute).ProviderPath
    if (-not $resolved.Equals($absolute,[System.StringComparison]::OrdinalIgnoreCase)) {throw 'Resolved target differs.'}
    $targets+=$absolute
}
$protected=Get-Content -LiteralPath 'F:\MCM\mcm-skill-work\artifacts\text-corpus\native-20261029-v1\legacy-preimages.json' -Encoding UTF8 -Raw | ConvertFrom-Json
foreach($property in $protected.PSObject.Properties) {
    $path=[System.IO.Path]::GetFullPath((Join-Path 'F:\MCM\mcm-skill-work' $property.Name))
    foreach($target in $targets) {
        if ($path.StartsWith($target+'\',[System.StringComparison]::OrdinalIgnoreCase)) {throw ('Protected historical input inside target: '+$path)}
    }
}
$log=Join-Path $archive 'removal-progress.tsv'
if (Test-Path -LiteralPath $log) {throw 'A deletion attempt already exists; inspect it before any resume.'}
$writer=[System.IO.StreamWriter]::new($log,$false,[System.Text.UTF8Encoding]::new($false))
$before=([System.IO.DriveInfo]::new('F')).AvailableFreeSpace
$removed=0
try {
    $writer.WriteLine("state`tpath");$writer.Flush()
    foreach($target in $targets) {
        $writer.WriteLine("START`t"+$target);$writer.Flush()
        # Delete only the fully resolved, allowlisted root in this same shell.
        # The native directory implementation avoids a million provider objects.
        [System.IO.Directory]::Delete($target,$true)
        if (Test-Path -LiteralPath $target) {throw ('Target still exists: '+$target)}
        $removed++
        $writer.WriteLine("REMOVED`t"+$target);$writer.Flush()
        Write-Output ('REMOVED '+$removed+'/49 '+$target+' freeGiB='+[math]::Round(([System.IO.DriveInfo]::new('F')).AvailableFreeSpace/1GB,2))
    }
} finally {$writer.Dispose()}
$after=([System.IO.DriveInfo]::new('F')).AvailableFreeSpace
[pscustomobject]@{RemovedDirectories=$removed;RemovedLogicalBytes=$verified.logical_bytes;RemovedFiles=$verified.files;FreeBefore=$before;FreeAfter=$after;ObservedFreeGain=($after-$before);RetentionPolicy=$verified.policy;OldPayloadsRecoverable=$false;KeptNativeAndV16=$true} | ConvertTo-Json | Out-File -LiteralPath (Join-Path $archive 'removal-completed.json') -Encoding UTF8
Write-Output 'Deletion completed under the explicit manifest-only permanent-deletion policy.'
