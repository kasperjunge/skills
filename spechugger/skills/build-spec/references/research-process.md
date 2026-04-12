# Research Process

Use this process to produce `research.md`. The purpose is to document what exists, not what should change.

## Research Order

1. Read the user's request and any directly mentioned files in full.
2. Decide whether pre-research clarification would materially improve the research direction.
3. If useful, ask a small number of concrete questions before broad repository exploration.
4. After the user answers, reassess whether the answers reveal more high-impact ambiguity. Continue asking focused follow-up questions until the research direction is clear enough.
5. Inspect repository structure and relevant configuration.
6. Find likely implementation surfaces with `rg`, `rg --files`, and targeted file reads.
7. Trace integration points, call sites, data flow, tests, and verification commands.
8. Record facts with file paths and line numbers.
9. Mark inference explicitly.
10. Capture unresolved questions without answering them by assumption.

## Pre-Research Clarification

Before researching broadly, pause and decide whether a clarifying question would change what you inspect.

Ask before research when the answer would affect:

- Which product area, package, service, or user flow to investigate.
- Whether the request is a bug fix, feature, refactor, migration, or cleanup.
- Which users, platforms, environments, or integrations matter.
- Which constraints are hard requirements, such as compatibility, deadlines, API stability, or data preservation.
- Which source artifact is authoritative when the user provided conflicting context.

Do not ask before research when:

- The likely code area is obvious and the question can be answered by repository inspection.
- The answer would only affect implementation details later.
- The user explicitly asked for autonomous progress and the ambiguity is low-risk.

If asking, keep each round short. Prefer one to three questions, each tied to why it changes the research. After the user answers, evaluate whether the answer creates another material question. Continue with follow-up rounds until no remaining ambiguity would substantially change what you research.

Stop asking and begin research when:

- The remaining ambiguity can be resolved by inspecting the repository.
- The remaining ambiguity can safely be deferred to spec drafting, planning, or implementation.
- Additional questions would only refine preferences without changing the research target.

## Boundaries

- Do not propose behavior in `research.md`.
- Do not critique the implementation unless the user's request is explicitly diagnostic.
- Do not collapse uncertainty into a requirement.
- Do not rely on old docs when repository inspection can verify the current state.

## Useful Research Targets

- Existing commands in `package.json`, `pyproject.toml`, `justfile`, `Makefile`, CI files, or similar.
- Nearby tests and fixtures.
- Existing naming, error handling, configuration, logging, and dependency patterns.
- Public APIs, CLI flags, routes, schemas, database migrations, generated files, and build outputs.
- Ownership boundaries between packages, apps, services, or modules.

## Output Guidance

`research.md` must answer: "What did we learn from the repository that should constrain the spec?"

Use this structure:

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

In `Open Questions`, separate:

- Questions that must be answered before writing a useful spec.
- Questions that can safely be deferred to planning or implementation.
