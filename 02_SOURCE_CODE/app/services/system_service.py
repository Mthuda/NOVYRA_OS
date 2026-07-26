"""
System service for NOVYRA OS.

This module provides application-level operations related to
system and project information.
"""

from app.core.config import AppConfig
from app.core.paths import get_project_root
from app.core.project_info import (
    PROJECT_NAME,
    PROJECT_STAGE,
    PROJECT_VERSION,
)


def get_system_summary(config: AppConfig) -> dict[str, object]:
    """
    Build a summary of the current NOVYRA OS runtime.

    Args:
        config: Current application configuration.

    Returns:
        Dictionary containing project and runtime information.
    """

    return {
        "project_name": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "stage": PROJECT_STAGE,
        "environment": config.environment,
        "debug": config.debug,
        "project_root": str(get_project_root()),
    }