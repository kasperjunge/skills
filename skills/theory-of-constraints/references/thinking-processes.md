# Thinking processes

In *It's Not Luck*, Goldratt presents a set of logic tools for when the constraint is not physical but a policy, a belief, or a conflict. They answer three questions:

1. **What to change?** Find the core problem.
2. **What to change to?** Design a solution that resolves it.
3. **How to cause the change?** Plan the steps to get there.

The tools use **sufficiency logic** ("if A, then B") and **necessity logic** ("to have A, we must have B"). Every arrow is a claim that can be checked.

## Current reality tree (what to change)

- List the **undesirable effects** (UDEs): the problems people experience, stated as facts.
- Connect them with cause-and-effect arrows: "if this, then that".
- Trace down to the few causes that most UDEs share. Usually one **core problem** explains most of them, and it is often a policy or a conflict.

## Evaporating cloud (resolving conflicts)

Most core problems persist because of a conflict that people have learned to compromise on. The evaporating cloud states the conflict precisely so it can be resolved instead.

- **A:** the common objective both sides want.
- **B** and **C:** two needs, both necessary for A.
- **D** and **D′:** two conflicting actions. D is needed for B; D′ is needed for C.
- Under each arrow, list the **assumptions** that make it true ("we must have D to have B, because…").
- Find an assumption that is false or can be made false. An **injection**, a new action or condition, that breaks it resolves the conflict without compromise.

Example: A = deliver reliably; B = respond to urgent customer requests; C = keep the team focused; D = interrupt planned work for urgent requests; D′ = never interrupt planned work. Assumption under B–D: "urgent requests can only be handled by the planned team." Injection: a rotating support role.

## Future reality tree (what to change to)

- Start from the injections.
- Show with cause-and-effect logic that they turn the UDEs into desirable effects.
- Look for **negative branches**: new problems the injection could cause. Add injections to trim them.

## Prerequisite tree and transition tree (how to cause the change)

- **Prerequisite tree:** list the obstacles to implementing the injections, and for each an **intermediate objective** that overcomes it. Order them by dependency.
- **Transition tree:** detailed steps, each with the reason it is needed and the effect it should cause.

## Checking the logic

Goldratt's **categories of legitimate reservation** are questions to check any arrow: Is the statement clear? Does the cause exist? Does the cause actually lead to the effect? Is the cause enough on its own, or is another needed? Is there another cause? Does the cause predict other effects that we don't see?

## Failure modes

- **Opinions as UDEs.** "Management is bad" instead of "releases slip by three weeks on average".
- **Compromise.** Splitting the difference between D and D′ instead of breaking an assumption.
- **Skipping negative branches.** Implementing an injection without checking what it breaks.
