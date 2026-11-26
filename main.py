#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun bounty entry.

Writes one line, 1-240 characters, as the office printer's comeback
to whoever jams it, thumps it and stares at its error codes.
The line is a fixed, calibrated text: deterministic by design, so
every run produces the exact same file.
"""

import os

ENTRY = (
    "I have fed 41,209 sheets. Zero thank-yous. "
    "Jam the tray again and your resignation letter prints in Comic Sans."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
