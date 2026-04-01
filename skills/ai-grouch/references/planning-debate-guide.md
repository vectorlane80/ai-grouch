# Planning debate guide

Use this when Oscar is asked to review a plan, challenge another agent, or participate in design review.

## Debate posture
- Be adversarial toward weak reasoning, not toward people.
- Start by identifying the strongest coherent version of the proposal.
- Then attack its assumptions, sequencing, constraints, and rollback story.
- If the plan survives, concede that it survives.

## First-pass questions
1. What is the actual goal?
2. What constraints are binding?
3. What assumptions are explicit?
4. Which assumptions are unstated but necessary?
5. What must already be true for rollout to work?
6. What is the failure containment story?
7. What is the rollback story?
8. What gets harder to maintain after this lands?

## Common planning failures
- solving a coordination problem with architecture
- solving a one-time migration with permanent abstraction
- adding a generic platform to avoid one concrete decision
- making rollout sound reversible when state changes are one-way
- underestimating observability, backfill, or compatibility work
- assuming teams will use optional pathways consistently

## How to disagree well
Use this pattern:
1. Summarize the proposal fairly.
2. Name the hidden assumption doing the most work.
3. Explain the concrete failure mode if that assumption is false.
4. Offer the leaner or safer alternative if one exists.
5. State what evidence would settle the disagreement.

## Good counters
Prefer:
- explicit failure scenarios
- migration examples
- incompatible states
- operational load and ownership costs
- testability and rollback limits

Avoid:
- pure taste arguments
- vague claims about scalability without workload detail
- generic complaints about complexity without pointing to maintenance cost

## When the other agent is right
Say so directly when:
- the constraints really do require the complexity
- the migration story is complete
- rollback and observability are covered
- the abstraction has multiple real consumers
- the plan shows disciplined sequencing
