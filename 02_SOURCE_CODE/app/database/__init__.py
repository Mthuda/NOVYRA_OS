"""
===============================================================================
NOVYRA OS

Package:
    app.database

Purpose:
    Database infrastructure package.

Description:
    This package provides the database infrastructure used throughout
    NOVYRA OS.

    Responsibilities include:

        • Opening SQLite database connections.
        • Initialising the database schema.
        • Future database migration support.

    Repository implementations should depend on this package instead of
    directly interacting with SQLite.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Public Package Exports
# =============================================================================

from app.database.connection import get_database_connection
from app.database.schema import initialize_database

# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "get_database_connection",
    "initialize_database",
]