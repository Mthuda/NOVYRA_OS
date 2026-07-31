"""
===============================================================================
NOVYRA OS

File:
    main.py

Purpose:
    Application entry point.

Description:
    This module starts the NOVYRA OS application.

    It is intentionally lightweight and acts only as an orchestrator.

    Responsibilities include:

        • Configure application logging
        • Initialize core platform services
        • Display startup information
        • Gracefully shut down resources

    Business logic must never be implemented here.
    All business operations belong inside the appropriate service layer.

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from app.core.config import get_app_config
from app.core.logging_setup import setup_logging
from app.services.database_service import (
    close_database,
    get_database,
    initialize,
)
from app.services.system_service import get_system_summary

# =============================================================================
# Main Application
# =============================================================================


def main() -> None:
    """
    Start the NOVYRA OS application.

    This function coordinates application startup and shutdown while
    delegating all operational work to the service layer.
    """

    # -------------------------------------------------------------------------
    # Configure application logging.
    # -------------------------------------------------------------------------

    setup_logging()

    # -------------------------------------------------------------------------
    # Load application configuration.
    # -------------------------------------------------------------------------

    config = get_app_config()

    # -------------------------------------------------------------------------
    # Initialize the database.
    # -------------------------------------------------------------------------

    database_result = initialize()

    if not database_result.success:
        print(f"ERROR: {database_result.message}")

        if database_result.error_code:
            print(f"Error Code: {database_result.error_code}")

        return

    # -------------------------------------------------------------------------
    # Obtain the active database connection.
    # -------------------------------------------------------------------------

    connection_result = get_database()

    if not connection_result.success:
        print(f"ERROR: {connection_result.message}")

        if connection_result.error_code:
            print(f"Error Code: {connection_result.error_code}")

        return

    database_connection = connection_result.data

    if database_connection is None:
        print("ERROR: Database connection unavailable.")
        return

    try:
        # ---------------------------------------------------------------------
        # Retrieve system information.
        # ---------------------------------------------------------------------

        result = get_system_summary(config)

        if not result.success:
            print(f"ERROR: {result.message}")

            if result.error_code:
                print(f"Error Code: {result.error_code}")

            return

        summary = result.data

        if summary is None:
            print("ERROR: System summary returned no data.")
            return

        # ---------------------------------------------------------------------
        # Display startup banner.
        # ---------------------------------------------------------------------

        print("=" * 50)
        print(summary["project_name"])
        print("=" * 50)
        print(f"Version: {summary['version']}")
        print(f"Stage: {summary['stage']}")
        print(f"Environment: {summary['environment']}")
        print(f"Debug Mode: {summary['debug']}")
        print(f"Project Root: {summary['project_root']}")
        print("=" * 50)

    finally:
        # ---------------------------------------------------------------------
        # Always close the database connection.
        # ---------------------------------------------------------------------

        close_result = close_database(database_connection)

        if not close_result.success:
            print(f"WARNING: {close_result.message}")


# =============================================================================
# Program Entry Point
# =============================================================================

if __name__ == "__main__":
    main()