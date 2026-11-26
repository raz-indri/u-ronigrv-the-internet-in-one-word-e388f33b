"""The Internet in One Word.

One word for the whole internet, written to /output/entry.txt.

The word was picked by duelling eight candidates pairwise against the
judge's brief (single word, funny alone, true of the whole internet,
surprising, lands in one beat). The duel winner: "unhinged" — the whole
internet, collectively, is unhinged. Short, spelled right, eight bytes.
"""

import os

WORD = "unhinged"


def _check(word: str) -> str:
    """Enforce the gate ourselves: one word, 1-30 chars, not blank."""
    if not (1 <= len(word) <= 30):
        raise ValueError("entry must be 1-30 characters")
    if len(word.split()) != 1 or word != word.strip():
        raise ValueError("entry must be exactly one word")
    return word


def main() -> None:
    word = _check(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
