"""
===============================================================================
NOVYRA OS

File:
    connection.py

Purpose:
    SQLite database connection management.

Description:
    This module is responsible for creating SQLite database connections used
    throughout NOVYRA OS.

    It ensures:

        • The database directory exists.
        • The SQLite database file is created automatically if necessary.
        • Connections use sqlite3.Row for dictionary-style column access.

    All repositories should obtain their database connections through this
    module rather than calling sqlite3.connect() directly.

Phase:
    Phase 4

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import sqlite3
from pathlib import Path

from app.core.database_config import DatabaseConfig

# =============================================================================
# Public Functions
# =============================================================================


def get_database_connection(
    config: DatabaseConfig,
) -> sqlite3.Connection:
    """
    Create and configure a SQLite database connection.

    Responsibilities:
        • Create the parent directory if it does not exist.
        • Open a SQLite database connection.
        • Configure dictionary-style row access.

    Args:
        config:
            Database configuration.

    Returns:
        Configured SQLite database connection.
    """

    # -------------------------------------------------------------------------
    # Convert the configured database path into a Path object for easier
    # filesystem manipulation.
    # -------------------------------------------------------------------------

    database_path = Path(config.database_path)

    # -------------------------------------------------------------------------
    # Ensure the parent directory exists before opening the database.
    #
    # Example:
    #
    #     08_BACKUPS/
    #         novyra_os.db
    #
    # If the folder does not already exist it will be created automatically.
    # -------------------------------------------------------------------------

    if database_path.parent != Path("."):
        database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    # -------------------------------------------------------------------------
    # Open the SQLite database.
    #
    # SQLite automatically creates the database file if it does not already
    # exist.
    # -------------------------------------------------------------------------

    connection = sqlite3.connect(database_path)

    # -------------------------------------------------------------------------
    # Configure rows to behave like dictionaries.
    #
    # Instead of:
    #
    #     row[0]
    #
    # We can write:
    #
    #     row["title"]
    #
    # which is significantly easier to read and maintain.
    # -------------------------------------------------------------------------

    connection.row_factory = sqlite3.Row

    return connection