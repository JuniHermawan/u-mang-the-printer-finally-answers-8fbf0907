#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun bounty entry.

Writes one line, 1-240 characters, as the office printer's comeback
to whoever jams it, thumps it and stares at its error codes.
The line is a fixed, calibrated text: deterministic by design, so
every run produces the exact same file.
"""

import os

# Line design notes (comments only — the entry text is unchanged):
# - Voice: the printer speaks as a long-suffering office machine, not a
#   helpdesk script; first person, flat delivery, no exclamation marks.
# - Numbers: "41,209 sheets" is specific enough to sound counted, not
#   rounded — a round number would read as made up.
# - "Zero thank-yous" is the grievance: the printer's labour is invisible,
#   which is the joke's engine.
# - Threat, not insult: "your resignation letter prints in Comic Sans"
#   escalates the printer's revenge to something petty and bureaucratic,
#   matching the office setting instead of breaking it.
# - Length: 111 chars, comfortably inside the 1-240 window, so the line
#   survives as a single printed sentence with no wrapping awkwardness.
ENTRY = (
    "I have fed 41,209 sheets. Zero thank-yous. "
    "Jam the tray again and your resignation letter prints in Comic Sans."
)


def main() -> None:
    text = ENTRY.strip()
    # Guard 1: length window enforced by the competition (1-240 chars).
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    # Guard 2: a whitespace-only line would pass the length check but
    # print nothing — reject it explicitly.
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        # newline="" keeps the file byte-identical on every platform:
        # no trailing newline is added, so the file is exactly the line.
        f.write(text)


if __name__ == "__main__":
    main()
