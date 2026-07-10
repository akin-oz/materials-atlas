#!/usr/bin/env python3
"""Validate repository documentation with the Python standard library.

Purpose:
    Check Markdown filenames, trailing whitespace, local links, frontmatter,
    Mermaid fences, curriculum sequence, and canonical Mermaid IDs.

Usage:
    python3 scripts/check_docs.py [path ...]
    python3 scripts/check_docs.py --all

Inputs:
    Optional repository-relative Markdown paths. Without paths, the script reads
    staged files from Git. --all validates every Markdown file in the repository.

Output:
    Prints each validation error and exits non-zero on failure. It does not
    modify repository files.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIAGRAM_DIRECTORY = ROOT / "references" / "diagrams"
MODULE_DIRECTORY = ROOT / "roadmaps" / "software-engineer-to-computational-materials-scientist"
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)\)")
DIAGRAM_ID = re.compile(r"^# (D-\d{3})(?:\s|$)", re.MULTILINE)
MODULE_FILE = re.compile(r"^module-(\d{2})-[a-z0-9-]+\.md$")
MODULE_HEADING = re.compile(r"^# Module (\d{2}) [—-] .+$", re.MULTILINE)
CONTINUE_WITH = re.compile(r"^\*\*Module (\d{2}) [—-] .+\*\*$", re.MULTILINE)


def relative(path: Path) -> str:
    """Return a repository-relative display path."""

    return path.relative_to(ROOT).as_posix()


def markdown_files() -> list[Path]:
    """Return all Markdown files in deterministic order."""

    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
    )


def normalize_paths(paths: list[str]) -> list[Path]:
    """Convert existing repository-relative paths into Markdown paths."""

    normalized: list[Path] = []
    for raw_path in paths:
        candidate = Path(raw_path)
        path = candidate if candidate.is_absolute() else ROOT / candidate
        if path.suffix == ".md" and path.is_file():
            normalized.append(path.resolve())
    return sorted(set(normalized))


def staged_files() -> list[Path]:
    """Return staged, added, copied, modified, or renamed Markdown files."""

    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return normalize_paths(result.stdout.splitlines())


def valid_markdown_filename(path: Path) -> bool:
    """Accept lowercase kebab-case or established uppercase canonical names."""

    if path.name == "README.md":
        return True
    return bool(
        re.fullmatch(r"[A-Z][A-Z0-9_.-]*(?:v[0-9]+(?:\.[0-9]+)*)?\.md", path.name)
        or re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.md", path.name)
    )


def internal_link_issues(files: list[Path]) -> list[str]:
    """Return missing repository-local Markdown link targets for files."""

    issues: list[str] = []
    for path in files:
        for target in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "mailto:", "#")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (path.parent / local_target).resolve().exists():
                issues.append(f"{relative(path)}: missing local link target {target}")
    return issues


def mermaid_fence_issues(files: list[Path]) -> list[str]:
    """Return malformed Mermaid fence errors for files."""

    issues: list[str] = []
    for path in files:
        in_mermaid = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if line == "```mermaid":
                if in_mermaid:
                    issues.append(f"{relative(path)}:{line_number}: nested Mermaid fence")
                in_mermaid = True
            elif line == "```" and in_mermaid:
                in_mermaid = False
        if in_mermaid:
            issues.append(f"{relative(path)}: unterminated Mermaid fence")
    return issues


def frontmatter_issues(files: list[Path]) -> list[str]:
    """Return structural errors for optional YAML frontmatter blocks.

    Materials Atlas does not require frontmatter today. When a page introduces
    it, the block must begin on line one and close with a second delimiter.
    """

    issues: list[str] = []
    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        if lines and lines[0] == "---" and "---" not in lines[1:]:
            issues.append(f"{relative(path)}: unterminated frontmatter block")
    return issues


def canonical_diagram_ids() -> dict[str, list[str]]:
    """Return canonical Mermaid diagram IDs and their owning files."""

    owners: dict[str, list[str]] = defaultdict(list)
    for path in sorted(DIAGRAM_DIRECTORY.glob("*.md")):
        for diagram_id in DIAGRAM_ID.findall(path.read_text(encoding="utf-8")):
            owners[diagram_id].append(relative(path))
    return dict(owners)


def duplicate_diagram_id_issues() -> list[str]:
    """Return duplicate canonical Mermaid ID errors."""

    return [
        f"duplicate canonical diagram ID {diagram_id}: {', '.join(owners)}"
        for diagram_id, owners in canonical_diagram_ids().items()
        if len(owners) > 1
    ]


def module_issues() -> list[str]:
    """Return curriculum filename, heading, and Continue With chain errors."""

    modules = sorted(MODULE_DIRECTORY.glob("module-*.md"))
    issues: list[str] = []
    numbers: list[int] = []
    module_content: list[tuple[Path, int, str]] = []

    for path in modules:
        filename_match = MODULE_FILE.fullmatch(path.name)
        if filename_match is None:
            issues.append(f"{relative(path)}: invalid module filename")
            continue

        number = int(filename_match.group(1))
        numbers.append(number)
        content = path.read_text(encoding="utf-8")
        module_content.append((path, number, content))
        heading_match = MODULE_HEADING.search(content)
        if heading_match is None or int(heading_match.group(1)) != number:
            issues.append(f"{relative(path)}: heading must match module filename number")

    if not numbers:
        return issues

    final_number = max(numbers)
    for path, number, content in module_content:
        targets = CONTINUE_WITH.findall(content)
        expected_target = number + 1
        if number != final_number:
            if targets != [f"{expected_target:02d}"]:
                issues.append(
                    f"{relative(path)}: Continue With must name Module {expected_target:02d}"
                )
        elif targets:
            issues.append(f"{relative(path)}: final module must not name a Continue With target")

    expected_numbers = list(range(final_number + 1))
    if sorted(numbers) != expected_numbers:
        issues.append("curriculum modules must form a continuous sequence starting at Module 00")
    return issues


def documentation_issues(files: list[Path]) -> list[str]:
    """Return all documentation-integrity errors for a validation run."""

    issues: list[str] = []
    for path in files:
        if not valid_markdown_filename(path):
            issues.append(
                f"{relative(path)}: filename must use lowercase kebab-case "
                "or an established uppercase canonical name"
            )
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(keepends=True), start=1
        ):
            if re.search(r"[ \t]+\n$", line):
                issues.append(f"{relative(path)}:{line_number}: trailing whitespace")
    issues.extend(internal_link_issues(files))
    issues.extend(frontmatter_issues(files))
    issues.extend(mermaid_fence_issues(markdown_files()))
    issues.extend(duplicate_diagram_id_issues())
    issues.extend(module_issues())
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="repository-relative Markdown paths")
    parser.add_argument("--all", action="store_true", help="validate every Markdown file")
    args = parser.parse_args()

    if args.all:
        files = markdown_files()
    elif args.paths:
        files = normalize_paths(args.paths)
    else:
        files = staged_files()

    issues = documentation_issues(files)
    if issues:
        print("\n".join(issues))
        return 1

    print("Documentation checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
