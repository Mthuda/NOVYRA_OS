"""
Tests for the NOVYRA OS path service.
"""

from pathlib import Path

from app.services import path_service


# =============================================================================
# Root Directory
# =============================================================================


def test_get_root_directory():
    """
    Verify that the project root directory can be retrieved.
    """

    result = path_service.get_root_directory()

    assert result.success is True
    assert result.data is not None
    assert isinstance(result.data, Path)
    assert result.data.exists()


# =============================================================================
# Source Directory
# =============================================================================


def test_get_source_directory():
    """
    Verify that the source directory is returned.
    """

    result = path_service.get_source_directory()

    assert result.success is True
    assert result.data is not None
    assert result.data.name == "02_SOURCE_CODE"
    assert result.data.exists()


# =============================================================================
# Documentation Directory
# =============================================================================


def test_get_documentation_directory():
    """
    Verify that the documentation directory is returned.
    """

    result = path_service.get_documentation_directory()

    assert result.success is True
    assert result.data is not None
    assert result.data.name == "09_DOCUMENTATION"
    assert result.data.exists()


# =============================================================================
# Backup Directory
# =============================================================================


def test_get_backup_directory():
    """
    Verify that the backup directory is returned.
    """

    result = path_service.get_backup_directory()

    assert result.success is True
    assert result.data is not None
    assert result.data.name == "08_BACKUPS"
    assert result.data.exists()


# =============================================================================
# Database Path
# =============================================================================


def test_get_database_path():
    """
    Verify that the database path is returned.
    """

    result = path_service.get_database_path()

    assert result.success is True
    assert result.data is not None

    assert result.data.name == "novyra_os.db"
    assert result.data.parent.name == "08_BACKUPS"