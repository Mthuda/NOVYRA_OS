"""
===============================================================================
NOVYRA OS

File:
    database_config.py

Purpose:
    Database configuration management.

Description:
    Loads database configuration from environment variables and provides
    a single immutable configuration object for database infrastructure.

    Centralising database configuration allows the persistence layer to
    remain independent from hard-coded paths or storage technologies.

    Although NOVYRA currently uses SQLite, this configuration layer is
    intentionally designed so future versions can support additional
    database engines with minimal changes.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import os
from dataclasses import dataclass

# =============================================================================
# Database Configuration Model
# =============================================================================


@dataclass(frozen=True)
class DatabaseConfig:
    """
    Immutable database configuration.

    Attributes:
        database_path:
            Filesystem path to the SQLite database.
    """

    database_path: str


# =============================================================================
# Public Functions
# =============================================================================


def get_database_config() -> DatabaseConfig:
    """
    Load database configuration from environment variables.

    Environment Variables

        NOVYRA_DATABASE_PATH
            Location of the SQLite database file.

    Returns:
        Immutable DatabaseConfig instance.
    """

    # -------------------------------------------------------------------------
    # Read the database location.
    #
    # A default value is supplied so that a development environment works
    # immediately after cloning the repository without requiring additional
    # configuration.
    # -------------------------------------------------------------------------

    database_path = os.getenv(
        "NOVYRA_DATABASE_PATH",
        "08_BACKUPS/novyra_os.db",
    ).strip()

    # -------------------------------------------------------------------------
    # Return a single immutable configuration object.
    #
    # Keeping configuration immutable prevents accidental runtime changes
    # that could affect database behaviour.
    # -------------------------------------------------------------------------

    return DatabaseConfig(
        database_path=database_path,
    )