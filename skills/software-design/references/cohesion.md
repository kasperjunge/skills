# Cohesion

Cohesion is how closely the elements of a module belong together. Farley's rule: pull unrelated things further apart, and put related things closer together. High cohesion means a change lands in one place. Low cohesion means a change is scattered, or a module changes for unrelated reasons.

## Principles

- **Things that change together live together.** Use co-change as the main test of relatedness, not technical type.
- **Group by feature or domain concept, not by technical layer, when the feature is what changes.** A `controllers/`, `services/`, `models/` split spreads one feature across three folders.
- **Cohesion and coupling are two sides of one coin.** Raising cohesion inside a module usually lowers coupling between modules.
- **Too much cohesion is also a smell.** Merging everything that is vaguely related produces god objects. Aim for the smallest unit that contains a complete idea.

## Signs of low cohesion

- One logical change needs edits in many files or modules (shotgun surgery).
- A module changes for several unrelated reasons (divergent change).
- A method uses another object's data more than its own (feature envy).
- The module's name is vague: `Manager`, `Processor`, `Handler`, `Utils`.
- Fields or methods inside a class split into groups that never touch each other.

## Techniques

- Move behavior to the data it uses.
- Split a class whose fields fall into disjoint groups.
- Organize folders by feature or bounded context.
- Use version control history to find files that always change together, then consider moving them closer.

## Check

- Does the module's name describe everything in it?
- Would a likely future change touch one module or many?
- Does every part of the module use the same core data or concept?
