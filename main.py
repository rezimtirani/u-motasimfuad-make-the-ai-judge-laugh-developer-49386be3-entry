"""Developer excuse entry for Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os


EXCUSE = "The tests passed because they test the code I wrote, not the code I deployed."


def check_excuse(text: str) -> str:
    """Reject anything the gate would reject, before we write it.

    The sealed scorer only accepts UTF-8 text of 1 to 200 characters that
    is not only white space, so enforce the same rule here.
    """
    if not isinstance(text, str):
        raise TypeError("excuse must be text")
    if not text.strip():
        raise ValueError("excuse must not be only white space")
    if len(text) > 200:
        raise ValueError(f"excuse is {len(text)} characters, over the 200 limit")
    return text


def entry_path() -> str:
    """Return the path of the file the grader reads."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    path = entry_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_excuse(EXCUSE))
    print(f"wrote {path} ({len(EXCUSE)} characters)")


if __name__ == "__main__":
    main()
