"""
emoji_to_text.py

Convert emojis in an input string into readable names.

This script uses Python's standard library `unicodedata.name()` to obtain
the Unicode name of each non-ASCII character. For common emoji, the names
are descriptive (e.g., "GRINNING FACE"). If a character has no Unicode
name (rare), it is left as-is.

Usage:
    python emoji_to_text.py
Then type or paste text containing emoji and press Enter.
"""

import unicodedata


def emoji_to_description(text):
    """Replace each non-ascii character with its unicode name in brackets.
    ASCII characters are kept as-is. For control/unknown characters, fallback to the char.
    Example: "Hi 😊" -> "Hi [SMILING FACE WITH SMILING EYES]"
    """
    parts = []
    for ch in text:
        # treat emoji & other non-ascii chars
        if ord(ch) > 127:
            try:
                name = unicodedata.name(ch)
                # Some Unicode names are long — replace spaces with underscore or keep spaces
                parts.append(f"[{name}]")
            except ValueError:
                # no name available
                parts.append(ch)
        else:
            parts.append(ch)
    return "".join(parts)


def interactive():
    print("Emoji → Text Converter (type 'quit' to exit)\n")
    while True:
        s = input("Enter text: ")
        if s.strip().lower() in ("quit", "exit"):
            print("Bye.")
            break
        converted = emoji_to_description(s)
        print("Converted:", converted)
        print()


if __name__ == "__main__":
    interactive()
