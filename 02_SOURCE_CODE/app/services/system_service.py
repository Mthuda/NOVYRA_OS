"""
System information service for NOVYRA OS.

This module provides application-level system information
through a consistent ServiceResult interface.
"""

from app.core.config import AppConfig
from app.core.paths import get_project_root
from app.core.project_info import (
    PROJECT_NAME,
    PROJECT_STAGE,
    PROJECT_VERSION,
)
from app.core.service_result import ServiceResult


def get_system_summary(
    config: AppConfig,
) -> ServiceResult[dict[str, object]]:
    """
    Build a summary of the current NOVYRA OS runtime.

    Args:
        config:
            Application configuration.

    Returns:
        ServiceResult containing system summary information.
    """

    summary = {
        "project_name": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "stage": PROJECT_STAGE,
        "environment": config.environment,
        "debug": config.debug,
        "project_root": str(get_project_root()),
    }

    return ServiceResult.ok(
        data=summary,
        message="System summary generated successfully.",
    )