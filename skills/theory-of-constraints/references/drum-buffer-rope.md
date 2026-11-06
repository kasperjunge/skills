# Drum-buffer-rope

Drum-buffer-rope (DBR) is Goldratt's method for scheduling a system around its constraint. It puts steps 2 and 3 of the [five focusing steps](five-focusing-steps.md) into practice.

## The three parts

- **Drum:** the constraint sets the pace of the whole system. Its schedule is the only detailed schedule needed.
- **Buffer:** a time buffer in front of the constraint, so it always has work ready even when upstream steps are late. The buffer protects the constraint from variation.
- **Rope:** a signal that ties the release of new work to the constraint's pace. New work enters the system only when the constraint consumes work, so work in progress doesn't build up.

In *The Goal*, the scouts tie a rope between Herbie at the front and the leader, so the troop can't spread out.

## Simplified DBR

When the market is the constraint, which is common once internal constraints are under control, the drum is customer demand and the buffer protects delivery dates. Work is released a fixed time before it is due, and the shipping buffer is what gets managed.

## Buffer management

The buffer is also the main source of information about the system.

- Divide each buffer into three zones: **green**, **yellow**, and **red**.
- If work arrives at the constraint while its buffer is green, everything is fine.
- If it is in yellow, check what is happening and prepare to act.
- If it is in red, expedite.
- Record why each buffer penetrated into red. The most frequent causes show where to improve next.
- If buffers are almost never consumed, they are too large and can be reduced. If they are often red, they are too small or the system is overloaded.

## Failure modes

- **Releasing work early to keep people busy.** Breaks the rope and floods the system with work in progress.
- **Detailed schedules for every step.** Only the drum needs one.
- **Buffers without buffer management.** The buffer is set once and never used as a signal.
