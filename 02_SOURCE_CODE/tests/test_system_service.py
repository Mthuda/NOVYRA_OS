"""
Tests for the NOVYRA OS system service.
"""

from app.core.config import AppConfig
from app.services.system_service import get_system_summary


def test_system_summary():
    """Test that the system summary contains expected information."""

    config = AppConfig(
        project_name="NOVYRA OS",
        environment="development",
        debug=True,
    )

    summary = get_system_summary(config)

    assert summary["project_name"] == "NOVYRA OS"
    assert summary["version"] == "0.2.0"
    assert summary["stage"] == "Phase 2 - Core Application Skeleton"
    assert summary["environment"] == "development"
    assert summary["debug"] is True
    assert "project_root" in summary