# The five focusing steps

Goldratt's process of ongoing improvement. Start by stating the goal and how it is measured; see [The goal and its measures](goal-and-measures.md).

## 1. Identify the constraint

Find the one thing that limits the system's progress toward its goal.

- Look for where work queues. Work piles up in front of the constraint, and steps after it wait.
- Look at what everyone is waiting on, expediting, or arguing about.
- Check the market. If the system can produce more than it can sell, the constraint is demand, not capacity.
- Check policies. A rule, a measure, or an approval step can be the constraint even when all resources have spare capacity.

There is usually one constraint at a time. If there seem to be many, look for the one that the others are waiting on.

## 2. Exploit the constraint

Get the most out of the constraint with what you already have, before spending money.

- Make sure it never sits idle: no waiting for input, no breaks in hand-offs.
- Make sure it only works on things that produce throughput, not on rework, defects, or low-value work.
- Move work that doesn't need the constraint to other resources.
- Check quality before work reaches the constraint, so it doesn't waste time on bad input.

## 3. Subordinate everything else to the constraint

Make every other part of the system serve the constraint's pace, even if that means they are less busy.

- Release work into the system at the rate the constraint can handle, not faster. See [Drum-buffer-rope](drum-buffer-rope.md).
- Prioritise work that feeds the constraint.
- Accept idle time at non-constraints. Spare capacity there is what protects the constraint from variation.

This step is usually the hardest, because it goes against local measures that reward everyone for being busy.

## 4. Elevate the constraint

If exploiting and subordinating isn't enough, increase the constraint's capacity: hire, buy, automate, outsource, or redesign. Do this only after steps 2 and 3, because they are cheaper and often enough.

## 5. Repeat, and don't let inertia become the constraint

When the constraint is broken, another part of the system becomes the constraint. Go back to step 1. The policies created to manage the old constraint may now be in the way. Goldratt's warning: don't let inertia, the rules that made sense for the previous constraint, become the system's constraint.

## Failure modes

- **Skipping to elevate.** Buying capacity before exploiting what exists.
- **Improving everywhere at once.** Spreading effort across all steps, most of which don't limit the system.
- **Forgetting to subordinate.** Exploiting the constraint while the rest of the system keeps flooding it with work.
- **Not noticing the constraint has moved.** Continuing to optimise the old constraint after it stopped being one.
