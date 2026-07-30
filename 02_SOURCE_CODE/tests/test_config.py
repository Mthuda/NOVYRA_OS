"""
===============================================================================
NOVYRA OS

File:
    test_config.py

Purpose:
    Unit tests for application configuration.

Description:
    Verifies that the application's configuration loader correctly reads
    environment variables and applies sensible defaults.

    These tests validate:

        • Default configuration values
        • Production configuration
        • Accepted boolean values
        • Rejected boolean values

Phase:
    Phase 4
===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import pytest

from app.core.config import (
    AppConfig,
    get_app_config,
)

# =============================================================================
# Default Configuration Tests
# =============================================================================


def test_default_configuration(monkeypatch) -> None:
    """
    Verify that default configuration values are loaded when no
    environment variables are defined.
    """

    # -------------------------------------------------------------------------
    # Remove environment variables to simulate a clean environment.
    # -------------------------------------------------------------------------

    monkeypatch.delenv(
        "NOVYRA_PROJECT_NAME",
        raising=False,
    )
    monkeypatch.delenv(
        "NOVYRA_ENVIRONMENT",
        raising=False,
    )
    monkeypatch.delenv(
        "NOVYRA_DEBUG",
        raising=False,
    )

    config = get_app_config()

    assert isinstance(config, AppConfig)
    assert config.project_name == "NOVYRA OS"
    assert config.environment == "development"
    assert config.debug is True


# =============================================================================
# Production Configuration Tests
# =============================================================================


def test_production_configuration(monkeypatch) -> None:
    """
    Verify that production configuration is loaded from
    environment variables.
    """

    monkeypatch.setenv(
        "NOVYRA_PROJECT_NAME",
        "NOVYRA OS",
    )

    monkeypatch.setenv(
        "NOVYRA_ENVIRONMENT",
        "production",
    )

    monkeypatch.setenv(
        "NOVYRA_DEBUG",
        "false",
    )

    config = get_app_config()

    assert config.project_name == "NOVYRA OS"
    assert config.environment == "production"
    assert config.debug is False


# =============================================================================
# Debug Boolean Parsing Tests
# =============================================================================


@pytest.mark.parametrize(
    "value",
    [
        "true",
        "TRUE",
        "True",
        "1",
        "yes",
        "on",
    ],
)
def test_debug_true_values(
    monkeypatch,
    value,
) -> None:
    """
    Verify that all supported truthy values enable debug mode.
    """

    monkeypatch.setenv(
        "NOVYRA_DEBUG",
        value,
    )

    config = get_app_config()

    assert config.debug is True


@pytest.mark.parametrize(
    "value",
    [
        "false",
        "FALSE",
        "False",
        "0",
        "no",
        "off",
    ],
)
def test_debug_false_values(
    monkeypatch,
    value,
) -> None:
    """
    Verify that all supported falsy values disable debug mode.
    """

    monkeypatch.setenv(
        "NOVYRA_DEBUG",
        value,
    )

    config = get_app_config()

    assert config.debug is False


# =============================================================================
# Validation Tests
# =============================================================================


def test_invalid_debug_value(monkeypatch) -> None:
    """
    Verify that invalid boolean values raise ValueError.

    This protects the application from silently accepting unsupported
    configuration values.
    """

    monkeypatch.setenv(
        "NOVYRA_DEBUG",
        "invalid-value",
    )

    with pytest.raises(ValueError):
        get_app_config()