# Bad applications

Use this as a checklist when reviewing an improvement plan or a constraint analysis.

## Traps

- **No goal.** Improvements aren't tied to what the system is for.
- **Constraint guessed, not found.** Named from the loudest complaint instead of where work queues.
- **Several "constraints".** No decision about which one limits the system now.
- **Improving non-constraints.** Effort spent on steps that don't limit output.
- **Elevating before exploiting.** Buying capacity before using the existing capacity well.
- **No subordination.** The rest of the system keeps releasing work at its own pace.
- **Local efficiency measures.** Utilisation targets that reward building inventory.
- **Balanced capacity.** Removing all spare capacity from non-constraints.
- **Compromise instead of resolution.** A conflict split down the middle instead of an assumption broken.
- **Inertia.** Policies from the previous constraint left in place after it moved.

## Review questions

1. What is the system's goal, and how is progress measured?
2. Where does work queue, and what is everyone waiting on?
3. Is the constraint physical, a policy, or the market?
4. Is the constraint ever idle, or working on things that don't produce throughput?
5. How is work released into the system, and is it tied to the constraint's pace?
6. Which improvements in the plan touch the constraint, and which don't?
7. What will become the constraint once this one is broken?

## Before and after

| Bad | Better |
|---|---|
| Hire two more developers to ship faster. | Work waits an average of four days for review. Make review the first priority for every developer, limit work in progress to six items, then measure lead time again. |
| Target 90% utilisation for every team. | Measure lead time and throughput for the whole flow; accept idle time outside the constraint. |
| Improve every step of the pipeline by 10%. | Find the step where work waits longest and improve only that step until it isn't the constraint. |
