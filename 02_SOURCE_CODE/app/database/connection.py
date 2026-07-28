"""
SQLite database connection utilities for NOVYRA OS.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from app.core.database_config import DatabaseConfig


def get_database_connection(
    config: DatabaseConfig,
) -> sqlite3.Connection:
    """
    Create a SQLite database connection.

    Args:
        config: Database configuration.

    Returns:
        SQLite database connection.
    """

    database_path = Path(config.database_path)

    if database_path.parent != Path("."):
        database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    connection = sqlite3.connect(database_path)

    connection.row_factory = sqlite3.Row

    return connection