# Contributing and maintenance

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Design workflow](design-workflow.md) · [Contributing](contributing.md)

---

## Adding or changing a skill

1. Check the catalog: if an upstream skill already does it, install that instead of copying.
2. Create `plugins/<plugin>/skills/<skill-name>/SKILL.md` (create the plugin and add it to
   `marketplace.json` if it is the first skill in that domain).
3. If it is derived from another source, check its license and record it in the plugin's
   `NOTICE.md`; keep copyright notices.
4. Write the `description` as "Use when ...", add numbered rules and a verification step, and put
   long detail in `references/`.
5. Add `evals/evals.json` (3 to 5 realistic prompts with assertions), and evaluate the skill with
   `skill-creator`.
6. Write the plugin guide `docs/<plugin>.md`, link it from the README catalog and navigation,
   bump the plugin version, then run `claude plugin validate .` and `python scripts/check.py`.

## Language

All text in this repository is in English: skills (including folder and `name` values), docs,
comments, plugin descriptions and commit messages. Skill names are English kebab-case.

## Self-check

```
python scripts/check.py
```

Verifies marketplace and plugin manifests, `SKILL.md` frontmatter (name equals folder,
description starts with "Use"), that every reference file is linked and every skill has valid
evals, all Markdown links and anchors, and the style rules (no emojis, no em dashes, no
non-English accented letters). It needs only Python and also runs in CI on every push and pull
request.

## Maintenance

- After changing a plugin here: `claude plugin validate .`, then `/plugin update design-kit` (or
  reinstall) to refresh the installed copy.
- Review the catalog when a plugin updates upstream; versions here are those last seen.
- Watch for duplicates between standalone skills and plugins.

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Design workflow](design-workflow.md) · [Contributing](contributing.md)
