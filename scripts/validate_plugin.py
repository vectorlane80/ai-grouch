#!/usr/bin/env python3
"""Repo-level smoke checks for the ai-grouch plugin bundle."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        fail(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def load_simple_yaml(path: Path) -> dict[str, dict[str, str]]:
    try:
        lines = path.read_text().splitlines()
    except FileNotFoundError:
        fail(f"missing file: {path}")

    data: dict[str, dict[str, str]] = {}
    section: str | None = None

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            if not line.endswith(":"):
                fail(f"unsupported YAML structure in {path}: {raw_line}")
            section = line[:-1]
            data[section] = {}
            continue
        if section is None:
            fail(f"unexpected indented line before section in {path}: {raw_line}")
        key, sep, value = line.strip().partition(":")
        if not sep:
            fail(f"unsupported YAML key/value in {path}: {raw_line}")
        value = value.strip()
        if value in {"true", "false"}:
            parsed = value
        elif value.startswith('"') and value.endswith('"'):
            parsed = value[1:-1]
        else:
            parsed = value
        data[section][key] = parsed

    return data


def ensure(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def main() -> None:
    plugin_manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    plugin_agent_path = ROOT / "agents" / "openai.yaml"
    skill_agent_path = ROOT / "skills" / "ai-grouch" / "agents" / "openai.yaml"
    skill_path = ROOT / "skills" / "ai-grouch" / "SKILL.md"

    ensure(plugin_manifest_path.exists(), "missing plugin manifest")
    ensure(plugin_agent_path.exists(), "missing plugin-level agents/openai.yaml")
    ensure(skill_agent_path.exists(), "missing embedded skill agents/openai.yaml")
    ensure(skill_path.exists(), "missing embedded skill SKILL.md")

    ensure(not (ROOT / "SKILL.md").exists(), "old root SKILL.md should not exist")
    ensure(not (ROOT / "references").exists(), "old root references/ should not exist")

    manifest = load_json(plugin_manifest_path)
    plugin_agent = load_simple_yaml(plugin_agent_path)
    skill_agent = load_simple_yaml(skill_agent_path)

    interface = manifest.get("interface", {})
    ensure(manifest.get("skills") == "./skills/", 'plugin "skills" must be "./skills/"')

    manifest_text = plugin_manifest_path.read_text()
    ensure("[TODO:" not in manifest_text, "plugin manifest contains scaffold TODO placeholders")

    manifest_name = interface.get("displayName")
    manifest_desc = interface.get("shortDescription")
    manifest_prompt = interface.get("defaultPrompt")

    ensure(manifest_name == "Oscar", 'plugin interface.displayName must be "Oscar"')
    ensure(plugin_agent["interface"].get("display_name") == manifest_name, "plugin agent display_name must match manifest displayName")
    ensure(skill_agent["interface"].get("display_name") == manifest_name, "skill agent display_name must match manifest displayName")

    ensure(plugin_agent["interface"].get("short_description") == manifest_desc, "plugin agent short_description must match manifest shortDescription")
    ensure(skill_agent["interface"].get("short_description") == manifest_desc, "skill agent short_description must match manifest shortDescription")
    ensure(plugin_agent["interface"].get("default_prompt") == manifest_prompt, "plugin agent default_prompt must match manifest defaultPrompt")

    skill_prompt = skill_agent["interface"].get("default_prompt", "")
    ensure("$ai-grouch" in skill_prompt, 'skill agent default_prompt must mention "$ai-grouch"')
    ensure("Oscar" in skill_prompt, 'skill agent default_prompt must mention "Oscar"')
    ensure(skill_agent["policy"].get("allow_implicit_invocation") == "true", "skill agent must keep implicit invocation enabled")
    ensure(plugin_agent["policy"].get("allow_implicit_invocation") == "true", "plugin agent must keep implicit invocation enabled")

    print("Plugin bundle smoke check passed.")


if __name__ == "__main__":
    main()
