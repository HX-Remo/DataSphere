# DataSphere Roadmap

The roadmap is ordered around visible proof. Every major feature should make the planet more real without breaking the zoning law.

## MVP: DataSphere Planet Planner

Goal: spawn a district from a folder, project, topic, or vibe and see it appear in a valid cell on the planet.

## Build Order

1. Static spherical grid renderer or placeholder grid renderer.
2. Cell coordinate system.
3. Empty/occupied zoning state.
4. Folder scanner or mock source scanner.
5. District proposal JSON.
6. District placement inside one cell.
7. Save/load world state.
8. Billboard text generation using a mock/local interface first.
9. Routes between districts.
10. First-person trench navigation.

## Phase 0: Orchestration Setup

Status: in progress.

Deliverables:
- source-of-truth docs
- Claude/Codex prompts
- validation script
- first Codex task

## Phase 1: Domain Model

Deliverables:
- grid/cell model
- district model
- zoning state
- validation errors
- tests for overlap, malformed districts, and empty cells

## Phase 2: Persistence

Deliverables:
- save/load world state
- schema version
- migration-friendly state format
- test fixtures

## Phase 3: Mock Planner

Deliverables:
- deterministic district proposals from folder-like metadata
- mock billboards in three voices
- no network calls

## Phase 4: Renderer Prototype

Deliverables:
- visible grid
- occupied/empty cells
- district markers
- route lines or trench highlights

## Phase 5: Desktop Shell

Deliverables:
- local app wrapper
- folder picker
- safe indexing settings
- privacy-first defaults

## Phase 6: Navigation Prototype

Deliverables:
- cruise movement
- trench-following camera
- banking turns
- district labels and billboard surfaces

## Weekly North-Star Check

Can the user spawn a new district from their own data and see the world grow?
