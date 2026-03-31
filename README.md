# AI Grouch

AI Grouch is a Codex skill bundle for hard-nosed code review, plan critique, and anti-slop analysis.

It packages a single reviewer persona, "Oscar", who starts skeptical, looks for real defects instead of style theater, and challenges weak reasoning in code, diffs, pull requests, architecture plans, and full repositories.

## What This Skill Does

AI Grouch helps Codex:

- review code for correctness, regression risk, edge cases, and maintenance hazards
- challenge plans and architecture proposals with concrete failure modes
- detect AI-shaped code smells such as fake abstractions, pseudo-generic helpers, and hand-wavy correctness
- format review output in a consistent, evidence-based structure

The skill is opinionated about one thing: criticism must be grounded in evidence. It should be severe but fair, and it should reverse course quickly when the code or plan is actually solid.

## Bundle Contents

- `SKILL.md`: the main skill instructions and trigger description
- `agents/openai.yaml`: UI metadata and default invocation prompt for the Oscar reviewer persona
- `references/anti-slop-checklist.md`: targeted prompts for finding AI slop and shallow abstractions
- `references/planning-debate-guide.md`: guidance for attacking or defending plans and design proposals
- `references/review-output-format.md`: the default output structure for reviews

## How To Use It

Install or place the `ai-grouch` folder where Codex can discover skills, then invoke it explicitly when you want a skeptical review pass.

Example prompts:

- `Use $ai-grouch to review this PR for real blockers, not style nits.`
- `Use $ai-grouch to challenge this rollout plan and identify the hidden assumptions.`
- `Use $ai-grouch to inspect this refactor for AI slop and fake abstractions.`
- `Use $ai-grouch to review this repository and focus on the highest-risk modules first.`

## Best Fit

Use AI Grouch when you want:

- pre-merge code review
- design review or planning debate
- second-pass critique of another agent's proposal
- whole-repo review focused on hotspots instead of broad summaries
- a reviewer that separates blockers from nits and explains why something is actually risky

It is less useful when you want friendly coaching, broad brainstorming, or style-only feedback.

## Validation

This repo validates as a skill bundle with the Codex `skill-creator` validator.

Example:

```bash
python3 -m venv .venv-skillvalidate
.venv-skillvalidate/bin/pip install PyYAML
.venv-skillvalidate/bin/python /Users/charlie/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Repository Purpose

This repository is the source for the skill bundle itself. It is not a software library or application runtime; it exists so the skill can be versioned, reviewed, and shared as a reusable Codex skill.
