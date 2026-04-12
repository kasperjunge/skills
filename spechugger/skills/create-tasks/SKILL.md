---
name: create-tasks
description: Create a Spechugger tasks.md checklist from plan.md, spec.md, and optional research.md. Use after create-plan to generate ordered T001-style markdown checkbox tasks for a single-worker Ralph implementation loop.
---

# Create Tasks

Turn Spechugger planning artifacts into one canonical `tasks.md` checklist. `tasks.md` is the source of truth for implementation progress.

## Inputs

- Path to `plan.md`.
- Path to `spec.md`, normally beside `plan.md`.
- Optional path to `research.md`.

If the user provides only `plan.md`, look for `spec.md` and `research.md` in the same directory.

## Scripted Input Resolution And Validation

Use the bundled resolver before reading artifacts:

```bash
python3 <skill-dir>/scripts/resolve_inputs.py <path-to-plan.md>
```

Options:

- `--spec <path>`: explicit `spec.md`.
- `--research <path>`: explicit `research.md`.
- `--output <path>`: explicit `tasks.md` output.

The resolver validates required inputs and prints JSON with `spec_dir`, `plan_path`, `spec_path`, optional `research_path`, and `tasks_path`.

After writing `tasks.md`, validate it:

```bash
python3 <skill-dir>/scripts/validate_tasks.py <path-to-tasks.md>
```

Fix validation errors before reporting completion.

## Workflow

1. Run `scripts/resolve_inputs.py` to resolve and validate artifact paths.
2. Read `spec.md`, `plan.md`, and `research.md` if present in full from the script-reported paths.
3. Extract phases, dependencies, known files, and verification commands.
4. Generate tasks ordered so one worker can pick the first unchecked eligible task.
5. Mark tasks as `[P]` only when they touch separate files and have no dependency on another incomplete task.
6. Write `tasks.md` to the script-reported `tasks_path`.
7. Run `scripts/validate_tasks.py` and fix any errors.
8. Report task count, verification commands, and the Ralph invocation.

## Task Rules

- Use sequential IDs: `T001`, `T002`, `T003`, and so on.
- Every implementation task must have an ID.
- Include exact file paths whenever a file is known.
- Keep tasks small enough for one fresh agent context to complete.
- Put routine test commands in `## Verification Commands`, not as checklist tasks.
- Include verification tasks only when they require code or documentation changes.
- Keep dependency notes human-readable for v1; order tasks so top-to-bottom execution works.

Task line format:

```text
- [ ] T001 [P] [optional-label] Action with exact file path when known
```

Completion format:

```text
- [x] T001 [P] [optional-label] Action with exact file path when known
```

## `tasks.md` Contract

```markdown
# Tasks: <title>

**Input**: `spec.md`, `research.md`, `plan.md`
**Source of truth**: Markdown checkboxes in this file.

## Format

## Phase 1: <name>

- [ ] T001 ...
- [ ] T002 [P] ...

## Phase 2: <name>

- [ ] T003 ...

## Dependencies And Execution Order

## Parallel Opportunities

## Verification Commands

## Ralph Notes
```

## Verification Commands Section

List concrete commands the Ralph should run during implementation. If the plan contains conditional or uncertain commands, resolve them from repository inspection before writing `tasks.md`, or state that manual verification is required.

Example:

```markdown
## Verification Commands

- `npm test`
- `npm run lint`
```

## Final Response

After writing the file, respond with:

```text
Created <spec-dir>/tasks.md with <N> tasks.

Run: ralph run .agents/ralphs/implement-tasks --spec-dir <spec-dir>
```
