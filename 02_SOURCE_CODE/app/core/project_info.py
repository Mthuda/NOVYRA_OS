"""
===============================================================================
NOVYRA OS

File:
    project_info.py

Purpose:
    Centralised project metadata.

Description:
    This module contains application-wide constants that describe the current
    NOVYRA OS build.

    These values are intentionally centralised so that every part of the
    application reports the same project information.

    Typical consumers include:

        • Startup banner
        • Logging
        • System services
        • Documentation
        • Future REST API
        • Mobile application
        • Desktop application
        • Web dashboard

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Project Identity
# =============================================================================

# Human-readable application name.
PROJECT_NAME = "NOVYRA OS"

# Current semantic version.
PROJECT_VERSION = "0.2.0"

# =============================================================================
# Development Stage
# =============================================================================

# Current implementation milestone.
#
# This value is displayed by the application startup screen and may also
# appear in logs, diagnostics, and future user interfaces.
PROJECT_STAGE = "Phase 3 - Persistence Foundation"