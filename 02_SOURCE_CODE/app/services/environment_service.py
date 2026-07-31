"""
===============================================================================
NOVYRA OS

File:
    environment_service.py

Purpose:
    Runtime environment service.

Description:
    Provides information about the runtime environment.

    This service centralizes operating system information,
    Python runtime information, host information, and the
    configured NOVYRA environment.

    Future versions will also expose:

        • CPU information
        • Memory statistics
        • Disk usage
        • Network interfaces
        • Installed plugins
        • Runtime diagnostics

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import platform
import socket
import sys

from app.core.config import get_app_config
from app.core.service_result import ServiceResult
from app.services.logging_service import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Environment
# =============================================================================


def get_environment() -> ServiceResult[str]:
    """
    Return the configured NOVYRA environment.
    """

    try:
        config = get_app_config()

        return ServiceResult.ok(
            data=config.environment,
            message="Environment retrieved successfully.",
        )

    except Exception:
        logger.exception("Unable to determine environment.")

        return ServiceResult.fail(
            message="Unable to determine environment.",
            error_code="ENVIRONMENT_ERROR",
        )


# =============================================================================
# Development Check
# =============================================================================


def is_development() -> ServiceResult[bool]:
    """
    Determine whether NOVYRA is running in development mode.
    """

    result = get_environment()

    if not result.success or result.data is None:
        return ServiceResult.fail(
            message="Unable to determine environment.",
            error_code="ENVIRONMENT_ERROR",
        )

    return ServiceResult.ok(
        data=result.data.lower() == "development",
        message="Development status determined successfully.",
    )


# =============================================================================
# Python Version
# =============================================================================


def get_python_version() -> ServiceResult[str]:
    """
    Return the current Python version.
    """

    return ServiceResult.ok(
        data=platform.python_version(),
        message="Python version retrieved successfully.",
    )


# =============================================================================
# Platform
# =============================================================================


def get_platform_name() -> ServiceResult[str]:
    """
    Return the operating system name.
    """

    return ServiceResult.ok(
        data=platform.system(),
        message="Platform retrieved successfully.",
    )


# =============================================================================
# Hostname
# =============================================================================


def get_hostname() -> ServiceResult[str]:
    """
    Return the computer hostname.
    """

    return ServiceResult.ok(
        data=socket.gethostname(),
        message="Hostname retrieved successfully.",
    )


# =============================================================================
# Environment Summary
# =============================================================================


def get_environment_summary() -> ServiceResult[dict[str, object]]:
    """
    Return a summary of the runtime environment.
    """

    config = get_app_config()

    summary = {
        "environment": config.environment,
        "debug": config.debug,
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "hostname": socket.gethostname(),
        "architecture": platform.machine(),
        "python_executable": sys.executable,
    }

    return ServiceResult.ok(
        data=summary,
        message="Environment summary retrieved successfully.",
    )