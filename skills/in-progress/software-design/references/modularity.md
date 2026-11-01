# Modularity

A system is modular when it is made of parts that can be understood, changed, tested, and deployed independently. Modularity limits how much of the system anyone has to hold in their head at once, and it is what makes incremental change possible.

## Principles

- **A module is defined by its interface, not its size.** It can be a function, a class, a package, or a service. It counts as a module if it can be used through a small, stable surface without knowing its internals.
- **Draw boundaries around reasons to change.** Group code by the decisions it embodies (a business rule, a data format, an external system), so that a change to one decision stays inside one module.
- **Prefer boundaries from the problem domain.** Modules like `billing` or `inventory` outlast modules like `utils`, `helpers`, or `managers`, which collect unrelated code.
- **Modularity is fractal.** Apply the same thinking at every level: functions in a class, classes in a package, services in a system.
- **Don't distribute before you modularize.** A monolith that is modular can be split later. A distributed system that is not modular becomes a distributed monolith.

## Signs of poor modularity

- Understanding one feature requires reading many unrelated files.
- A small change forces edits across many modules, or a coordinated release.
- A module cannot be tested without starting most of the system.
- Generic catch-all modules (`common`, `shared`, `utils`) keep growing.
- Circular dependencies between modules.

## Techniques

- Start from the use cases and find the decisions most likely to change. Make each one a module.
- Give each module a single, explicit public entry point and keep everything else private.
- Enforce boundaries with the language or tooling: visibility modifiers, package rules, architecture tests.
- When a module grows hard to describe in one sentence, split it along its reasons to change.

## Check

- Can you describe each module's responsibility in one sentence?
- Can each module be tested on its own?
- Does a typical change stay inside one module?
