"""
===============================================================================
NOVYRA OS

Package:
    app.services

Purpose:
    Business service layer.

Description:
    This package contains the application's business services.

    Services coordinate work between:

        • Domain models
        • Repositories
        • Configuration
        • Infrastructure

    Services should contain business logic but should not contain
    user interface code or direct database implementation details.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Public Package Exports
# =============================================================================

from app.services.opportunity_service import create_opportunity
from app.services.system_service import get_system_summary

# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "create_opportunity",
    "get_system_summary",
]