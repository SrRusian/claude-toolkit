#!/usr/bin/env python3
"""Self-check for the claude-toolkit repository.

Run from anywhere:  python scripts/check.py
Exit code 0 when everything passes, 1 otherwise. Uses only the standard library.

Checks:
  - marketplace.json and every plugin manifest (names, sources, semver, README and docs coverage)
  - every SKILL.md (name equals folder, description starts with "Use", length, linked references)
  - evals.json exists, is valid and matches its skill
  - Markdown links and anchors in README, docs and plugins
  - style: no emojis, no em dashes, no non-English accented letters
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿⬀-⯿️]")
EM_DASH = "—"
ACCENTS = re.compile("[áéíóúñ¿¡ÁÉÍÓÚÑ]")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
TEXT_EXT = (".md", ".json", ".css", ".py", ".yml", ".yaml")
SKIP_DIRS = {".git", "node_modules"}

errors = []


def err(msg):
    errors.append(msg)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def text_files():
    for base, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.endswith(TEXT_EXT):
                yield os.path.normpath(os.path.join(base, name))


# ------------------------------------------------------------------ plugins
def check_plugins():
    path = ".claude-plugin/marketplace.json"
    try:
        market = json.loads(read(path))
    except (OSError, ValueError) as exc:
        err(f"{path}: cannot read ({exc})")
        return
    readme = read("README.md")
    for plugin in market.get("plugins", []):
        name = plugin.get("name", "?")
        source = plugin.get("source", "")
        folder = os.path.normpath(source)
        manifest = os.path.join(folder, ".claude-plugin", "plugin.json")
        if not os.path.isdir(folder):
            err(f"marketplace: plugin '{name}' source '{source}' does not exist")
            continue
        try:
            data = json.loads(read(manifest))
        except (OSError, ValueError) as exc:
            err(f"{manifest}: cannot read ({exc})")
            continue
        if data.get("name") != name:
            err(f"{manifest}: name '{data.get('name')}' differs from marketplace '{name}'")
        if not SEMVER.match(str(data.get("version", ""))):
            err(f"{manifest}: version is not semver")
        if not data.get("description"):
            err(f"{manifest}: missing description")
        if f"docs/{name}.md" not in readme:
            err(f"README.md: no link to docs/{name}.md for plugin '{name}'")
        if not os.path.exists(f"docs/{name}.md"):
            err(f"docs/{name}.md: missing guide for plugin '{name}'")
    listed = {os.path.normpath(p.get("source", "")) for p in market.get("plugins", [])}
    for folder in glob.glob("plugins/*"):
        if os.path.normpath(folder) not in listed:
            err(f"{folder}: plugin folder not listed in marketplace.json")


# ------------------------------------------------------------------- skills
def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return None
    out = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return out


def check_skills():
    for skill in sorted(glob.glob("plugins/*/skills/*/SKILL.md")):
        folder = os.path.dirname(skill)
        slug = os.path.basename(folder)
        text = read(skill)
        fm = frontmatter(text)
        if fm is None:
            err(f"{skill}: missing frontmatter")
            continue
        if fm.get("name") != slug:
            err(f"{skill}: name '{fm.get('name')}' differs from folder '{slug}'")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug):
            err(f"{skill}: folder name is not kebab-case")
        desc = fm.get("description", "")
        if not desc.startswith("Use"):
            err(f"{skill}: description should start with 'Use'")
        if len(desc) > 1024:
            err(f"{skill}: description is longer than 1024 characters")
        for target in glob.glob(folder + "/references/*") + glob.glob(folder + "/assets/*"):
            if os.path.basename(target) not in text:
                err(f"{skill}: '{os.path.basename(target)}' is not referenced")
        evals = os.path.join(folder, "evals", "evals.json")
        if not os.path.exists(evals):
            err(f"{folder}: missing evals/evals.json")
            continue
        try:
            data = json.loads(read(evals))
        except ValueError as exc:
            err(f"{evals}: invalid JSON ({exc})")
            continue
        if data.get("skill_name") != slug:
            err(f"{evals}: skill_name '{data.get('skill_name')}' differs from '{slug}'")
        for item in data.get("evals", []):
            for key in ("id", "prompt", "expected_output", "assertions"):
                if key not in item:
                    err(f"{evals}: eval {item.get('id', '?')} lacks '{key}'")


# -------------------------------------------------------------------- links
def slug_of(heading):
    heading = re.sub(r"[`*]", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors_of(path):
    found = set()
    in_code = False
    for line in read(path).splitlines():
        if line.startswith("```"):
            in_code = not in_code
        match = None if in_code else re.match(r"#{1,6}\s+(.*)", line)
        if match:
            found.add(slug_of(match.group(1)))
    return found


def check_links():
    for md in sorted(p for p in text_files() if p.endswith(".md")):
        text = re.sub(r"```.*?```", "", read(md), flags=re.S)
        for link in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"[a-z]+:", link):
                continue
            target, _, anchor = link.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(md), target)) if target else md
            if not os.path.exists(dest):
                err(f"{md}: broken link '{link}'")
            elif anchor and dest.endswith(".md") and anchor not in anchors_of(dest):
                err(f"{md}: broken anchor '{link}'")


# -------------------------------------------------------------------- style
def check_style():
    me = os.path.normpath("scripts/check.py")
    for path in text_files():
        if path == me:
            continue
        for number, line in enumerate(read(path).splitlines(), 1):
            if EMOJI.search(line):
                err(f"{path}:{number}: emoji")
            if EM_DASH in line:
                err(f"{path}:{number}: em dash")
            if ACCENTS.search(line):
                err(f"{path}:{number}: non-English accented letter")


def main():
    check_plugins()
    check_skills()
    check_links()
    check_style()
    if errors:
        print(f"{len(errors)} problem(s):")
        for message in errors:
            print("  - " + message)
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
