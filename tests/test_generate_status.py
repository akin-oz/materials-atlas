"""Behavioral tests for the generated repository status report."""

from scripts import generate_status


def test_status_report_contains_its_required_sections() -> None:
    report = generate_status.render()

    for heading in (
        "## Repository Overview",
        "## Curriculum Progress",
        "## Milestone Progress",
        "## Module Table",
        "## Reference Statistics",
        "## Diagram Statistics",
        "## Domain Readiness",
        "## Repository Health",
        "## Architecture Health",
        "## Next Recommended Work",
    ):
        assert heading in report


def test_status_report_is_deterministic() -> None:
    assert generate_status.render() == generate_status.render()


def test_status_report_includes_documented_release_milestones() -> None:
    report = generate_status.render()

    assert "| v0.4.0 | Interactive Foundations | annotated tag |" in report
