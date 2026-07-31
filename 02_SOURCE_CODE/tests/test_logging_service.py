"""
===============================================================================
NOVYRA OS

Tests for the logging service.

Phase:
    Phase 4 – Core Platform Services
===============================================================================
"""

import logging

from app.services.logging_service import (
    get_logger,
)


def test_get_logger_returns_logger():
    """
    Verify that a Logger instance is returned.
    """

    logger = get_logger(
        "novyra.test"
    )

    assert isinstance(
        logger,
        logging.Logger,
    )


def test_get_logger_returns_same_instance():
    """
    Verify that requesting the same logger returns the
    same Logger instance.
    """

    first = get_logger(
        "novyra.test"
    )

    second = get_logger(
        "novyra.test"
    )

    assert first is second


def test_logger_name():
    """
    Verify that the logger name is preserved.
    """

    logger = get_logger(
        "novyra.database"
    )

    assert logger.name == "novyra.database"