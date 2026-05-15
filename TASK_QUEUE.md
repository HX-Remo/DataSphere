# DataSphere Task Queue

Tasks are ordered by MVP value. Codex should only implement the task copied into NEXT_CODEX_TASK.md.

## P0-001: Initial domain model

Goal: Create the initial DataSphere domain model for cells, districts, zoning state, and validation.

Likely files touched:
- src or datasphere_core domain files depending on repo stack
- tests for the domain model
- CHANGELOG.md
- CODEX_REPORT.md

Input:
- grid dimensions
- district proposal object
- current occupancy state

Output:
- valid cell coordinate model
- valid district model
- zoning state model
- placement validation result

Validation:
- accepts a district in an empty valid cell
- rejects overlapping cell placement
- rejects malformed district JSON
- preserves empty cells
- rejects out-of-range coordinates

Failure cases:
- duplicate district id
- invalid cell coordinate
- occupied cell
- missing district fields
- density or height outside allowed range

## P0-002: World state persistence

Goal: Save and load a validated world state.

Validation:
- round-trip save/load preserves cells and districts
- malformed state fails closed
- schema version is present

## P0-003: Mock district planner

Goal: Convert folder-like metadata into a deterministic district proposal.

Validation:
- same input produces same district proposal
- output matches district schema
- no network calls

## P0-004: Mock billboard engine

Goal: Generate three short messages for each district using local deterministic templates.

Validation:
- creates carnival_barker, dry_poet, and familiar_friend fields
- handles missing metadata safely

## P1-001: Placeholder grid renderer

Goal: Show occupied and empty cells in a simple visible grid before full 3D rendering.

Validation:
- empty cells render distinctly
- occupied cells show district labels

## P1-002: Route graph prototype

Goal: Build route relationships between occupied cells over the grid.

Validation:
- routes only use valid neighboring cells
- stale district ids are rejected

## P2-001: Spherical renderer prototype

Goal: Render a dark sphere with a visible cell grid and district markers.

Validation:
- grid remains visible
- districts stay visually inside cells
