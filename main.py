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

LINE = (
    "I have 42 snacks and one working coil, and every day at 3 p.m. you "
    "press D4 like it owes you money. Press it once more, slowly, and I "
    "will drop two: the machine is flirting, the snack is a witness."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
