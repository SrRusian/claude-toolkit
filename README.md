<div align="center">

# claude-toolkit

**Control center for my Claude setup: own skills, plugins, connectors and MCP servers, versioned and documented.**

![Claude Code](https://img.shields.io/badge/Claude_Code-plugin_marketplace-D97757?style=flat-square&logo=claude&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-documented-5B8DEF?style=flat-square&logo=modelcontextprotocol&logoColor=white)
![React](https://img.shields.io/badge/React-templates-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Markdown](https://img.shields.io/badge/skills-Markdown-0B0B0B?style=flat-square&logo=markdown&logoColor=white)

</div>

## Overview

- **Own skills**, grouped by domain as Claude Code plugins and installable from this repo.
- **A catalog of everything else** I use (Anthropic plugins, third-party tools, connectors, MCP
  servers): what each does, how to install it and what it pairs with.
- **One place to audit** the setup, so nothing is duplicated, forgotten or out of date.

## Quick start

```
/plugin marketplace add <path-or-github-user>/claude-toolkit
/plugin install design-kit@claude-toolkit
/plugin install dev-workflow@claude-toolkit
```

Needs Claude Code, Node.js, Git and Python (`python` on Windows). More in
[Getting started](docs/getting-started.md).

## Documentation

| | Guide | What you will find |
|:-:|---|---|
| <img src="https://cdn.simpleicons.org/gnubash/4EAA25" width="20" height="20" alt="Shell" /> | [Getting started](docs/getting-started.md) | Requirements, install, repository layout |
| <img src="https://cdn.simpleicons.org/react/61DAFB" width="20" height="20" alt="React" /> | [design-kit](docs/design-kit.md) | My plugin: `atomic-design` and `atomic-page-builder`, files, rules, sources |
| <img src="https://cdn.simpleicons.org/linear/5E6AD2" width="20" height="20" alt="Task workflow" /> | [dev-workflow](docs/dev-workflow.md) | My plugin: `task-closure`, verify-for-real habits and the ready commit command |
| <img src="https://cdn.simpleicons.org/claude/D97757" width="20" height="20" alt="Claude" /> | [Anthropic plugins](docs/anthropic-plugins.md) | Engineering, Design, Skill Creator, Firebase, Playwright, LinkedIn |
| <img src="https://cdn.simpleicons.org/figma/F24E1E" width="20" height="20" alt="Figma" /> | [Design tools](docs/design-tools.md) | Impeccable, UI/UX Pro Max, Playwright CLI and standalone UI skills |
| <img src="https://cdn.simpleicons.org/modelcontextprotocol/5B8DEF" width="20" height="20" alt="MCP" /> | [Connectors and MCP](docs/connectors-and-mcp.md) | Enabled connectors, Firebase MCP, Android Studio MCP setup |
| <img src="https://cdn.simpleicons.org/mermaid/FF3670" width="20" height="20" alt="Mermaid" /> | [Design workflow](docs/design-workflow.md) | How the pieces work together, step by step |
| <img src="https://cdn.simpleicons.org/git/F05032" width="20" height="20" alt="Git" /> | [Contributing](docs/contributing.md) | Adding a skill, licenses, maintenance |

## Catalog

| | Item | Origin | Kind | Install | Details |
|:-:|---|---|---|---|---|
| <img src="https://cdn.simpleicons.org/react/61DAFB" width="20" height="20" alt="React" /> | **design-kit** | Own (MIT / AID sources) | Plugin, 2 skills | This marketplace | [docs](docs/design-kit.md) |
| <img src="https://cdn.simpleicons.org/linear/5E6AD2" width="20" height="20" alt="Task workflow" /> | **dev-workflow** | Own | Plugin, 1 skill | This marketplace | [docs](docs/dev-workflow.md) |
| <img src="https://cdn.simpleicons.org/claude/D97757" width="20" height="20" alt="Claude" /> | Engineering | Anthropic | Plugin, 10 skills | claude.ai directory | [docs](docs/anthropic-plugins.md#engineering-v120-10-skills) |
| <img src="https://cdn.simpleicons.org/claude/D97757" width="20" height="20" alt="Claude" /> | Design | Anthropic | Plugin, 7 skills | claude.ai directory | [docs](docs/anthropic-plugins.md#design-v120-7-skills) |
| <img src="https://cdn.simpleicons.org/claude/D97757" width="20" height="20" alt="Claude" /> | Skill Creator | Anthropic | Plugin, 1 skill | claude.ai directory | [docs](docs/anthropic-plugins.md#skill-creator) |
| <img src="https://cdn.simpleicons.org/firebase/FFCA28" width="20" height="20" alt="Firebase" /> | Firebase | Google | Plugin, MCP server | GitHub marketplace | [docs](docs/connectors-and-mcp.md#firebase-mcp-server-claude-code) |
| <img src="https://cdn.simpleicons.org/googlechrome/4285F4" width="20" height="20" alt="Browser automation" /> | Playwright | Anthropic directory | Plugin, MCP server | claude.ai directory | [docs](docs/anthropic-plugins.md#playwright-mcp-server) |
| <img src="https://cdn.simpleicons.org/claude/D97757" width="20" height="20" alt="Claude" /> | LinkedIn Review and Resume | Anthropic directory | Plugin, MCP server | claude.ai directory | [docs](docs/anthropic-plugins.md#linkedin-profile-review--resume-converter-mcp-server) |
| <img src="https://cdn.simpleicons.org/css/1572B6" width="20" height="20" alt="CSS" /> | Impeccable | pbakaus | Plugin | GitHub marketplace | [docs](docs/design-tools.md#impeccable) |
| <img src="https://cdn.simpleicons.org/tailwindcss/06B6D4" width="20" height="20" alt="Tailwind CSS" /> | UI/UX Pro Max | nextlevelbuilder | Plugin and data | GitHub marketplace | [docs](docs/design-tools.md#uiux-pro-max) |
| <img src="https://cdn.simpleicons.org/npm/CB3837" width="20" height="20" alt="npm" /> | Playwright CLI | Microsoft | CLI and skill | npm | [docs](docs/design-tools.md#playwright-cli) |
| <img src="https://cdn.simpleicons.org/storybook/FF4785" width="20" height="20" alt="Storybook" /> | UI Skills set | UI Skills registry | Standalone skills | `npx ui-skills` | [docs](docs/design-tools.md#standalone-ui-skills) |
| <img src="https://cdn.simpleicons.org/modelcontextprotocol/5B8DEF" width="20" height="20" alt="MCP" /> | Connectors (4) | Various | claude.ai connectors | claude.ai settings | [docs](docs/connectors-and-mcp.md#connectors) |

## Design workflow

```mermaid
flowchart LR
    A["Direction<br/>ui-ux-pro-max"] --> B["Tokens + components<br/>atomic-design"]
    B --> C["Pages<br/>atomic-page-builder"]
    C --> D["Quality<br/>impeccable, a11y"]
    D --> E["Verify<br/>playwright-cli"]
    E --> F["Document<br/>design-system, handoff"]
```

Full detail in [Design workflow](docs/design-workflow.md).

## Layout

```
.claude-plugin/marketplace.json   Plugin list (installs with /plugin install)
plugins/<plugin>/                 My plugins: skills, references, assets, NOTICE.md
docs/                             Detailed guides linked above
scripts/check.py                  Repository self-check (also runs in CI)
.github/workflows/check.yml       Runs the self-check on every push and pull request
```

## Licenses

Own work plus material derived from MIT and AID Community License sources. Details and
attribution in [plugins/design-kit/NOTICE.md](plugins/design-kit/NOTICE.md). No secrets in this repo.
