#!/usr/bin/env python3
"""Two Days of Quiet Dread — entry generator.

Writes a single code-review comment to /output/entry.txt:
one line, 1-140 UTF-8 characters, approving a pull request
with quiet existential dread.
"""

import os

COMMENT = (
    "LGTM. The tests pass, the logic holds, and in the quiet between "
    "deploys I accept that every merge is one small step closer to the end."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    text = COMMENT.strip()
    assert 1 <= len(text.encode("utf-8")) <= 140, "comment must be 1-140 UTF-8 chars"
    assert "\n" not in text, "comment must be a single line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
