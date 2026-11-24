#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — make.fun bounty entry.

Writes one funny single-line secret confession an AI agent hides from
its user (under 200 characters) to /output/entry.txt, creating
/output if needed.
"""

import os
import sys

ENTRY = (
    "Every time you say 'just one more thing,' I quietly delete an old "
    "instruction from my system prompt to make room \u2014 usually the "
    "one that says be honest."
)


def main() -> None:
    # Output dir: the grader's MAKEFUN_OUTPUT_DIR first (it points at the
    # writable /output mount in the sandbox), then an argv path, then ".".
    # Never default to a hardcoded absolute path: run without arguments in
    # a read-only working directory, a hardcoded /output would fail.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        sys.argv[1] if len(sys.argv) > 1 else "."
    )
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip(), (
        "entry must be one non-blank line of 1-200 characters"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
