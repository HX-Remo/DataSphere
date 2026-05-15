#!/usr/bin/env python3
"""Validate that the DataSphere orchestration docs exist.

This script intentionally checks only lightweight repository setup files.
It does not scan user data, call the network, or mutate files.
"""

from __future__ import annotations

from pathlib import Path
import sys

REQUIRED_FILES = [
    "README.md",
    "VISION.md",
    "ARCHITECTURE.md",
    "ROADMAP.md",
    "AGENTS.md",
    "TASK_QUEUE.md",
    "NEXT_CODEX_TASK.md",
    "CODEX_REPORT_TEMPLATE.md",
    "CLAUDE_REVIEW_TEMPLATE.md",
    "DECISIONS.md",
    "PROJECT_STATE.md",
    "CHANGELOG.md",
    "INBOX_THOUGHTS.md",
    "prompts/claude_architect_prompt.md",
    "prompts/codex_builder_prompt.md",
    "prompts/claude_review_prompt.md",
    "scripts/check_datasphere_docs.py",
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    missing: list[str] = []

    print("DataSphere orchestration checklist")
    print("==================================")

    for relative_path in REQUIRED_FILES:
        path = repo_root / relative_path
        if path.exists():
            print(f"[PASS] {relative_path}")
        else:
            print(f"[FAIL] {relative_path}")
            missing.append(relative_path)

    print()
    if missing:
        print("Missing required files:")
        for relative_path in missing:
            print(f"- {relative_path}")
        return 1

    print("All required orchestration files are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
