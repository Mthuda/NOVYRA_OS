"""
Public service exports for NOVYRA OS.
"""

from app.services.config_service import (
    get_configuration,
    get_configuration_information,
    reload_configuration,
)
from app.services.database_service import (
    check_database_health,
    close_database,
    get_database,
    get_database_information,
    initialize,
)
from app.services.logging_service import get_logger
from app.services.opportunity_service import (
    create_opportunity,
    delete_opportunity,
    get_opportunity,
    list_opportunities,
)
from app.services.system_service import get_system_summary

__all__ = [
    # Configuration
    "get_configuration",
    "reload_configuration",
    "get_configuration_information",

    # Database
    "get_database",
    "initialize",
    "close_database",
    "check_database_health",
    "get_database_information",

    # Logging
    "get_logger",

    # Opportunity
    "create_opportunity",
    "get_opportunity",
    "list_opportunities",
    "delete_opportunity",

    # System
    "get_system_summary",
]