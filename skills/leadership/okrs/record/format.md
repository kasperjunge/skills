# OKR format

A durable record of one year's OKRs in a single file with a fixed, checkable format.

## Filename

`okrs-<yyyy>.md`, for example `okrs-2027.md`. One file per year. Place it wherever fits the project.

## Format

Copy the [template](template.md) and fill it in.

## Rules

1. **Title.** The first line is exactly `# OKRs <yyyy>`. The year matches the filename.
2. **Status.** The next line is `Status: draft`, `Status: active`, or `Status: closed`. See [Status](#status). Nothing else sits between the title and the first objective.
3. **Objective heading.** `## O<id>: <title>`. Every objective uses `##`, at any depth.
4. **Nesting.** The ID carries the depth: `O1.2` is a sub-objective of `O1`, and `O1.2.3` of `O1.2`. Any depth is allowed. The parent must exist. See [Sub-objectives](#sub-objectives).
5. **Order.** Objectives appear depth-first in ID order: `O1`, `O1.1`, `O1.1.1`, `O1.2`, `O2`.
6. **Owner.** Required, directly under the heading: `Owner: <name>`. Name the one person accountable for the objective.
7. **Description.** Required, after the owner. One or more plain paragraphs. Inline links are fine. No lists, tables, quotes, or code blocks.
8. **Key results.** A list directly after the description. Each item is `- KR<objective id>.<n>: <text>`. A long key result continues on indented lines.
9. **Result and score.** When the status is `closed`, every key result has exactly two sub-bullets, in this order: `- Result: <what was achieved>` and `- Score: <0.0 to 1.0>`. In any other status they are not allowed. No other sub-bullets are allowed.
10. **Nothing else.** An objective holds a heading, an owner, a description, and key results. No notes after the key results and no other headings.
11. **Counts.** 1 to 5 top-level objectives, at most 5 sub-objectives per objective, and 1 to 5 key results per objective.
12. **IDs.** Numbers are unique and ascending among siblings. Gaps are allowed, so IDs stay stable when an OKR is stopped.
13. **Language.** `OKRs`, `Status` and its values, `O`, `KR`, `Owner`, `Result`, and `Score` are fixed. All other text can be in any language.

When a key result has a separate target per person or team, write one key result for each.

## Status

| Status | Meaning | Placeholders | Result and score |
|---|---|---|---|
| `draft` | The OKRs are being written. | Allowed, reported as warnings. | Not allowed. |
| `active` | The OKRs are agreed and the year is running. | Errors. | Not allowed. |
| `closed` | The year is over and the OKRs are graded. | Errors. | Required on every key result. |

A placeholder is text in square brackets that is not a link, such as `[number]`. Use placeholders in a draft for values not yet decided.

A closed key result looks like this:

```markdown
- KR1.1: Monthly recurring revenue reaches 200,000 by 31 December 2027.
  - Result: 140,000.
  - Score: 0.7
```

Score as described in [Tracking](../references/tracking.md).

## Sub-objectives

A sub-objective is a narrower objective that contributes to its parent objective. It has its own owner, description, and key results.

The term is this skill's own. It differs from cascading in [Alignment](../references/alignment.md), where a key result at one level becomes the objective of the team or person below. A sub-objective hangs under an objective, not under a key result.

## Not in the format yet

- **Quarterly OKRs.** For simplicity, this skill records annual OKRs only for now. Quarterly OKRs will be supported in a future release.
- **Committed and aspirational.** [Stretch](../references/stretch.md) says to label each OKR as committed or aspirational. The format has no field for the label yet, and a future release might add one. Until then, state it in the objective's description when it matters.
- **Teams.** An objective has one owner, a person. There is no field for a team.

## Check

Run the check after every edit and fix all errors:

```
python3 scripts/check_okrs.py <path>/okrs-<yyyy>.md
```

The script path is relative to this skill's directory. It prints each error with its line number and exits with 1 if there are errors. Warnings do not fail the check.
