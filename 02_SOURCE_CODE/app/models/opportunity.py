"""
===============================================================================
NOVYRA OS

File:
    opportunity.py

Purpose:
    Opportunity domain entity.

Description:
    Defines the Opportunity business object used throughout NOVYRA OS.

    An Opportunity represents a discoverable item that may provide value to
    the user, such as:

        • Jobs
        • Scholarships
        • Grants
        • Funding
        • Competitions
        • Tenders
        • Business opportunities

    The model is intentionally independent of database storage and user
    interface concerns.

Phase:
    Phase 4

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from app.models.base import (
    normalize_optional_text,
    require_non_empty,
)

# =============================================================================
# Private Helper Functions
# =============================================================================


def _utc_now() -> datetime:
    """
    Return the current UTC timestamp.

    Using a helper function instead of datetime.now() directly makes the
    default value easier to understand and simplifies future testing.
    """

    return datetime.now(timezone.utc)


# =============================================================================
# Domain Model
# =============================================================================


@dataclass(frozen=True, slots=True)
class Opportunity:
    """
    Represents an Opportunity within NOVYRA OS.

    Attributes:
        id:
            Globally unique identifier.

        title:
            Human-readable title.

        source:
            Origin of the opportunity.

        description:
            Optional detailed description.

        created_at:
            UTC timestamp recording when the Opportunity object was created.

        metadata:
            Flexible key/value data for future expansion without requiring
            schema changes.
    """

    # -------------------------------------------------------------------------
    # Core business fields.
    # -------------------------------------------------------------------------

    id: str
    title: str
    source: str

    # -------------------------------------------------------------------------
    # Optional descriptive information.
    # -------------------------------------------------------------------------

    description: str = ""

    # -------------------------------------------------------------------------
    # Automatically generated timestamp.
    # -------------------------------------------------------------------------

    created_at: datetime = field(
        default_factory=_utc_now,
    )

    # -------------------------------------------------------------------------
    # Flexible extension data.
    # -------------------------------------------------------------------------

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    def __post_init__(self) -> None:
        """
        Validate and normalise values after object creation.

        Because the dataclass is frozen, object.__setattr__() is used to
        update values during initialisation.
        """

        object.__setattr__(
            self,
            "id",
            require_non_empty(
                self.id,
                "Opportunity.id",
            ),
        )

        object.__setattr__(
            self,
            "title",
            require_non_empty(
                self.title,
                "Opportunity.title",
            ),
        )

        object.__setattr__(
            self,
            "source",
            require_non_empty(
                self.source,
                "Opportunity.source",
            ),
        )

        object.__setattr__(
            self,
            "description",
            normalize_optional_text(
                self.description,
            ),
        )