"""
===============================================================================
NOVYRA OS

File:
    logging_setup.py

Purpose:
    Central logging configuration.

Description:
    Provides a single location responsible for configuring the application's
    logging behaviour.

    Every component in NOVYRA—including services, repositories, database
    infrastructure, REST APIs, desktop applications, and the future Kivy
    mobile application—will use Python's built-in logging framework.

    Centralising logging ensures the entire application follows the same
    formatting and log level configuration.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Imports
# =============================================================================

import logging

# =============================================================================
# Public Functions
# =============================================================================


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure the application's logging system.

    This function should be called once during application startup before
    any other modules begin writing log messages.

    Args:
        level:
            Minimum logging level.

            Common values include:

                logging.DEBUG
                logging.INFO
                logging.WARNING
                logging.ERROR
                logging.CRITICAL
    """

    # -------------------------------------------------------------------------
    # Configure the root logger.
    #
    # Every logger created throughout NOVYRA inherits this configuration unless
    # explicitly overridden.
    #
    # The selected format includes:
    #
    #   • Timestamp
    #   • Log level
    #   • Logger name
    #   • Log message
    #
    # Example:
    #
    #   2026-08-04 10:15:22 | INFO | app.services | Database initialised
    # -------------------------------------------------------------------------

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )