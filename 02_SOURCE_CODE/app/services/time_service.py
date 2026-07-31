"""
===============================================================================
NOVYRA OS

File:
    time_service.py

Purpose:
    Centralized date and time service.

Description:
    This service provides a single location for obtaining and manipulating
    timestamps throughout NOVYRA OS.

    All application components should obtain dates and times from this service
    instead of calling datetime.now() or datetime.utcnow() directly.

    Responsibilities include:

        • Current UTC time
        • Current local time
        • ISO datetime formatting
        • ISO datetime parsing
        • Unix timestamps
        • Time summary information

    Future enhancements may include:

        • Time zone conversion
        • Scheduler support
        • Relative time formatting
        • Business calendars
        • Clock synchronization
        • Time mocking utilities

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from datetime import datetime, timezone

from app.core.service_result import ServiceResult
from app.services.logging_service import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# UTC Time
# =============================================================================


def get_current_utc() -> ServiceResult[datetime]:
    """
    Return the current UTC date and time.

    Returns:
        ServiceResult containing a timezone-aware UTC datetime.
    """

    try:
        value = datetime.now(timezone.utc)

        logger.info("UTC time retrieved.")

        return ServiceResult.ok(
            data=value,
            message="UTC time retrieved successfully.",
        )

    except Exception:
        logger.exception("Failed to retrieve UTC time.")

        return ServiceResult.fail(
            message="Unable to retrieve UTC time.",
            error_code="TIME_UTC_ERROR",
        )


# =============================================================================
# Local Time
# =============================================================================


def get_current_local() -> ServiceResult[datetime]:
    """
    Return the current local date and time.

    Returns:
        ServiceResult containing a timezone-aware local datetime.
    """

    try:
        value = datetime.now().astimezone()

        logger.info("Local time retrieved.")

        return ServiceResult.ok(
            data=value,
            message="Local time retrieved successfully.",
        )

    except Exception:
        logger.exception("Failed to retrieve local time.")

        return ServiceResult.fail(
            message="Unable to retrieve local time.",
            error_code="TIME_LOCAL_ERROR",
        )


# =============================================================================
# ISO Formatting
# =============================================================================


def format_datetime(
    value: datetime,
) -> ServiceResult[str]:
    """
    Convert a datetime into ISO-8601 format.

    Args:
        value:
            Datetime to format.

    Returns:
        ServiceResult containing the ISO formatted string.
    """

    try:
        formatted = value.isoformat()

        return ServiceResult.ok(
            data=formatted,
            message="Datetime formatted successfully.",
        )

    except Exception:
        logger.exception("Failed to format datetime.")

        return ServiceResult.fail(
            message="Unable to format datetime.",
            error_code="TIME_FORMAT_ERROR",
        )


# =============================================================================
# ISO Parsing
# =============================================================================


def parse_datetime(
    value: str,
) -> ServiceResult[datetime]:
    """
    Parse an ISO-8601 datetime string.

    Args:
        value:
            ISO formatted datetime.

    Returns:
        ServiceResult containing the parsed datetime.
    """

    try:
        parsed = datetime.fromisoformat(value)

        return ServiceResult.ok(
            data=parsed,
            message="Datetime parsed successfully.",
        )

    except Exception:
        logger.exception("Failed to parse datetime.")

        return ServiceResult.fail(
            message="Invalid datetime format.",
            error_code="TIME_PARSE_ERROR",
        )


# =============================================================================
# Unix Timestamp
# =============================================================================


def get_timestamp() -> ServiceResult[float]:
    """
    Return the current Unix timestamp.

    Returns:
        ServiceResult containing the timestamp.
    """

    try:
        timestamp = datetime.now(timezone.utc).timestamp()

        return ServiceResult.ok(
            data=timestamp,
            message="Timestamp retrieved successfully.",
        )

    except Exception:
        logger.exception("Failed to retrieve timestamp.")

        return ServiceResult.fail(
            message="Unable to retrieve timestamp.",
            error_code="TIMESTAMP_ERROR",
        )


# =============================================================================
# Time Summary
# =============================================================================


def get_time_summary() -> ServiceResult[dict[str, object]]:
    """
    Return useful information about the current system time.

    Returns:
        ServiceResult containing a time summary.
    """

    utc_result = get_current_utc()
    local_result = get_current_local()
    timestamp_result = get_timestamp()

    if (
        not utc_result.success
        or utc_result.data is None
        or not local_result.success
        or local_result.data is None
        or not timestamp_result.success
        or timestamp_result.data is None
    ):
        return ServiceResult.fail(
            message="Unable to retrieve time summary.",
            error_code="TIME_SUMMARY_ERROR",
        )

    summary = {
        "utc": utc_result.data,
        "local": local_result.data,
        "timestamp": timestamp_result.data,
        "utc_iso": utc_result.data.isoformat(),
        "local_iso": local_result.data.isoformat(),
    }

    return ServiceResult.ok(
        data=summary,
        message="Time summary retrieved successfully.",
    )