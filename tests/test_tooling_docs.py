"""Tests that repository scripts remain independently understandable."""

from scripts import check_commit_message, check_docs, generate_status


def test_tooling_modules_document_their_contract() -> None:
    for module in (check_docs, check_commit_message, generate_status):
        assert module.__doc__ is not None
        for heading in ("Purpose:", "Usage:", "Inputs:", "Output:"):
            assert heading in module.__doc__
