"""
Repository implementations for NOVYRA OS.
"""

from app.repositories.opportunity_repository import (
    OpportunityRepository,
)
from app.repositories.sqlite_opportunity_repository import (
    SQLiteOpportunityRepository,
)

__all__ = [
    "OpportunityRepository",
    "SQLiteOpportunityRepository",
]