"""
===============================================================================
NOVYRA OS

Package:
    app.core

Purpose:
    Core infrastructure package.

Description:
    This package contains the fundamental infrastructure used throughout
    NOVYRA OS.

    The modules inside this package provide:

        • Application configuration
        • Database configuration
        • Logging configuration
        • Project metadata
        • Project path utilities
        • Standard service result objects

    These modules are intentionally independent from business logic and
    provide reusable functionality for every other package in the system.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Public Package Exports
# =============================================================================

from app.core.config import AppConfig, get_app_config
from app.core.database_config import (
    DatabaseConfig,
    get_database_config,
)
from app.core.logging_setup import setup_logging
from app.core.paths import get_project_root
from app.core.project_info import (
    PROJECT_NAME,
    PROJECT_STAGE,
    PROJECT_VERSION,
)
from app.core.service_result import ServiceResult

# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "AppConfig",
    "DatabaseConfig",
    "ServiceResult",
    "PROJECT_NAME",
    "PROJECT_VERSION",
    "PROJECT_STAGE",
    "get_app_config",
    "get_database_config",
    "get_project_root",
    "setup_logging",
]