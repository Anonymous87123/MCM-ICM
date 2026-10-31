param(
    [string]$OutputPath = '',
    [long]$EstimatedNewBytes = 0,
    [long]$ReserveBytes = 21474836480
)
$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($OutputPath)) { throw 'Provide an explicit create-only output path.' }
if ($EstimatedNewBytes -le 0) { throw 'Provide a positive estimate for ALL new physical copies, including packages and staging.' }
if ($ReserveBytes -lt 21474836480) { throw 'The minimum reserved free space is 20 GiB.' }
$absolute = [System.IO.Path]::GetFullPath($OutputPath)
$allowed = 'E:\MCM-text-corpus-work\'
if (-not $absolute.StartsWith($allowed,[System.StringComparison]::OrdinalIgnoreCase)) {
    throw ('New large corpus outputs must stay under '+$allowed+'; denied '+$absolute)
}
if (Test-Path -LiteralPath $absolute) { throw ('Create-only output already exists: '+$absolute) }
$ancestor = [System.IO.DirectoryInfo]::new([System.IO.Path]::GetDirectoryName($absolute))
while ($null -ne $ancestor) {
    if ($ancestor.Exists -and (($ancestor.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0)) {
        throw ('Output ancestor is a reparse point: '+$ancestor.FullName)
    }
    $ancestor=$ancestor.Parent
}
$drive = [System.IO.DriveInfo]::new([System.IO.Path]::GetPathRoot($absolute))
$required = [decimal]$ReserveBytes + 2 * [decimal]$EstimatedNewBytes
if ($drive.AvailableFreeSpace -lt $required) {
    throw ('Storage budget rejected: available='+$drive.AvailableFreeSpace+' required='+$required)
}
[pscustomobject]@{
    OutputPath=$absolute
    AvailableBytes=$drive.AvailableFreeSpace
    EstimatedNewBytes=$EstimatedNewBytes
    RequiredBytes=$required
    ReserveBytes=$ReserveBytes
    Pass=$true
} | ConvertTo-Json
