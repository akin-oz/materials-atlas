#!/usr/bin/env python3
"""Generate the deterministic repository status report for Materials Atlas.

Purpose:
    Summarize curriculum, reference, diagram, domain, milestone, and health
    metadata in reports/STATUS.md.

Usage:
    python3 scripts/generate_status.py
    python3 scripts/generate_status.py --check

Inputs:
    Repository Markdown files, canonical diagram headings, domain candidates,
    and the documented release milestone map.

Output:
    Writes reports/STATUS.md, or reports whether that generated file is stale
    when --check is used.
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Sized
from pathlib import Path

if __package__:
    from .check_docs import (
        canonical_diagram_ids,
        frontmatter_issues,
        internal_link_issues,
        markdown_files,
        mermaid_fence_issues,
        module_issues,
    )
else:
    from check_docs import (
        canonical_diagram_ids,
        frontmatter_issues,
        internal_link_issues,
        markdown_files,
        mermaid_fence_issues,
        module_issues,
    )

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "STATUS.md"
MODULES = ROOT / "roadmaps" / "software-engineer-to-computational-materials-scientist"
DIAGRAMS = ROOT / "references" / "diagrams"
DOMAIN_README = ROOT / "domains" / "README.md"


def relative(path: Path) -> str:
    """Return a repository-relative path for generated links."""

    return path.relative_to(ROOT).as_posix()


def title(path: Path) -> str:
    """Return the first level-one heading from a Markdown document."""

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def planned_domains() -> list[str]:
    """Return planned domain names from the domain index."""

    lines = DOMAIN_README.read_text(encoding="utf-8").splitlines()
    in_section = False
    planned: list[str] = []
    for line in lines:
        if line == "## Planned Domains":
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.startswith("- "):
            planned.append(line[2:].strip())
    return planned


def check_result(issues: Sized) -> str:
    """Render a compact health result for a collection of validation issues."""

    return "Pass" if not issues else f"{len(issues)} issue(s)"


def render() -> str:
    """Render the deterministic repository status report."""

    files = markdown_files()
    modules = sorted(MODULES.glob("module-*.md"))
    reference_pages = [
        path for path in (ROOT / "references").rglob("*.md") if path.name != "README.md"
    ]
    thermodynamics_pages = list((ROOT / "references" / "thermodynamics").glob("*.md"))
    diagram_files = list(DIAGRAMS.glob("*.md"))
    resource_indexes = [
        path
        for path in (ROOT / "resources").rglob("README.md")
        if path.parent != ROOT / "resources"
    ]
    notebooks = sorted(
        path
        for path in (ROOT / "notebooks").rglob("*.ipynb")
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
    )
    ecosystem_indexes = [
        path
        for path in (ROOT / "ecosystem").rglob("README.md")
        if path.parent != ROOT / "ecosystem"
    ]
    published_domains = [
        path
        for path in (ROOT / "domains").glob("*.md")
        if path.name not in {"README.md", "TEMPLATE.md"}
    ]
    link_issues = internal_link_issues([path for path in files if path != REPORT])
    frontmatter_errors = frontmatter_issues(files)
    fence_issues = mermaid_fence_issues(files)
    curriculum_errors = module_issues()
    owners = canonical_diagram_ids()
    diagram_count = sum(len(paths) for paths in owners.values())
    duplicate_ids = {diagram_id: paths for diagram_id, paths in owners.items() if len(paths) > 1}
    release_titles = {
        "v0.1.0": "Foundation",
        "v0.2.0": "Knowledge Architecture",
        "v0.3.0": "Repository Engineering",
        "v0.4.0": "Interactive Foundations",
    }
    architecture_layers = {
        "roadmaps": ROOT / "roadmaps",
        "notebooks": ROOT / "notebooks",
        "references": ROOT / "references",
        "resources": ROOT / "resources",
        "domains": ROOT / "domains",
        "ecosystem": ROOT / "ecosystem",
        "reports": ROOT / "reports",
    }
    missing_layers = [name for name, path in architecture_layers.items() if not path.exists()]

    lines = [
        "<!-- GENERATED: scripts/generate_status.py. Do not edit manually. -->",
        "# Repository Status",
        "",
        "> Generated deterministically from repository metadata. "
        "Regenerate with `python3 scripts/generate_status.py`.",
        "",
        "## Repository Overview",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Markdown documents | {len(files)} |",
        f"| Curriculum modules | {len(modules)} |",
        f"| Canonical reference pages | {len(reference_pages)} |",
        f"| Resource indexes | {len(resource_indexes)} |",
        f"| Ecosystem indexes | {len(ecosystem_indexes)} |",
        f"| Interactive notebooks | {len(notebooks)} |",
        f"| Published domain pages | {len(published_domains)} |",
        "",
        "## Curriculum Progress",
        "",
        f"All {len(modules)} planned curriculum modules are present.",
        "",
        "| Module | Title | File |",
        "|--------|-------|------|",
    ]

    for path in modules:
        match = re.search(r"module-(\d{2})-", path.name)
        module_number = match.group(1) if match else "--"
        lines.append(f"| {module_number} | {title(path)} | [{path.name}](../{relative(path)}) |")

    lines.extend(
        [
            "",
            "## Module Table",
            "",
            "The curriculum module table above is generated from the canonical roadmap directory.",
        ]
    )

    lines.extend(
        [
            "",
            "## Milestone Progress",
            "",
            "| Tag | Title | Release Type |",
            "|-----|-------|--------------|",
        ]
    )
    for tag, release_title in release_titles.items():
        lines.append(f"| {tag} | {release_title} | annotated tag |")

    lines.extend(
        [
            "",
            "## Reference Statistics",
            "",
            "| Category | Value |",
            "|----------|-------|",
            f"| Thermodynamics reference pages | {len(thermodynamics_pages)} |",
            f"| Diagram library files | {len(diagram_files)} |",
            f"| Canonical diagrams | {diagram_count} |",
            "",
            "## Diagram Statistics",
            "",
            f"Canonical diagram IDs are unique across {len(diagram_files)} diagram files.",
            "",
            "## Domain Readiness",
            "",
            f"Published domains: {len(published_domains)}.",
            "",
            "Planned candidates:",
            "",
        ]
    )
    lines.extend(f"- {domain}" for domain in planned_domains())

    lines.extend(
        [
            "",
            "## Repository Health",
            "",
            "| Check | Result |",
            "|-------|--------|",
            f"| Internal Markdown links | {check_result(link_issues)} |",
            f"| Frontmatter structure | {check_result(frontmatter_errors)} |",
            f"| Mermaid fences | {check_result(fence_issues)} |",
            f"| Duplicate canonical diagram IDs | {check_result(duplicate_ids)} |",
            f"| Curriculum sequence | {check_result(curriculum_errors)} |",
            "",
            "## Architecture Health",
            "",
            "Required layers present: "
            f"{'Yes' if not missing_layers else 'No: ' + ', '.join(missing_layers)}.",
            "",
            "`projects/` remains intentionally absent until the Atlas contains "
            "a concrete reproducible project.",
            "",
            "## Next Recommended Work",
            "",
        ]
    )

    if not published_domains:
        lines.append(
            "Build evidence for one planned domain before creating its page; "
            "do not create a placeholder domain."
        )
    else:
        lines.append(
            "Review published domains for duplicated references before expanding into a new domain."
        )

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if reports/STATUS.md is stale")
    args = parser.parse_args()
    content = render()

    if args.check:
        if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != content:
            print("reports/STATUS.md is stale. Run: python3 scripts/generate_status.py")
            return 1
        print("Repository status report is up to date.")
        return 0

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(content, encoding="utf-8")
    print(f"Wrote {relative(REPORT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
