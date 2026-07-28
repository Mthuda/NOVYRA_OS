"""
Database configuration for NOVYRA OS.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class DatabaseConfig:
    """
    Immutable database configuration.

    Attributes:
        database_path: Filesystem path to the SQLite database.
    """

    database_path: str


def get_database_config() -> DatabaseConfig:
    """
    Load database configuration from environment variables.

    Environment variables:

        NOVYRA_DATABASE_PATH
            Path to the SQLite database file.

    Returns:
        DatabaseConfig containing database configuration.
    """

    database_path = os.getenv(
        "NOVYRA_DATABASE_PATH",
        "08_BACKUPS/novyra_os.db",
    ).strip()

    return DatabaseConfig(
        database_path=database_path,
    )