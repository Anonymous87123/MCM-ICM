param(
    [switch]$Apply,
    [switch]$Verify,
    [switch]$Probe,
    [string]$AuditDirectory = 'E:\MCM-text-corpus-work\artifacts\storage-recovery-20261031-v1'
)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
if (-not (Test-Path -LiteralPath $AuditDirectory)) {
    New-Item -ItemType Directory -Path $AuditDirectory | Out-Null
}
$source = @'
using System;
using System.IO;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using Microsoft.Win32.SafeHandles;

public static class CorpusStorageRecovery {
    [StructLayout(LayoutKind.Sequential)]
    struct Info {
        public uint Attributes;
        public System.Runtime.InteropServices.ComTypes.FILETIME Creation, Access, Write;
        public uint Volume, SizeHigh, SizeLow, Links, IndexHigh, IndexLow;
    }
    [DllImport("kernel32.dll", SetLastError=true)]
    static extern bool GetFileInformationByHandle(SafeFileHandle handle, out Info info);
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
    static extern bool CreateHardLink(string link, string existing, IntPtr security);
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
    static extern bool MoveFileEx(string existing, string destination, uint flags);
    [DllImport("kernel32.dll", CharSet=CharSet.Unicode, SetLastError=true)]
    static extern uint GetCompressedFileSize(string path, out uint high);

    const string Base = @"F:\MCM\mcm-skill-work\artifacts\";
    static readonly StringComparison CI = StringComparison.OrdinalIgnoreCase;
    static string Identity(Info i) { return i.Volume+":"+i.IndexHigh+":"+i.IndexLow; }
    static string Stamp(Info i) { return Identity(i)+":"+i.SizeHigh+":"+i.SizeLow+":"+i.Write.dwHighDateTime+":"+i.Write.dwLowDateTime; }
    static Info Stat(FileStream stream) {
        Info i;
        if (!GetFileInformationByHandle(stream.SafeFileHandle,out i)) throw new System.ComponentModel.Win32Exception();
        return i;
    }
    static string Hash(FileStream stream) {
        stream.Position=0;
        using(var sha=SHA256.Create()) return BitConverter.ToString(sha.ComputeHash(stream)).Replace("-","").ToLowerInvariant();
    }
    static void SafePath(string path) {
        string p=Path.GetFullPath(path);
        if (!p.StartsWith(Base,CI)) throw new Exception("Outside approved artifact root: "+p);
        for (var item=new DirectoryInfo(Path.GetDirectoryName(p));item!=null;item=item.Parent) {
            if ((item.Attributes & FileAttributes.ReparsePoint)!=0) throw new Exception("Reparse ancestor: "+item.FullName);
        }
        if (File.Exists(p) && (File.GetAttributes(p)&FileAttributes.ReparsePoint)!=0) throw new Exception("Reparse file: "+p);
    }
    static IEnumerable<FileInfo> Files(string root) {
        var stack=new Stack<DirectoryInfo>(); stack.Push(new DirectoryInfo(root));
        while(stack.Count>0) {
            var dir=stack.Pop();
            if ((dir.Attributes&FileAttributes.ReparsePoint)!=0) throw new Exception("Reparse directory: "+dir.FullName);
            foreach(var file in dir.EnumerateFiles()) {
                if((file.Attributes&FileAttributes.ReparsePoint)!=0) throw new Exception("Reparse file: "+file.FullName);
                yield return file;
            }
            foreach(var child in dir.EnumerateDirectories()) stack.Push(child);
        }
    }
    static List<string> Roots() {
        var result=new List<string>();
        string corpus=Base+"text-corpus";
        foreach(string root in Directory.GetDirectories(corpus).OrderBy(x=>x,StringComparer.OrdinalIgnoreCase)) {
            string n=Path.GetFileName(root);
            if(System.Text.RegularExpressions.Regex.IsMatch(n,@"^(native|reflow)-202610(29|30|31)-v[0-9]+$")) result.Add(root);
        }
        foreach(string root in Directory.GetDirectories(Base+"skill-packages").OrderBy(x=>x,StringComparer.OrdinalIgnoreCase)) {
            if(System.Text.RegularExpressions.Regex.IsMatch(Path.GetFileName(root),@"^text-corpus-preview-202610(29|30|31)-v[0-9]+$")) result.Add(root);
        }
        foreach(string root in result) {
            SafePath(Path.Combine(root,"__validation_only__"));
            if((File.GetAttributes(root)&FileAttributes.ReparsePoint)!=0) throw new Exception("Reparse root");
        }
        return result;
    }
    public static void Run(string audit, bool apply, bool probe) {
        var roots=Roots();
        if(probe) roots=roots.Where(x=>Path.GetFileName(x)=="native-20261029-v1"||Path.GetFileName(x)=="reflow-20261029-v2").ToList();
        var candidates=new List<FileInfo>();
        var sizes=new Dictionary<long,int>();
        long count=0,total=0;
        string inventory=Path.Combine(audit,apply?"inventory-apply.tsv":"inventory-preview.tsv");
        using(var inv=new StreamWriter(new FileStream(inventory,FileMode.CreateNew),new UTF8Encoding(false))) {
            inv.WriteLine("root\tfiles\tlogical_bytes");
            foreach(string root in roots) {
                long n=0,bytes=0;
                foreach(var f in (probe ? new[]{new FileInfo(Path.Combine(root,"legacy-preimages.json"))} : Files(root))) {
                    n++;bytes+=f.Length;
                    // Frozen files only. Never touch SQLite databases or live reading runs.
                    string ext=f.Extension.ToLowerInvariant();
                    if(f.Length<65536 || !(ext==".jsonl"||ext==".json"||ext==".bin"||ext==".md"||ext==".txt"||ext==".py")) continue;
                    candidates.Add(f);
                    if(!sizes.ContainsKey(f.Length))sizes[f.Length]=0;
                    sizes[f.Length]++;
                }
                count+=n;total+=bytes;
                inv.WriteLine(root+"\t"+n+"\t"+bytes);inv.Flush();
                Console.WriteLine("INVENTORY "+Path.GetFileName(root)+" files="+n+" GiB="+(bytes/1073741824.0).ToString("F3"));
            }
        }
        Console.WriteLine("TOTAL files="+count+" logicalGiB="+(total/1073741824.0).ToString("F3")+" candidates="+candidates.Count);
        if(!apply)return;
        long before=new DriveInfo("F").AvailableFreeSpace;
        string logPath=Path.Combine(audit,"replacements.tsv");
        var canonical=new Dictionary<string,string>();
        var cache=new Dictionary<string,string>();
        long linked=0,already=0,logical=0,allocation=0,examined=0;
        using(var log=new StreamWriter(new FileStream(logPath,FileMode.CreateNew,FileAccess.Write,FileShare.Read),new UTF8Encoding(false))) {
            log.WriteLine("state\ttarget\tcanonical\tsha256\tlogical_bytes\toriginal_links\toriginal_identity");log.Flush();
            foreach(var file in candidates) {
                if(sizes[file.Length]<2)continue;
                SafePath(file.FullName);
                using(var target=new FileStream(file.FullName,FileMode.Open,FileAccess.Read,FileShare.Read|FileShare.Delete)) {
                    Info ti=Stat(target); string stamp=Stamp(ti),hash;
                    if(!cache.TryGetValue(stamp,out hash)) { hash=Hash(target);cache[stamp]=hash; }
                    string key=target.Length+":"+hash,source;
                    if(!canonical.TryGetValue(key,out source)) {canonical[key]=file.FullName;continue;}
                    SafePath(source);
                    // Renaming any hardlink requires DELETE sharing on all open
                    // handles of that physical file. Still deny all byte writes.
                    using(var existing=new FileStream(source,FileMode.Open,FileAccess.Read,FileShare.Read|FileShare.Delete)) {
                        Info si=Stat(existing);
                        if(Identity(si)==Identity(ti)) {already++;continue;}
                        string sh;
                        if(!cache.TryGetValue(Stamp(si),out sh)) {sh=Hash(existing);cache[Stamp(si)]=sh;}
                        if(sh!=hash || existing.Length!=target.Length)throw new Exception("Canonical changed: "+source);
                        // Keep the temporary basename shorter than long evidence
                        // hashes; appending to the original can exceed MAX_PATH.
                        string temp=Path.Combine(file.DirectoryName,".dd-"+Guid.NewGuid().ToString("N"));
                        uint high;uint low=GetCompressedFileSize(file.FullName,out high);
                        long allocated=((long)high<<32)|low;
                        string record=file.FullName+"\t"+source+"\t"+hash+"\t"+target.Length+"\t"+ti.Links+"\t"+Identity(ti);
                        log.WriteLine("PREPARE\t"+record);log.Flush();
                        if(!CreateHardLink(temp,source,IntPtr.Zero))throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error(),"Create hardlink: "+temp);
                        long targetLength=target.Length;
                        // Windows/NTFS can reject replacement of an open target
                        // even with DELETE sharing. These are frozen generations;
                        // release read handles immediately before the atomic rename.
                        target.Dispose();existing.Dispose();
                        try {
                            // Atomic replacement only after both complete SHA-256 hashes agree.
                            // The old target remains intact if this call fails.
                            if(!MoveFileEx(temp,file.FullName,0x1|0x8))throw new System.ComponentModel.Win32Exception(Marshal.GetLastWin32Error(),"Atomic replace: "+file.FullName);
                        } finally {if(File.Exists(temp))File.Delete(temp);}
                        using(var check=new FileStream(file.FullName,FileMode.Open,FileAccess.Read,FileShare.Read)) {
                            if(Identity(Stat(check))!=Identity(si)||check.Length!=targetLength)throw new Exception("Replacement identity mismatch");
                        }
                        linked++;logical+=targetLength;if(ti.Links==1)allocation+=allocated;
                        log.WriteLine("COMMIT\t"+record);log.Flush();
                    }
                }
                examined++;
                if(examined%500==0)Console.WriteLine("DEDUP linked="+linked+" already="+already+" freeGiB="+(new DriveInfo("F").AvailableFreeSpace/1073741824.0).ToString("F3"));
            }
        }
        long after=new DriveInfo("F").AvailableFreeSpace;
        string summary="linked_files="+linked+"\nalready_linked="+already+"\nlogical_duplicate_bytes="+logical+"\nestimated_released_allocation="+allocation+"\nfree_before="+before+"\nfree_after="+after+"\nobserved_free_gain="+(after-before)+"\n";
        using(var w=new StreamWriter(new FileStream(Path.Combine(audit,"summary.txt"),FileMode.CreateNew),new UTF8Encoding(false)))w.Write(summary);
        Console.WriteLine(summary);
    }
    public static void Verify(string audit) {
        var cache=new Dictionary<string,string>();long verified=0;
        foreach(string line in File.ReadLines(Path.Combine(audit,"replacements.tsv"))) {
            if(!line.StartsWith("COMMIT\t",StringComparison.Ordinal))continue;
            var row=line.Split('\t');SafePath(row[1]);
            using(var f=new FileStream(row[1],FileMode.Open,FileAccess.Read,FileShare.Read)) {
                string stamp=Stamp(Stat(f)),hash;
                if(!cache.TryGetValue(stamp,out hash)){hash=Hash(f);cache[stamp]=hash;}
                if(hash!=row[3]||f.Length!=long.Parse(row[4]))throw new Exception("VERIFY FAILED: "+row[1]);
            }
            verified++;
            if(verified%5000==0)Console.WriteLine("VERIFY "+verified);
        }
        using(var w=new StreamWriter(new FileStream(Path.Combine(audit,"verification.txt"),FileMode.CreateNew),new UTF8Encoding(false)))w.WriteLine("PASS sha256_verified_paths="+verified+" unique_physical_files="+cache.Count);
        Console.WriteLine("PASS sha256_verified_paths="+verified+" unique_physical_files="+cache.Count);
    }
}
'@
Add-Type -TypeDefinition $source -Language CSharp
try {
    if ($Verify) { [CorpusStorageRecovery]::Verify($AuditDirectory) }
    else { [CorpusStorageRecovery]::Run($AuditDirectory, $Apply.IsPresent, $Probe.IsPresent) }
} catch {
    $inner=$_.Exception.InnerException
    if ($inner -is [System.ComponentModel.Win32Exception]) { Write-Output ('NativeErrorCode='+$inner.NativeErrorCode) }
    throw
}
