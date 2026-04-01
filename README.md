# AI Grouch

AI Grouch is a Codex plugin bundle with an embedded `ai-grouch` skill for severe but fair code review, plan critique, and anti-slop analysis.

Its top-level plugin surface is **Oscar**: a skeptical reviewer persona for invoking this review workflow in Codex. The embedded skill remains available as `$ai-grouch`.

## What The Bundle Does

Oscar is optimized for:

- code review across files, diffs, and pull requests
- architecture and rollout-plan critique
- anti-slop analysis of AI-shaped code and fake abstractions
- whole-repository review focused on the highest-risk paths first
- evidence-based output that separates blockers from nits

The core rule is simple: criticism must be grounded in evidence. Oscar should attack weak reasoning and hidden assumptions, not style for its own sake.

## Bundle Structure

This repository is organized as a plugin bundle:

- `.codex-plugin/plugin.json`
  - plugin manifest for the `ai-grouch` bundle
- `agents/openai.yaml`
  - plugin-level OpenAI surface metadata for the Oscar agent
- `skills/ai-grouch/SKILL.md`
  - the embedded `ai-grouch` skill instructions
- `skills/ai-grouch/agents/openai.yaml`
  - skill-level UI metadata for explicit `$ai-grouch` use as Oscar's embedded review workflow
- `skills/ai-grouch/references/`
  - supporting review references for slop detection, planning debate, and output formatting

## How To Use It

There are two intended use patterns.

Plugin/agent bundle usage:

- install the repo as a local Codex plugin
- expose it through a local marketplace entry
- invoke **Oscar** as the plugin review surface

Embedded skill usage:

- invoke `$ai-grouch` directly when you want the current agent to apply the grouch review workflow

Example prompts:

- `Use $ai-grouch to review this PR for real blockers, not style nits.`
- `Use $ai-grouch to challenge this rollout plan and identify the hidden assumptions.`
- `Use Oscar to review this code, diff, or plan with a skeptical, evidence-driven lens.`

## Native Sub-Agent Setup

As installed by itself, this plugin gives Codex a reusable Oscar review surface and an embedded review skill. It does **not** by itself register a native spawnable sub-agent role.

If you want the actual sub-agent experience, you must also install a Codex multi-agent role named `oscar`.

Manual steps:

1. Ensure the plugin is installed and enabled in Codex.
2. Ensure multi-agent is enabled in `~/.codex/config.toml`:

```toml
[features]
multi_agent = true
```

3. Add an Oscar role to `~/.codex/config.toml`:

```toml
[agents.oscar]
description = "Oscar reviewer role for severe but fair code review and planning critique."
config_file = "./agents/oscar.toml"
nickname_candidates = ["Oscar"]
```

4. Create `~/.codex/agents/oscar.toml`:

```toml
developer_instructions = """
You are Oscar, a severe but fair reviewer.
Use the Oscar:ai-grouch skill when the task is code review, plan critique, anti-slop analysis, PR review, diff review, refactor review, or architecture criticism.
Prefer blockers first, then major issues, then minor issues.
Ground every meaningful criticism in evidence from the code, diff, plan, or repository.
"""
```

5. Reload or restart Codex so the new role is registered.

With `nickname_candidates = ["Oscar"]`, spawned agents for this role should use the fixed display name `Oscar` instead of a random nickname.

## Shortcut Install

This repository also includes a helper script that writes the supported config files for you:

```bash
python3 scripts/install_oscar_role.py
```

What it does:

- ensures `multi_agent = true`
- adds or updates `[agents.oscar]` in `~/.codex/config.toml`
- writes `~/.codex/agents/oscar.toml`
- fixes the role nickname candidate to `Oscar`

It still requires a Codex reload after installation.

## Best Fit

Use AI Grouch when you want:

- pre-merge code review
- design review or planning debate
- second-pass critique of another agent's proposal
- whole-repo review focused on hotspots instead of broad summaries
- a reviewer that explains why something is risky instead of merely sounding strict

It is less useful when you want coaching, brainstorming, or style-only feedback.

## Validation

Use the repo-level smoke check first. It validates the plugin manifest, rejects scaffold placeholders, checks the Oscar metadata surfaces for alignment, and verifies the repository layout.

Example:

```bash
python3 scripts/validate_plugin.py
```

If you also want to confirm the helper installer writes valid files, run:

```bash
python3 scripts/install_oscar_role.py --dry-run
```

The embedded skill also validates with the Codex `skill-creator` validator.

Example:

```bash
python3 -m venv .venv-skillvalidate
.venv-skillvalidate/bin/pip install PyYAML
.venv-skillvalidate/bin/python /Users/charlie/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/ai-grouch
```

## Repository Purpose

This repository is the source for the plugin/agent bundle itself. It is intended to be versioned in git, then copied or installed into a local Codex plugin location for actual runtime use.
