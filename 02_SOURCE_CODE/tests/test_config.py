import pytest

from app.core.config import AppConfig, get_app_config


def test_default_configuration(monkeypatch):
    """Test the default application configuration."""

    monkeypatch.delenv("NOVYRA_PROJECT_NAME", raising=False)
    monkeypatch.delenv("NOVYRA_ENVIRONMENT", raising=False)
    monkeypatch.delenv("NOVYRA_DEBUG", raising=False)

    config = get_app_config()

    assert isinstance(config, AppConfig)
    assert config.project_name == "NOVYRA OS"
    assert config.environment == "development"
    assert config.debug is True


def test_production_configuration(monkeypatch):
    """Test production environment configuration."""

    monkeypatch.setenv("NOVYRA_PROJECT_NAME", "NOVYRA OS")
    monkeypatch.setenv("NOVYRA_ENVIRONMENT", "production")
    monkeypatch.setenv("NOVYRA_DEBUG", "false")

    config = get_app_config()

    assert config.project_name == "NOVYRA OS"
    assert config.environment == "production"
    assert config.debug is False


@pytest.mark.parametrize(
    "value",
    ["true", "TRUE", "True", "1", "yes", "on"],
)
def test_debug_true_values(monkeypatch, value):
    """Test accepted true values for debug mode."""

    monkeypatch.setenv("NOVYRA_DEBUG", value)

    config = get_app_config()

    assert config.debug is True


@pytest.mark.parametrize(
    "value",
    ["false", "FALSE", "False", "0", "no", "off"],
)
def test_debug_false_values(monkeypatch, value):
    """Test accepted false values for debug mode."""

    monkeypatch.setenv("NOVYRA_DEBUG", value)

    config = get_app_config()

    assert config.debug is False


def test_invalid_debug_value(monkeypatch):
    """Test that invalid debug values raise an error."""

    monkeypatch.setenv("NOVYRA_DEBUG", "invalid-value")

    with pytest.raises(ValueError):
        get_app_config()
