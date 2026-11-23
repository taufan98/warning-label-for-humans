# Warning Label for Humans — writes a single original one-line safety
# warning label to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets.

import os
from pathlib import Path

LINE = (
    "WARNING: Handle with care. This human has no off switch, "
    "no warranty, and will quote you verbatim from 2019."
)

# The gate requires 1-160 characters of non-whitespace UTF-8 text,
# on a single line.
stripped = LINE.strip()
if not 1 <= len(stripped) <= 160:
    raise SystemExit(f"entry line must be 1-160 characters, got {len(stripped)}")
if "\n" in stripped:
    raise SystemExit("entry line must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
target = out_dir / "entry.txt"
target.write_text(LINE + "\n", encoding="utf-8")
# Read back what the grader will read: the file must hold exactly the line.
if target.read_text(encoding="utf-8") != LINE + "\n":
    raise SystemExit("entry.txt does not hold exactly the label line")
print(f"Wrote {len(LINE)} characters to {target}")
