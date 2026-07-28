"""
Database schema management for NOVYRA OS.
"""

from __future__ import annotations

import sqlite3


def initialize_database(connection: sqlite3.Connection) -> None:
    """
    Initialize the NOVYRA OS database schema.

    Args:
        connection: Active SQLite database connection.
    """

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS opportunities (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            source TEXT NOT NULL,
            description TEXT
        )
        """
    )

    connection.commit()