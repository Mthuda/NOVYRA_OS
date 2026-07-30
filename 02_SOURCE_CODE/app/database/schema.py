"""
===============================================================================
NOVYRA OS

File:
    schema.py

Purpose:
    Database schema management.

Description:
    This module creates and maintains the SQLite database schema used by
    NOVYRA OS.

    The schema creation process is intentionally idempotent, allowing the
    application to initialise the database safely every time it starts.

    Future project phases will expand this module with additional tables,
    indexes, constraints and database migrations.

Phase:
    Phase 4

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import sqlite3

# =============================================================================
# Public Functions
# =============================================================================


def initialize_database(connection: sqlite3.Connection) -> None:
    """
    Initialise the NOVYRA OS database schema.

    Calling this function multiple times is safe because every CREATE TABLE
    statement uses IF NOT EXISTS.

    Args:
        connection:
            Active SQLite database connection.
    """

    # -------------------------------------------------------------------------
    # Create the Opportunities table.
    #
    # This table stores every opportunity collected by NOVYRA OS.
    #
    # Future phases will extend this schema with:
    #
    #     • Users
    #     • Companies
    #     • Saved searches
    #     • Notifications
    #     • AI processing metadata
    # -------------------------------------------------------------------------

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS opportunities (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            source TEXT NOT NULL,
            description TEXT,
            metadata TEXT NOT NULL DEFAULT '{}'
        )
        """
    )

    # -------------------------------------------------------------------------
    # Persist schema changes.
    # -------------------------------------------------------------------------

    connection.commit()