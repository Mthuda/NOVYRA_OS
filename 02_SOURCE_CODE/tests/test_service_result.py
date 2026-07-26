"""
Tests for the NOVYRA OS service result foundation.
"""

from app.core.service_result import ServiceResult


def test_successful_service_result():
    """Test creation of a successful service result."""

    result = ServiceResult.ok(
        data={"status": "ready"},
        message="Operation completed successfully.",
    )

    assert result.success is True
    assert result.data == {"status": "ready"}
    assert result.message == "Operation completed successfully."
    assert result.error_code is None


def test_failed_service_result():
    """Test creation of a failed service result."""

    result = ServiceResult.fail(
        message="Operation failed.",
        error_code="OPERATION_FAILED",
    )

    assert result.success is False
    assert result.data is None
    assert result.message == "Operation failed."
    assert result.error_code == "OPERATION_FAILED"


def test_successful_result_without_data():
    """Test a successful result with no data."""

    result = ServiceResult.ok(
        message="System is ready.",
    )

    assert result.success is True
    assert result.data is None
    assert result.message == "System is ready."
    assert result.error_code is None


def test_failed_result_without_error_code():
    """Test a failed result without an error code."""

    result = ServiceResult.fail(
        message="An unknown error occurred.",
    )

    assert result.success is False
    assert result.data is None
    assert result.message == "An unknown error occurred."
    assert result.error_code is None


def test_service_result_is_immutable():
    """Test that ServiceResult instances cannot be modified."""

    result = ServiceResult.ok(
        data="test",
    )

    try:
        result.success = False
    except AttributeError:
        pass
    else:
        raise AssertionError(
            "ServiceResult should be immutable."
        )