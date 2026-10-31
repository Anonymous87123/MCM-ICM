$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
Add-Type -TypeDefinition @'
using System;using System.IO;using System.Linq;using System.Collections.Generic;
public class MCMSizeRow {public string Path;public long Files;public long Bytes;}
public static class MCMSizeReport {
 public static MCMSizeRow[] Run(){
  var result=new Dictionary<string,MCMSizeRow>();
  var stack=new Stack<DirectoryInfo>();stack.Push(new DirectoryInfo(@"F:\MCM"));
  while(stack.Count>0){var d=stack.Pop();if((d.Attributes&FileAttributes.ReparsePoint)!=0)continue;
   foreach(var f in d.EnumerateFiles()){
    var parts=f.FullName.Substring(7).Split('\\');
    for(int depth=0;depth<=Math.Min(3,parts.Length-1);depth++){
     string key=depth==0?"TOTAL":string.Join("\\",parts.Take(depth));MCMSizeRow r;
     if(!result.TryGetValue(key,out r)){r=new MCMSizeRow{Path=key};result[key]=r;}r.Files++;r.Bytes+=f.Length;
    }
   }
   foreach(var c in d.EnumerateDirectories())stack.Push(c);
  }
  return result.Values.OrderByDescending(x=>x.Bytes).ToArray();
 }
}
'@
$rows=[MCMSizeReport]::Run()
$report=[pscustomobject]@{MeasuredAt=(Get-Date -Format o);Total=($rows|Where-Object{$_.Path -eq 'TOTAL'});Largest=($rows|Where-Object{$_.Path -ne 'TOTAL'}|Select-Object -First 20);FRemaining=([System.IO.DriveInfo]::new('F')).AvailableFreeSpace}
$report|ConvertTo-Json -Depth 4|Out-File -LiteralPath 'E:\MCM-text-corpus-work\archives\F-MCM-obsolete-generations-20261031-v4\mcm-size-after.json' -Encoding UTF8
$report|ConvertTo-Json -Depth 4
