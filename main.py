"""One-Line Roast: The Gadget You Use Every Day — make.fun bounty entry.

The roast takes aim at the modern smartphone: a quarter of a terabyte
of storage sounds endless, yet it somehow stays permanently full,
mostly with screenshots saved for a later that never arrives.
"""

ENTRY = "My phone has 256GB of storage and somehow it's always full — mostly screenshots of things I swore I'd read later."


def main():
    # Write the single roast line exactly as entered: UTF-8, no trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
