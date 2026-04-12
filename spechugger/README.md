# Spechugger

Spechugger is an agr package for turning a rough implementation idea into durable markdown artifacts and then executing those tasks one at a time with a Ralph loop.

## Contents

- `build-spec` researches the target repository and writes `research.md` and `spec.md`.
- `create-plan` turns the spec and research into `plan.md`.
- `create-tasks` turns the plan into a dependency-ordered `tasks.md`.
- `implement-tasks` implements one unchecked task per Ralph iteration, verifies it, marks it complete, and commits.

The skills include small dependency-free helper scripts for mechanical work:

- `build-spec/scripts/init_artifact_dir.py` infers the owner from `git remote get-url origin`, creates the artifact directory, and prints output paths as JSON.
- `create-plan/scripts/resolve_inputs.py` resolves and validates `spec.md`, `research.md`, and `plan.md` paths.
- `create-tasks/scripts/resolve_inputs.py` resolves task-generation inputs and output path.
- `create-tasks/scripts/validate_tasks.py` checks task IDs and verification commands before handoff to the Ralph.

## Install

```bash
agr add kasperjunge/skills/spechugger
```

## Workflow

```text
/build-spec <rough idea or ticket text>
/create-plan specs/<owner>/<date-name>/spec.md
/create-tasks specs/<owner>/<date-name>/plan.md
```

Then run the Ralph with the generated spec directory:

```bash
ralph run implement-tasks --spec-dir specs/<owner>/<date-name>
```
