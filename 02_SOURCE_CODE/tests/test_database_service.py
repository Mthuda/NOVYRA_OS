"""
===============================================================================
NOVYRA OS

File:
    test_database_service.py

Purpose:
    Unit tests for the Database Service.

Description:
    These tests verify that the Database Service correctly manages the
    lifecycle of the application's database.

    The service is responsible for:

        • Creating database connections
        • Initializing the database
        • Closing database connections
        • Performing health checks
        • Returning database information

    These tests intentionally verify the service layer rather than the lower
    level database infrastructure.

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

import pytest

from app.core.database_config import DatabaseConfig
from app.services import database_service


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def temporary_database(monkeypatch, tmp_path):
    """
    Configure the Database Service to use a temporary SQLite database.

    Each test receives its own isolated database, preventing tests from
    interfering with one another.
    """

    database_path = tmp_path / "novyra_test.db"

    monkeypatch.setattr(
        database_service,
        "get_database_config",
        lambda: DatabaseConfig(
            database_path=str(database_path),
        ),
    )

    return database_path


# =============================================================================
# Database Connection Tests
# =============================================================================


def test_get_database_returns_connection(
    temporary_database,
):
    """
    Verify that the service returns a valid SQLite connection.
    """

    result = database_service.get_database()

    assert result.success is True
    assert result.data is not None

    connection = result.data

    connection.execute("SELECT 1")

    connection.close()


# =============================================================================
# Database Initialization Tests
# =============================================================================


def test_initialize_database(
    temporary_database,
):
    """
    Verify that the database initializes successfully.
    """

    result = database_service.initialize()

    assert result.success is True
    assert result.error_code is None

    assert temporary_database.exists()


def test_initialize_database_is_idempotent(
    temporary_database,
):
    """
    Verify that database initialization can be executed multiple times.
    """

    first = database_service.initialize()
    second = database_service.initialize()

    assert first.success is True
    assert second.success is True


# =============================================================================
# Database Shutdown Tests
# =============================================================================


def test_close_database(
    temporary_database,
):
    """
    Verify that database connections can be closed successfully.
    """

    result = database_service.get_database()

    connection = result.data

    assert connection is not None

    close_result = database_service.close_database(
        connection,
    )

    assert close_result.success is True


# =============================================================================
# Database Health Tests
# =============================================================================


def test_database_health_check(
    temporary_database,
):
    """
    Verify that the database passes a health check.
    """

    database_service.initialize()

    result = database_service.check_database_health()

    assert result.success is True
    assert result.error_code is None


# =============================================================================
# Database Information Tests
# =============================================================================


def test_database_information(
    temporary_database,
):
    """
    Verify that the service returns database metadata.
    """

    database_service.initialize()

    result = database_service.get_database_information()

    assert result.success is True
    assert result.data is not None

    information = result.data

    assert information.database_exists is True
    assert information.database_name == "novyra_test.db"

    expected_directory = str(
        Path(temporary_database).parent.resolve()
    )

    assert information.database_directory == expected_directory

    assert information.database_path.endswith(
        "novyra_test.db"
    )