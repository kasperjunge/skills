# Constraints record

A durable record of the system, its current constraint, and how the constraint has moved over time.

```
theory-of-constraints/
├── README.md                     # the system: goal, measures, flow, current constraint
├── constraints/
│   └── <yyyy-mm-dd>-<constraint>.md  # one per constraint, through the focusing steps
└── clouds/
    └── <conflict>.md             # optional: evaporating clouds for policy conflicts
```

Each constraint file records how it was identified and what was done at each focusing step. When a constraint is broken, close its file and start a new one. The history shows how the constraint moved.

Templates are a starting point: add, drop, or rename sections to fit what you learn.

- [System](templates/system.md)
- [Constraint](templates/constraint.md)
- [Evaporating cloud](templates/cloud.md)

After creating a record, offer to add it to the [Strategic Context](templates/strategic-context.md).
