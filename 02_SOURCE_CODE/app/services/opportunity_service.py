"""
Opportunity service for NOVYRA OS.

This module creates and validates Opportunity domain objects and returns
standardized service results.
"""

from __future__ import annotations

from typing import Any

from app.core.service_result import ServiceResult
from app.models.opportunity import Opportunity


def create_opportunity(
    opportunity_id: str,
    title: str,
    source: str,
    description: str = "",
    metadata: dict[str, Any] | None = None,
) -> ServiceResult[Opportunity]:
    """
    Create an Opportunity domain object.

    Args:
        opportunity_id: Stable opportunity identifier.
        title: Human-readable title.
        source: Origin of the opportunity.
        description: Optional detailed description.
        metadata: Optional structured metadata.

    Returns:
        A ServiceResult containing the Opportunity on success.
    """
    try:
        opportunity = Opportunity(
            id=opportunity_id,
            title=title,
            source=source,
            description=description,
            metadata=metadata or {},
        )
        return ServiceResult.ok(
            data=opportunity,
            message="Opportunity created successfully.",
        )
    except ValueError as exc:
        return ServiceResult.fail(
            message=str(exc),
            error_code="OPPORTUNITY_VALIDATION_ERROR",
        )