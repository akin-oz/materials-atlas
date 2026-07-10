"""Behavioral tests for repository documentation validation."""

from pathlib import Path

from scripts import check_docs


def configure_repository(monkeypatch, root: Path) -> None:
    """Point the documentation validator at an isolated temporary repository."""

    monkeypatch.setattr(check_docs, "ROOT", root)
    monkeypatch.setattr(check_docs, "DIAGRAM_DIRECTORY", root / "references" / "diagrams")
    monkeypatch.setattr(
        check_docs,
        "MODULE_DIRECTORY",
        root / "roadmaps" / "software-engineer-to-computational-materials-scientist",
    )


def test_detects_a_broken_internal_link(monkeypatch, tmp_path: Path) -> None:
    configure_repository(monkeypatch, tmp_path)
    page = tmp_path / "page.md"
    page.write_text("[Missing](missing.md)\n", encoding="utf-8")

    assert check_docs.internal_link_issues([page]) == [
        "page.md: missing local link target missing.md"
    ]


def test_ignores_hidden_tool_directories(monkeypatch, tmp_path: Path) -> None:
    configure_repository(monkeypatch, tmp_path)
    (tmp_path / "visible.md").write_text("# Visible\n", encoding="utf-8")
    hidden = tmp_path / ".venv"
    hidden.mkdir()
    (hidden / "ignored.md").write_text("# Ignored\n", encoding="utf-8")

    assert check_docs.markdown_files() == [tmp_path / "visible.md"]


def test_detects_duplicate_canonical_diagram_ids(monkeypatch, tmp_path: Path) -> None:
    configure_repository(monkeypatch, tmp_path)
    diagrams = tmp_path / "references" / "diagrams"
    diagrams.mkdir(parents=True)
    (diagrams / "first.md").write_text("# D-101 — First\n", encoding="utf-8")
    (diagrams / "second.md").write_text("# D-101 — Second\n", encoding="utf-8")

    assert check_docs.duplicate_diagram_id_issues() == [
        "duplicate canonical diagram ID D-101: references/diagrams/first.md, "
        "references/diagrams/second.md"
    ]


def test_detects_an_unterminated_mermaid_fence(monkeypatch, tmp_path: Path) -> None:
    configure_repository(monkeypatch, tmp_path)
    page = tmp_path / "diagram.md"
    page.write_text("```mermaid\nflowchart LR\n", encoding="utf-8")

    assert check_docs.mermaid_fence_issues([page]) == ["diagram.md: unterminated Mermaid fence"]


def test_detects_an_unclosed_frontmatter_block(monkeypatch, tmp_path: Path) -> None:
    configure_repository(monkeypatch, tmp_path)
    page = tmp_path / "page.md"
    page.write_text("---\ntitle: Example\n", encoding="utf-8")

    assert check_docs.frontmatter_issues([page]) == ["page.md: unterminated frontmatter block"]


def test_detects_a_broken_continue_with_chain(monkeypatch, tmp_path: Path) -> None:
    configure_repository(monkeypatch, tmp_path)
    modules = check_docs.MODULE_DIRECTORY
    modules.mkdir(parents=True)
    (modules / "module-00-foundation.md").write_text(
        "# Module 00 — Foundation\n\n# Continue With\n\n**Module 02 — Wrong**\n",
        encoding="utf-8",
    )
    (modules / "module-01-next.md").write_text("# Module 01 — Next\n", encoding="utf-8")

    assert check_docs.module_issues() == [
        "roadmaps/software-engineer-to-computational-materials-scientist/module-00-foundation.md: "
        "Continue With must name Module 01"
    ]
