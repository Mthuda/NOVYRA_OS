"""
===============================================================================
NOVYRA OS

File:
    test_smoke.py

Purpose:
    Smoke test.

Description:
    This module contains the most basic test in the NOVYRA OS test suite.

    A smoke test verifies that:

        • pytest is installed correctly.
        • The test discovery mechanism is working.
        • The testing environment is configured correctly.

    This test does not verify application functionality. Instead, it
    confirms that the testing infrastructure itself is operational.

Phase:
    Phase 4

===============================================================================
"""

# =============================================================================
# Smoke Tests
# =============================================================================


def test_smoke() -> None:
    """
    Verify that the testing framework is functioning.

    This test should always pass. If it fails, the problem is with the
    testing environment rather than the NOVYRA OS application.
    """

    # -------------------------------------------------------------------------
    # A successful assertion confirms that pytest can discover and execute
    # test cases correctly.
    # -------------------------------------------------------------------------

    assert True