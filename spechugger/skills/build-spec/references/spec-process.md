# Spec Process

Use this process after `research.md` is complete. The purpose is to translate the user's intent and repository facts into a proposed end state.

## Before Drafting

Review `research.md` and classify open questions:

- **Blocking**: the answer materially changes goals, behavior, data model, interfaces, or acceptance criteria.
- **Non-blocking**: the answer can be decided during planning or implementation without changing the user's desired outcome.

Ask the user only the blocking questions. Keep questions concrete and explain why the answer changes the spec. If the user's answers reveal more blocking ambiguity, keep asking focused follow-up questions until the spec can be drafted without guessing on material behavior.

## Drafting The Spec

The spec should describe the desired result, not the implementation plan. Include enough implementation constraints to keep the later plan grounded in repository reality.

Use this structure:

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

## Review Checkpoint

Before treating `spec.md` as final, present a concise proposed spec summary to the user:

- Problem.
- Goals.
- Non-goals.
- Key requirements.
- Acceptance criteria.
- Important constraints from research.

Ask whether it aligns with what they want. If the user changes direction, update the spec before moving on.

If the user explicitly asked for fully autonomous artifact generation, write the proposed `spec.md` and label it as needing review in the final response instead of waiting.

## Spec Quality Rules

- Requirements must be testable.
- Acceptance criteria must describe observable outcomes.
- Non-goals should prevent scope creep.
- Constraints should reference observed repository facts when possible.
- References should link back to `research.md` and any user-provided ticket, document, or source text.
- Do not include unresolved blocking questions in a finalized spec.
