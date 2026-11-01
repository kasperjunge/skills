# Controlling the variables

In an experiment, you control variables so a result has a known cause. Farley applies this to software: make builds, tests, environments, and deployments reproducible and deterministic, so that when something changes you know why. Without control, feedback is noise.

## Principles

- **Same input, same output.** Code, tests, and builds should behave identically every run. Non-determinism hides causes.
- **Isolate sources of variation.** Time, randomness, concurrency, network, and external services are variables. Put each behind a seam that can be fixed in tests.
- **Version everything.** Code, tests, configuration, infrastructure, schemas, and dependency versions all go in version control, so any state can be reproduced.
- **Automate repeatable processes.** Manual steps vary between runs. Automate build, test, provisioning, and deployment.
- **Keep environments consistent.** Build the artifact once and promote the same artifact through every environment. Differences between environments should be explicit configuration only.
- **Change one thing at a time.** Small, separate changes make it clear which change caused which effect.

## Signs of uncontrolled variables

- Flaky tests that pass or fail without code changes.
- "Works on my machine."
- Behavior depends on the current time, ordering of a hash map, or test execution order.
- Unpinned dependency versions or mutable base images.
- Manual configuration of servers or environments.
- Tests that share state or depend on external services.

## Techniques

- Inject a clock and a random source instead of calling system time or global randomness directly.
- Pin dependency versions and use lock files.
- Define infrastructure as code and run builds in containers or hermetic environments.
- Give each test its own isolated data and reset state between tests.
- Replace external services in tests with fakes, stubs, or contract-tested simulators.
- Make deployments idempotent and repeatable from a single pipeline.

## Check

- Will this code and its tests behave the same on every machine and every run?
- Is every input that affects behavior either passed in explicitly or versioned?
- Can you reproduce any past build or environment exactly?
