"""
===============================================================================
NOVYRA OS

File:
    config_service.py

Purpose:
    Configuration service.

Description:
    This service provides the official interface for accessing the NOVYRA OS
    application configuration.

    Rather than allowing application components to interact directly with the
    configuration layer, all configuration requests should pass through this
    service.

    Responsibilities include:

        • Loading application configuration
        • Reloading configuration
        • Providing configuration information
        • Returning standardized ServiceResult objects

    Future enhancements may include:

        • Environment profile support
        • User-specific configuration
        • Configuration validation
        • Database-backed configuration
        • Remote configuration providers

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from app.core.config import (
    AppConfig,
    get_app_config,
)
from app.core.service_result import ServiceResult
from app.services.logging_service import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Configuration Loading
# =============================================================================


def get_configuration() -> ServiceResult[AppConfig]:
    """
    Load the current application configuration.

    Returns:
        ServiceResult containing the active AppConfig instance.
    """

    try:
        config = get_app_config()

        logger.info(
            "Application configuration loaded successfully."
        )

        return ServiceResult.ok(
            data=config,
            message="Configuration loaded successfully.",
        )

    except Exception:
        logger.exception(
            "Failed to load application configuration."
        )

        return ServiceResult.fail(
            message="Failed to load application configuration.",
            error_code="CONFIGURATION_LOAD_ERROR",
        )


# =============================================================================
# Configuration Reload
# =============================================================================


def reload_configuration() -> ServiceResult[AppConfig]:
    """
    Reload the application configuration.

    Returns:
        ServiceResult containing the refreshed configuration.
    """

    logger.info(
        "Reloading application configuration."
    )

    return get_configuration()


# =============================================================================
# Configuration Information
# =============================================================================


def get_configuration_information(
) -> ServiceResult[dict[str, object]]:
    """
    Retrieve configuration metadata.

    Returns:
        ServiceResult containing configuration information.
    """

    result = get_configuration()

    if not result.success:
        return ServiceResult.fail(
            message=result.message,
            error_code=result.error_code,
        )

    config = result.data

    if config is None:
        logger.error(
            "Configuration service returned no configuration."
        )

        return ServiceResult.fail(
            message="Configuration unavailable.",
            error_code="CONFIGURATION_MISSING",
        )

    information = {
        "project_name": config.project_name,
        "environment": config.environment,
        "debug": config.debug,
    }

    logger.info(
        "Configuration information retrieved successfully."
    )

    return ServiceResult.ok(
        data=information,
        message="Configuration information retrieved successfully.",
    )