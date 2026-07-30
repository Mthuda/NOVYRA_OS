"""
===============================================================================
NOVYRA OS

File:
    base.py

Purpose:
    Shared domain model helper functions.

Description:
    This module contains reusable validation and normalisation helpers that
    are shared by multiple domain models.

    Keeping these functions in one location prevents duplicated validation
    logic and ensures every model behaves consistently.

Phase:
    Phase 4

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Public Functions
# =============================================================================


def require_non_empty(value: str, field_name: str) -> str:
    """
    Validate that a required string contains meaningful content.

    Leading and trailing whitespace is removed before validation.

    Args:
        value:
            Input value.

        field_name:
            Field name used when constructing error messages.

    Returns:
        Cleaned string.

    Raises:
        ValueError:
            If the value is empty after trimming whitespace.
    """

    # Remove surrounding whitespace.
    cleaned = value.strip()

    # Reject empty values.
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")

    return cleaned


def normalize_optional_text(value: str | None) -> str:
    """
    Normalise optional text values.

    Args:
        value:
            Optional text supplied by the caller.

    Returns:
        A trimmed string.

        If no value is supplied, an empty string is returned.
    """

    # Convert missing values into an empty string.
    if value is None:
        return ""

    # Remove unnecessary whitespace.
    return value.strip()