"""
===============================================================================
NOVYRA OS

File:
    test_opportunity.py

Purpose:
    Unit tests for the Opportunity domain model.

Description:
    Verifies that the Opportunity model correctly validates required
    business fields, initializes default values, and creates immutable
    domain objects that represent opportunities within NOVYRA OS.

    These tests form the foundation for all future opportunity-related
    features including AI discovery, ranking, synchronization, and
    presentation in the mobile, web, and desktop applications.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import pytest

from app.models.opportunity import Opportunity

# =============================================================================
# Opportunity Creation Tests
# =============================================================================


def test_opportunity_creation() -> None:
    """
    Verify that a valid Opportunity is created successfully.

    The model should preserve all supplied values while automatically
    creating sensible defaults for optional fields.
    """

    # Arrange / Act
    opportunity = Opportunity(
        id="opp-001",
        title="Grant opportunity",
        source="web",
        description="A useful funding opportunity",
    )

    # Assert
    assert opportunity.id == "opp-001"
    assert opportunity.title == "Grant opportunity"
    assert opportunity.source == "web"
    assert opportunity.description == "A useful funding opportunity"

    # Default values
    assert opportunity.metadata == {}

    # Timestamp should always be timezone-aware (UTC)
    assert opportunity.created_at.tzinfo is not None


# =============================================================================
# Validation Tests
# =============================================================================


def test_opportunity_rejects_empty_id() -> None:
    """
    Verify that an Opportunity cannot be created with an empty ID.

    Every Opportunity must have a unique identifier.
    """

    with pytest.raises(ValueError):
        Opportunity(
            id=" ",
            title="Title",
            source="web",
        )


def test_opportunity_rejects_empty_title() -> None:
    """
    Verify that an Opportunity cannot be created with an empty title.

    The title is required because it is the primary human-readable
    identifier shown throughout the application.
    """

    with pytest.raises(ValueError):
        Opportunity(
            id="opp-001",
            title=" ",
            source="web",
        )


def test_opportunity_rejects_empty_source() -> None:
    """
    Verify that an Opportunity cannot be created without a source.

    Tracking where opportunities originate is essential for auditing,
    ranking, and future synchronization.
    """

    with pytest.raises(ValueError):
        Opportunity(
            id="opp-001",
            title="Title",
            source=" ",
        )