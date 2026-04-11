# Project Instructions

## What this is

Kasper Junge's personal registry of agent skills. Each skill is a folder containing a `SKILL.md` that defines a repeatable workflow a coding agent can follow. Skills follow the [Agent Skills open standard](https://agentskills.io) and are distributed via [agr](https://github.com/computerlovetech/agr) as `kasperjunge/skills/<skill-name>`.

## Layout

- `<skill-name>/SKILL.md` — top-level skill. Frontmatter `name:` must match the directory name.
- `development/<skill-name>/` — skills grouped under the `development` category (same `SKILL.md` structure, but nested one level deeper).
- `README.md` — the public index of skills in this repo.

## Keep README.md up to date

**When you add, remove, or rename a skill, update `README.md` in the same change.** The README is how people browsing on GitHub — and anyone running `agr add kasperjunge/<skill-name>` — discover what lives here. Before committing, check that every skill folder has a corresponding README entry and every README entry points to a folder that still exists.
