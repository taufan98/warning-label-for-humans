# Warning Label for Humans — writes a single original one-line safety
# warning label to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets.

import os
from pathlib import Path

LINE = (
    "WARNING: Handle with care. This human has no off switch, "
    "no warranty, and remembers everything you said in 2019."
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
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
