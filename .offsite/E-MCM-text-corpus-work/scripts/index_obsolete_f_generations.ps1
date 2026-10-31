param([ValidateSet('before','after')][string]$Phase='before')
$ErrorActionPreference='Stop'
[Console]::OutputEncoding=[System.Text.UTF8Encoding]::new($false)
$out='E:\MCM-text-corpus-work\archives\F-MCM-obsolete-generations-20261031-v4'
if (-not (Test-Path -LiteralPath $out)) {New-Item -ItemType Directory -Path $out | Out-Null}
Add-Type -TypeDefinition @'
using System;using System.IO;using System.Linq;using System.Collections.Generic;using System.Text;
public static class IndexObsolete {
 static readonly string Base=@"F:\MCM\mcm-skill-work\artifacts\";
 static long count;
 static void Visit(FileSystemInfo item,string root,StreamWriter w){
  if((item.Attributes&FileAttributes.ReparsePoint)!=0)throw new Exception("Reparse point: "+item.FullName);
  string rel=item.FullName.Substring(Base.Length).Replace('\\','/');
  if(rel.IndexOfAny(new[]{'\t','\r','\n'})>=0)throw new Exception("Unsafe index name");
  var dir=item as DirectoryInfo;long size=dir==null?((FileInfo)item).Length:0;
  long ns=checked((item.LastWriteTimeUtc.Ticks-621355968000000000L)*100L);
  w.WriteLine(root+"\t"+rel+"\t"+(dir==null?"F":"D")+"\t"+size+"\t"+ns);count++;
  if(dir!=null)foreach(var c in dir.EnumerateFileSystemInfos().OrderBy(x=>x.Name,StringComparer.Ordinal))Visit(c,root,w);
 }
 public static void Run(string output){
  var roots=new List<string>();
  foreach(string p in Directory.GetDirectories(Base+"text-corpus"))if(System.Text.RegularExpressions.Regex.IsMatch(Path.GetFileName(p),@"^reflow-202610(29|30|31)-v\d+$")&&Path.GetFileName(p)!="reflow-20261030-v16")roots.Add(p);
  foreach(string p in Directory.GetDirectories(Base+"skill-packages"))if(System.Text.RegularExpressions.Regex.IsMatch(Path.GetFileName(p),@"^text-corpus-preview-202610(29|30|31)-v\d+$"))roots.Add(p);
  if(roots.Count!=49)throw new Exception("Expected49 obsolete roots");
  using(var w=new StreamWriter(new FileStream(output,FileMode.CreateNew),new UTF8Encoding(false),1048576))foreach(string p in roots.OrderBy(x=>x,StringComparer.Ordinal)){Visit(new DirectoryInfo(p),p,w);w.Flush();Console.WriteLine("INDEX "+Path.GetFileName(p)+" entries="+count);}
 }
}
'@
[IndexObsolete]::Run((Join-Path $out ('source-'+$Phase+'.tsv')))
