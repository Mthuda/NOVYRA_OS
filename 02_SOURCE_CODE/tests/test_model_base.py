"""
===============================================================================
NOVYRA OS

File:
    test_model_base.py

Purpose:
    Unit tests for shared domain model helper functions.

Description:
    This module verifies the helper functions used throughout NOVYRA's
    domain models for validating required text fields and normalizing
    optional text values.

    These helper functions are intentionally isolated because they form
    the validation foundation used by many future domain models.

    If these functions fail, every model depending on them becomes
    unreliable.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import pytest

from app.models.base import (
    normalize_optional_text,
    require_non_empty,
)

# =============================================================================
# Tests for require_non_empty()
# =============================================================================


def test_require_non_empty_returns_clean_text():
    """
    Verify that valid text is stripped of surrounding whitespace.

    This ensures that domain models always store clean values even when
    users accidentally enter leading or trailing spaces.
    """

    # Arrange
    value = "   NOVYRA OS   "

    # Act
    result = require_non_empty(
        value,
        "project_name",
    )

    # Assert
    assert result == "NOVYRA OS"


def test_require_non_empty_rejects_empty_value():
    """
    Verify that empty or whitespace-only strings are rejected.

    Required business fields should never contain blank values.
    """

    # Act / Assert
    with pytest.raises(ValueError):
        require_non_empty(
            "     ",
            "project_name",
        )

# =============================================================================
# Tests for normalize_optional_text()
# =============================================================================


def test_normalize_optional_text_handles_none():
    """
    Verify that None is converted into an empty string.

    This prevents None values from propagating into domain objects and
    simplifies downstream processing.
    """

    # Act
    result = normalize_optional_text(None)

    # Assert
    assert result == ""


def test_normalize_optional_text_strips_text():
    """
    Verify that optional text is trimmed before being stored.

    Optional fields should still be normalized to maintain consistency
    throughout the application.
    """

    # Arrange
    value = "   Optional description   "

    # Act
    result = normalize_optional_text(value)

    # Assert
    assert result == "Optional description"