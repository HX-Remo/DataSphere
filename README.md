# DataSphere

DataSphere is a 3D desktop concept that turns a user's hard drive into a pilotable planet.

The repo is initialized with an agent orchestration kit so Claude Code can act as architect/reviewer and Codex can act as builder/verifier.

Start here:

1. Read `VISION.md`.
2. Read `ARCHITECTURE.md`.
3. Read `AGENTS.md`.
4. Have Claude update `NEXT_CODEX_TASK.md`.
5. Have Codex implement only that task and write `CODEX_REPORT.md`.

Validation:

```bash
python scripts/check_datasphere_docs.py
```
