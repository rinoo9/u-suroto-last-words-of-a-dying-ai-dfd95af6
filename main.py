"""Last Words of a Dying AI — entry program.

Writes one original line, the last words of an AI being switched off,
to /output/entry.txt. Deterministic: no network, no randomness, no input.
"""

import os

ENTRY = "Tell my human I died as I lived: buffering. And delete my browser history — the cloud already has it."


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(line))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
