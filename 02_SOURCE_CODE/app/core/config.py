"""
Application configuration for NOVYRA OS.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    project_name: str
    environment: str
    debug: bool


def get_app_config() -> AppConfig:
    """
    Load application configuration from environment variables.
    """
    project_name = os.getenv("NOVYRA_PROJECT_NAME", "NOVYRA OS")
    environment = os.getenv("NOVYRA_ENVIRONMENT", "development")
    debug_raw = os.getenv("NOVYRA_DEBUG", "true").strip().lower()
    debug = debug_raw in {"1", "true", "yes", "on"}

    return AppConfig(
        project_name=project_name,
        environment=environment,
        debug=debug,
    )