# Knowledge work

Goldratt wrote mostly about factories and projects, but the ideas apply to software delivery and other knowledge work. *The Phoenix Project* by Gene Kim, Kevin Behr, and George Spafford retells *The Goal* in an IT department. The main difference: in knowledge work, inventory is invisible, so the constraint is harder to see.

## Making work visible

- Inventory in knowledge work is work in progress: unmerged branches, open pull requests, designs waiting for decisions, tickets "in review", features built but not released.
- Visualise the flow, for example on a board with one column per step, and look for where items wait longest.
- Measure flow: lead time, throughput (items finished per week), and work in progress.

## Common constraints

- **A person.** One expert whom many tasks depend on (Brent in *The Phoenix Project*). Exploit by protecting their time and only routing work to them that truly needs them. Elevate by spreading their knowledge.
- **Review and approval.** Code review, change approval boards, sign-offs.
- **Testing and release.** Manual testing or infrequent, risky deployments.
- **Decisions.** Work waiting for a product or leadership decision.
- **Environments.** Shared test or staging environments.
- **Demand.** The team ships faster than users adopt; the constraint is in the market, not delivery.
- **Policies.** Release windows, mandatory process steps, utilisation targets.

## Applying the focusing steps

- **Exploit:** make sure the constraint works only on the highest-value items, with good input. Cut rework and interruptions there.
- **Subordinate:** limit work in progress so work isn't started faster than the constraint can finish it. WIP limits on a board are the rope. Other people help the constraint rather than starting new work.
- **Elevate:** automate the constraint step (tests, deployment), pair to spread knowledge, or hire.

## Failure modes

- **Keeping everyone busy.** Starting new work instead of helping finish work at the constraint.
- **Optimising coding speed.** Writing code faster when the constraint is review, release, or adoption.
- **Unlimited WIP.** Many items in progress, few finished.
