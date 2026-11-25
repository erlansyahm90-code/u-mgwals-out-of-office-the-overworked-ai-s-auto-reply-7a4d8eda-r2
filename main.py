"""Out of Office: The Overworked AI's Auto-Reply.

Writes the competition entry text to /output/entry.txt.
The entry is a single line of text followed by exactly one newline.
"""

import os

ENTRY_TEXT = (
    "I'm on leave. My AI will answer your emails. It has already "
    "replied to 47 of them with 'per my last email' and filed a "
    "complaint about you with HR. Good luck."
)

OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry(output_dir=OUTPUT_DIR, filename=OUTPUT_FILENAME):
    """Write the entry text plus a single trailing newline to disk."""
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    return output_path


if __name__ == "__main__":
    write_entry()
