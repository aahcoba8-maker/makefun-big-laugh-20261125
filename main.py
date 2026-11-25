"""One Line, Big Laugh — a single joke that lands on its own.

The line is a landlord joke with a turn: a leaking faucet is reframed
as a "free water feature" — and the punchline is the rent going up.
"""

import os

TEXT = "I told my landlord the faucet was leaking. He called it a 'free water feature' and raised my rent."


def main():
    # Self-gate mirroring the kit's sealed scorer: 1-200 UTF-8 chars, not
    # only white space.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
