# Kasper Junge’s agent skills

A small collection of reusable instructions for working with AI agents. Each skill focuses on a specific way of thinking or working, rather than prescribing an entire process.

Use them as they are, or adapt them to how you work.

## Installation

Install with the [skills CLI](https://skills.sh/):

```bash
npx skills add kasperjunge/skills
```

Choose the skill and agent you want to install it for when prompted.

You can also read the `SKILL.md` file directly and copy it into your agent’s skill directory.

## Why these skills exist

An agent can make steady progress on an implementation without getting closer to the actual objective. Sometimes the most useful next step is not another improvement, but questioning whether we are solving the right problem.

This collection starts with a skill for doing that. The aim is to keep each skill focused, understandable, and easy to adapt.

## Skills

### [globalmaxxing](./globalmaxxing/SKILL.md)

Challenge the current approach to avoid local maxima and identify fundamentally better solutions.

Use it when you want to zoom out, question assumptions, rethink a strategy, or check whether an implementation is optimizing the wrong thing. It compares alternatives against the actual objective and recommends whether to continue, adjust, or rethink, with a concrete next step.

Example:

> Use globalmaxxing to assess this plan. Are we improving the current solution, or moving toward the best outcome?

The goal is not to force a rewrite or pivot. Sometimes the best conclusion is to keep going.

## Repository structure

Each skill lives in its own directory with a `SKILL.md` containing its description and instructions:

```text
globalmaxxing/
  SKILL.md
```

There is no required workflow or setup beyond installing the skill you want to use.
