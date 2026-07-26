"""
Shared helpers for NOVYRA OS domain models.
"""

from __future__ import annotations


def require_non_empty(value: str, field_name: str) -> str:
    """
    Validate that a string value is not empty or whitespace.

    Args:
        value: Input string.
        field_name: Name of the field for error messages.

    Returns:
        The stripped string.

    Raises:
        ValueError: If the value is empty.
    """
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")
    return cleaned


def normalize_optional_text(value: str | None) -> str:
    """
    Normalize optional text input.

    Args:
        value: Optional input text.

    Returns:
        Trimmed text, or an empty string if no value was provided.
    """
    if value is None:
        return ""
    return value.strip()