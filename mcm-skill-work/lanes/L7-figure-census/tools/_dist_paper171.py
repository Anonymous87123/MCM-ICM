from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = ["a", "b", "c", "d", "e", "f"]
out = HERE.parent / ".proxy" / "_t171_all.py"
out.write_text("".join(
    (HERE.parent / ".proxy" / f"_t171{p}.py").read_text(encoding="utf-8")
    for p in PARTS), encoding="utf-8")
print("wrote", out)
