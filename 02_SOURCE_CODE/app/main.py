"""
===============================================================================
NOVYRA OS

File:
    main.py

Purpose:
    Application entry point.

Description:
    This module is responsible for starting the NOVYRA OS backend.

    During startup it performs the following initialization sequence:

        1. Configure logging
        2. Load application configuration
        3. Load database configuration
        4. Establish the database connection
        5. Initialize the database schema
        6. Collect system information
        7. Display startup information
        8. Shut down cleanly

    As NOVYRA grows, additional initialization tasks (AI services,
    schedulers, background workers, API servers, and mobile integration)
    will be added here while keeping the startup process organized.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Future Imports
# =============================================================================

from __future__ import annotations

# =============================================================================
# Application Imports
# =============================================================================

from app.core.config import get_app_config
from app.core.database_config import get_database_config
from app.core.logging_setup import setup_logging
from app.database.connection import get_database_connection
from app.database.schema import initialize_database
from app.services.system_service import get_system_summary

# =============================================================================
# Application Entry Point
# =============================================================================


def main() -> None:
    """
    Start the NOVYRA OS application.

    This function coordinates the complete application startup process.

    Returns:
        None
    """

    # -------------------------------------------------------------------------
    # Configure the application's logging system before performing any work.
    # -------------------------------------------------------------------------

    setup_logging()

    # -------------------------------------------------------------------------
    # Load runtime configuration from environment variables.
    # -------------------------------------------------------------------------

    config = get_app_config()

    # -------------------------------------------------------------------------
    # Load database configuration and establish the SQLite connection.
    # -------------------------------------------------------------------------

    database_config = get_database_config()

    database_connection = get_database_connection(
        database_config,
    )

    try:

        # ---------------------------------------------------------------------
        # Ensure the database schema exists before services begin using it.
        # ---------------------------------------------------------------------

        initialize_database(database_connection)

        # ---------------------------------------------------------------------
        # Gather runtime information used for diagnostics and startup.
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
        # Display application startup information.
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
        # Always close the database connection to avoid resource leaks.
        # ---------------------------------------------------------------------

        database_connection.close()


# =============================================================================
# Script Entry Point
# =============================================================================

if __name__ == "__main__":
    main()