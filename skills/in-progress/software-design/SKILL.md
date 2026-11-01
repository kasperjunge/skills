---
name: software-design
description: Design concepts for managing complexity in software, from David Farley's Modern Software Engineering — modularity, cohesion, separation of concerns, information hiding and abstraction, coupling, testability, and controlling the variables. Use when designing or restructuring code, modules, interfaces, or services; reviewing a design; or when code is hard to change, hard to test, flaky, or tangled across boundaries.
---

# Software Design

These concepts help you manage complexity when designing software. They are drawn from David Farley's *Modern Software Engineering*. They reinforce each other: a weakness in one usually shows up in another, and code that is hard to test most often reveals it.

## Table of contents

| Concept | Read when |
|---|---|
| [Modularity](references/modularity.md) | Splitting a system into parts, or deciding where a boundary goes. |
| [Cohesion](references/cohesion.md) | Deciding what belongs together, or when one change touches many places. |
| [Separation of concerns](references/separation-of-concerns.md) | A unit does several jobs, or domain logic is mixed with I/O, UI, or infrastructure. |
| [Information hiding and abstraction](references/information-hiding.md) | Designing an interface or API, or callers depend on internals. |
| [Managing coupling](references/coupling.md) | Parts can't change, deploy, or be tested independently, or work crosses team or service boundaries. |
| [Testability](references/testability.md) | Code is hard to test, or you are using tests to judge a design. |
| [Controlling the variables](references/controlling-variables.md) | Behavior is non-deterministic, flaky, or environment-dependent, or a result has no clear cause. |
