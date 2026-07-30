"""
===============================================================================
NOVYRA OS

Package:
    app.repositories

Purpose:
    Repository package.

Description:
    This package contains repository implementations responsible for
    persisting and retrieving domain models.

    Repositories act as the boundary between the business layer and the
    database layer.

    Current implementations:

        • OpportunityRepository
            In-memory repository used mainly for testing.

        • SQLiteOpportunityRepository
            SQLite-backed persistent repository.

    Because the service layer depends only on repository behaviour rather
    than a specific database, the storage engine can be replaced in the
    future without major changes.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Public Package Exports
# =============================================================================

from app.repositories.opportunity_repository import OpportunityRepository
from app.repositories.sqlite_opportunity_repository import (
    SQLiteOpportunityRepository,
)

# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "OpportunityRepository",
    "SQLiteOpportunityRepository",
]