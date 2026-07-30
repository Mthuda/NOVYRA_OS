"""
===============================================================================
NOVYRA OS

File:
    test_opportunity_repository.py

Purpose:
    Unit tests for the in-memory Opportunity repository.

Description:
    This module verifies the behavior of the in-memory repository used
    during early development and testing.

    The repository provides CRUD operations (Create, Read, Update,
    Delete) and serves as the reference implementation for the repository
    interface before persistent storage is introduced.

    These tests ensure that repository behavior remains consistent,
    regardless of whether the underlying implementation is memory,
    SQLite, PostgreSQL, or another future database.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

from app.models.opportunity import Opportunity
from app.repositories.opportunity_repository import OpportunityRepository

# =============================================================================
# Test Helper Functions
# =============================================================================


def create_sample_opportunity(
    opportunity_id: str = "opp-001",
) -> Opportunity:
    """
    Create a reusable Opportunity instance for repository tests.

    Args:
        opportunity_id:
            Identifier assigned to the sample Opportunity.

    Returns:
        A valid Opportunity object.
    """

    return Opportunity(
        id=opportunity_id,
        title="Test Opportunity",
        source="test-source",
        description="Test opportunity description",
    )


# =============================================================================
# Repository Initialization Tests
# =============================================================================


def test_repository_starts_empty() -> None:
    """
    Verify that a newly created repository contains no Opportunities.
    """

    repository = OpportunityRepository()

    assert repository.count() == 0
    assert repository.list_all() == []


# =============================================================================
# Save Operation Tests
# =============================================================================


def test_save_opportunity() -> None:
    """
    Verify that saving an Opportunity stores it in the repository.
    """

    repository = OpportunityRepository()

    opportunity = create_sample_opportunity()

    result = repository.save(opportunity)

    assert result == opportunity
    assert repository.count() == 1


def test_save_replaces_existing_opportunity() -> None:
    """
    Verify that saving an Opportunity with an existing identifier
    replaces the previous entity rather than creating a duplicate.
    """

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


# =============================================================================
# Retrieval Tests
# =============================================================================


def test_get_opportunity_by_id() -> None:
    """
    Verify that an Opportunity can be retrieved by its identifier.
    """

    repository = OpportunityRepository()

    opportunity = create_sample_opportunity()

    repository.save(opportunity)

    result = repository.get_by_id("opp-001")

    assert result == opportunity


def test_get_missing_opportunity_returns_none() -> None:
    """
    Verify that requesting a missing Opportunity returns None.
    """

    repository = OpportunityRepository()

    result = repository.get_by_id("missing-id")

    assert result is None


def test_list_all_opportunities() -> None:
    """
    Verify that all stored Opportunities are returned.
    """

    repository = OpportunityRepository()

    first = create_sample_opportunity("opp-001")
    second = create_sample_opportunity("opp-002")

    repository.save(first)
    repository.save(second)

    result = repository.list_all()

    assert len(result) == 2
    assert first in result
    assert second in result


# =============================================================================
# Delete Operation Tests
# =============================================================================


def test_delete_existing_opportunity() -> None:
    """
    Verify that an existing Opportunity can be deleted.
    """

    repository = OpportunityRepository()

    opportunity = create_sample_opportunity()

    repository.save(opportunity)

    result = repository.delete("opp-001")

    assert result is True
    assert repository.get_by_id("opp-001") is None
    assert repository.count() == 0


def test_delete_missing_opportunity_returns_false() -> None:
    """
    Verify that deleting a non-existent Opportunity returns False.
    """

    repository = OpportunityRepository()

    result = repository.delete("missing-id")

    assert result is False


# =============================================================================
# Existence Tests
# =============================================================================


def test_exists_returns_true_for_existing_opportunity() -> None:
    """
    Verify that exists() returns True for a stored Opportunity.
    """

    repository = OpportunityRepository()

    repository.save(
        create_sample_opportunity(),
    )

    assert repository.exists("opp-001") is True


def test_exists_returns_false_for_missing_opportunity() -> None:
    """
    Verify that exists() returns False when the Opportunity
    is not present in the repository.
    """

    repository = OpportunityRepository()

    assert repository.exists("missing-id") is False