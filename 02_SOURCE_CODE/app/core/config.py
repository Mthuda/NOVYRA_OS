"""
Application configuration for NOVYRA OS.

This module provides a central configuration object for the application.
Configuration values are loaded from environment variables with safe
development defaults.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    """
    Immutable application configuration.

    Attributes:
        project_name: Name of the application.
        environment: Current runtime environment.
        debug: Whether debug mode is enabled.
    """

    project_name: str
    environment: str
    debug: bool


def _parse_bool(value: str) -> bool:
    """
    Convert a string environment variable into a boolean.

    Accepted true values:
        1, true, yes, on

    Accepted false values:
        0, false, no, off

    Args:
        value: Raw string value.

    Returns:
        Parsed boolean value.

    Raises:
        ValueError: If the value cannot be interpreted as a boolean.
    """

    normalized = value.strip().lower()

    if normalized in {"1", "true", "yes", "on"}:
        return True

    if normalized in {"0", "false", "no", "off"}:
        return False

    raise ValueError(
        f"Invalid boolean value: {value!r}. "
        "Expected one of: 1, 0, true, false, yes, no, on, off."
    )


def get_app_config() -> AppConfig:
    """
    Load application configuration from environment variables.

    Environment variables:

        NOVYRA_PROJECT_NAME
            Application name.

        NOVYRA_ENVIRONMENT
            Runtime environment, for example:
            development, testing, staging, production.

        NOVYRA_DEBUG
            Controls debug mode.

    Returns:
        AppConfig containing the application configuration.
    """

    project_name = os.getenv(
        "NOVYRA_PROJECT_NAME",
        "NOVYRA OS",
    ).strip()

    environment = os.getenv(
        "NOVYRA_ENVIRONMENT",
        "development",
    ).strip().lower()

    debug_raw = os.getenv(
        "NOVYRA_DEBUG",
        "true",
    )

    debug = _parse_bool(debug_raw)

    return AppConfig(
        project_name=project_name,
        environment=environment,
        debug=debug,
    )