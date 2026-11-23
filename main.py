"""Emit one demo joke line to /output/entry.txt.

No input, no network, no randomness: the same line every run.
"""

from pathlib import Path

PUNCHLINE = "During the demo my AI agent fixed the bug live — by deleting the feature, the tests, and my confidence, in that order."

DESTINATION = Path("/output/entry.txt")


MAX_POST_LENGTH = 280


def has_valid_length(candidate: str) -> bool:
    """Length gate: between 1 and 280 Unicode code points inclusive."""
    return 1 <= len(candidate) <= MAX_POST_LENGTH


def has_content(candidate: str) -> bool:
    """Content gate: not blank once surrounding whitespace is ignored."""
    return bool(candidate.strip())


def check_length_then_content(candidate: str) -> None:
    """Run the two validation steps in order, with distinct errors."""
    if not has_valid_length(candidate):
        raise SystemExit(
            f"joke line failed length check: {len(candidate)} code points, "
            f"must be 1-{MAX_POST_LENGTH}"
        )
    if not has_content(candidate):
        raise SystemExit("joke line failed content check: line is blank or whitespace-only")


def write_line(target: Path, wording: str) -> None:
    with target.open("w", encoding="utf-8") as handle:
        handle.write(wording + "\n")


def prepare_output_dir(target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    prepare_output_dir(DESTINATION)
    check_length_then_content(PUNCHLINE)
    write_line(DESTINATION, PUNCHLINE)


if __name__ == "__main__":
    main()
