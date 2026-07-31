"""
===============================================================================
NOVYRA OS

File:
    logging_setup.py

Purpose:
    Configure the NOVYRA OS logging system.

Description:
    This module initializes the application's logging infrastructure.

    Logging is configured only once during application startup and provides:

        • Console logging
        • File logging
        • Consistent log formatting
        • Automatic log directory creation

    Every logger obtained through the logging service inherits this
    configuration automatically.

    Future enhancements may include:

        • Log rotation
        • JSON structured logging
        • Remote logging
        • Audit logging
        • Security logging

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import logging
from pathlib import Path

# =============================================================================
# Constants
# =============================================================================

LOG_DIRECTORY = Path("logs")
LOG_FILE = LOG_DIRECTORY / "novyra.log"

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

# =============================================================================
# Logging Setup
# =============================================================================


def setup_logging() -> None:
    """
    Configure the NOVYRA logging system.

    Calling this function multiple times is safe. Logging will only be
    configured once.
    """

    if logging.getLogger().handlers:
        return

    LOG_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    formatter = logging.Formatter(
        LOG_FORMAT,
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        formatter,
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setFormatter(
        formatter,
    )

    root_logger = logging.getLogger()

    root_logger.setLevel(
        logging.INFO,
    )

    root_logger.addHandler(
        console_handler,
    )

    root_logger.addHandler(
        file_handler,
    )

    root_logger.info(
        "Logging system initialized."
    )