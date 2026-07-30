"""
===============================================================================
NOVYRA OS

Package:
    app.models

Purpose:
    Domain model package.

Description:
    This package contains the business entities (domain models) used
    throughout NOVYRA OS.

    Domain models represent real-world objects that exist independently of
    the database, user interface, or external services.

    Current models include:

        • Opportunity

    Shared validation helpers are also provided for reuse across future
    domain models.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Public Package Exports
# =============================================================================

from app.models.base import (
    normalize_optional_text,
    require_non_empty,
)
from app.models.opportunity import Opportunity

# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "Opportunity",
    "normalize_optional_text",
    "require_non_empty",
]