"""
Project path utilities for NOVYRA OS.
"""

from pathlib import Path


def get_project_root() -> Path:
    """
    Return the root folder of the NOVYRA OS project.
    """
    return Path(__file__).resolve().parents[3]