# NOVYRA OS Codebase Guide

---

# Purpose

This document serves as the master navigation guide for the NOVYRA OS source code.

Unlike the Architecture document, which explains how the system is designed, this guide explains where everything lives, why it exists, and where future code should be added.

Every developer working on NOVYRA should read this document before making architectural changes.

---

# Current Project Structure

```
NOVYRA_OS/

│
├── 01_REQUIREMENTS/
├── 02_SOURCE_CODE/
│
│   ├── app/
│   │
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── tests/
│
├── 08_BACKUPS/
├── 09_DOCUMENTATION/
│
├── verify_database.py
└── README.md
```

---

# Source Code Overview

## app/core/

Contains application-wide infrastructure.

Examples:

- Configuration
- Logging
- Paths
- Constants
- ServiceResult
- Database configuration

Business logic should never live here.

---

## app/database/

Contains database infrastructure.

Responsibilities include

- Database connections
- Schema creation
- Database initialization

Database queries belong inside repositories.

---

## app/models/

Contains domain models.

Examples

- Opportunity
- User (future)
- Project (future)

Models represent business entities.

Models should never contain persistence code.

---

## app/repositories/

Responsible for persistence.

Repositories isolate business logic from databases.

Current implementation

- In-memory repository
- SQLite repository

Future implementations

- PostgreSQL
- Cloud Database
- REST Repository
- Offline Sync Repository

---

## app/services/

Contains business logic.

Services coordinate

Models

↓

Repositories

↓

Business Rules

↓

ServiceResult

Services should never know whether data comes from SQLite, PostgreSQL or another source.

---

## app/tests/

Contains automated tests.

Every new feature should include

- unit tests
- integration tests (when appropriate)

---

# Dependency Flow

The intended dependency direction is

```
Interface

↓

Services

↓

Repositories

↓

Database

↓

Storage
```

Higher layers should never depend directly on lower implementation details.

---

# Where New Code Belongs

## New business entity

Create

```
models/

repositories/

services/

tests/
```

---

## New AI capability

Create

```
services/ai/

or

services/intelligence/
```

depending on responsibility.

---

## New interface

Never modify business logic.

Create a new interface layer

Examples

```
mobile/

api/

web/

desktop/
```

---

# Documentation Policy

Every Python file should contain

- File Header
- Purpose
- Description
- Phase
- Imports section
- Logical section separators
- Docstrings
- WHY comments

---

# Testing Policy

Every new feature requires

- Tests
- Documentation
- Verification

before merging.

---

# Refactoring Policy

Never refactor simply because a file becomes large.

Refactor only when

- responsibilities increase
- readability improves
- duplication exists
- architecture benefits

---

# Public API Rule

Internal structure may change.

Public imports should remain stable.

Example

```
from app.services.opportunity import create_opportunity
```

instead of exposing internal implementation files.

---

# Long-Term Vision

One backend.

Multiple interfaces.

- Kivy Mobile Application
- REST API
- Web Dashboard
- Desktop Application

Every interface consumes the same business services.

---

# This Guide

This document is a living document.

It should evolve as NOVYRA grows.

Whenever a major architectural decision changes the project layout, this guide should be updated.