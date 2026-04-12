#!/usr/bin/env python3
"""Validate basic Spechugger tasks.md checklist invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TASK_RE = re.compile(r"^- \[[ xX]\] (T\d{3})(?:\s|$)")
VERIFY_HEADING_RE = re.compile(r"^## Verification Commands\s*$")
HEADING_RE = re.compile(r"^##\s+")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tasks", help="Path to tasks.md")
    args = parser.parse_args()

    path = Path(args.tasks)
    if not path.exists():
        print(f"Missing tasks file: {path}", file=sys.stderr)
        return 2

    lines = path.read_text().splitlines()
    ids: list[str] = []
    errors: list[str] = []

    for line_no, line in enumerate(lines, start=1):
        if not line.startswith("- ["):
            continue
        match = TASK_RE.match(line)
        if not match:
            errors.append(f"Line {line_no}: checkbox task is missing T### ID")
            continue
        ids.append(match.group(1))

    expected = [f"T{i:03d}" for i in range(1, len(ids) + 1)]
    if ids != expected:
        errors.append(f"Task IDs must be unique and monotonic: expected {expected}, got {ids}")

    verification_commands = extract_verification_commands(lines)
    if not verification_commands:
        errors.append("Missing commands under ## Verification Commands")

    payload = {
        "tasks_path": str(path),
        "task_count": len(ids),
        "verification_commands": verification_commands,
        "errors": errors,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if errors else 0


def extract_verification_commands(lines: list[str]) -> list[str]:
    in_section = False
    commands: list[str] = []
    for line in lines:
        if VERIFY_HEADING_RE.match(line):
            in_section = True
            continue
        if in_section and HEADING_RE.match(line):
            break
        if in_section:
            stripped = line.strip()
            if stripped.startswith("- `") and stripped.endswith("`"):
                commands.append(stripped[3:-1])
    return commands


if __name__ == "__main__":
    raise SystemExit(main())
