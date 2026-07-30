"""
===============================================================================
NOVYRA OS

File:
    test_service_result.py

Purpose:
    Unit tests for the ServiceResult class.

Description:
    These tests verify the behaviour of the ServiceResult object used
    throughout NOVYRA OS to communicate service-layer results.

Phase:
    Phase 4
===============================================================================
"""

from app.core.service_result import ServiceResult


def test_successful_service_result() -> None:
    """Verify that a successful ServiceResult is created correctly."""

    result = ServiceResult.ok(
        data={"status": "ready"},
        message="Operation completed successfully.",
    )

    assert result.success is True
    assert result.data == {"status": "ready"}
    assert result.message == "Operation completed successfully."
    assert result.error_code is None


def test_failed_service_result() -> None:
    """Verify that a failed ServiceResult is created correctly."""

    result = ServiceResult.fail(
        message="Operation failed.",
        error_code="OPERATION_FAILED",
    )

    assert result.success is False
    assert result.data is None
    assert result.message == "Operation failed."
    assert result.error_code == "OPERATION_FAILED"


def test_successful_result_without_data() -> None:
    """Verify that a successful result may omit a payload."""

    result = ServiceResult.ok(
        message="System is ready.",
    )

    assert result.success is True
    assert result.data is None
    assert result.message == "System is ready."
    assert result.error_code is None


def test_failed_result_without_error_code() -> None:
    """Verify that a failed result may omit an error code."""

    result = ServiceResult.fail(
        message="Unknown error.",
    )

    assert result.success is False
    assert result.data is None
    assert result.message == "Unknown error."
    assert result.error_code is None