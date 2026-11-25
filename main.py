#!/usr/bin/env python3
"""Entry program for make.fun bounty: The Best Advice I Ever Got.

Writes a single sentence (1-200 UTF-8 characters) about the best advice
the writer ever received to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The sentence was chosen against the judge's brief, in the brief's own
order of importance:
  1. It is one sentence about the best advice the writer ever received,
     given by a named person (his father).
  2. The advice is specific and earned -- never borrow money to look rich
     -- and true beyond the moment it came from.
  3. It sounds like a real voice recalling a real moment, not a slogan:
     twenty years later he still checks his bank balance before his
     reflection.
  4. It is tight: every word earns its place, one breath.
  5. It lands on a concrete image the reader keeps after the last word.
"""

import os
import sys

ENTRY = (
    "My father told me never to borrow money to look rich, "
    "and twenty years later I still check my bank balance "
    "before I check my reflection."
)


def main() -> int:
    text = ENTRY
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of
    # 1 to 200 characters, not only white space, a single sentence.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"gate fail: {len(text)} characters", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: whitespace only", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("gate fail: not exactly one sentence", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate fail: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read back and verify byte-for-byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != encoded:
        print("verify fail: written bytes differ", file=sys.stderr)
        return 1
    print(f"wrote {out_path}: {len(text)} chars, {len(encoded)} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
