---
name: build-spec
description: Research a codebase from a rough implementation idea, ticket, bug report, or initial spec, then create Spechugger research.md and spec.md artifacts under specs/<owner>/<date-name>/. Use before create-plan for larger coding work that needs durable specification artifacts.
---

# Build Spec

Turn a rough implementation request into two files:

- `research.md`: observed repository facts, patterns, integration points, tests, and unresolved questions.
- `spec.md`: desired end state, requirements, acceptance criteria, constraints, and references.

Keep a clear boundary between research and specification. Research documents the current repository. The spec proposes the desired future behavior.

## Inputs

- A rough idea, ticket, bug description, initial spec, or user constraints.

## Artifact Directory

Default path:

```text
specs/<owner>/<YYYY-MM-DD-short-name>/
```

Use the current local date for `YYYY-MM-DD`. Build `short-name` as a concise kebab-case summary of the work.

Choose `<owner>` this way:

1. Use an explicit owner namespace from the user when provided.
2. Otherwise infer the GitHub owner from `git remote get-url origin` when possible.
3. If no owner can be inferred, ask the user for an owner namespace. Use `local` only if the user accepts that fallback.

If the user provides an artifact directory override, use it exactly.

## Scripted Setup

Use the bundled script to create and report the artifact directory before writing files:

```bash
python3 <skill-dir>/scripts/init_artifact_dir.py "<short title>"
```

Options:

- `--owner <owner>`: explicit owner namespace.
- `--dir <path>`: exact artifact directory override.
- `--allow-local`: use `local` when the git owner cannot be inferred.

The script reads `git remote get-url origin`, extracts the GitHub owner when possible, creates the directory, and prints JSON with `spec_dir`, `research_path`, and `spec_path`. If owner inference fails, ask the user for an owner namespace unless they already accepted the `local` fallback.

## Workflow

1. Run `scripts/init_artifact_dir.py` to create the artifact directory and resolve output paths.
2. Read [research-process.md](references/research-process.md).
3. Before broad repository exploration, decide whether clarifying questions would materially improve the research direction. Ask focused questions if useful, and keep asking follow-ups while the answers reveal more high-impact ambiguity.
4. Research the repository and write `research.md` to the script-reported path.
5. Review `research.md` for open questions.
6. If any open question would materially change the spec, ask the user before drafting the final spec.
7. Read [spec-process.md](references/spec-process.md), then draft a proposed `spec.md` from the user's request and the research.
8. Present the proposed spec summary to the user and ask whether it aligns with what they want.
9. If the user confirms or gives adjustments, write the final `spec.md` to the script-reported path. If the user explicitly requested autonomous generation, write `spec.md` immediately and label it as needing review.
10. Report the file paths and a short summary.

## Research Rules

- Follow [research-process.md](references/research-process.md).
- Use web search only when the user explicitly asks for external information or the task depends on current external facts.

## `research.md` Contract

```markdown
# Research: <title>

## Research Question

## Summary

## Detailed Findings

## Existing Patterns

## Testing And Verification

## Code References

## Open Questions
```

## `spec.md` Contract

```markdown
# Spec: <title>

## Problem

## Goals

## Non-Goals

## Users And Use Cases

## Requirements

## Acceptance Criteria

## Constraints

## References
```

Requirements must be testable. Acceptance criteria must describe observable outcomes. Non-goals should prevent scope creep. References should link to `research.md` and any source ticket, file, or user-provided text.

## Final Response

After writing the files, respond with:

```text
Created Spechugger artifacts in <spec-dir>:
- research.md: <one-line summary>
- spec.md: <one-line summary>

Next: run create-plan <spec-dir>/spec.md
```
