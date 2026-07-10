"""Behavioral tests for commit-message validation."""

from scripts.check_commit_message import validate


def test_accepts_a_valid_commit_subject() -> None:
    assert validate("reference: add thermodynamic quantities reference") == []


def test_accepts_a_specific_maintainer_category() -> None:
    assert validate("tooling: establish Python validation foundation") == []


def test_rejects_an_unknown_category() -> None:
    errors = validate("chore: update repository")

    assert "allowed '<category>: ' prefix" in errors[0]


def test_rejects_a_non_imperative_style_subject() -> None:
    errors = validate("reference: Added thermodynamic quantities.")

    assert "lowercase imperative verb" in errors[0]
