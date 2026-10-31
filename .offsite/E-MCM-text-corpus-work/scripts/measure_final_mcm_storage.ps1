$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
Add-Type -TypeDefinition @'
using System;using System.IO;using System.Text;using System.Linq;using System.Collections.Generic;using System.Runtime.InteropServices;using Microsoft.Win32.SafeHandles;
public class FinalMCMRow {public string Path;public long Files,LogicalBytes,UniqueFiles,StoredBytes;}
public static class FinalMCMStorage {
 [StructLayout(LayoutKind.Sequential)]struct Info{public uint Attributes;public System.Runtime.InteropServices.ComTypes.FILETIME Creation,Access,Write;public uint Volume,SizeHigh,SizeLow,Links,IndexHigh,IndexLow;}
 [DllImport("kernel32.dll",SetLastError=true)]static extern bool GetFileInformationByHandle(SafeFileHandle h,out Info i);
 [DllImport("kernel32.dll",CharSet=CharSet.Unicode,SetLastError=true)]static extern uint GetCompressedFileSize(string path,out uint high);
 public static FinalMCMRow[] Run(){
  const string root=@"F:\MCM";
  var groups=new Dictionary<string,FinalMCMRow>();var seen=new Dictionary<string,HashSet<string>>();var stack=new Stack<DirectoryInfo>();stack.Push(new DirectoryInfo(root));
  long n=0;
  while(stack.Count>0){var d=stack.Pop();if((d.Attributes&FileAttributes.ReparsePoint)!=0)continue;
   foreach(var f in d.EnumerateFiles()){
    if((f.Attributes&FileAttributes.ReparsePoint)!=0)continue;
    Info info;using(var stream=new FileStream(f.FullName,FileMode.Open,FileAccess.Read,FileShare.ReadWrite|FileShare.Delete)){if(!GetFileInformationByHandle(stream.SafeFileHandle,out info))throw new System.ComponentModel.Win32Exception();}
    string id=info.Volume+":"+info.IndexHigh+":"+info.IndexLow;uint high;uint low=GetCompressedFileSize(f.FullName,out high);
    if(low==uint.MaxValue&&Marshal.GetLastWin32Error()!=0)throw new System.ComponentModel.Win32Exception();
    long stored=((long)high<<32)|low;
    string[] parts=f.FullName.Substring(root.Length+1).Split('\\');
    for(int depth=0;depth<=Math.Min(3,parts.Length-1);depth++){
     string key=depth==0?"TOTAL":string.Join("/",parts.Take(depth));FinalMCMRow row;
     if(!groups.TryGetValue(key,out row)){row=new FinalMCMRow{Path=key};groups[key]=row;seen[key]=new HashSet<string>();}
     row.Files++;row.LogicalBytes+=f.Length;if(seen[key].Add(id)){row.UniqueFiles++;row.StoredBytes+=stored;}
    }
    n++;if(n%30000==0)Console.WriteLine("Read-only final storage measurement: "+n+" files");
   }
   foreach(var c in d.EnumerateDirectories())stack.Push(c);
  }
  return groups.Values.OrderByDescending(x=>x.LogicalBytes).ToArray();
 }
}
'@
$rows=[FinalMCMStorage]::Run()
$out='E:\MCM-text-corpus-work\artifacts\storage-cleanup-20261031-v5\final-storage.json'
if(Test-Path -LiteralPath $out){throw 'Do not replace the final measurement'}
$report=[pscustomobject]@{Total=($rows|Where-Object{$_.Path -eq 'TOTAL'});Largest=($rows|Where-Object{$_.Path -ne 'TOTAL'}|Select-Object -First 18);FRemaining=([IO.DriveInfo]::new('F')).AvailableFreeSpace;ERemaining=([IO.DriveInfo]::new('E')).AvailableFreeSpace;StoredBytesDefinition='GetCompressedFileSize summed once per unique NTFS file identity; excludes directory/MFT metadata and uncompressed cluster slack. Cross-subdirectory shared bytes must not be summed twice.'}
$report|ConvertTo-Json -Depth 5|Out-File -LiteralPath $out -Encoding UTF8
$report|ConvertTo-Json -Depth 5
