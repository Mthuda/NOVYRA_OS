"""
Main entry point for NOVYRA OS.
"""

from __future__ import annotations

from app.core.config import get_app_config
from app.core.database_config import get_database_config
from app.core.logging_setup import setup_logging
from app.database.connection import get_database_connection
from app.database.schema import initialize_database
from app.services.system_service import get_system_summary


def main() -> None:
    """
    Start the NOVYRA OS application.
    """

    setup_logging()

    config = get_app_config()

    database_config = get_database_config()
    database_connection = get_database_connection(database_config)

    try:
        initialize_database(database_connection)

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
        database_connection.close()


if __name__ == "__main__":
    main()