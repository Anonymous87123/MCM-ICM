"""Conservative local secret-pattern scan; findings contain no matched secret bytes."""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(r"F:\MCM")
OUT = Path(r"E:\MCM-text-corpus-work\artifacts\git-offsite-backup-20261031-v1")
BINARY = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".7z", ".gz", ".bin", ".sqlite3", ".sqlite", ".db", ".pyc", ".ico", ".webp", ".ttf", ".woff", ".woff2", ".exe", ".dll"}
RULES = {
    "github_token": rb"\bgh[pousr]_[A-Za-z0-9]{30,255}\b",
    "github_fine_grained_token": rb"\bgithub_pat_[A-Za-z0-9_]{40,255}\b",
    "provider_api_key": rb"\bsk-(?:proj-|svcacct-|ant-(?:api\d+-)?)?[A-Za-z0-9_-]{20,220}\b",
    "aws_access_key": rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "google_api_key": rb"\bAIza[0-9A-Za-z_-]{35}\b",
    "private_key_header": rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----",
    "literal_credential_assignment": rb'''(?i)(?:api[_-]?key|access[_-]?token|password|secret[_-]?key|authorization)\s*(?:=|:)\s*["']((?:Bearer\s+)?[^"'\r\n]{12,256})["']''',
}
PATTERNS = {name: re.compile(pattern) for name, pattern in RULES.items()}
PREFIXES = {
    "github_token": (b"ghp_", b"gho_", b"ghu_", b"ghs_", b"ghr_"),
    "github_fine_grained_token": (b"github_pat_",),
    "provider_api_key": (b"sk-",),
    "aws_access_key": (b"AKIA", b"ASIA"),
    "google_api_key": (b"AIza",),
    "private_key_header": (b"PRIVATE KEY-----",),
    "literal_credential_assignment": (b"api", b"access", b"password", b"secret", b"authorization"),
}


def scan(stream, size, origin, findings):
    remaining = size
    tail = b""
    offset = 0
    seen = set()
    while remaining:
        body = stream.read(min(1024**2, remaining))
        if not body:
            raise ValueError("Truncated source")
        remaining -= len(body)
        block = tail + body
        lower_block = block.lower()
        for name, pattern in PATTERNS.items():
            haystack = lower_block if name == "literal_credential_assignment" else block
            if not any(prefix in haystack for prefix in PREFIXES[name]):
                continue
            for match in pattern.finditer(block):
                absolute = offset - len(tail) + match.start()
                if (name, absolute) in seen:
                    continue
                seen.add((name, absolute))
                value = match.group(1) if match.lastindex else match.group()
                lower = value.lower()
                if name != "private_key_header" and (len(set(value)) < 7 or any(x in lower for x in
                    (b"your_api", b"your-api", b"example", b"placeholder", b"replace_me", b"changeme", b"test_token", b"dummy"))):
                    continue
                findings.append({"origin": origin, "rule": name, "byte_offset": absolute,
                                 "match_sha256": hashlib.sha256(value).hexdigest(), "match_length": len(value)})
        offset += len(body)
        tail = block[-512:]


def main():
    findings = []
    objects = json.loads((OUT / "reachable-objects.json").read_text(encoding="utf-8"))
    candidates = [row for row in objects if row["type"] == "blob" and Path(row["path"]).suffix.lower() not in BINARY]
    proc = subprocess.Popen(["git", "-C", str(ROOT), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for index, row in enumerate(candidates):
        proc.stdin.write((row["oid"] + "\n").encode("ascii")); proc.stdin.flush()
        header = proc.stdout.readline().decode("ascii").split()
        if len(header) != 3 or int(header[2]) != row["bytes"]:
            raise ValueError("Unexpected Git object header")
        scan(proc.stdout, row["bytes"], {"kind": "history_blob", "oid": row["oid"], "path": row["path"]}, findings)
        if proc.stdout.read(1) != b"\n":
            raise ValueError("Git object framing mismatch")
        if (index+1) % 4000 == 0:
            print(json.dumps({"history_blobs_scanned": index+1, "findings": len(findings)}), flush=True)
    proc.stdin.close()
    if proc.wait() != 0:
        raise ValueError("Git blob reader failed")
    files = json.loads((OUT / "working-files.json").read_text(encoding="utf-8"))
    current = [row for row in files if Path(row["path"]).suffix.lower() not in BINARY and
               not row["path"].startswith("mcm-skill-work/artifacts/text-corpus/")]
    for index, row in enumerate(current):
        with (ROOT / row["path"]).open("rb") as source:
            scan(source, row["bytes"], {"kind": "working_file", "path": row["path"]}, findings)
        if (index+1) % 4000 == 0:
            print(json.dumps({"working_text_files_scanned": index+1, "findings": len(findings)}), flush=True)
    report = {"history_text_blobs_scanned": len(candidates), "working_text_files_scanned": len(current),
              "finding_count": len(findings), "rule_counts": dict(collections.Counter(r["rule"] for r in findings)),
              "findings": findings,
              "limitation": "Pattern-based screening, not proof that arbitrary private information is absent; full new corpus data not selected for publication."}
    with (OUT / "secret-scan.json").open("x", encoding="utf-8") as output:
        json.dump(report, output, ensure_ascii=False, indent=2)
    print(json.dumps({k: v for k, v in report.items() if k != "findings"}), flush=True)
    print(json.dumps({"finding_paths": list(dict.fromkeys(r["origin"]["path"] for r in findings))[:30]}, ensure_ascii=True), flush=True)


if __name__ == "__main__":
    main()
