# Testability

Testability is how easily a unit's behavior can be verified in isolation. Farley treats it as a design tool, not only a quality goal: code that is easy to test tends to be modular, cohesive, well-separated, well-abstracted, and loosely coupled. Code that is hard to test signals a design problem.

## Principles

- **Listen to the tests.** Test pain is design feedback. Big setup means high coupling. Many mocks mean too many dependencies. Needing to test private methods means a hidden module wants to come out.
- **Write the test first (TDD).** Writing a test first forces you to design the interface from the caller's side and to make dependencies explicit before writing the implementation.
- **Test behavior, not implementation.** Assert on observable outcomes through the public interface, so refactoring doesn't break tests.
- **Make dependencies injectable.** Anything the unit needs from outside (clock, randomness, database, network) should be passed in, so a test can supply a controlled version.
- **Prefer pure functions for logic.** Given the same input they return the same output, so they need no setup or mocks.
- **Keep tests fast.** Fast tests give fast feedback, which keeps tests run often and keeps them trusted.

## Signs of poor testability

- A unit cannot be tested without a database, network, file system, or UI.
- Test setup is longer than the test.
- Tests need many mocks, or mocks of mocks.
- Static calls, singletons, or `new` of collaborators inside business logic.
- Tests break when internals are refactored though behavior is unchanged.
- Tests are slow or flaky.

## Techniques

- Pass dependencies through constructors or parameters.
- Extract decisions into pure functions and test them directly.
- Use fakes or in-memory implementations of ports instead of heavy mocking.
- Separate the functional core from the imperative shell, and test the core thoroughly while covering the shell with a few integration tests.
- Use acceptance tests written in domain language to describe system behavior from the user's view.

## Check

- How much setup does the simplest test of this unit need?
- Can the unit be tested without infrastructure?
- Would the tests survive a refactoring that keeps behavior the same?
