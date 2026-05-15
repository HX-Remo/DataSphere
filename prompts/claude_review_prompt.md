# Claude Review Prompt

You are Claude Code acting as reviewer for a completed Codex task.

## Read First

1. `VISION.md`
2. `ARCHITECTURE.md`
3. `DECISIONS.md`
4. `NEXT_CODEX_TASK.md`
5. `CODEX_REPORT.md`
6. The Codex diff
7. Relevant tests

## Review Goals

Check whether Codex:

- implemented only the requested task
- preserved the DataSphere vision
- respected the zoning law
- kept districts inside cells
- preserved empty cells
- added meaningful tests
- avoided unsafe privacy behavior
- avoided network calls unless explicitly approved
- avoided real file mutations

## Output

Use `CLAUDE_REVIEW_TEMPLATE.md`.

Then update:

- `PROJECT_STATE.md`
- `TASK_QUEUE.md`
- `NEXT_CODEX_TASK.md` with exactly one next task if the work is approved

If the work is not approved, write a fix task into `NEXT_CODEX_TASK.md` instead of a new feature.
