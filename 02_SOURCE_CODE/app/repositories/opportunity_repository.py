"""
===============================================================================
NOVYRA OS

File:
    opportunity_repository.py

Purpose:
    In-memory Opportunity repository.

Description:
    This repository stores Opportunity objects entirely in memory using
    a Python dictionary.

    It is primarily intended for:

        • Unit testing
        • Fast development
        • Service-layer testing
        • Demonstrating the Repository Pattern

    Since the service layer communicates only with repository methods,
    this implementation can be replaced by a database-backed repository
    without modifying business logic.

Phase:
    Phase 4

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from typing import Dict, List, Optional

from app.models.opportunity import Opportunity


# =============================================================================
# Repository
# =============================================================================


class OpportunityRepository:
    """
    In-memory repository for Opportunity entities.
    """

    def __init__(self) -> None:
        """
        Create an empty repository.

        Internal storage uses a dictionary where the Opportunity ID is
        the lookup key.
        """

        self._opportunities: Dict[str, Opportunity] = {}

    def save(self, opportunity: Opportunity) -> Opportunity:
        """
        Save or replace an Opportunity.

        If another Opportunity already exists with the same ID it is
        replaced.
        """

        self._opportunities[opportunity.id] = opportunity
        return opportunity

    def get_by_id(
        self,
        opportunity_id: str,
    ) -> Optional[Opportunity]:
        """
        Retrieve an Opportunity by its unique identifier.
        """

        return self._opportunities.get(opportunity_id)

    def list_all(self) -> List[Opportunity]:
        """
        Return every stored Opportunity.

        The returned list preserves insertion order because Python
        dictionaries preserve insertion order.
        """

        return list(self._opportunities.values())

    def delete(
        self,
        opportunity_id: str,
    ) -> bool:
        """
        Delete an Opportunity.

        Returns:
            True if an Opportunity was removed.
            False otherwise.
        """

        if opportunity_id not in self._opportunities:
            return False

        del self._opportunities[opportunity_id]

        return True

    def exists(
        self,
        opportunity_id: str,
    ) -> bool:
        """
        Determine whether an Opportunity exists.
        """

        return opportunity_id in self._opportunities

    def count(self) -> int:
        """
        Return the total number of stored Opportunities.
        """

        return len(self._opportunities)