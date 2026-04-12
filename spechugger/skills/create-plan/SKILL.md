---
name: create-plan
description: Create a phased Spechugger implementation plan.md from a spec.md and research.md. Use after build-spec when the next step is turning specification artifacts into concrete implementation phases with file paths, scope boundaries, and verification criteria.
---

# Create Plan

Turn Spechugger `spec.md` and `research.md` artifacts into `plan.md` in the same artifact directory unless the user overrides the output path.

## Inputs

- Path to `spec.md`.
- Path to `research.md`, normally beside `spec.md`.
- Optional additional constraints from the user.

If the user provides only `spec.md`, look for `research.md` in the same directory.

## Scripted Input Resolution

Use the bundled script before reading artifacts:

```bash
python3 <skill-dir>/scripts/resolve_inputs.py <path-to-spec.md>
```

Options:

- `--research <path>`: explicit `research.md`.
- `--output <path>`: explicit `plan.md` output.

The script validates that `spec.md` and `research.md` exist and prints JSON with `spec_dir`, `spec_path`, `research_path`, and `plan_path`.

## Workflow

1. Run `scripts/resolve_inputs.py` to resolve and validate artifact paths.
2. Read `spec.md` and `research.md` in full from the script-reported paths.
3. Read any additional user-provided files or constraints.
4. Verify that open questions are resolved before finalizing. If a remaining question would change the plan, stop and ask.
5. Inspect repository files as needed to confirm paths, APIs, tests, and commands.
6. Write `plan.md` to the script-reported `plan_path` with small, independently verifiable phases.
7. Report the path and concise phase summary.

## Planning Rules

- Include exact file paths wherever known.
- Each phase must include concrete changes and verification.
- Include explicit scope boundaries and out-of-scope work.
- Include automated and manual verification criteria.
- Avoid placeholders in finalized plans.
- Prefer phases that can be verified independently and ordered by dependency.
- Do not invent missing implementation details when the spec or research leaves a material gap.

## `plan.md` Contract

```markdown
# Plan: <title>

## Overview

## Current State

## Desired End State

## Implementation Approach

## Phases

## Verification

## Risks And Mitigations

## Rollback

## Out Of Scope

## References
```

## Phase Guidance

For each phase under `## Phases`, include:

- Purpose.
- Concrete file changes.
- Dependencies on earlier phases.
- Automated verification commands.
- Manual verification checks when applicable.

## Final Response

After writing the file, respond with:

```text
Created <spec-dir>/plan.md with <N> phases.

Next: run $create-tasks <spec-dir>/plan.md
```
