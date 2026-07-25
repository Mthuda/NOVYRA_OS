"""
NOVYRA OS
Phase 2 - Core Application Skeleton

This is the main entry point for the application.
"""

from app.core.logging_setup import setup_logging
from app.core.config import get_app_config
from app.core.project_info import PROJECT_NAME, PROJECT_VERSION, PROJECT_STAGE


def main() -> None:
    """
    Main entry point for NOVYRA OS.
    """
    setup_logging()
    config = get_app_config()

    print("=" * 50)
    print(PROJECT_NAME)
    print("=" * 50)
    print(f"Version: {PROJECT_VERSION}")
    print(f"Stage: {PROJECT_STAGE}")
    print(f"Project Name: {config.project_name}")
    print(f"Environment: {config.environment}")
    print(f"Debug Mode: {config.debug}")
    print("=" * 50)


if __name__ == "__main__":
    main()