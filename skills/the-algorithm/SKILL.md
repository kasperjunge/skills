---
name: the-algorithm
description: Apply Elon Musk's five-step process — question requirements, delete, simplify, accelerate, then automate. Use when reviewing an overcomplicated design or workflow, challenging inherited requirements, or deciding what to remove before optimizing or automating.
---

# The Algorithm

Apply the five steps in order. Improving something that should not exist wastes effort; automating it makes the waste repeatable.

The sequence comes from Musk's engineering process, described in [Everyday Astronaut's Starbase tour and interview](https://everydayastronaut.com/starbase-tour-and-interview-with-elon-musk/). The application guidance below adapts it for agent work.

## The five steps

1. **Question every requirement.** Find its purpose and the person who can explain it. A department name or an expert's reputation is not sufficient justification.
2. **Delete unnecessary parts or processes.** Ask whether each one needs to exist at all. Musk's heuristic is that if you never need to restore anything, you probably have not pushed deletion far enough. Treat his roughly 10% add-back figure as a challenge to conservatism, not a quota.
3. **Simplify and optimize.** Improve the parts that survive deletion. Do not polish a component before deciding whether it belongs.
4. **Accelerate cycle time.** Make the remaining process faster after addressing the first three steps.
5. **Automate.** Automate the process only after establishing that it is necessary and works.

## Applying it

Start with the user's intended outcome, the current design or workflow, and the evidence that would show an improvement. Keep the scope of the user's request: a review calls for recommendations; an implementation request permits changes within its authorized scope.

Trace requirements to their rationale using the available code, documents, and conversation. Distinguish explicit constraints from assumptions. Mark missing owners or evidence as unknown; do not invent them or treat their absence as proof that a requirement is unnecessary. Questioning a constraint does not itself authorize overriding it.

For each deletion candidate, explain what purpose it currently serves, what would happen without it, and how to check the result. Prefer reversible experiments where the benefit is uncertain. In software, fewer lines alone do not prove improvement: check callers, dependencies, and required behavior. Apply the same reasoning to tests and checks; passing results alone do not show that a check has no purpose.

Once deletion and simplification are settled, measure elapsed time through the whole workflow. Target delays that affect the user's outcome. Before automating, confirm the remaining steps have clear inputs, expected outputs, and a way to detect failure. If an earlier step remains unresolved, identify what evidence would resolve it and defer dependent optimization or automation.

Report the requirements challenged, changes made or proposed, evidence for keeping what remains, and how the result was or will be checked. Scale the explanation to the task; do not manufacture changes for every step when the existing design already earns its place.
