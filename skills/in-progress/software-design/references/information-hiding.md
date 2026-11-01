# Information hiding and abstraction

Hide each design decision that is likely to change behind an interface, so the rest of the system cannot depend on it (Parnas). Abstraction is the other half: present a simpler model of the problem so callers think in terms of what, not how.

## Principles

- **Hide decisions, not just data.** Data formats, algorithms, storage choices, and third-party libraries are decisions. Each one should be known to exactly one module.
- **Design interfaces from the caller's point of view.** Express what the caller needs in domain terms, not what the implementation happens to do.
- **Prefer deep modules.** A small interface over a lot of functionality hides more complexity than a large interface over a little (Ousterhout).
- **Abstractions should model the problem, not the technology.** `OrderRepository.save(order)` hides storage. `SqlHelper.execute(query)` exposes it.
- **Don't abstract speculatively.** An abstraction with one implementation and no expected variation adds indirection without hiding anything. Abstract when a decision is likely to change or when it simplifies the caller.
- **Leaky abstractions are coupling.** If callers must know implementation details to use an interface correctly, those details are not hidden.

## Signs of poor information hiding

- Callers reach into internal structures, or get and set fields to make decisions the object should make.
- Changing a data format, library, or storage engine ripples through many modules.
- Interfaces return framework or vendor types.
- Many tiny pass-through methods or layers that add no simplification (shallow modules).
- Callers must call methods in a specific undocumented order.

## Techniques

- Tell objects what to do instead of asking for their data (tell, don't ask).
- Return domain types, not library types, from public interfaces.
- Wrap third-party APIs in an adapter that speaks your domain's language.
- Make fields and helpers private by default. Widen visibility only with a reason.
- Name interfaces after their role in the domain.

## Check

- Which design decisions are likely to change, and is each one hidden in a single module?
- Can a caller use the interface correctly without reading its implementation?
- Does the abstraction make the caller's code simpler?
