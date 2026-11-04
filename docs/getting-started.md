# Getting started

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)

---

## Quick start

On a new machine, in Claude Code:

```
/plugin marketplace add <path-or-github-user>/claude-toolkit
/plugin install design-kit@claude-toolkit
```

Then install the upstream pieces from the sections below. Requirements: Node.js (npm), Python
(use `python`, not `python3`, on Windows), and Git.

## Repository layout

```
.claude-plugin/marketplace.json      Lists my plugins (so they install with /plugin install)
plugins/<plugin>/
  .claude-plugin/plugin.json         Name, description, version
  NOTICE.md                          Sources and licenses of anything derived
  skills/<skill-name>/
    SKILL.md                         Instructions (frontmatter: name, description)
    references/                      Detail files loaded only when needed
    assets/                          Starter files (e.g. tokens.css)
    evals/                           Test prompts for the skill
README.md                            This catalog
```

Rules: a skill is copied here only when I customize it; everything else is installed from its
upstream so it keeps updating. Skill folder name = `name` in frontmatter (kebab-case).
`description` starts with "Use when..." because it decides when Claude activates the skill. No
secrets in the repo.

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)
