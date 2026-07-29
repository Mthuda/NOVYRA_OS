# NOVYRA OS Database Documentation

**Database Engine:** SQLite

**Current Version:** v0.3.0

**Current Phase:** Phase 3 – Persistence Foundation

---

# 1. Overview

NOVYRA OS currently uses SQLite as its primary persistence engine.

SQLite was selected because it provides:

- Zero configuration
- Excellent reliability
- Cross-platform compatibility
- Fast local development
- Easy backup and deployment

The database layer has been designed so that SQLite can later be replaced or
supplemented with another database engine (such as PostgreSQL) with minimal
changes to the service layer.

---

# 2. Database Location

Default database file:

```
08_BACKUPS/novyra_os.db
```

The location can be changed using the environment variable:

```
NOVYRA_DATABASE_PATH
```

---

# 3. Database Architecture

The database layer consists of:

```
Application Services
        │
Repositories
        │
SQLite Repository
        │
SQLite Connection
        │
SQLite Database
```

Business logic never communicates directly with SQLite.

All database operations are performed through repositories.

---

# 4. Current Schema

## opportunities

| Column | Type | Constraints |
|---------|------|-------------|
| id | TEXT | PRIMARY KEY |
| title | TEXT | NOT NULL |
| source | TEXT | NOT NULL |
| description | TEXT | NULL |
| metadata | TEXT | NOT NULL DEFAULT '{}' |

---

# 5. Current Tables

The current database contains:

- opportunities

Future versions will introduce additional tables as needed.

---

# 6. Repository Responsibilities

The SQLiteOpportunityRepository is responsible for:

- Saving opportunities
- Retrieving opportunities
- Updating opportunities
- Deleting opportunities
- Listing all opportunities
- Counting opportunities
- Checking for existence

The repository translates between SQLite rows and Opportunity domain objects.

---

# 7. Database Initialization

The database schema is created using:

```
initialize_database(connection)
```

The schema initialization is idempotent.

Running it multiple times does not destroy existing data.

---

# 8. Testing

Database functionality is verified through automated tests covering:

- Database configuration
- Connection creation
- Row factory configuration
- Schema initialization
- Idempotent initialization
- Database file creation
- SQLite repository persistence
- Repository reopen persistence

All database tests must pass before a phase is considered complete.

---

# 9. Future Database Evolution

Planned additions include:

- Opportunity status
- Categories
- Priorities
- Deadlines
- Created timestamps
- Updated timestamps
- User information
- Notifications
- Search history
- Analytics

Schema migrations will be introduced when structural changes become necessary.

---

# 10. Backup Strategy

The default database is stored in:

```
08_BACKUPS/
```

This location simplifies backup and recovery during development.

Future versions may include:

- Automatic backups
- Database export
- Cloud synchronization
- Restore utilities

---

# 11. Design Goals

The database layer is designed to provide:

- Reliability
- Simplicity
- Maintainability
- Repository abstraction
- Future scalability
- Easy migration to larger database systems

This document should be updated whenever the database schema changes.