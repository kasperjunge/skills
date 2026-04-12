#!/usr/bin/env python3
"""Resolve Spechugger create-tasks input and output paths."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", help="Path to plan.md")
    parser.add_argument("--spec", help="Path to spec.md")
    parser.add_argument("--research", help="Path to research.md")
    parser.add_argument("--output", help="Path to tasks.md")
    args = parser.parse_args()

    plan_path = Path(args.plan)
    if not plan_path.exists():
        print(f"Missing plan file: {plan_path}", file=sys.stderr)
        return 2

    spec_dir = plan_path.parent
    spec_path = Path(args.spec) if args.spec else spec_dir / "spec.md"
    if not spec_path.exists():
        print(f"Missing spec file: {spec_path}", file=sys.stderr)
        return 2

    research_path = Path(args.research) if args.research else spec_dir / "research.md"
    payload = {
        "spec_dir": str(spec_dir),
        "plan_path": str(plan_path),
        "spec_path": str(spec_path),
        "research_path": str(research_path) if research_path.exists() else None,
        "tasks_path": str(Path(args.output) if args.output else spec_dir / "tasks.md"),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
