"""
NOVYRA OS
Phase 2 - Core Application Skeleton

This is the main entry point for the application.
"""

from app.core.logging_setup import setup_logging
from app.core.config import get_app_config


def main() -> None:
    """
    Main entry point for NOVYRA OS.
    """
    setup_logging()
    config = get_app_config()

    print("=" * 50)
    print("NOVYRA OS")
    print("=" * 50)
    print(f"Project Name: {config.project_name}")
    print(f"Environment: {config.environment}")
    print(f"Debug Mode: {config.debug}")
    print("=" * 50)


if __name__ == "__main__":
    main()