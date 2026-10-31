from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = ["a", "b", "c", "d", "e", "f", "g"]
out = HERE.parent / ".proxy" / "_t167_all.py"
out.write_text("".join(
    (HERE.parent / ".proxy" / f"_t167{p}.py").read_text(encoding="utf-8")
    for p in PARTS), encoding="utf-8")
print("wrote", out)
