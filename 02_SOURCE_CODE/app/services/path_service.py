"""
===============================================================================
NOVYRA OS

File:
    path_service.py

Purpose:
    Filesystem path service.

Description:
    This service provides the official interface for accessing important
    filesystem locations used throughout NOVYRA OS.

    Rather than constructing filesystem paths directly, application components
    should retrieve paths through this service.

    Responsibilities include:

        • Project root
        • Database directory
        • Backup directory
        • Documentation directory
        • Source code directory
        • Log directory

    Future enhancements may include:

        • User workspace
        • Plugin directory
        • AI memory storage
        • Cache directory
        • Temporary files
        • Import/Export locations

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

from app.core.paths import get_project_root
from app.core.service_result import ServiceResult
from app.services.logging_service import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Root Directory
# =============================================================================


def get_root_directory() -> ServiceResult[Path]:
    """
    Return the NOVYRA project root directory.
    """

    try:
        root = get_project_root()

        logger.info("Project root directory retrieved.")

        return ServiceResult.ok(
            data=root,
            message="Project root directory retrieved successfully.",
        )

    except Exception:
        logger.exception(
            "Failed to retrieve project root."
        )

        return ServiceResult.fail(
            message="Unable to determine project root.",
            error_code="ROOT_DIRECTORY_ERROR",
        )


# =============================================================================
# Source Code Directory
# =============================================================================


def get_source_directory() -> ServiceResult[Path]:
    """
    Return the source code directory.
    """

    root = get_root_directory()

    if not root.success or root.data is None:
        return ServiceResult.fail(
            message="Unable to determine source directory.",
            error_code="SOURCE_DIRECTORY_ERROR",
        )

    return ServiceResult.ok(
        data=root.data / "02_SOURCE_CODE",
        message="Source directory retrieved successfully.",
    )


# =============================================================================
# Documentation Directory
# =============================================================================


def get_documentation_directory() -> ServiceResult[Path]:
    """
    Return the documentation directory.
    """

    root = get_root_directory()

    if not root.success or root.data is None:
        return ServiceResult.fail(
            message="Unable to determine documentation directory.",
            error_code="DOCUMENTATION_DIRECTORY_ERROR",
        )

    return ServiceResult.ok(
        data=root.data / "09_DOCUMENTATION",
        message="Documentation directory retrieved successfully.",
    )


# =============================================================================
# Backup Directory
# =============================================================================


def get_backup_directory() -> ServiceResult[Path]:
    """
    Return the backup directory.
    """

    root = get_root_directory()

    if not root.success or root.data is None:
        return ServiceResult.fail(
            message="Unable to determine backup directory.",
            error_code="BACKUP_DIRECTORY_ERROR",
        )

    return ServiceResult.ok(
        data=root.data / "08_BACKUPS",
        message="Backup directory retrieved successfully.",
    )


# =============================================================================
# Database File
# =============================================================================


def get_database_path() -> ServiceResult[Path]:
    """
    Return the default SQLite database path.
    """

    backup = get_backup_directory()

    if not backup.success or backup.data is None:
        return ServiceResult.fail(
            message="Unable to determine database path.",
            error_code="DATABASE_PATH_ERROR",
        )

    return ServiceResult.ok(
        data=backup.data / "novyra_os.db",
        message="Database path retrieved successfully.",
    )