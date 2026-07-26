"""
Tests for the Opportunity domain model.
"""

from datetime import datetime, timezone

import pytest

from app.models.opportunity import Opportunity


def test_opportunity_creation():
    opportunity = Opportunity(
        id="opp-001",
        title="Grant opportunity",
        source="web",
        description="A useful funding opportunity",
    )

    assert opportunity.id == "opp-001"
    assert opportunity.title == "Grant opportunity"
    assert opportunity.source == "web"
    assert opportunity.description == "A useful funding opportunity"
    assert opportunity.metadata == {}
    assert opportunity.created_at.tzinfo is not None


def test_opportunity_rejects_empty_id():
    with pytest.raises(ValueError):
        Opportunity(id=" ", title="Title", source="web")


def test_opportunity_rejects_empty_title():
    with pytest.raises(ValueError):
        Opportunity(id="opp-001", title=" ", source="web")


def test_opportunity_rejects_empty_source():
    with pytest.raises(ValueError):
        Opportunity(id="opp-001", title="Title", source=" ")