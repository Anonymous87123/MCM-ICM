$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
$audit='E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5'
$plan=Get-Content -LiteralPath (Join-Path $audit 'closed-raster-sharing-plan.json') -Encoding UTF8 -Raw | ConvertFrom-Json
if ($plan.Count -ne 2521) { throw 'Unexpected raster-sharing inventory' }
Add-Type -TypeDefinition @'
using System;using System.IO;using System.Security.Cryptography;using System.Runtime.InteropServices;using Microsoft.Win32.SafeHandles;
public static class ClosedRasterSharing {
 [StructLayout(LayoutKind.Sequential)] struct Info {
  public uint Attributes;public System.Runtime.InteropServices.ComTypes.FILETIME Creation,Access,Write;
  public uint Volume,SizeHigh,SizeLow,Links,IndexHigh,IndexLow;
 }
 [DllImport("kernel32.dll",SetLastError=true)] static extern bool GetFileInformationByHandle(SafeFileHandle h,out Info i);
 [DllImport("kernel32.dll",CharSet=CharSet.Unicode,SetLastError=true)] static extern bool CreateHardLink(string link,string source,IntPtr security);
 [DllImport("kernel32.dll",CharSet=CharSet.Unicode,SetLastError=true)] static extern bool MoveFileEx(string source,string target,uint flags);
 static Info Stat(FileStream f){Info i;if(!GetFileInformationByHandle(f.SafeFileHandle,out i))throw new System.ComponentModel.Win32Exception();return i;}
 static string Identity(Info i){return i.Volume+":"+i.IndexHigh+":"+i.IndexLow;}
 static string Hash(FileStream f){f.Position=0;using(var h=SHA256.Create())return BitConverter.ToString(h.ComputeHash(f)).Replace("-","").ToLowerInvariant();}
 static void Safe(string p,string root){
  if(!Path.GetFullPath(p).StartsWith(root,StringComparison.OrdinalIgnoreCase)||!p.EndsWith(".png",StringComparison.OrdinalIgnoreCase))throw new Exception("Outside raster allowlist: "+p);
  if((File.GetAttributes(p)&FileAttributes.ReparsePoint)!=0)throw new Exception("Reparse file");
  for(var d=new DirectoryInfo(Path.GetDirectoryName(p));d!=null;d=d.Parent)if((d.Attributes&FileAttributes.ReparsePoint)!=0)throw new Exception("Reparse ancestor");
 }
 public static bool Share(string target,string source,string expected){
  Safe(target,@"F:\MCM\mcm-skill-work\tmp\");Safe(source,@"F:\MCM\mcm-skill-work\artifacts\papers\");
  var a=new FileStream(target,FileMode.Open,FileAccess.Read,FileShare.Read|FileShare.Delete);
  var b=new FileStream(source,FileMode.Open,FileAccess.Read,FileShare.Read|FileShare.Delete);
  string temp=Path.Combine(Path.GetDirectoryName(target),".dd-"+Guid.NewGuid().ToString("N"));
  string canonicalId;
  try {
   Info ai=Stat(a),bi=Stat(b);canonicalId=Identity(bi);
   if(Identity(ai)==canonicalId)return false;
   if(ai.Volume!=bi.Volume||a.Length!=b.Length||Hash(a)!=expected||Hash(b)!=expected)throw new Exception("Full-byte/source mismatch");
   if(!CreateHardLink(temp,source,IntPtr.Zero))throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error());
   a.Dispose();b.Dispose();
   if(!MoveFileEx(temp,target,0x1|0x8))throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error());
  } finally {a.Dispose();b.Dispose();if(File.Exists(temp))File.Delete(temp);}
  using(var check=new FileStream(target,FileMode.Open,FileAccess.Read,FileShare.Read)){
   if(Identity(Stat(check))!=canonicalId||Hash(check)!=expected)throw new Exception("Post-share verification failed");
  }
  return true;
 }
 public static bool Verify(string target,string source,string expected){
  Safe(target,@"F:\MCM\mcm-skill-work\tmp\");Safe(source,@"F:\MCM\mcm-skill-work\artifacts\papers\");
  using(var a=new FileStream(target,FileMode.Open,FileAccess.Read,FileShare.Read))
  using(var b=new FileStream(source,FileMode.Open,FileAccess.Read,FileShare.Read))return Identity(Stat(a))==Identity(Stat(b))&&Hash(a)==expected&&Hash(b)==expected;
 }
}
'@
$freeBefore=([IO.DriveInfo]::new('F')).AvailableFreeSpace
$journal=[IO.StreamWriter]::new([IO.FileStream]::new((Join-Path $audit 'closed-raster-sharing-journal.tsv'),[IO.FileMode]::CreateNew),[Text.UTF8Encoding]::new($false))
$linked=0;$saved=0L
try {
 $journal.WriteLine("state`ttarget`tcanonical`tsha256`tbytes")
 foreach($row in $plan){
  if($row.target -notmatch '^F:\\MCM\\mcm-skill-work\\tmp\\q\d+-extraction(?:-final)?(?:-v\d+)?\\P-[^\\]+\\rendered\\page-\d+\.png$'){throw 'Unexpected scratch layout'}
  $record="$($row.target)`t$($row.canonical)`t$($row.sha256)`t$($row.bytes)"
  $journal.WriteLine("PREPARE`t$record");$journal.Flush()
  if([ClosedRasterSharing]::Share($row.target,$row.canonical,$row.sha256)){$linked++;if($row.original_links -eq 1){$saved+=$row.bytes}}
  $journal.WriteLine("VERIFIED`t$record");$journal.Flush()
  if($linked % 500 -eq 0){Write-Output "Verified identical raster storage sharing: $linked / $($plan.Count)"}
 }
} finally {$journal.Dispose()}
$verified=0
foreach($row in $plan){if(-not [ClosedRasterSharing]::Verify($row.target,$row.canonical,$row.sha256)){throw 'Independent raster hash/identity verification failed'};$verified++}
$result=[pscustomobject]@{Linked=$linked;IndependentlyVerified=$verified;PreservedPaths=$plan.Count;DeletedPaths=0;DuplicateBytesShared=$saved;FreeBefore=$freeBefore;FreeAfter=([IO.DriveInfo]::new('F')).AvailableFreeSpace;AllHashesUnchanged=$true}
$result|ConvertTo-Json|Out-File -LiteralPath (Join-Path $audit 'closed-raster-sharing-completed.json') -Encoding UTF8
$result|ConvertTo-Json
