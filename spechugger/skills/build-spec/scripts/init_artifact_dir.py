#!/usr/bin/env python3
"""Create a Spechugger artifact directory and report its resolved paths."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Short human-readable title for the work")
    parser.add_argument("--owner", help="Owner namespace override")
    parser.add_argument("--dir", help="Artifact directory override")
    parser.add_argument("--allow-local", action="store_true", help="Use owner 'local' when git owner cannot be inferred")
    args = parser.parse_args()

    if args.dir:
        spec_dir = Path(args.dir)
        owner = args.owner or spec_dir.parent.name or "local"
        short_name = spec_dir.name
    else:
        owner = args.owner or infer_git_owner()
        if not owner:
            if not args.allow_local:
                print(
                    "Could not infer owner from git remote. Provide --owner or rerun with --allow-local.",
                    file=sys.stderr,
                )
                return 2
            owner = "local"
        short_name = slugify(args.title)
        today = dt.date.today().isoformat()
        spec_dir = Path("specs") / owner / f"{today}-{short_name}"

    spec_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "spec_dir": str(spec_dir),
        "owner": owner,
        "short_name": short_name,
        "research_path": str(spec_dir / "research.md"),
        "spec_path": str(spec_dir / "spec.md"),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


def infer_git_owner() -> str | None:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return owner_from_remote(result.stdout.strip())


def owner_from_remote(remote: str) -> str | None:
    if not remote:
        return None

    scp_like = re.match(r"^(?:[^@]+@)?[^:]+:([^/]+)/[^/]+(?:\.git)?$", remote)
    if scp_like:
        return scp_like.group(1)

    parsed = urlparse(remote)
    if parsed.scheme and parsed.path:
        parts = [part for part in parsed.path.split("/") if part]
        if len(parts) >= 2:
            return parts[-2]

    parts = [part for part in remote.split("/") if part]
    if len(parts) >= 2:
        return parts[-2]
    return None


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:60].strip("-") or "work"


if __name__ == "__main__":
    raise SystemExit(main())
