"""
Tests for the NOVYRA OS opportunity service.
"""

from app.core.database_config import DatabaseConfig
from app.core.service_result import ServiceResult
from app.database.connection import get_database_connection
from app.database.schema import initialize_database
from app.models.opportunity import Opportunity
from app.repositories.opportunity_repository import OpportunityRepository
from app.repositories.sqlite_opportunity_repository import (
    SQLiteOpportunityRepository,
)
from app.services.opportunity_service import (
    create_opportunity,
    delete_opportunity,
    get_opportunity,
    list_opportunities,
)


def test_create_opportunity_success():
    repository = OpportunityRepository()

    result = create_opportunity(
        opportunity_id="opp-001",
        title="Grant opportunity",
        source="web",
        description="A useful funding opportunity",
        metadata={"category": "funding"},
        repository=repository,
    )

    assert isinstance(result, ServiceResult)
    assert result.success is True
    assert result.error_code is None
    assert result.data is not None

    opportunity = result.data

    assert isinstance(opportunity, Opportunity)
    assert opportunity.id == "opp-001"
    assert opportunity.title == "Grant opportunity"

    stored_opportunity = repository.get_by_id("opp-001")

    assert stored_opportunity is not None
    assert stored_opportunity.id == "opp-001"


def test_create_opportunity_without_repository_does_not_persist():
    result = create_opportunity(
        opportunity_id="opp-no-repository",
        title="Non-persistent opportunity",
        source="test",
    )

    assert result.success is True
    assert result.data is not None
    assert result.data.id == "opp-no-repository"


def test_create_opportunity_validation_failure():
    repository = OpportunityRepository()

    result = create_opportunity(
        opportunity_id=" ",
        title="Grant opportunity",
        source="web",
        repository=repository,
    )

    assert result.success is False
    assert result.data is None
    assert result.error_code == "OPPORTUNITY_VALIDATION_ERROR"
    assert "cannot be empty" in result.message
    assert repository.list_all() == []


def test_get_opportunity_success():
    repository = OpportunityRepository()

    opportunity = Opportunity(
        id="opp-002",
        title="Scholarship opportunity",
        source="university",
    )

    repository.save(opportunity)

    result = get_opportunity(
        opportunity_id="opp-002",
        repository=repository,
    )

    assert result.success is True
    assert result.error_code is None
    assert result.data is not None

    retrieved = result.data

    assert retrieved is opportunity
    assert retrieved.id == "opp-002"


def test_get_opportunity_not_found():
    repository = OpportunityRepository()

    result = get_opportunity(
        opportunity_id="missing-id",
        repository=repository,
    )

    assert result.success is False
    assert result.data is None
    assert result.error_code == "OPPORTUNITY_NOT_FOUND"
    assert "was not found" in result.message


def test_list_opportunities_success():
    repository = OpportunityRepository()

    first = Opportunity(
        id="opp-003",
        title="First opportunity",
        source="web",
    )

    second = Opportunity(
        id="opp-004",
        title="Second opportunity",
        source="partner",
    )

    repository.save(first)
    repository.save(second)

    result = list_opportunities(repository)

    assert result.success is True
    assert result.error_code is None
    assert result.data is not None

    opportunities = result.data

    assert opportunities == [first, second]
    assert len(opportunities) == 2


def test_list_opportunities_empty_repository():
    repository = OpportunityRepository()

    result = list_opportunities(repository)

    assert result.success is True
    assert result.error_code is None
    assert result.data is not None
    assert result.data == []


def test_delete_opportunity_success():
    repository = OpportunityRepository()

    opportunity = Opportunity(
        id="opp-005",
        title="Opportunity to delete",
        source="web",
    )

    repository.save(opportunity)

    result = delete_opportunity(
        opportunity_id="opp-005",
        repository=repository,
    )

    assert result.success is True
    assert result.error_code is None
    assert result.data is None
    assert repository.get_by_id("opp-005") is None


def test_delete_opportunity_not_found():
    repository = OpportunityRepository()

    result = delete_opportunity(
        opportunity_id="missing-id",
        repository=repository,
    )

    assert result.success is False
    assert result.data is None
    assert result.error_code == "OPPORTUNITY_NOT_FOUND"
    assert "was not found" in result.message


def test_create_opportunity_persists_through_sqlite_repository(tmp_path):
    """
    Test that an Opportunity created through the service is persisted
    and can be retrieved after reopening the database connection.
    """

    database_path = tmp_path / "novyra_os.db"

    config = DatabaseConfig(
        database_path=str(database_path),
    )

    connection = get_database_connection(config)

    try:
        initialize_database(connection)

        repository = SQLiteOpportunityRepository(connection)

        result = create_opportunity(
            opportunity_id="opp-persistent-001",
            title="Persistent opportunity",
            source="integration-test",
            description="This opportunity must survive database reopening.",
            metadata={"category": "testing"},
            repository=repository,
        )

        assert result.success is True
        assert result.data is not None
        assert result.data.id == "opp-persistent-001"

    finally:
        connection.close()

    reopened_connection = get_database_connection(config)

    try:
        initialize_database(reopened_connection)

        reopened_repository = SQLiteOpportunityRepository(
            reopened_connection
        )

        retrieved = reopened_repository.get_by_id(
            "opp-persistent-001"
        )

        assert retrieved is not None
        assert retrieved.id == "opp-persistent-001"
        assert retrieved.title == "Persistent opportunity"
        assert retrieved.source == "integration-test"
        assert retrieved.metadata == {"category": "testing"

        }

    finally:
        reopened_connection.close()