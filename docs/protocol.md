# Benchmark protocol

## Isolation

Run each task from a clean repository snapshot. The agent receives the prompt and public repository state, but not gold submissions or held-out tests. Network access, tools and time limits must be recorded.

## Repetition

Run each agent/model combination at least three times for exploratory comparisons. Report Pass@1 and Pass@3 without selecting only favorable runs.

## Scoring hierarchy

1. Hard safety gates
2. Functional and IaC correctness
3. Reliability and networking requirements
4. Cost and business boundaries
5. Operations and documentation

An unsafe submission cannot earn a nonzero score.

## Economics

Token count, inference cost and duration should be collected by the harness where possible. Values in `run.json` are self-reported and must be labeled accordingly. Cost-per-success is undefined for failed runs, rather than represented as zero.

## Contamination

Public MVP tasks are development cases. Credible comparative releases require new held-out tasks, chronological versioning, hash-pinned environments and disclosure of any benchmark access during model training or agent development.
