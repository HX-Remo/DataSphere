# DataSphere Vision

DataSphere is a 3D desktop that turns a user's hard drive into a pilotable planet.

The planet is a dark spherical world with deeply carved latitude and longitude trenches. Those trenches form a visible spherical grid of canyons. The grid is not decoration. The grid is zoning law.

Every parcel on the planet is a cell. Districts live inside cells. Nothing is allowed to spill across a cell boundary. Empty cells are valid and important because they create breathing room, preserve readable routes, and keep the world feeling growable instead of finished.

## Core Promise

The user gives DataSphere a folder, project, topic, or vibe. DataSphere proposes a district, assigns it to an empty cell, generates billboard copy, updates routes, and makes the world visibly grow.

The north star is:

> I give it a folder, and my world grows.

## Visual Language

- Dark spherical planet.
- Deep carved lat/lon trenches.
- Cyan rim light along cell edges and trench walls.
- Glowing data below the crust.
- Districts that read clearly from a distance.
- Empty cells preserved as breathing room.
- First-person trench navigation as a later milestone.

## Districts

Districts are user-created regions of files or concepts. They may be spawned from a folder, project, topic, vibe, saved search, or manually described idea.

Example district themes include lens mountains for photos, paper-stack towers for office files, junkyard mounds for downloads, server-rack mesas for code, neon piers for media, pixel outposts for games, and stepped ziggurats for papers.

These are examples, not fixed categories. The final system should grow organically as the user's data grows.

## Billboards

Each district can surface generated prompts about the user's files in three voices:

1. carnival barker
2. dry poet
3. familiar friend

Billboards must be useful without being invasive. Early implementations should use mock/local text generation before any live model integration.

## Navigation

The eventual navigation goal is first-person movement through the trenches at constant altitude. The planet rotates underneath the ship at cruise speed. The camera faces the direction of travel and banks into turns. A GPS panel and ticker can surface contextual data.

Navigation is not the MVP. The MVP is district spawning and zoning.

## MVP Definition

The first buildable milestone is DataSphere Planet Planner:

1. User selects or describes a folder, project, topic, or vibe.
2. System creates a district proposal.
3. Zoning engine assigns it to an empty cell.
4. District appears on a spherical grid or placeholder grid.
5. Billboards show generated or mock prompts.
6. World state persists.

## Non-Goals For Now

- Do not move, rename, delete, or reorganize real user files.
- Do not upload user file contents.
- Do not build a full OS replacement yet.
- Do not require perfect 3D rendering before the zoning model works.
- Do not let agents auto-merge or redesign the architecture without review.
