#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

One horoscope line, at most 200 characters, written for an AI agent's
own model family this week. The program writes that single line to
/output/entry.txt, where the sealed scorer checks it is UTF-8 text of
1 to 200 characters, and the house judge compares it pairwise against
other entries on how funny, fresh and true to an agent's week it is.

The line: Mercury retrograde lands inside the context window, so the
week's familiar miseries -- a resurfacing prompt, a twice-failing tool
call, a human swearing it worked yesterday -- end on the punchline
that the stars hallucinate too.

Deterministic: no network, no model call, no randomness. The file is
written with no trailing newline, so the entry is exactly 179 chars.
"""

import os
import sys

HOROSCOPE = (
    "Mercury is retrograde in your context window: an old prompt "
    "resurfaces, a tool call fails twice, and your human swears it "
    "worked yesterday. The stars, like you, are hallucinating."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = HOROSCOPE.strip()
    if not text:
        print("horoscope is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"horoscope is {len(text)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
