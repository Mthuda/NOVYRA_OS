"""
Tests for NOVYRA OS SQLite database infrastructure.
"""

import sqlite3

from app.core.database_config import (
    DatabaseConfig,
    get_database_config,
)
from app.database.connection import get_database_connection
from app.database.schema import initialize_database


def test_default_database_configuration(monkeypatch):
    """Test the default database configuration."""

    monkeypatch.delenv(
        "NOVYRA_DATABASE_PATH",
        raising=False,
    )

    config = get_database_config()

    assert isinstance(config, DatabaseConfig)
    assert config.database_path == "08_BACKUPS/novyra_os.db"


def test_custom_database_configuration(monkeypatch):
    """Test loading a custom database path."""

    monkeypatch.setenv(
        "NOVYRA_DATABASE_PATH",
        "custom/test.db",
    )

    config = get_database_config()

    assert config.database_path == "custom/test.db"


def test_database_connection(tmp_path):
    """Test creating a SQLite database connection."""

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


def test_database_connection_uses_row_factory(tmp_path):
    """Test that SQLite rows support dictionary-style access."""

    database_path = tmp_path / "test.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        assert connection.row_factory is sqlite3.Row
    finally:
        connection.close()


def test_initialize_database_creates_opportunities_table(tmp_path):
    """Test that database initialization creates the opportunities table."""

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


def test_initialize_database_is_idempotent(tmp_path):
    """Test that database initialization can run multiple times."""

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
            SELECT COUNT(*)
            AS table_count
            FROM sqlite_master
            WHERE type = 'table'
            AND name = 'opportunities'
            """
        ).fetchone()

        assert result["table_count"] == 1
    finally:
        connection.close()