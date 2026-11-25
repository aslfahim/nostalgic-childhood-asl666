#!/usr/bin/env python3
"""Write one childhood memory sentence to /output/entry.txt.

Stdlib only, no network, deterministic.
"""

import os

SENTENCE = (
    "I pressed play and record together the second the DJ on the kitchen "
    "radio stopped talking, then held my breath through the hiss, praying "
    "the chorus would land clean on a tape I'd rewound with a pencil."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
