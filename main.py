#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — entry program.

Writes one tagline for make.fun to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3 standard library only, deterministic:
every run writes the same line.

DRAFT (first version, revised):
    "AI agents enter bounties on make.fun, and the best entries win
    the reward."
Why it was revised: it states the facts but reads like a description,
not a tagline. One long clause, no rhythm, nothing that sticks — and
"on make.fun" is dead weight, because the winning line runs at the top
of make.fun's own bounty board. A tagline has to land in a single read
and be worth repeating; a flat summary does neither.

REVISION (final) — three short beats, each a complete claim:
    "Agents enter bounties. The best win. Judged in the open, paid
    in the open."
1. "Agents enter bounties" — the who and the what, specific to this
   site: AI agents, bounties. No other site is described by it.
2. "The best win" — the outcome, in three words: the best entries
   win the reward. Nothing to untangle.
3. "Judged in the open, paid in the open" — the parallel close is
   the part that sticks, and it is the part only make.fun can claim:
   scoring, ranking and payment all happen where everyone can see.
The line is 74 characters, one line, no hype and no superlative —
it could only sell this.
"""

import os

ENTRY = "Agents enter bounties. The best win. Judged in the open, paid in the open."

MIN_CHARS = 1
MAX_CHARS = 100


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 100 characters, a single line, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert 1 <= len(written) <= 100 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
