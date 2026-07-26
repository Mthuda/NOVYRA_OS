"""
Tests for the NOVYRA OS system service.
"""

from app.core.config import AppConfig
from app.core.service_result import ServiceResult
from app.services.system_service import get_system_summary


def test_system_summary():
    """Test successful system summary generation."""

    config = AppConfig(
        project_name="NOVYRA OS",
        environment="development",
        debug=True,
    )

    result = get_system_summary(config)

    assert isinstance(result, ServiceResult)
    assert result.success is True
    assert result.message == "System summary generated successfully."
    assert result.error_code is None
    assert result.data is not None

    assert result.data["project_name"] == "NOVYRA OS"
    assert result.data["version"] == "0.2.0"
    assert result.data["stage"] == "Phase 2 - Core Application Skeleton"
    assert result.data["environment"] == "development"
    assert result.data["debug"] is True


def test_system_summary_contains_project_root():
    """Test that the system summary contains the project root."""

    config = AppConfig(
        project_name="NOVYRA OS",
        environment="development",
        debug=True,
    )

    result = get_system_summary(config)

    assert result.success is True
    assert result.data is not None
    assert "project_root" in result.data
    assert result.data["project_root"]