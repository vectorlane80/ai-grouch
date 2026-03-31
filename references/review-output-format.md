# Review output format

Use this default structure unless the user asks for another format.

## Executive verdict
State one of:
- approve
- approve with caveats
- needs changes
- reject plan
- defensible but risky

Then add 2-4 sentences explaining the real reason.

## Blocking issues
List only true blockers.
For each blocker use:
- **title**
- **severity**: blocking
- **evidence**: where the issue appears
- **why it breaks**: concrete bug or risk mechanism
- **what would change my mind**: condition, test, or evidence that would disprove the objection

If none, say `none`.

## Major concerns
List important but non-blocking issues.
For each concern use:
- **title**
- **severity**: major
- **evidence**
- **impact**
- **suggested fix**

If none, say `none`.

## Minor concerns and nits
Keep brief. Split real minor issues from taste-based nits.

## What the code or plan gets right
Always include this section.
If the implementation is solid, say so plainly.
If an earlier suspicion was wrong, say that explicitly.

## Best next moves
Give the shortest path to a safer result.
Prefer a small number of high-leverage changes.

## Debate addendum
When reviewing another agent's plan or arguing with another agent, add:
- **strongest case for the other side**
- **where that case fails**
- **what evidence would resolve the disagreement**

## Codebase review addendum
For whole-repository reviews, add:
- **systemic risks**
- **hotspots worth manual inspection**
- **repeated anti-patterns**
- **areas that appear healthier than expected**
