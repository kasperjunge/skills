#!/usr/bin/env python3
"""Resolve Spechugger create-plan input and output paths."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", help="Path to spec.md")
    parser.add_argument("--research", help="Path to research.md")
    parser.add_argument("--output", help="Path to plan.md")
    args = parser.parse_args()

    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"Missing spec file: {spec_path}", file=sys.stderr)
        return 2

    spec_dir = spec_path.parent
    research_path = Path(args.research) if args.research else spec_dir / "research.md"
    if not research_path.exists():
        print(f"Missing research file: {research_path}", file=sys.stderr)
        return 2

    output_path = Path(args.output) if args.output else spec_dir / "plan.md"
    payload = {
        "spec_dir": str(spec_dir),
        "spec_path": str(spec_path),
        "research_path": str(research_path),
        "plan_path": str(output_path),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
