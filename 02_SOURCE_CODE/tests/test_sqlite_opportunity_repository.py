"""
Tests for the SQLite Opportunity repository.
"""

from app.core.database_config import DatabaseConfig
from app.database.connection import (
    get_database_connection,
)
from app.database.schema import (
    initialize_database,
)
from app.models.opportunity import Opportunity
from app.repositories.sqlite_opportunity_repository import (
    SQLiteOpportunityRepository,
)


def create_repository(tmp_path):
    """
    Create a SQLite repository backed by a temporary database.
    """

    database_path = (
        tmp_path / "test_opportunities.db"
    )

    config = DatabaseConfig(
        database_path=str(database_path)
    )

    connection = get_database_connection(
        config
    )

    initialize_database(
        connection
    )

    repository = (
        SQLiteOpportunityRepository(
            connection
        )
    )

    return connection, repository


def test_repository_starts_empty(tmp_path):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        assert repository.count() == 0
        assert repository.list_all() == []
    finally:
        connection.close()


def test_save_and_get_opportunity(tmp_path):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        opportunity = Opportunity(
            id="opp-001",
            title="Funding opportunity",
            source="web",
            description="Test opportunity",
            metadata={
                "category": "funding",
                "priority": "high",
            },
        )

        repository.save(
            opportunity
        )

        result = repository.get_by_id(
            "opp-001"
        )

        assert result is not None
        assert result.id == "opp-001"
        assert (
            result.title
            == "Funding opportunity"
        )
        assert (
            result.description
            == "Test opportunity"
        )

        assert result.metadata == {
            "category": "funding",
            "priority": "high",
        }

    finally:
        connection.close()


def test_get_missing_opportunity_returns_none(
    tmp_path,
):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        result = repository.get_by_id(
            "missing-id"
        )

        assert result is None

    finally:
        connection.close()


def test_save_replaces_existing_opportunity(
    tmp_path,
):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        first = Opportunity(
            id="opp-001",
            title="Original",
            source="web",
        )

        second = Opportunity(
            id="opp-001",
            title="Updated",
            source="partner",
            metadata={
                "updated": True
            },
        )

        repository.save(first)
        repository.save(second)

        result = repository.get_by_id(
            "opp-001"
        )

        assert result is not None
        assert result.title == "Updated"
        assert result.source == "partner"
        assert result.metadata == {
            "updated": True
        }

        assert repository.count() == 1

    finally:
        connection.close()


def test_list_all_opportunities(
    tmp_path,
):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        first = Opportunity(
            id="opp-001",
            title="First",
            source="web",
        )

        second = Opportunity(
            id="opp-002",
            title="Second",
            source="partner",
        )

        repository.save(first)
        repository.save(second)

        results = repository.list_all()

        assert len(results) == 2
        assert results[0].id == "opp-001"
        assert results[1].id == "opp-002"

    finally:
        connection.close()


def test_delete_opportunity(
    tmp_path,
):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        opportunity = Opportunity(
            id="opp-001",
            title="Delete me",
            source="web",
        )

        repository.save(
            opportunity
        )

        assert repository.exists(
            "opp-001"
        )

        deleted = repository.delete(
            "opp-001"
        )

        assert deleted is True
        assert repository.exists(
            "opp-001"
        ) is False
        assert repository.count() == 0

    finally:
        connection.close()


def test_delete_missing_opportunity_returns_false(
    tmp_path,
):
    connection, repository = create_repository(
        tmp_path
    )

    try:
        deleted = repository.delete(
            "missing-id"
        )

        assert deleted is False

    finally:
        connection.close()


def test_repository_data_survives_connection_reopen(
    tmp_path,
):
    database_path = (
        tmp_path / "persistent.db"
    )

    config = DatabaseConfig(
        database_path=str(database_path)
    )

    connection = get_database_connection(
        config
    )

    initialize_database(
        connection
    )

    repository = (
        SQLiteOpportunityRepository(
            connection
        )
    )

    opportunity = Opportunity(
        id="opp-persistent",
        title="Persistent opportunity",
        source="database",
        metadata={
            "persistent": True
        },
    )

    repository.save(
        opportunity
    )

    connection.close()

    reopened_connection = (
        get_database_connection(
            config
        )
    )

    try:
        initialize_database(
            reopened_connection
        )

        reopened_repository = (
            SQLiteOpportunityRepository(
                reopened_connection
            )
        )

        result = (
            reopened_repository.get_by_id(
                "opp-persistent"
            )
        )

        assert result is not None
        assert (
            result.title
            == "Persistent opportunity"
        )

        assert result.metadata == {
            "persistent": True
        }

    finally:
        reopened_connection.close()