"""
===============================================================================
NOVYRA OS

File:
    test_database.py

Purpose:
    Unit tests for the SQLite database infrastructure.

Description:
    Verifies the database configuration system, connection creation,
    schema initialization, and database file generation.

    These tests ensure that the persistence layer behaves correctly before
    higher-level repositories and services interact with it.

Phase:
    Phase 4
===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import sqlite3

from app.core.database_config import (
    DatabaseConfig,
    get_database_config,
)
from app.database.connection import get_database_connection
from app.database.schema import initialize_database

# =============================================================================
# Configuration Tests
# =============================================================================


def test_default_database_configuration(monkeypatch) -> None:
    """
    Verify that the default SQLite database path is used when no
    environment variable has been configured.
    """

    monkeypatch.delenv(
        "NOVYRA_DATABASE_PATH",
        raising=False,
    )

    config = get_database_config()

    assert isinstance(config, DatabaseConfig)
    assert config.database_path == "08_BACKUPS/novyra_os.db"


def test_custom_database_configuration(monkeypatch) -> None:
    """
    Verify that a custom database path can be loaded from
    an environment variable.
    """

    monkeypatch.setenv(
        "NOVYRA_DATABASE_PATH",
        "custom/test.db",
    )

    config = get_database_config()

    assert config.database_path == "custom/test.db"


# =============================================================================
# Connection Tests
# =============================================================================


def test_database_connection(tmp_path) -> None:
    """
    Verify that a SQLite connection can be created successfully and that
    the database file is automatically created.
    """

    database_path = tmp_path / "test.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        assert isinstance(
            connection,
            sqlite3.Connection,
        )

        assert database_path.exists()

    finally:
        connection.close()


def test_database_connection_uses_row_factory(tmp_path) -> None:
    """
    Verify that SQLite rows are returned as sqlite3.Row objects,
    allowing dictionary-style column access.
    """

    database_path = tmp_path / "test.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        assert connection.row_factory is sqlite3.Row

    finally:
        connection.close()


# =============================================================================
# Schema Initialization Tests
# =============================================================================


def test_initialize_database_creates_opportunities_table(
    tmp_path,
) -> None:
    """
    Verify that database initialization creates the Opportunities table.
    """

    database_path = tmp_path / "test.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        initialize_database(connection)

        result = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            AND name = 'opportunities'
            """
        ).fetchone()

        assert result is not None
        assert result["name"] == "opportunities"

    finally:
        connection.close()


def test_initialize_database_is_idempotent(tmp_path) -> None:
    """
    Verify that running schema initialization multiple times
    does not create duplicate tables or raise errors.
    """

    database_path = tmp_path / "test.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        initialize_database(connection)
        initialize_database(connection)

        result = connection.execute(
            """
            SELECT COUNT(*) AS table_count
            FROM sqlite_master
            WHERE type='table'
            AND name='opportunities'
            """
        ).fetchone()

        assert result["table_count"] == 1

    finally:
        connection.close()


# =============================================================================
# Database File Tests
# =============================================================================


def test_database_file_is_created(tmp_path) -> None:
    """
    Verify that initializing the database creates the SQLite
    database file on disk.
    """

    database_path = tmp_path / "novyra_os.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        initialize_database(connection)

        assert database_path.exists()
        assert database_path.is_file()

    finally:
        connection.close()