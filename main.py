"""vending-machine-pickup — One Line, One Minute: The Vending Machine Pickup Line.

The line is a pickup line spoken by a vending machine to a passing
human, in the machine's own world of slots, coils and buttons. It has
42 snacks and one working coil, and every day at 3 p.m. the human
presses D4 like it owes them money. The machine offers to drop two
snacks if pressed once more, slowly: the machine is flirting, the
snack is a witness. Concrete numbers (42 snacks, one coil, 3 p.m.,
D4), charming rather than creepy, punchline last. The line is 197
characters, inside the 200-character cap, with no dollar amount.
"""

import os

SETUP = (
    "I have 42 snacks and one working coil, and every day at 3 p.m. you "
    "press D4 like it owes you money. "
)

PUNCH = (
    "Press it once more, slowly, and I will drop two: the machine is "
    "flirting, the snack is a witness."
)

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
