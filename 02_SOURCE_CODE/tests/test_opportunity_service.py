"""
Tests for the NOVYRA OS opportunity service.
"""

from app.core.service_result import ServiceResult
from app.models.opportunity import Opportunity
from app.services.opportunity_service import create_opportunity


def test_create_opportunity_success():
    result = create_opportunity(
        opportunity_id="opp-001",
        title="Grant opportunity",
        source="web",
        description="A useful funding opportunity",
        metadata={"category": "funding"},
    )

    assert isinstance(result, ServiceResult)
    assert result.success is True
    assert result.error_code is None
    assert isinstance(result.data, Opportunity)
    assert result.data.id == "opp-001"
    assert result.data.title == "Grant opportunity"


def test_create_opportunity_validation_failure():
    result = create_opportunity(
        opportunity_id=" ",
        title="Grant opportunity",
        source="web",
    )

    assert result.success is False
    assert result.data is None
    assert result.error_code == "OPPORTUNITY_VALIDATION_ERROR"
    assert "cannot be empty" in result.message