---
name: ship
description: Make atomic commits and push them to trunk. Use when asked to ship, commit and push to main, or make logical or atomic commits.
disable-model-invocation: true
---

Commit the changes as atomic commits, one logical change per commit, and push them to trunk, the repository's main branch. Before pushing, run the repository's checks and tests and fix any failures. After pushing, watch CI and fix any failures until it passes.
