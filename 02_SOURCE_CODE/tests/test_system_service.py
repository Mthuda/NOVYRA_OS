"""
===============================================================================
NOVYRA OS

File:
    test_system_service.py

Purpose:
    Unit tests for the System Service.

Description:
    This module verifies that the System Service correctly reports
    application metadata and runtime information.

    The System Service provides information that is useful for:

        • Application startup
        • Diagnostics
        • Logging
        • Health monitoring
        • Future REST API endpoints
        • Future Kivy mobile application
        • Future Web Dashboard
        • Future Desktop application

    These tests ensure that the service always returns accurate project
    information wrapped inside a ServiceResult.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

from app.core.config import AppConfig
from app.services.system_service import get_system_summary

# =============================================================================
# Test Fixtures
# =============================================================================


def create_test_config() -> AppConfig:
    """
    Create a reusable application configuration for the system service tests.

    Returns:
        A development AppConfig instance.
    """

    return AppConfig(
        project_name="NOVYRA OS",
        environment="development",
        debug=True,
    )


# =============================================================================
# System Summary Tests
# =============================================================================


def test_system_summary() -> None:
    """
    Verify that the system summary returns the expected project metadata.

    The returned ServiceResult should contain the application's
    version information together with the current runtime configuration.
    """

    # Arrange
    config = create_test_config()

    # Act
    result = get_system_summary(config)

    # Assert
    assert result.success is True
    assert result.error_code is None
    assert result.data is not None

    assert result.data["project_name"] == "NOVYRA OS"
    assert result.data["version"] == "0.3.0"
    assert result.data["stage"] == "Phase 4 - Core Platform Services"
    assert result.data["environment"] == "development"
    assert result.data["debug"] is True


def test_system_summary_contains_project_root() -> None:
    """
    Verify that the system summary contains the project's root directory.

    The project root is required by future components that need to locate
    configuration files, databases, logs, backups, and documentation.
    """

    # Arrange
    config = create_test_config()

    # Act
    result = get_system_summary(config)

    # Assert
    assert result.success is True
    assert result.data is not None

    project_root = result.data["project_root"]

    assert isinstance(project_root, str)
    assert project_root != ""