"""
===============================================================================
NOVYRA OS

Tests for the Time Service.

Verifies:

    • Current date/time retrieval
    • Timestamp generation
    • Date formatting
    • Date parsing
    • Time information summary

===============================================================================
"""

from __future__ import annotations

from datetime import datetime, timezone

from app.services import time_service


"""
===============================================================================
Current Time Tests
===============================================================================
"""


def test_get_current_utc() -> None:
    """
    Verify that the current UTC datetime is returned.
    """

    result = time_service.get_current_utc()

    assert result.success is True
    assert result.data is not None
    assert isinstance(result.data, datetime)
    assert result.data.tzinfo == timezone.utc


def test_get_current_local() -> None:
    """
    Verify that the current local datetime is returned.
    """

    result = time_service.get_current_local()

    assert result.success is True
    assert result.data is not None
    assert isinstance(result.data, datetime)
    assert result.data.tzinfo is not None


def test_get_timestamp() -> None:
    """
    Verify that a Unix timestamp is returned.
    """

    result = time_service.get_timestamp()

    assert result.success is True
    assert result.data is not None
    assert isinstance(result.data, float)
    assert result.data > 0

"""
===============================================================================
Formatting Tests
===============================================================================
"""


def test_format_datetime() -> None:
    """
    Verify formatting a datetime into ISO-8601.
    """

    value = datetime(
        2026,
        1,
        1,
        12,
        30,
        tzinfo=timezone.utc,
    )

    result = time_service.format_datetime(value)

    assert result.success is True
    assert result.data == value.isoformat()


def test_parse_datetime() -> None:
    """
    Verify parsing an ISO-8601 datetime string.
    """

    value = "2026-01-01T12:30:00+00:00"

    result = time_service.parse_datetime(value)

    assert result.success is True
    assert result.data is not None
    assert result.data == datetime.fromisoformat(value)


def test_get_time_summary() -> None:
    """
    Verify the returned time summary.
    """

    result = time_service.get_time_summary()

    assert result.success is True
    assert result.data is not None

    from typing import cast

    summary = result.data

    utc = cast(datetime, summary["utc"])
    local = cast(datetime, summary["local"])
    timestamp = cast(float, summary["timestamp"])
    utc_iso = cast(str, summary["utc_iso"])
    local_iso = cast(str, summary["local_iso"])

    assert isinstance(utc, datetime)
    assert isinstance(local, datetime)

    assert timestamp > 0

    assert utc_iso == utc.isoformat()
    assert local_iso == local.isoformat()