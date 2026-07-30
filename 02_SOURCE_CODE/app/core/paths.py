"""
===============================================================================
NOVYRA OS

File:
    paths.py

Purpose:
    Project path utilities.

Description:
    Provides helper functions for locating important directories within the
    NOVYRA OS project.

    Centralising path calculations ensures every module uses the same logic
    when locating project resources such as:

        - database files
        - documentation
        - configuration files
        - backups
        - assets

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

from pathlib import Path

# =============================================================================
# Public Functions
# =============================================================================


def get_project_root() -> Path:
    """
    Return the absolute path to the NOVYRA OS project root.

    Returns:
        Absolute Path object representing the project root directory.
    """

    # -------------------------------------------------------------------------
    # File structure
    #
    #     app/
    #         core/
    #             paths.py
    #
    # We therefore move three directory levels upward:
    #
    #     paths.py
    #         ↑
    #     core
    #         ↑
    #     app
    #         ↑
    #     02_SOURCE_CODE
    #         ↑
    #     NOVYRA_OS   <-- project root
    # -------------------------------------------------------------------------

    project_root = Path(__file__).resolve().parents[3]

    return project_root