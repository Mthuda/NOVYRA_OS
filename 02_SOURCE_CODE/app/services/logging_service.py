"""
===============================================================================
NOVYRA OS

File:
    logging_service.py

Purpose:
    Centralized logging service.

Description:
    Provides a consistent interface for obtaining application loggers.

    Rather than importing Python's logging module throughout the project,
    application components should request a logger from this service.

    Benefits include:

        • Centralized logging
        • Consistent logger naming
        • Easier future enhancements
        • Reduced coupling to the logging framework

    Future enhancements may include:

        • File logging
        • Log rotation
        • Structured JSON logging
        • Audit logging
        • Remote logging
        • Log filtering

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import logging

# =============================================================================
# Logger Factory
# =============================================================================


def get_logger(
    name: str,
) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name:
            Name of the requesting module.

    Returns:
        Configured Logger instance.
    """

    return logging.getLogger(name)