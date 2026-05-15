# DataSphere Decisions

This file records architectural decisions that agents must preserve unless a later decision explicitly changes them.

## 0001: Grid is zoning law

The lat/lon grid is not decoration. It is the spatial law of the world. Every cell is a parcel.

## 0002: Districts are clamped to one cell first

The first implementation supports one district per cell and one cell per district. Multi-cell districts are out of scope until the core zoning model is stable.

## 0003: Empty cells are valid

Empty cells are not failures. They preserve breathing room, routes, and future growth.

## 0004: Observe before mutate

DataSphere should observe and represent the user's data before it ever organizes, moves, renames, edits, or deletes files.

## 0005: Metadata first

Early scanning uses metadata, not private file contents.

## 0006: Local/mock generation first

Billboards and district planning should start with deterministic local/mock generation before live model calls.

## 0007: Fail closed

Malformed district data, malformed world state, out-of-range cells, duplicate ids, and overlapping placements must be rejected.

## 0008: Claude plans, Codex builds

Claude Code owns architecture and review. Codex owns implementation and tests. Codex implements only `NEXT_CODEX_TASK.md`.
