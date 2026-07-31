"""
Tests for the NOVYRA OS environment service.
"""

from app.services import environment_service


def test_get_environment():
    """
    Verify that the configured environment is returned.
    """

    result = environment_service.get_environment()

    assert result.success is True
    assert result.data in (
        "development",
        "production",
        "testing",
    )


def test_is_development():
    """
    Verify that development mode detection works.
    """

    result = environment_service.is_development()

    assert result.success is True
    assert isinstance(result.data, bool)


def test_python_version():
    """
    Verify that the Python version is available.
    """

    result = environment_service.get_python_version()

    assert result.success is True
    assert isinstance(result.data, str)
    assert "." in result.data


def test_platform_name():
    """
    Verify that the platform name is returned.
    """

    result = environment_service.get_platform_name()

    assert result.success is True
    assert isinstance(result.data, str)
    assert len(result.data) > 0


def test_hostname():
    """
    Verify that the hostname is returned.
    """

    result = environment_service.get_hostname()

    assert result.success is True
    assert isinstance(result.data, str)
    assert len(result.data) > 0


def test_environment_summary():
    """
    Verify that the environment summary contains expected information.
    """

    result = environment_service.get_environment_summary()

    assert result.success is True
    assert result.data is not None

    summary = result.data

    assert "environment" in summary
    assert "debug" in summary
    assert "python_version" in summary
    assert "platform" in summary
    assert "hostname" in summary
    assert "architecture" in summary