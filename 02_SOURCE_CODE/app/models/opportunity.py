"""
Opportunity domain model for NOVYRA OS.

This module defines the first core business entity used by the platform
to represent a discoverable and actionable opportunity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from app.models.base import normalize_optional_text, require_non_empty


def _utc_now() -> datetime:
    """Return the current UTC timestamp."""
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Opportunity:
    """
    Represents a candidate opportunity inside NOVYRA OS.
    """

    id: str
    title: str
    source: str
    description: str = ""
    created_at: datetime = field(default_factory=_utc_now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "id", require_non_empty(self.id, "Opportunity.id"))
        object.__setattr__(self, "title", require_non_empty(self.title, "Opportunity.title"))
        object.__setattr__(self, "source", require_non_empty(self.source, "Opportunity.source"))
        object.__setattr__(self, "description", normalize_optional_text(self.description))