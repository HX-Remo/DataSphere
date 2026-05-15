# Next Codex Task

## Task: Create the initial DataSphere domain model

Create the initial DataSphere domain model for cells, districts, zoning state, and validation.

## Goal

Give the project a small, testable core that enforces the main rule:

> The grid is zoning law. Districts are assigned to cells. Empty cells remain valid.

## Required behavior

Implement models for:

- Cell coordinate
- District
- Billboard set
- Zoning/world state
- Placement validation result

The implementation language and location should follow the repo's existing stack. If the stack is still empty or unclear, prefer a simple Python module under `datasphere_core/` with tests under `tests/`.

## Minimum rules

- A cell coordinate has `lat_band` and `lon_band` integer values.
- Cell coordinates must be inside the configured grid bounds.
- A district must have a unique `district_id`.
- A district must belong to exactly one cell.
- Two districts cannot occupy the same cell.
- Empty cells must be preserved and queryable.
- Malformed district data must fail closed.
- `density`, `height`, and `route_priority` must be bounded from 0.0 to 1.0.

## Suggested Python shape if stack is empty

```txt
datasphere_core/
  __init__.py
  domain.py

tests/
  test_domain.py
```

## Validation tests

Add tests that prove:

1. a valid district can be placed in an empty valid cell
2. overlapping placement is rejected
3. out-of-range cell coordinates are rejected
4. malformed district JSON/data is rejected
5. empty cells remain empty and queryable
6. duplicate district ids are rejected

## Constraints

- Do not implement rendering yet.
- Do not scan the user's real file system yet.
- Do not add network calls.
- Do not mutate user files.
- Do not create a full app shell yet.
- Keep this as a small reviewable domain-model change.

## Completion report

After implementation, write `CODEX_REPORT.md` using `CODEX_REPORT_TEMPLATE.md`.
