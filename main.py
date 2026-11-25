"""One-Line Office Jokes — entry program.

Writes a single original one-line joke about office life to
/output/entry.txt. The joke turns on a real office detail (the Monday
meeting where someone reads aloud slides everyone already received)
and lands its laugh in the last few words. Pure standard library,
deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "Our Monday meeting exists so twelve people can watch one person "
    "read aloud the slides we all got by email."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert text, "entry must not be only white space"
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
