"""
===============================================================================
NOVYRA OS

File:
    database_info.py

Purpose:
    Database information model.

Description:
    Defines a strongly-typed model representing information about the active
    NOVYRA OS database.

    Returning this model instead of a generic dictionary improves:

        • Type safety
        • IDE autocompletion
        • Static analysis
        • Refactoring support
        • Code readability

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

from dataclasses import dataclass

# =============================================================================
# Database Information Model
# =============================================================================


@dataclass(frozen=True, slots=True)
class DatabaseInfo:
    """
    Represents information about the configured database.
    """

    database_path: str
    database_exists: bool
    database_name: str
    database_directory: str