"""
Tests for the Opportunity repository.
"""

from app.models.opportunity import Opportunity
from app.repositories.opportunity_repository import OpportunityRepository


def create_sample_opportunity(
    opportunity_id: str = "opp-001",
) -> Opportunity:
    """Create a sample Opportunity for repository tests."""
    return Opportunity(
        id=opportunity_id,
        title="Test Opportunity",
        source="test-source",
        description="Test opportunity description",
    )


def test_repository_starts_empty():
    """Test that a new repository contains no Opportunities."""
    repository = OpportunityRepository()

    assert repository.count() == 0
    assert repository.list_all() == []


def test_save_opportunity():
    """Test saving an Opportunity."""
    repository = OpportunityRepository()
    opportunity = create_sample_opportunity()

    result = repository.save(opportunity)

    assert result == opportunity
    assert repository.count() == 1


def test_get_opportunity_by_id():
    """Test retrieving an Opportunity by ID."""
    repository = OpportunityRepository()
    opportunity = create_sample_opportunity()

    repository.save(opportunity)

    result = repository.get_by_id("opp-001")

    assert result == opportunity


def test_get_missing_opportunity_returns_none():
    """Test retrieving a missing Opportunity."""
    repository = OpportunityRepository()

    result = repository.get_by_id("missing-id")

    assert result is None


def test_list_all_opportunities():
    """Test retrieving all stored Opportunities."""
    repository = OpportunityRepository()

    first = create_sample_opportunity("opp-001")
    second = create_sample_opportunity("opp-002")

    repository.save(first)
    repository.save(second)

    result = repository.list_all()

    assert len(result) == 2
    assert first in result
    assert second in result


def test_save_replaces_existing_opportunity():
    """Test that saving the same ID replaces the existing entity."""
    repository = OpportunityRepository()

    original = create_sample_opportunity("opp-001")
    updated = Opportunity(
        id="opp-001",
        title="Updated Opportunity",
        source="updated-source",
    )

    repository.save(original)
    repository.save(updated)

    result = repository.get_by_id("opp-001")

    assert result == updated
    assert repository.count() == 1


def test_delete_existing_opportunity():
    """Test deleting an existing Opportunity."""
    repository = OpportunityRepository()
    opportunity = create_sample_opportunity()

    repository.save(opportunity)

    result = repository.delete("opp-001")

    assert result is True
    assert repository.get_by_id("opp-001") is None
    assert repository.count() == 0


def test_delete_missing_opportunity_returns_false():
    """Test deleting an Opportunity that does not exist."""
    repository = OpportunityRepository()

    result = repository.delete("missing-id")

    assert result is False


def test_exists_returns_true_for_existing_opportunity():
    """Test existence check for an existing Opportunity."""
    repository = OpportunityRepository()
    opportunity = create_sample_opportunity()

    repository.save(opportunity)

    assert repository.exists("opp-001") is True


def test_exists_returns_false_for_missing_opportunity():
    """Test existence check for a missing Opportunity."""
    repository = OpportunityRepository()

    assert repository.exists("missing-id") is False