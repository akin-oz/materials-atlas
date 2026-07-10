#!/usr/bin/env python3
"""Validate Materials Atlas commit subjects.

Purpose:
    Enforce the repository commit convention without external dependencies.

Usage:
    python3 scripts/check_commit_message.py <message-file>

Inputs:
    A Git commit-message file.

Output:
    Prints a concise reason and exits non-zero when the subject does not follow
    '<category>: <imperative summary>'. It does not modify the message file.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ALLOWED_CATEGORIES = {
    "architecture",
    "curriculum",
    "diagram",
    "docs",
    "domain",
    "ecosystem",
    "editorial",
    "governance",
    "reference",
    "release",
    "research",
    "resources",
    "tooling",
    "automation",
}


def subject_from(path: Path) -> str | None:
    """Return the first non-empty, non-comment commit message line."""

    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            return line
    return None


def validate(subject: str) -> list[str]:
    """Return convention violations for a commit subject."""

    errors: list[str] = []
    if len(subject) > 72:
        errors.append("Commit subject must be 72 characters or fewer.")

    category, separator, summary = subject.partition(": ")
    if not separator or category not in ALLOWED_CATEGORIES:
        errors.append("Commit subject must start with an allowed '<category>: ' prefix.")
    elif not summary or not summary[0].islower() or summary.endswith((".", "!", "?")):
        errors.append(
            "Commit summary must begin with a lowercase imperative verb "
            "and omit trailing punctuation."
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("message_file", type=Path, help="Git commit-message file")
    args = parser.parse_args()

    subject = subject_from(args.message_file)
    if subject is None:
        print("Commit message must include a subject.")
        return 1

    errors = validate(subject)
    if errors:
        print("\n".join(errors))
        print(f"Allowed categories: {', '.join(sorted(ALLOWED_CATEGORIES))}.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
