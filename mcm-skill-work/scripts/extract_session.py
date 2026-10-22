import json, sys

def parts(content):
    """Split content into (text_segments, tool_use_list, has_tool_result, has_image)."""
    texts, tools, tr, img = [], [], False, False
    if isinstance(content, str):
        return [content], tools, tr, img
    if isinstance(content, list):
        for p in content:
            if not isinstance(p, dict):
                continue
            t = p.get("type")
            if t == "text":
                texts.append(p.get("text", ""))
            elif t == "tool_use":
                tools.append((p.get("name"), p.get("input")))
            elif t == "tool_result":
                tr = True
            elif t == "image":
                img = True
    return texts, tools, tr, img

path = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "user"
out = []
with open(path, encoding="utf-8") as fh:
    for i, line in enumerate(fh, 1):
        if len(line) > 2_000_000:
            continue
        try:
            d = json.loads(line)
        except Exception:
            continue
        ty = d.get("type")
        m = d.get("message") if isinstance(d.get("message"), dict) else None
        if not m or ty not in ("user", "assistant"):
            continue
        texts, tools, tr, img = parts(m.get("content"))
        if mode == "user":
            if m.get("role") != "user" or tr:
                continue
            body = "\n".join(texts).strip()
            if not body:
                continue
            out.append("### U line %d %s\n%s\n" % (i, d.get("timestamp", ""), body[:4000]))
        else:
            if m.get("role") != "assistant":
                continue
            if texts:
                out.append("### A line %d %s\n%s\n" % (i, d.get("timestamp", ""), "\n".join(texts)[:1500]))
            for name, inp in tools:
                s = json.dumps(inp, ensure_ascii=False)
                out.append("### T line %d %s  %s\n%s\n" % (i, d.get("timestamp", ""), name, s[:400]))
open(sys.argv[3], "w", encoding="utf-8").write("\n".join(out))
print("wrote", len(out), "records")
