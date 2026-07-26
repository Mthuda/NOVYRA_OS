"""
In-memory repository for Opportunity domain entities.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from app.models.opportunity import Opportunity


class OpportunityRepository:
    """
    Repository for storing and retrieving Opportunity entities.

    This implementation uses an in-memory dictionary as temporary storage.
    It provides a persistence abstraction that can later be replaced by
    SQLite, PostgreSQL, or another database implementation without requiring
    major changes to the service layer.
    """

    def __init__(self) -> None:
        """Initialize an empty in-memory repository."""
        self._opportunities: Dict[str, Opportunity] = {}

    def save(self, opportunity: Opportunity) -> Opportunity:
        """
        Save or replace an Opportunity.

        Args:
            opportunity: Opportunity entity to store.

        Returns:
            The saved Opportunity.
        """
        self._opportunities[opportunity.id] = opportunity
        return opportunity

    def get_by_id(self, opportunity_id: str) -> Optional[Opportunity]:
        """
        Retrieve an Opportunity by ID.

        Args:
            opportunity_id: Unique Opportunity identifier.

        Returns:
            The matching Opportunity, or None if not found.
        """
        return self._opportunities.get(opportunity_id)

    def list_all(self) -> List[Opportunity]:
        """
        Return all stored Opportunities.

        Returns:
            A list containing all stored Opportunity entities.
        """
        return list(self._opportunities.values())

    def delete(self, opportunity_id: str) -> bool:
        """
        Delete an Opportunity by ID.

        Args:
            opportunity_id: Unique Opportunity identifier.

        Returns:
            True if the Opportunity was deleted, otherwise False.
        """
        if opportunity_id not in self._opportunities:
            return False

        del self._opportunities[opportunity_id]
        return True

    def exists(self, opportunity_id: str) -> bool:
        """
        Check whether an Opportunity exists.

        Args:
            opportunity_id: Unique Opportunity identifier.

        Returns:
            True if the Opportunity exists, otherwise False.
        """
        return opportunity_id in self._opportunities

    def count(self) -> int:
        """
        Return the number of stored Opportunities.

        Returns:
            Number of Opportunities currently stored.
        """
        return len(self._opportunities)