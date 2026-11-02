# Separation of concerns

Each piece of code should do one thing and do it well. Farley considers this perhaps the most important design principle, because it drives modularity, cohesion, testability, and low coupling together.

## Principles

- **One concern per unit.** A function, class, or module should have one job. If describing it needs "and", it probably has two.
- **Separate essential from accidental complexity.** Essential complexity is the problem domain: business rules and policies. Accidental complexity is everything needed to run it: persistence, networking, UI, frameworks, messaging. Keep domain logic free of accidental complexity.
- **Isolate the edges.** Put I/O, frameworks, and third-party APIs behind ports and adapters (hexagonal architecture), with the domain at the center depending on nothing external.
- **Separate deciding from doing.** Pure logic computes what should happen. A thin outer layer carries it out (functional core, imperative shell).
- **Separate policy from mechanism.** What the system should do changes for business reasons. How it does it changes for technical reasons. Keep them apart.

## Signs of mixed concerns

- Business rules call the database, HTTP clients, or file system directly.
- SQL, HTML, or JSON handling appears next to domain decisions.
- A function both computes a result and logs, persists, or sends it.
- Testing a business rule requires a database, network, or UI.
- Framework annotations or types leak into the domain model.

## Techniques

- Extract pure functions for calculations and decisions. Pass data in and return data out.
- Define interfaces (ports) in the domain's own language for what it needs from the outside, and implement them in adapters.
- Use dependency injection to supply adapters at the edges.
- Translate external data formats at the boundary into domain types.

## Check

- Can the domain logic be run and tested without any infrastructure?
- Could you swap the database, UI, or framework without touching business rules?
- Does each unit have one reason to change?
