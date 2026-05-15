# DataSphere Architecture

DataSphere is organized around a small set of modules. The renderer can evolve, but the domain rules must remain stable: the grid is zoning law, districts live inside cells, and empty cells are valid.

## Module Map

```txt
filesystem_indexer -> district_planner -> zoning_engine -> state_store
                                      -> billboard_engine
                                      -> routing_engine
state_store -> planet_renderer
```

## filesystem_indexer

Responsibility: Read selected folders and produce safe metadata for planning.

Inputs:
- folder path or virtual source id
- scan depth and file limits
- allowlist/ignore rules

Outputs:
- file count
- extension summary
- size summary
- modified-time summary
- optional sample names when allowed

Failure cases:
- inaccessible path
- permission error
- path too large
- unsupported source

Privacy constraints:
- default to metadata only
- do not upload file contents
- do not mutate user files

## district_planner

Responsibility: Turn a folder, project, topic, or vibe into a district proposal.

Inputs:
- source metadata
- user hint
- available district themes

Outputs:
- district id
- theme
- structure type
- density
- height
- color palette
- billboard seeds
- neighbor hints

Failure cases:
- malformed source metadata
- ambiguous user hint
- invalid density or height
- duplicate district id

Privacy constraints:
- use local/mock generation first
- keep prompts derived from metadata unless user opts in to deeper scanning

## zoning_engine

Responsibility: Assign districts to cells and enforce the grid rules.

Inputs:
- district proposal
- current world state
- available cells

Outputs:
- accepted district placement
- rejected placement with reason
- updated occupancy map

Failure cases:
- cell occupied
- cell outside grid
- district exceeds bounds
- malformed cell coordinate

Privacy constraints:
- stores references and metadata, not file contents

## billboard_engine

Responsibility: Generate surface text for districts.

Inputs:
- district metadata
- voice name
- safety/privacy settings

Outputs:
- short billboard messages
- fallback placeholder messages

Failure cases:
- missing district metadata
- generation unavailable
- unsafe or over-personal text

Privacy constraints:
- local/mock interface first
- no network calls unless explicitly enabled later

## routing_engine

Responsibility: Create route relationships between cells and districts using trenches as streets.

Inputs:
- grid topology
- occupied cells
- district neighbor hints

Outputs:
- route graph
- nearest-neighbor suggestions
- route priority values

Failure cases:
- disconnected grid
- invalid neighbor id
- stale route after district removal

Privacy constraints:
- routes are spatial metadata only

## planet_renderer

Responsibility: Visualize the world state.

Inputs:
- grid definition
- district placements
- routes
- camera/navigation state

Outputs:
- spherical grid
- district markers or meshes
- labels/billboards
- route/trench highlights

Failure cases:
- missing assets
- impossible geometry
- renderer cannot fit district within cell

Privacy constraints:
- do not reveal sensitive filenames in public capture modes

## state_store

Responsibility: Persist the user's DataSphere world.

Inputs:
- grid state
- districts
- routes
- user settings

Outputs:
- saved world file or database rows
- loaded world state
- validation errors

Failure cases:
- malformed state file
- schema mismatch
- duplicate ids
- occupied-cell conflict

Privacy constraints:
- keep paths local
- avoid storing file contents
- support redacted/export-safe state later

## Core Data Shape

```json
{
  "district_id": "photos_ski_trip_2024",
  "source_ref": "local-folder-ref",
  "cell": { "lat_band": 4, "lon_band": 12 },
  "theme": "frozen lens mountain",
  "structure_type": "lens_mountain",
  "density": 0.62,
  "height": 0.48,
  "color_palette": ["cyan", "ice_blue", "white"],
  "billboards": {
    "carnival_barker": "A bright little archive with snow, motion, and unfinished stories.",
    "dry_poet": "Cold light, saved twice, waiting.",
    "familiar_friend": "This looks like a memory cluster worth revisiting."
  },
  "neighbors": [],
  "route_priority": 0.74
}
```
