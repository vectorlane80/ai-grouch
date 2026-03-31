# Anti-slop checklist

Use this checklist when you suspect AI-shaped code or pseudo-rigorous planning.

## 1. Fake abstraction
Look for:
- helper layers with one caller and no independent value
- strategy/factory/plugin patterns with no real variation
- interfaces introduced without a second implementation need
- config knobs added without a real operational scenario

Challenge with:
- What concrete future case justifies this abstraction now?
- What becomes simpler if this layer is deleted?

## 2. Data-flow opacity
Look for:
- values renamed repeatedly across wrappers
- request/context objects passed everywhere without clear contract
- mutation spread across helpers
- hidden global state, caching, or ambient dependencies

Challenge with:
- Can the critical state transition be described in one straight line?
- Which function actually owns the invariant?

## 3. Hand-wavy correctness
Look for:
- confident names without enforcement
- comments that promise safety but code does not check it
- broad try/except or catch blocks
- default branches that silently swallow impossible states

Challenge with:
- What exact condition guarantees this is safe?
- What failure is being hidden instead of handled?

## 4. Pseudo-generic code
Look for:
- functions parameterized for cases that do not exist
- generic options that only support one real branch
- indirection whose only purpose is sounding reusable

Challenge with:
- What real second use case exists today?
- Does this generality reduce or increase clarity?

## 5. Missing edge cases
Look for:
- empty inputs
- null / none / undefined behavior
- duplicate inputs
- malformed payloads
- partial failure during multi-step work
- concurrency or reentrancy
- timeout, cancellation, retry, and rollback behavior
- version or schema mismatch

Challenge with:
- What happens on the ugliest legal input?
- What happens halfway through failure?

## 6. Framework cargo culting
Look for:
- patterns copied from tutorials without a repo-specific reason
- hooks, effects, middleware, decorators, or dependency injection used by reflex
- state management layers heavier than the problem
- lifecycle misuse

Challenge with:
- Which framework rule or lifecycle assumption matters here?
- Is this pattern solving a real repo problem or imitating a pattern?

## 7. Weak tests
Look for:
- snapshot tests standing in for behavior checks
- mocks that duplicate implementation logic
- happy-path-only coverage
- assertions that prove execution happened but not correctness
- missing regression tests for risky paths

Challenge with:
- What bug would still pass these tests?
- Which invariant is not actually asserted?

## 8. Performance theater
Look for:
- caching before measurement
- batching or memoization without hotspot evidence
- async or concurrency used for prestige rather than need
- N+1, repeated parsing, repeated allocation, or repeated I/O hidden behind helpers

Challenge with:
- What is the actual bottleneck?
- What complexity or latency cost was added for speculative performance?

## 9. Operational blindness
Look for:
- missing logging where diagnosis matters
- missing metrics around risky flows
- no feature flag or rollback path for risky changes
- migration steps with no validation or backout plan

Challenge with:
- How will the team know this broke?
- How will they recover safely?

## 10. Planning slop
Look for:
- plans that assume implementation details away
- sequencing that ignores prerequisites
- rollout plans without rollback
- architecture diagrams that hide ownership or migration pain
- debate positions that sound strong but lack constraints

Challenge with:
- What unstated constraint kills this plan?
- What missing prerequisite turns this into rework?

## When to reverse course
If the code or plan is actually disciplined, say so.
Signals of quality:
- direct data flow
- clear invariants
- focused abstractions
- boring but correct error handling
- tests that exercise the real risk
- names that match behavior
- operational paths considered honestly
