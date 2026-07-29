"""
SQLite repository for Opportunity domain entities.

This module provides persistent storage for Opportunity objects using SQLite.
"""

from __future__ import annotations

import json
import sqlite3
from typing import List, Optional

from app.models.opportunity import Opportunity


class SQLiteOpportunityRepository:
    """
    SQLite-backed repository for Opportunity entities.

    The repository is responsible for translating between:
        - Opportunity domain objects
        - SQLite database rows

    The service layer does not need to know how persistence is implemented.
    """

    def __init__(self, connection: sqlite3.Connection) -> None:
        """
        Initialize the SQLite Opportunity repository.

        Args:
            connection: Active SQLite database connection.
        """
        self._connection = connection

    def save(self, opportunity: Opportunity) -> Opportunity:
        """
        Save or replace an Opportunity.

        Args:
            opportunity: Opportunity entity to persist.

        Returns:
            The saved Opportunity.
        """

        metadata_json = json.dumps(
            opportunity.metadata,
            sort_keys=True,
        )

        self._connection.execute(
            """
            INSERT INTO opportunities (
                id,
                title,
                source,
                description,
                metadata
            )
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(id)
            DO UPDATE SET
                title = excluded.title,
                source = excluded.source,
                description = excluded.description,
                metadata = excluded.metadata
            """,
            (
                opportunity.id,
                opportunity.title,
                opportunity.source,
                opportunity.description,
                metadata_json,
            ),
        )

        self._connection.commit()

        return opportunity

    def get_by_id(
        self,
        opportunity_id: str,
    ) -> Optional[Opportunity]:
        """
        Retrieve an Opportunity by ID.

        Args:
            opportunity_id: Unique Opportunity identifier.

        Returns:
            The matching Opportunity, or None if not found.
        """

        row = self._connection.execute(
            """
            SELECT
                id,
                title,
                source,
                description,
                metadata
            FROM opportunities
            WHERE id = ?
            """,
            (opportunity_id,),
        ).fetchone()

        if row is None:
            return None

        return self._row_to_opportunity(row)

    def list_all(self) -> List[Opportunity]:
        """
        Return all stored Opportunities.

        Returns:
            List of Opportunity entities.
        """

        rows = self._connection.execute(
            """
            SELECT
                id,
                title,
                source,
                description,
                metadata
            FROM opportunities
            ORDER BY id
            """
        ).fetchall()

        return [
            self._row_to_opportunity(row)
            for row in rows
        ]

    def delete(
        self,
        opportunity_id: str,
    ) -> bool:
        """
        Delete an Opportunity by ID.

        Args:
            opportunity_id: Unique Opportunity identifier.

        Returns:
            True if an Opportunity was deleted.
            False if no matching Opportunity existed.
        """

        cursor = self._connection.execute(
            """
            DELETE FROM opportunities
            WHERE id = ?
            """,
            (opportunity_id,),
        )

        self._connection.commit()

        return cursor.rowcount > 0

    def exists(
        self,
        opportunity_id: str,
    ) -> bool:
        """
        Check whether an Opportunity exists.

        Args:
            opportunity_id: Unique Opportunity identifier.

        Returns:
            True if the Opportunity exists.
            False otherwise.
        """

        row = self._connection.execute(
            """
            SELECT 1
            FROM opportunities
            WHERE id = ?
            LIMIT 1
            """,
            (opportunity_id,),
        ).fetchone()

        return row is not None

    def count(self) -> int:
        """
        Return the number of stored Opportunities.

        Returns:
            Number of stored Opportunities.
        """

        row = self._connection.execute(
            """
            SELECT COUNT(*) AS opportunity_count
            FROM opportunities
            """
        ).fetchone()

        return int(row["opportunity_count"])

    @staticmethod
    def _row_to_opportunity(
        row: sqlite3.Row,
    ) -> Opportunity:
        """
        Convert a SQLite row into an Opportunity domain object.

        Args:
            row: SQLite row containing Opportunity data.

        Returns:
            Reconstructed Opportunity object.
        """

        metadata = json.loads(
            row["metadata"]
        ) if row["metadata"] else {}

        return Opportunity(
            id=row["id"],
            title=row["title"],
            source=row["source"],
            description=row["description"] or "",
            metadata=metadata,
        )