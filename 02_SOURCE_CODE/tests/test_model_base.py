"""
Tests for shared NOVYRA OS model helpers.
"""

import pytest

from app.models.base import normalize_optional_text, require_non_empty


def test_require_non_empty_returns_clean_text():
    assert require_non_empty("  Hello  ", "Field") == "Hello"


def test_require_non_empty_rejects_empty_value():
    with pytest.raises(ValueError, match="Field cannot be empty."):
        require_non_empty("   ", "Field")


def test_normalize_optional_text_handles_none():
    assert normalize_optional_text(None) == ""


def test_normalize_optional_text_strips_text():
    assert normalize_optional_text("  NOVYRA  ") == "NOVYRA"