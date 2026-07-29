# NOVYRA OS API Specification

Version: 0.2.0

Status:
Internal Specification

---

# Purpose

This document defines the service API used internally by NOVYRA OS.

Although Phase 3 does not expose a REST API, every service is designed as though it could later become an HTTP endpoint.

This makes future migration to:

- Mobile App (Kivy)
- REST API
- Web Dashboard
- Desktop App

straightforward.

---

# ServiceResult Standard

Every service returns a ServiceResult object.

Example:

```python
ServiceResult.ok(
    data=data,
    message="Operation completed."
)
```

Failure:

```python
ServiceResult.fail(
    message="Opportunity not found.",
    error_code="OPPORTUNITY_NOT_FOUND"
)
```

---

# Opportunity Service

## Create Opportunity

Function

```python
create_opportunity(...)
```

Returns

```
ServiceResult[Opportunity]
```

Possible errors

```
OPPORTUNITY_VALIDATION_ERROR
```

---

## Get Opportunity

Function

```python
get_opportunity(opportunity_id)
```

Returns

```
ServiceResult[Opportunity]
```

Possible errors

```
OPPORTUNITY_NOT_FOUND
```

---

## List Opportunities

Function

```python
list_opportunities()
```

Returns

```
ServiceResult[list[Opportunity]]
```

---

## Delete Opportunity

Function

```python
delete_opportunity(opportunity_id)
```

Returns

```
ServiceResult[None]
```

Possible errors

```
OPPORTUNITY_NOT_FOUND
```

---

# System Service

## Get System Summary

Function

```python
get_system_summary(config)
```

Returns

```
ServiceResult[dict]
```

Data includes

- project_name
- version
- stage
- environment
- debug
- project_root

---

# Future REST API

Phase 8+

The internal service API maps directly to REST endpoints.

Example

```
GET /api/opportunities
```

↓

```
list_opportunities()
```

---

```
POST /api/opportunities
```

↓

```
create_opportunity()
```

---

```
GET /api/opportunities/{id}
```

↓

```
get_opportunity()
```

---

```
DELETE /api/opportunities/{id}
```

↓

```
delete_opportunity()
```

---

# Response Format

Future REST API responses will follow:

Success

```json
{
    "success": true,
    "message": "...",
    "data": {}
}
```

Failure

```json
{
    "success": false,
    "message": "...",
    "error_code": "..."
}
```