# Managing coupling

Coupling is the degree to which a change in one part forces a change in another. Some coupling is necessary, since parts must work together. Farley sees unmanaged coupling as the main limit on scaling software and the teams that build it. The goal is not zero coupling but deliberate coupling.

## Principles

- **Loose coupling between modules, high cohesion within them.**
- **Depend on abstractions, not concretions.** Depend on interfaces owned by the consumer, and point dependencies toward stable, abstract code (dependency inversion).
- **Coupling has kinds, from worst to best:**
  - *Content*: one part touches another's internals.
  - *Shared mutable state*: global variables or a shared database written by several services.
  - *Temporal*: parts must run in a fixed order or at the same time.
  - *Data structure*: parts share a large internal data model.
  - *Message/contract*: parts share only a small, explicit, versioned interface.
- **Coupling across team boundaries is the most expensive.** If teams must coordinate to release, they are coupled. Align module and service boundaries with team boundaries (Conway's law).
- **Microservices only pay off when independently deployable.** Services that must be deployed together are a distributed monolith, with the costs of both.
- **Some coupling is cheaper than the cure.** Inside one cohesive module, tight coupling is fine. Don't add indirection where nothing needs to vary independently.

## Signs of harmful coupling

- A change in one module breaks or requires changes in others.
- Services must be released in lockstep, or share a database schema.
- Tests need many collaborators set up to test one unit.
- Long chains of calls through objects (`a.getB().getC().doX()`).
- Circular dependencies.

## Techniques

- Introduce interfaces at boundaries and inject dependencies.
- Communicate across services with small, versioned contracts, and use contract tests to verify them.
- Prefer asynchronous messaging to remove temporal coupling where it fits.
- Give each service ownership of its data. Share via APIs or events, not tables.
- Use an anti-corruption layer when integrating with external or legacy models.
- Make dependency direction explicit and enforce it with architecture tests.

## Check

- Can each module or service be changed, tested, and deployed without changing others?
- What breaks if this module's internals change?
- Do any two teams need to coordinate to release?
