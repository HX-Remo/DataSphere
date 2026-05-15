# Claude Review Template

Claude should use this structure when reviewing Codex output.

## Vision Fit

Does the change support the DataSphere north star?

> I give it a folder, and my world grows.

## Architecture Fit

Does the change respect the module boundaries in `ARCHITECTURE.md`?

## Zoning Law Review

Confirm:

- districts stay inside cells
- empty cells remain valid
- overlapping cells are rejected
- malformed state fails closed

## Safety and Privacy Review

Confirm:

- no user file mutation
- no network calls unless explicitly approved
- no private file content upload
- metadata-only behavior where applicable

## Test Review

List what the tests prove and what is still missing.

## Scope Control

Did Codex implement only `NEXT_CODEX_TASK.md`?

## Required Fixes

List blocking fixes. Use `None` if no blocking fixes.

## Approved Next Task

Write exactly one next implementation task candidate.
