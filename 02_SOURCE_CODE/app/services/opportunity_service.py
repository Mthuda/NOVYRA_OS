"""
Opportunity service for NOVYRA OS.

This module provides application-level operations for creating, retrieving,
listing, and deleting Opportunity domain objects.

The service layer coordinates domain models with the repository layer and
returns standardized ServiceResult objects.
"""

from __future__ import annotations

from typing import Any

from app.core.service_result import ServiceResult
from app.models.opportunity import Opportunity
from app.repositories.opportunity_repository import OpportunityRepository


def create_opportunity(
    opportunity_id: str,
    title: str,
    source: str,
    description: str = "",
    metadata: dict[str, Any] | None = None,
    repository: OpportunityRepository | None = None,
) -> ServiceResult[Opportunity]:
    """
    Create and persist an Opportunity domain object.

    Args:
        opportunity_id: Stable opportunity identifier.
        title: Human-readable title.
        source: Origin of the opportunity.
        description: Optional detailed description.
        metadata: Optional structured metadata.
        repository: Optional repository instance used for persistence.

    Returns:
        A ServiceResult containing the Opportunity on success.
    """
    active_repository = repository or OpportunityRepository()

    try:
        opportunity = Opportunity(
            id=opportunity_id,
            title=title,
            source=source,
            description=description,
            metadata=metadata or {},
        )

        active_repository.save(opportunity)

        return ServiceResult.ok(
            data=opportunity,
            message="Opportunity created successfully.",
        )

    except ValueError as exc:
        return ServiceResult.fail(
            message=str(exc),
            error_code="OPPORTUNITY_VALIDATION_ERROR",
        )


def get_opportunity(
    opportunity_id: str,
    repository: OpportunityRepository,
) -> ServiceResult[Opportunity]:
    """
    Retrieve an Opportunity by its identifier.

    Args:
        opportunity_id: Identifier of the opportunity to retrieve.
        repository: Repository containing stored opportunities.

    Returns:
        A successful ServiceResult containing the Opportunity if found,
        otherwise a failure result.
    """
    opportunity = repository.get_by_id(opportunity_id)

    if opportunity is None:
        return ServiceResult.fail(
            message=f"Opportunity '{opportunity_id}' was not found.",
            error_code="OPPORTUNITY_NOT_FOUND",
        )

    return ServiceResult.ok(
        data=opportunity,
        message="Opportunity retrieved successfully.",
    )


def list_opportunities(
    repository: OpportunityRepository,
) -> ServiceResult[list[Opportunity]]:
    """
    Retrieve all stored opportunities.

    Args:
        repository: Repository containing stored opportunities.

    Returns:
        A successful ServiceResult containing all stored opportunities.
    """
    opportunities = repository.list_all()

    return ServiceResult.ok(
        data=opportunities,
        message="Opportunities retrieved successfully.",
    )


def delete_opportunity(
    opportunity_id: str,
    repository: OpportunityRepository,
) -> ServiceResult[None]:
    """
    Delete an Opportunity by its identifier.

    Args:
        opportunity_id: Identifier of the opportunity to delete.
        repository: Repository containing stored opportunities.

    Returns:
        A successful ServiceResult if the opportunity was deleted,
        otherwise a failure result.
    """
    deleted = repository.delete(opportunity_id)

    if not deleted:
        return ServiceResult.fail(
            message=f"Opportunity '{opportunity_id}' was not found.",
            error_code="OPPORTUNITY_NOT_FOUND",
        )

    return ServiceResult.ok(
        message="Opportunity deleted successfully.",
    )