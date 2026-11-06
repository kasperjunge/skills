# Kasper Junge’s agent skills

A small collection of reusable instructions for working with AI agents. Each skill focuses on a specific way of thinking or working, rather than prescribing an entire process.

Use them as they are, or adapt them to how you work.

## Installation

Install with the [skills CLI](https://skills.sh/):

```bash
npx skills add kasperjunge/skills
```

Choose the skill and agent you want to install it for when prompted.

You can also read the `SKILL.md` file directly and copy the skill's directory into your agent’s skill directory.

## Why these skills exist

An agent can make steady progress on an implementation without getting closer to the actual objective. Sometimes the most useful next step is not another improvement, but questioning whether we are solving the right problem.

Most skills here give the agent a well-known concept to reason with, such as Jobs To Be Done, positioning, or the Theory of Constraints. Each is drawn from its canonical sources and stands on its own. The aim is to keep each skill focused, understandable, and easy to adapt.

## Skills

### Thinking and writing

- **[globalmaxxing](./skills/globalmaxxing/SKILL.md)**: zoom out and look for a fundamentally better approach than the current one. Use it when iteration yields diminishing returns, or the work may be optimizing a proxy instead of the real goal.
- **[plain-english-standard](./skills/plain-english-standard/SKILL.md)**: a writing standard for simple, direct, jargon-free plain English. Use it when writing or reviewing docs, specs, reports, PR descriptions, or messages.

### Product

- **[jtbd](./skills/jtbd/SKILL.md)**: Jobs To Be Done, from Clayton Christensen and Bob Moesta. Use it to reason about why customers buy, switch, or stop using a product.
- **[positioning](./skills/positioning/SKILL.md)**: product positioning, from April Dunford's *Obviously Awesome* and *Sales Pitch*. Use it to decide how a product is positioned, which market category to compete in, and what messaging and sales narratives should build on.

### Leadership

- **[strategy-kernel](./skills/leadership/strategy-kernel/SKILL.md)**: Richard Rumelt's strategy kernel: diagnosis, guiding policy, and coherent actions. Use it to craft or review a strategy, plan, or roadmap.
- **[vision](./skills/leadership/vision/SKILL.md)**: organizational vision, from Jim Collins and Jerry Porras: core values, core purpose, BHAGs, and vivid descriptions.
- **[okrs](./skills/leadership/okrs/SKILL.md)**: Objectives and Key Results, from John Doerr's *Measure What Matters*. Use it to write, review, track, or grade OKRs.
- **[flywheel](./skills/leadership/flywheel/SKILL.md)**: Jim Collins's flywheel. Use it to design or review how a business or team builds momentum, or to understand why growth compounds or stalls.
- **[theory-of-constraints](./skills/theory-of-constraints/SKILL.md)**: Eliyahu Goldratt's Theory of Constraints: the five focusing steps, drum-buffer-rope, the thinking processes, and critical chain. Use it when work is slow or stuck, or to decide where to improve a system, team, or pipeline.

### Engineering

- **[software-design](./skills/software-design/SKILL.md)**: concepts for managing complexity, from David Farley's *Modern Software Engineering*. Use it when designing or restructuring code, or when code is hard to change or test.
- **[gherkin](./skills/gherkin/SKILL.md)**: Gherkin and Behaviour-Driven Development, from the Cucumber reference and *The BDD Books*. Use it to write or review `.feature` files and acceptance criteria. Includes a validator script.
- **[ship](./skills/ship/SKILL.md)**: make atomic commits, push them to trunk, and watch CI until it passes. Runs only when invoked explicitly.

## Repository structure

Each skill lives in its own directory under `skills/`, with a `SKILL.md` containing its description and instructions. Leadership skills are grouped under `skills/leadership/`.

Concept skills follow the same layout:

```text
skills/positioning/
  SKILL.md        # overview and a table of concepts, each with when to read it
  references/     # one file per concept
  record/         # optional: structure and templates for a durable record
  scripts/        # optional: tools such as validators
```

There is no required workflow or setup beyond installing the skill you want to use.
