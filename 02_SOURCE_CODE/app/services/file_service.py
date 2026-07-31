"""
===============================================================================
NOVYRA OS

File:
    file_service.py

Purpose:
    Centralized filesystem service.

Description:
    Provides the official interface for filesystem operations throughout
    NOVYRA OS.

    Application components should never manipulate files directly using
    pathlib or shutil. All filesystem interaction should go through this
    service.

Phase:
    Phase 4 – Core Platform Services

===============================================================================
"""

from __future__ import annotations

# =============================================================================
# Imports
# =============================================================================

import shutil
from pathlib import Path

from app.core.service_result import ServiceResult
from app.services.logging_service import get_logger

# =============================================================================
# Logger
# =============================================================================

logger = get_logger(__name__)

# =============================================================================
# Directory Operations
# =============================================================================


def create_directory(
    path: str | Path,
) -> ServiceResult[Path]:
    """
    Create a directory.

    Parent directories are created automatically.

    Args:
        path:
            Directory path.

    Returns:
        ServiceResult containing the created directory.
    """

    try:
        directory = Path(path)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info(
            "Created directory: %s",
            directory,
        )

        return ServiceResult.ok(
            data=directory,
            message="Directory created successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to create directory."
        )

        return ServiceResult.fail(
            message="Unable to create directory.",
            error_code="DIRECTORY_CREATE_ERROR",
        )


def directory_exists(
    path: str | Path,
) -> ServiceResult[bool]:
    """
    Determine whether a directory exists.
    """

    directory = Path(path)

    return ServiceResult.ok(
        data=directory.is_dir(),
        message="Directory existence checked.",
    )


# =============================================================================
# File Existence
# =============================================================================


def file_exists(
    path: str | Path,
) -> ServiceResult[bool]:
    """
    Determine whether a file exists.
    """

    file_path = Path(path)

    return ServiceResult.ok(
        data=file_path.is_file(),
        message="File existence checked.",
    )

# =============================================================================
# Text File Operations
# =============================================================================


def read_text(
    path: str | Path,
    encoding: str = "utf-8",
) -> ServiceResult[str]:
    """
    Read a text file.

    Args:
        path:
            File to read.

        encoding:
            File encoding.

    Returns:
        ServiceResult containing the file contents.
    """

    try:
        file_path = Path(path)

        content = file_path.read_text(
            encoding=encoding,
        )

        logger.info(
            "Read file: %s",
            file_path,
        )

        return ServiceResult.ok(
            data=content,
            message="File read successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to read file."
        )

        return ServiceResult.fail(
            message="Unable to read file.",
            error_code="FILE_READ_ERROR",
        )


def write_text(
    path: str | Path,
    content: str,
    encoding: str = "utf-8",
) -> ServiceResult[Path]:
    """
    Write text to a file.

    Missing parent directories are created automatically.

    Args:
        path:
            Destination file.

        content:
            Text to write.

        encoding:
            File encoding.

    Returns:
        ServiceResult containing the written file.
    """

    try:
        file_path = Path(path)

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path.write_text(
            content,
            encoding=encoding,
        )

        logger.info(
            "Wrote file: %s",
            file_path,
        )

        return ServiceResult.ok(
            data=file_path,
            message="File written successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to write file."
        )

        return ServiceResult.fail(
            message="Unable to write file.",
            error_code="FILE_WRITE_ERROR",
        )


# =============================================================================
# File Deletion
# =============================================================================


def delete_file(
    path: str | Path,
) -> ServiceResult[None]:
    """
    Delete a file.

    Args:
        path:
            File to delete.

    Returns:
        ServiceResult indicating success or failure.
    """

    try:
        file_path = Path(path)

        if file_path.exists():
            file_path.unlink()

            logger.info(
                "Deleted file: %s",
                file_path,
            )

        return ServiceResult.ok(
            message="File deleted successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to delete file."
        )

        return ServiceResult.fail(
            message="Unable to delete file.",
            error_code="FILE_DELETE_ERROR",
        )

# =============================================================================
# File Copy
# =============================================================================


def copy_file(
    source: str | Path,
    destination: str | Path,
) -> ServiceResult[Path]:
    """
    Copy a file.

    Missing destination directories are created automatically.

    Args:
        source:
            Source file.

        destination:
            Destination file.

    Returns:
        ServiceResult containing the copied file path.
    """

    try:
        source_path = Path(source)
        destination_path = Path(destination)

        destination_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.copy2(
            source_path,
            destination_path,
        )

        logger.info(
            "Copied file from %s to %s",
            source_path,
            destination_path,
        )

        return ServiceResult.ok(
            data=destination_path,
            message="File copied successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to copy file."
        )

        return ServiceResult.fail(
            message="Unable to copy file.",
            error_code="FILE_COPY_ERROR",
        )


# =============================================================================
# File Move
# =============================================================================


def move_file(
    source: str | Path,
    destination: str | Path,
) -> ServiceResult[Path]:
    """
    Move a file.

    Missing destination directories are created automatically.

    Args:
        source:
            Source file.

        destination:
            Destination file.

    Returns:
        ServiceResult containing the moved file path.
    """

    try:
        source_path = Path(source)
        destination_path = Path(destination)

        destination_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        shutil.move(
            str(source_path),
            str(destination_path),
        )

        logger.info(
            "Moved file from %s to %s",
            source_path,
            destination_path,
        )

        return ServiceResult.ok(
            data=destination_path,
            message="File moved successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to move file."
        )

        return ServiceResult.fail(
            message="Unable to move file.",
            error_code="FILE_MOVE_ERROR",
        )


# =============================================================================
# File Information
# =============================================================================


def get_file_information(
    path: str | Path,
) -> ServiceResult[dict[str, object]]:
    """
    Retrieve metadata about a file.

    Args:
        path:
            File path.

    Returns:
        ServiceResult containing file metadata.
    """

    try:
        file_path = Path(path)

        if not file_path.exists():
            return ServiceResult.fail(
                message="File does not exist.",
                error_code="FILE_NOT_FOUND",
            )

        information = {
            "name": file_path.name,
            "suffix": file_path.suffix,
            "parent": str(file_path.parent.resolve()),
            "absolute_path": str(file_path.resolve()),
            "size": file_path.stat().st_size,
            "exists": file_path.exists(),
            "is_file": file_path.is_file(),
            "is_directory": file_path.is_dir(),
        }

        logger.info(
            "Retrieved file information: %s",
            file_path,
        )

        return ServiceResult.ok(
            data=information,
            message="File information retrieved successfully.",
        )

    except Exception:
        logger.exception(
            "Unable to retrieve file information."
        )

        return ServiceResult.fail(
            message="Unable to retrieve file information.",
            error_code="FILE_INFORMATION_ERROR",
        )

# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "create_directory",
    "directory_exists",
    "file_exists",
    "read_text",
    "write_text",
    "delete_file",
    "copy_file",
    "move_file",
    "get_file_information",
]