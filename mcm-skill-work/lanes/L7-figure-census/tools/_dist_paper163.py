import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
PARTS = ["a", "b", "c", "d", "e", "f"]
text = "".join((LANE / ".proxy" / f"_t163{p}.py").read_text(encoding="utf-8") + "\n"
               for p in PARTS)
out = LANE / ".proxy" / "_t163_all.py"
out.write_text(text, encoding="utf-8")
print("wrote", out, len(text))
raise SystemExit(subprocess.run([sys.executable, "-I", "-X", "utf8", str(out)], cwd=LANE).returncode)
