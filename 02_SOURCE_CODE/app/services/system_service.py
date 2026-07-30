"""
===============================================================================
NOVYRA OS

File:
    system_service.py

Purpose:
    System information service.

Description:
    This service provides runtime information about the currently running
    NOVYRA OS application.

    The information returned by this module is intended for:

        • Startup screens
        • Health checks
        • Diagnostics
        • Future REST API endpoints
        • Administrative dashboards

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

from app.core.config import AppConfig
from app.core.paths import get_project_root
from app.core.project_info import (
    PROJECT_NAME,
    PROJECT_STAGE,
    PROJECT_VERSION,
)
from app.core.service_result import ServiceResult

# =============================================================================
# Public Functions
# =============================================================================


def get_system_summary(
    config: AppConfig,
) -> ServiceResult[dict[str, object]]:
    """
    Build a summary describing the current NOVYRA OS runtime.

    Args:
        config:
            Application configuration.

    Returns:
        Successful ServiceResult containing runtime information.
    """

    # -------------------------------------------------------------------------
    # Build a summary dictionary that can be safely consumed by any UI,
    # API endpoint or monitoring component.
    # -------------------------------------------------------------------------

    summary = {
        "project_name": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "stage": PROJECT_STAGE,
        "environment": config.environment,
        "debug": config.debug,
        "project_root": str(get_project_root()),
    }

    # -------------------------------------------------------------------------
    # Return the summary wrapped in a standard ServiceResult object.
    # -------------------------------------------------------------------------

    return ServiceResult.ok(
        data=summary,
        message="System summary generated successfully.",
    )