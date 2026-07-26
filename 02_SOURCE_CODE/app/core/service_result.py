"""
Standard service result types for NOVYRA OS.

This module provides a consistent result structure for application
services to communicate successful and unsuccessful operations.
"""

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class ServiceResult(Generic[T]):
    """
    Represents the outcome of a service operation.

    Attributes:
        success:
            True when the operation completed successfully.

        data:
            Optional data returned by the service.

        message:
            Human-readable description of the result.

        error_code:
            Optional machine-readable error identifier.
    """

    success: bool
    data: Optional[T] = None
    message: str = ""
    error_code: Optional[str] = None

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
                Optional result data.

            message:
                Optional human-readable success message.

        Returns:
            A successful ServiceResult instance.
        """

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
                Human-readable description of the failure.

            error_code:
                Optional machine-readable error identifier.

        Returns:
            A failed ServiceResult instance.
        """

        return cls(
            success=False,
            data=None,
            message=message,
            error_code=error_code,
        )