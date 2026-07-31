"""
===============================================================================
Tests for config_service.py
===============================================================================
"""

from app.core.config import AppConfig
from app.services import config_service


def test_get_configuration():
    """
    Verify that the configuration service returns an AppConfig instance.
    """

    result = config_service.get_configuration()

    assert result.success is True
    assert result.error_code is None
    assert isinstance(result.data, AppConfig)


def test_get_configuration_contains_expected_fields():
    """
    Verify expected configuration values are available.
    """

    result = config_service.get_configuration()

    assert result.success is True

    config = result.data

    assert config is not None

    assert config.project_name == "NOVYRA OS"
    assert config.environment in (
        "development",
        "production",
    )

    assert isinstance(config.debug, bool)


def test_get_configuration_information():
    """
    Verify configuration information returned by the service.
    """

    result = config_service.get_configuration_information()

    assert result.success is True

    information = result.data

    assert information is not None

    assert information["project_name"] == "NOVYRA OS"

    assert "environment" in information
    assert "debug" in information