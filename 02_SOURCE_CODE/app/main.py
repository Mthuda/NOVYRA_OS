"""
Main entry point for NOVYRA OS.
"""

from app.core.config import get_app_config
from app.core.logging_setup import setup_logging
from app.services.system_service import get_system_summary


def main() -> None:
    """
    Start the NOVYRA OS application.
    """

    setup_logging()

    config = get_app_config()
    summary = get_system_summary(config)

    print("=" * 50)
    print(summary["project_name"])
    print("=" * 50)
    print(f"Version: {summary['version']}")
    print(f"Stage: {summary['stage']}")
    print(f"Environment: {summary['environment']}")
    print(f"Debug Mode: {summary['debug']}")
    print(f"Project Root: {summary['project_root']}")
    print("=" * 50)


if __name__ == "__main__":
    main()