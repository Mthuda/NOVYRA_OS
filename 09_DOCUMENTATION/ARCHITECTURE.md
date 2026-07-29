# NOVYRA OS Architecture

**Project:** NOVYRA OS

**Current Version:** v0.3.0

**Current Phase:** Phase 3 – Persistence Foundation

---

# 1. Overview

NOVYRA OS is a modular opportunity intelligence platform designed to discover,
store, analyse and manage opportunities such as:

- Scholarships
- Bursaries
- Grants
- Jobs
- Learnerships
- Internships
- Business Funding
- Competitions
- Research Funding
- Innovation Challenges

The system follows a layered architecture that separates business logic from
data storage and user interfaces.

This makes the project maintainable, testable and scalable.

---

# 2. Design Principles

NOVYRA follows these engineering principles:

- Separation of Concerns
- Single Responsibility Principle
- Repository Pattern
- Service Layer Pattern
- Domain Driven Design (Lightweight)
- Test Driven Development
- Modular Architecture
- Future API-first Design

---

# 3. High-Level Architecture

                    User Interfaces
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          │                │                │
     Kivy Mobile      Web Dashboard    Desktop App
          │                │                │
          └────────────────┼────────────────┘
                           │
                    REST API (Future)
                           │
                   Application Services
                           │
                  Repository Abstraction
                           │
          ┌────────────────┴────────────────┐
          │                                 │
     In-Memory Repository          SQLite Repository
                           │
                      SQLite Database

---

# 4. Project Structure

NOVYRA_OS/

01_PROJECT_DOCUMENTS/

02_SOURCE_CODE/

app/

core/

database/

models/

repositories/

services/

utils/

tests/

08_BACKUPS/

09_DOCUMENTATION/

README.md

verify_database.py

---

# 5. Core Modules

## app/core

Contains application infrastructure.

Responsibilities include:

- Configuration
- Logging
- Paths
- Project metadata
- Database configuration
- ServiceResult

---

## app/models

Contains business entities.

Current entities:

- Opportunity

Future entities:

- User
- Notification
- AI Analysis
- Search History

---

## app/services

Contains business logic.

Current:

- SystemService
- OpportunityService

Future:

- SearchService
- NotificationService
- AIService
- RecommendationService

---

## app/repositories

Responsible for persistence.

Current:

- OpportunityRepository
- SQLiteOpportunityRepository

Future:

- PostgreSQLRepository
- RESTRepository

---

## app/database

Responsible for database infrastructure.

Contains:

- Connection management
- Schema creation
- Future migrations

---

# 6. Current Database

Engine:

SQLite

Current tables:

- opportunities

---

# 7. Testing Strategy

The project uses pytest.

Testing levels include:

- Unit Tests
- Repository Tests
- Integration Tests
- Database Tests
- Service Tests

All phases must finish with a fully passing test suite.

---

# 8. Development Workflow

Each development phase follows the same workflow:

1. Design
2. Implement
3. Test
4. Verify
5. Update Documentation
6. Commit
7. Push

No phase is considered complete until all steps succeed.

---

# 9. Planned User Interfaces

The backend is intentionally independent of any user interface.

Planned interfaces are:

## Phase 8A

Kivy Mobile Application

Primary interface.

---

## Phase 8B

REST API

Provides programmatic access to NOVYRA services.

---

## Phase 8C

Web Dashboard

Browser-based interface using the REST API.

---

## Phase 8D

Desktop Application

Desktop interface that consumes the same backend.

---

# 10. Future Growth

Planned major capabilities include:

- Opportunity scraping
- AI-powered opportunity scoring
- Automatic recommendations
- Deadline tracking
- Notification engine
- User accounts
- Cloud synchronization
- Analytics
- Reporting
- Machine learning

---

# 11. Architecture Goals

NOVYRA aims to provide:

- Clean architecture
- High maintainability
- Easy testing
- Low coupling
- High cohesion
- Multiple user interfaces sharing one backend
- Long-term scalability

This document should be updated whenever the system architecture changes.