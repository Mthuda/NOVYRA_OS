"""
===============================================================================
NOVYRA OS

Tests for the File Service.

Verifies filesystem operations including:

    • Directory creation
    • File creation
    • File reading
    • File writing
    • File deletion
    • File copying
    • File moving
    • File information retrieval

===============================================================================
"""

from pathlib import Path
from typing import cast

import pytest

from app.services import file_service


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def temporary_directory(
    tmp_path: Path,
) -> Path:
    """
    Provide a temporary working directory.
    """

    return tmp_path


# =============================================================================
# Directory Tests
# =============================================================================


def test_create_directory(
    temporary_directory: Path,
) -> None:
    """
    Verify that directories can be created.
    """

    directory = temporary_directory / "example"

    result = file_service.create_directory(directory)

    assert result.success is True
    assert result.data == directory
    assert directory.exists()
    assert directory.is_dir()


def test_directory_exists(
    temporary_directory: Path,
) -> None:
    """
    Verify directory existence detection.
    """

    directory = temporary_directory / "existing"

    directory.mkdir()

    result = file_service.directory_exists(directory)

    assert result.success is True
    assert result.data is True


def test_directory_does_not_exist(
    temporary_directory: Path,
) -> None:
    """
    Verify missing directory detection.
    """

    directory = temporary_directory / "missing"

    result = file_service.directory_exists(directory)

    assert result.success is True
    assert result.data is False

# =============================================================================
# File Tests
# =============================================================================


def test_file_exists(
    temporary_directory: Path,
) -> None:
    """
    Verify file existence detection.
    """

    file_path = temporary_directory / "example.txt"

    file_path.write_text(
        "NOVYRA",
        encoding="utf-8",
    )

    result = file_service.file_exists(file_path)

    assert result.success is True
    assert result.data is True


def test_write_text(
    temporary_directory: Path,
) -> None:
    """
    Verify writing a text file.
    """

    file_path = temporary_directory / "write.txt"

    result = file_service.write_text(
        file_path,
        "Hello NOVYRA",
    )

    assert result.success is True
    assert result.data == file_path
    assert file_path.exists()
    assert file_path.read_text(
        encoding="utf-8",
    ) == "Hello NOVYRA"


def test_read_text(
    temporary_directory: Path,
) -> None:
    """
    Verify reading a text file.
    """

    file_path = temporary_directory / "read.txt"

    file_path.write_text(
        "Read Successful",
        encoding="utf-8",
    )

    result = file_service.read_text(file_path)

    assert result.success is True
    assert result.data == "Read Successful"


def test_delete_file(
    temporary_directory: Path,
) -> None:
    """
    Verify deleting a file.
    """

    file_path = temporary_directory / "delete.txt"

    file_path.write_text(
        "Temporary",
        encoding="utf-8",
    )

    result = file_service.delete_file(file_path)

    assert result.success is True
    assert not file_path.exists()

# =============================================================================
# Copy / Move Tests
# =============================================================================


def test_copy_file(
    temporary_directory: Path,
) -> None:
    """
    Verify copying a file.
    """

    source = temporary_directory / "source.txt"
    destination = temporary_directory / "copy.txt"

    source.write_text(
        "NOVYRA",
        encoding="utf-8",
    )

    result = file_service.copy_file(
        source,
        destination,
    )

    assert result.success is True
    assert result.data == destination
    assert destination.exists()
    assert destination.read_text(
        encoding="utf-8",
    ) == "NOVYRA"


def test_move_file(
    temporary_directory: Path,
) -> None:
    """
    Verify moving a file.
    """

    source = temporary_directory / "move.txt"
    destination = temporary_directory / "moved.txt"

    source.write_text(
        "Move Me",
        encoding="utf-8",
    )

    result = file_service.move_file(
        source,
        destination,
    )

    assert result.success is True
    assert result.data == destination
    assert destination.exists()
    assert not source.exists()


# =============================================================================
# File Information Tests
# =============================================================================


def test_get_file_information(
    temporary_directory: Path,
) -> None:
    """
    Verify retrieving file metadata.
    """

    file_path = temporary_directory / "information.txt"

    file_path.write_text(
        "NOVYRA OS",
        encoding="utf-8",
    )

    result = file_service.get_file_information(
        file_path,
    )

    assert result.success is True
    assert result.data is not None

    information = result.data

    name = str(information["name"])
    suffix = str(information["suffix"])
    absolute_path = str(information["absolute_path"])
    parent = str(information["parent"])

    exists = bool(information["exists"])
    is_file = bool(information["is_file"])
    is_directory = bool(information["is_directory"])
    size = cast(int, information["size"])

    assert name == "information.txt"
    assert suffix == ".txt"

    assert exists is True
    assert is_file is True
    assert is_directory is False

    assert size > 0

    assert Path(absolute_path) == file_path.resolve()

    assert Path(parent) == file_path.parent.resolve()

def test_get_missing_file_information(
    temporary_directory: Path,
) -> None:
    """
    Verify requesting information for a missing file.
    """

    missing_file = temporary_directory / "missing.txt"

    result = file_service.get_file_information(
        missing_file,
    )

    assert result.success is False
    assert result.error_code == "FILE_NOT_FOUND"