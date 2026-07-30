"""
===============================================================================
NOVYRA OS

File:
    service_result.py

Purpose:
    Standard service response object.

Description:
    Defines a common response structure used by the service layer to
    communicate the outcome of business operations.

    Every service within NOVYRA returns a ServiceResult instead of raising
    application-level exceptions for expected business outcomes.

    This approach provides:

        • Consistent service contracts
        • Predictable error handling
        • Cleaner unit testing
        • Easier API development
        • Simpler UI integration

    Future interfaces—including the Kivy mobile app, REST API,
    web dashboard, and desktop application—will all consume this
    response model.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

# =============================================================================
# Generic Type
# =============================================================================

# Represents the type of data carried by a successful service result.
#
# Examples:
#
#     ServiceResult[Opportunity]
#     ServiceResult[list[Opportunity]]
#     ServiceResult[str]
#
T = TypeVar("T")

# =============================================================================
# Service Result
# =============================================================================


@dataclass(frozen=True)
class ServiceResult(Generic[T]):
    """
    Represents the outcome of a business service operation.

    Rather than returning raw values or raising exceptions for expected
    business conditions, every service returns a ServiceResult.

    Attributes:
        success:
            Indicates whether the operation completed successfully.

        data:
            Optional data produced by the operation.

        message:
            Human-readable explanation suitable for logs or user interfaces.

        error_code:
            Optional machine-readable identifier that allows callers to
            react programmatically to failures.
    """

    success: bool
    data: Optional[T] = None
    message: str = ""
    error_code: Optional[str] = None

    # =========================================================================
    # Factory Methods
    # =========================================================================

    @classmethod
    def ok(
        cls,
        data: Optional[T] = None,
        message: str = "",
    ) -> "ServiceResult[T]":
        """
        Create a successful service result.

        Args:
            data:
                Optional payload returned by the service.

            message:
                Optional human-readable success message.

        Returns:
            A successful ServiceResult instance.
        """

        # ---------------------------------------------------------------------
        # Successful operations never carry an error code.
        # ---------------------------------------------------------------------

        return cls(
            success=True,
            data=data,
            message=message,
            error_code=None,
        )

    @classmethod
    def fail(
        cls,
        message: str,
        error_code: Optional[str] = None,
    ) -> "ServiceResult[T]":
        """
        Create a failed service result.

        Args:
            message:
                Human-readable explanation of the failure.

            error_code:
                Optional machine-readable error identifier.

        Returns:
            A failed ServiceResult instance.
        """

        # ---------------------------------------------------------------------
        # Failed operations never return business data.
        # This guarantees callers only need to check one flag (success)
        # before using the returned data.
        # ---------------------------------------------------------------------

        return cls(
            success=False,
            data=None,
            message=message,
            error_code=error_code,
        )