"""
Logging configuration for NOVYRA OS.
"""

import logging


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure application logging.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )