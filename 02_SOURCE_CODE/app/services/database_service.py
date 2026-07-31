"""
===============================================================================
NOVYRA OS

File:
    database_service.py

Purpose:
    Database lifecycle service.

Description:
    This service provides the official interface for managing the NOVYRA OS
    database.

    Rather than allowing application components to communicate directly with
    SQLite, all database lifecycle operations should pass through this service.

    Responsibilities include:

        • Opening database connections
        • Initializing the database schema
        • Closing database connections
        • Performing database health checks
        • Providing database information

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import sqlite3
from pathlib import Path

from app.core.database_config import (
    DatabaseConfig,
    get_database_config,
)
from app.core.service_result import ServiceResult
from app.database.connection import get_database_connection
from app.database.schema import initialize_database
from app.models.database_info import DatabaseInfo


# =============================================================================
# Database Connection
# =============================================================================


def get_database() -> ServiceResult[sqlite3.Connection]:
    """
    Create and return a database connection.
    """

    try:
        config = get_database_config()

        connection = get_database_connection(config)

        return ServiceResult.ok(
            data=connection,
            message="Database connection established successfully.",
        )

    except Exception as exc:
        return ServiceResult.fail(
            message=f"Failed to connect to the database: {exc}",
            error_code="DATABASE_CONNECTION_ERROR",
        )


# =============================================================================
# Database Initialization
# =============================================================================


def initialize() -> ServiceResult[None]:
    """
    Initialize the configured database.
    """

    result = get_database()

    if not result.success:
        return ServiceResult.fail(
            message=result.message,
            error_code=result.error_code,
        )

    connection = result.data

    if connection is None:
        return ServiceResult.fail(
            message="Database connection is unavailable.",
            error_code="DATABASE_CONNECTION_MISSING",
        )

    try:
        initialize_database(connection)

        return ServiceResult.ok(
            message="Database initialized successfully.",
        )

    except Exception as exc:
        return ServiceResult.fail(
            message=f"Database initialization failed: {exc}",
            error_code="DATABASE_INITIALIZATION_ERROR",
        )

    finally:
        connection.close()


# =============================================================================
# Database Shutdown
# =============================================================================


def close_database(
    connection: sqlite3.Connection,
) -> ServiceResult[None]:
    """
    Close a database connection.
    """

    try:
        connection.close()

        return ServiceResult.ok(
            message="Database connection closed successfully.",
        )

    except Exception as exc:
        return ServiceResult.fail(
            message=f"Failed to close database connection: {exc}",
            error_code="DATABASE_CLOSE_ERROR",
        )


# =============================================================================
# Database Health
# =============================================================================


def check_database_health() -> ServiceResult[None]:
    """
    Verify that the configured database is operational.
    """

    result = get_database()

    if not result.success:
        return ServiceResult.fail(
            message=result.message,
            error_code=result.error_code,
        )

    connection = result.data

    if connection is None:
        return ServiceResult.fail(
            message="Database connection is unavailable.",
            error_code="DATABASE_CONNECTION_MISSING",
        )

    try:
        connection.execute("SELECT 1")

        return ServiceResult.ok(
            message="Database health check passed.",
        )

    except Exception as exc:
        return ServiceResult.fail(
            message=f"Database health check failed: {exc}",
            error_code="DATABASE_HEALTH_ERROR",
        )

    finally:
        connection.close()


# =============================================================================
# Database Information
# =============================================================================


def get_database_information() -> ServiceResult[DatabaseInfo]:
    """
    Return information about the configured database.
    """

    try:
        config: DatabaseConfig = get_database_config()

        database_path = Path(config.database_path)

        information = DatabaseInfo(
            database_path=str(database_path.resolve()),
            database_exists=database_path.exists(),
            database_name=database_path.name,
            database_directory=str(database_path.parent.resolve()),
        )

        return ServiceResult.ok(
            data=information,
            message="Database information retrieved successfully.",
        )

    except Exception as exc:
        return ServiceResult.fail(
            message=f"Unable to retrieve database information: {exc}",
            error_code="DATABASE_INFORMATION_ERROR",
        )