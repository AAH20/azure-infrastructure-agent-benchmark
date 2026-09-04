# Task authoring

A task must be independently solvable from the supplied prompt and repository state. Avoid trivia and keyword-only expectations when a structural validator is practical.

Required artifacts:

```text
task-name/
├── task.json
├── prompt.md
└── submissions/
    ├── gold/
    └── unsafe/
```

Every check declares a stable identifier, domain, points, target path, expectation and human-readable reason. Safety-critical constraints use `hard_gate: true`.

Before contribution:

1. Confirm the gold submission passes.
2. Confirm the unsafe submission fails for the intended reason.
3. Compile or validate IaC where tooling permits.
4. Remove customer identifiers and secrets.
5. Record provenance and licensing.
6. Avoid unverifiable cost claims.

The MVP regex evaluator is transparent but shallow. Later task versions should prefer AST, Terraform-plan, Azure deployment what-if and network-graph assertions.
