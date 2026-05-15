# DataSphere Project State

## Current Status

The repository is being initialized with a Claude Code + Codex orchestration kit.

## North Star

> I give it a folder, and my world grows.

## Current Milestone

MVP: DataSphere Planet Planner.

The MVP should prove that a user can create a district from a folder, project, topic, or vibe, assign it to a valid cell, preserve empty cells, and persist the world state.

## Current Next Task

Create the initial DataSphere domain model for cells, districts, zoning state, and validation.

See `NEXT_CODEX_TASK.md`.

## Active Risks

- Scope creep into full 3D navigation before the zoning model works.
- Agents inventing architecture instead of following source-of-truth docs.
- Renderer complexity hiding weak data/state rules.
- Privacy risks from scanning or uploading file contents too early.
- Auto-organization features mutating real files before the product is safe.

## Current Validation Command

```bash
python scripts/check_datasphere_docs.py
```

## Required Before Real Data Scanning

- explicit user-selected path only
- metadata-only defaults
- ignore rules
- size/depth limits
- no file mutations
- no network upload of file contents

## Agent Protocol

1. Claude updates `NEXT_CODEX_TASK.md` with exactly one task.
2. Codex implements only that task.
3. Codex writes `CODEX_REPORT.md`.
4. Claude reviews and updates project state.
