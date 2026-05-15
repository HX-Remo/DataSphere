# DataSphere Agent Workflow

This repo uses a two-agent workflow.

## Role Split

### Claude Code

Claude Code acts as:

- Architect
- Red Team
- Scribe

Claude owns product direction, architecture review, risk review, task breakdown, and project memory.

Claude should update:

- `VISION.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`
- `TASK_QUEUE.md`
- `NEXT_CODEX_TASK.md`
- `PROJECT_STATE.md`
- `DECISIONS.md`

Claude should not freestyle large implementations unless explicitly assigned.

### Codex

Codex acts as:

- Builder
- Verifier

Codex owns implementation, tests, validation, and concise reports.

Codex should update code, tests, `CHANGELOG.md`, and `CODEX_REPORT.md`.

Codex must only implement the task in `NEXT_CODEX_TASK.md`.

## Agent Loop

```txt
User thoughts -> Claude architecture/task -> Codex implementation -> Codex report -> Claude review -> project state update
```

## Required Workflow

1. User places raw ideas in `INBOX_THOUGHTS.md` or tells Claude directly.
2. Claude updates `TASK_QUEUE.md` and writes exactly one task into `NEXT_CODEX_TASK.md`.
3. Codex reads the source-of-truth docs and implements only that task.
4. Codex runs tests and writes `CODEX_REPORT.md`.
5. Claude reviews the report and diff using `CLAUDE_REVIEW_TEMPLATE.md`.
6. Claude updates `PROJECT_STATE.md`, `TASK_QUEUE.md`, and the next task.

## Branch Rules

Recommended branch pattern:

```txt
main
agent/codex-domain-model
agent/codex-zoning-engine
agent/claude-architecture-review
```

Rules:

- `main` should remain stable.
- Use agent branches for implementation.
- Do not auto-merge.
- Do not let agents make unrelated large rewrites.

## Safety Rules

- Do not move, rename, delete, or reorganize real user files yet.
- Do not upload file contents.
- Use metadata-only indexing first.
- Use mock/local generation before live model calls.
- Fail closed on malformed JSON or state.
- Keep empty cells valid.
- Clamp every district to exactly one cell until the architecture deliberately supports multi-cell districts.

## Scope Control

Every task must answer:

- What visible DataSphere behavior does this enable?
- What files are touched?
- How is it validated?
- What failure cases are tested?

If a task does not advance district spawning, zoning, rendering, persistence, routing, or safe indexing, it should usually wait.
