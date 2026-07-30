"""
===============================================================================
NOVYRA OS

File:
    config.py

Purpose:
    Centralised application configuration.

Description:
    Loads application configuration from environment variables and provides
    a single immutable configuration object that can be shared throughout
    the application.

Responsibilities:
    - Read environment variables
    - Validate configuration values
    - Convert text values into Python types
    - Produce an immutable AppConfig object

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import os
from dataclasses import dataclass

# =============================================================================
# Configuration Model
# =============================================================================


@dataclass(frozen=True)
class AppConfig:
    """
    Immutable application configuration.

    Attributes:
        project_name:
            Human-readable application name.

        environment:
            Current runtime environment such as:
                - development
                - testing
                - staging
                - production

        debug:
            Indicates whether debug mode is enabled.
    """

    project_name: str
    environment: str
    debug: bool


# =============================================================================
# Private Helper Functions
# =============================================================================


def _parse_bool(value: str) -> bool:
    """
    Convert a string environment variable into a boolean.

    Accepted true values:

        1
        true
        yes
        on

    Accepted false values:

        0
        false
        no
        off

    Args:
        value:
            Raw string value read from an environment variable.

    Returns:
        Parsed boolean value.

    Raises:
        ValueError:
            If the supplied value cannot be interpreted as a boolean.
    """

    # -------------------------------------------------------------------------
    # Environment variables are always strings.
    #
    # Normalise the value before comparison so the application accepts
    # different capitalisation such as:
    #
    #     TRUE
    #     True
    #     true
    #
    # while still producing the same boolean result.
    # -------------------------------------------------------------------------

    normalized = value.strip().lower()

    if normalized in {"1", "true", "yes", "on"}:
        return True

    if normalized in {"0", "false", "no", "off"}:
        return False

    raise ValueError(
        f"Invalid boolean value: {value!r}. "
        "Expected one of: "
        "1, 0, true, false, yes, no, on, off."
    )


# =============================================================================
# Public Functions
# =============================================================================


def get_app_config() -> AppConfig:
    """
    Load application configuration from environment variables.

    Environment Variables

        NOVYRA_PROJECT_NAME
            Application name.

        NOVYRA_ENVIRONMENT
            Runtime environment.

        NOVYRA_DEBUG
            Enables or disables debug mode.

    Returns:
        Immutable AppConfig instance.
    """

    # -------------------------------------------------------------------------
    # Load the application name.
    #
    # A default value is provided so the application can start even when
    # no environment variables have been configured.
    # -------------------------------------------------------------------------

    project_name = os.getenv(
        "NOVYRA_PROJECT_NAME",
        "NOVYRA OS",
    ).strip()

    # -------------------------------------------------------------------------
    # Load the runtime environment.
    #
    # The value is converted to lowercase so that values such as:
    #
    #     Development
    #     DEVELOPMENT
    #     development
    #
    # are treated identically.
    # -------------------------------------------------------------------------

    environment = os.getenv(
        "NOVYRA_ENVIRONMENT",
        "development",
    ).strip().lower()

    # -------------------------------------------------------------------------
    # Read the debug flag.
    #
    # Environment variables only contain text, therefore the value must be
    # converted into a proper Python boolean.
    # -------------------------------------------------------------------------

    debug_raw = os.getenv(
        "NOVYRA_DEBUG",
        "true",
    )

    debug = _parse_bool(debug_raw)

    # -------------------------------------------------------------------------
    # Return a single immutable configuration object that will be shared
    # across the application.
    # -------------------------------------------------------------------------

    return AppConfig(
        project_name=project_name,
        environment=environment,
        debug=debug,
    )