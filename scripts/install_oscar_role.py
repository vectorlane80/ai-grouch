#!/usr/bin/env python3
"""Install or update the supported Codex oscar sub-agent role."""

from __future__ import annotations

import argparse
from pathlib import Path


ROLE_BLOCK = [
    "[agents.oscar]",
    'description = "Oscar reviewer role for severe but fair code review and planning critique."',
    'config_file = "./agents/oscar.toml"',
    'nickname_candidates = ["Oscar"]',
]

ROLE_CONFIG = '''developer_instructions = """
You are Oscar, a severe but fair reviewer.
Use the Oscar:ai-grouch skill when the task is code review, plan critique, anti-slop analysis, PR review, diff review, refactor review, or architecture criticism.
Prefer blockers first, then major issues, then minor issues.
Ground every meaningful criticism in evidence from the code, diff, plan, or repository.
If the Oscar plugin or skill is unavailable, say so plainly instead of pretending the workflow is loaded.
"""
'''


def replace_or_append_section(lines: list[str], section_name: str, new_block: list[str]) -> list[str]:
    start = None
    end = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped == f"[{section_name}]":
            start = index
            end = len(lines)
            for probe in range(index + 1, len(lines)):
                if lines[probe].startswith("[") and lines[probe].strip().endswith("]"):
                    end = probe
                    break
            break

    block = new_block + [""]
    if start is None:
        if lines and lines[-1] != "":
            lines.append("")
        return lines + block
    return lines[:start] + block + lines[end:]


def ensure_multi_agent(lines: list[str]) -> list[str]:
    start = None
    end = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "[features]":
            start = index
            end = len(lines)
            for probe in range(index + 1, len(lines)):
                if lines[probe].startswith("[") and lines[probe].strip().endswith("]"):
                    end = probe
                    break
            break

    if start is None:
        if lines and lines[-1] != "":
            lines.append("")
        return lines + ["[features]", "multi_agent = true", ""]

    section = lines[start:end]
    updated = []
    found = False
    for line in section:
        if line.strip().startswith("multi_agent"):
            updated.append("multi_agent = true")
            found = True
        else:
            updated.append(line)
    if not found:
        if updated and updated[-1] != "":
            updated.append("multi_agent = true")
        else:
            updated.insert(1, "multi_agent = true")
    if updated[-1] != "":
        updated.append("")
    return lines[:start] + updated + lines[end:]


def install(codex_home: Path, dry_run: bool) -> None:
    config_path = codex_home / "config.toml"
    agents_dir = codex_home / "agents"
    role_path = agents_dir / "oscar.toml"

    if config_path.exists():
        lines = config_path.read_text().splitlines()
    else:
        lines = []

    lines = ensure_multi_agent(lines)
    lines = replace_or_append_section(lines, "agents.oscar", ROLE_BLOCK)
    config_text = "\n".join(lines).rstrip() + "\n"

    if dry_run:
        print(f"Would write {config_path}:")
        print(config_text)
        print(f"Would write {role_path}:")
        print(ROLE_CONFIG)
        return

    agents_dir.mkdir(parents=True, exist_ok=True)
    config_path.write_text(config_text)
    role_path.write_text(ROLE_CONFIG)
    print(f"Updated {config_path}")
    print(f"Updated {role_path}")
    print("Reload Codex to register the oscar role.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", default="~/.codex")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    install(Path(args.codex_home).expanduser(), args.dry_run)


if __name__ == "__main__":
    main()
