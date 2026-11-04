# claude-toolkit

Personal monorepo to version, organize and audit my Claude setup: my own skills (as plugins), and a
catalog of everything else I use (Anthropic plugins, third-party tools, connectors), with how to
install each one and how they fit together.

## Contents

1. [Quick start](#quick-start)
2. [Repository layout](#repository-layout)
3. [Catalog at a glance](#catalog-at-a-glance)
4. [Own plugin: design-kit](#own-plugin-design-kit)
5. [Anthropic plugins](#anthropic-plugins)
6. [Design tools (upstream)](#design-tools-upstream)
7. [Standalone UI skills](#standalone-ui-skills)
8. [Connectors](#connectors)
9. [MCP servers](#mcp-servers)
10. [How the pieces work together](#how-the-pieces-work-together)
11. [Adding or changing a skill](#adding-or-changing-a-skill)
12. [Maintenance](#maintenance)

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

## Catalog at a glance

| Item | Origin | Kind | Installed via | In this repo |
|---|---|---|---|---|
| design-kit (atomic-design, atomic-page-builder) | Own, derived from MIT/AID sources | Plugin, 2 skills | This marketplace | Yes |
| Engineering | Anthropic | Plugin, 10 skills | claude.ai directory | Link only |
| Design | Anthropic | Plugin, 7 skills | claude.ai directory | Link only |
| Skill Creator | Anthropic | Plugin, 1 skill | claude.ai directory | Link only |
| Firebase | Google (firebase-tools) | Plugin, MCP server | GitHub marketplace `firebase/firebase-tools` | Link only |
| Playwright | Anthropic directory | Plugin, MCP server | claude.ai directory | Link only |
| LinkedIn Profile Review & Resume Converter | Anthropic directory | Plugin, MCP server | claude.ai directory | Link only |
| Impeccable | pbakaus | Plugin (skill, commands, agents, engine) | GitHub marketplace | Link only |
| UI/UX Pro Max | nextlevelbuilder | Plugin (skills, searchable data) | GitHub marketplace | Link only |
| Playwright CLI | Microsoft | CLI + skill | npm | Link only |
| UI Skills set (baseline-ui, fixing-*, improve-ui, ...) | UI Skills registry | Standalone skills | `npx ui-skills` | Link only |
| Connectors (4) | Various | claude.ai connectors | claude.ai settings | Listed |

## Own plugin: design-kit

Frontend component architecture. Two skills that work as a pair: one creates components, the other
assembles pages from them.

**Install**

```
/plugin marketplace add <path-or-github-user>/claude-toolkit
/plugin install design-kit@claude-toolkit
```

Technologies: framework-agnostic methodology; code templates in React + TypeScript + CSS Modules,
with a mapping table for Vue, Svelte, Angular and Web Components; CSS custom properties for tokens.

### `atomic-design` (creates)

- **Does:** decomposes any UI into atoms, molecules, organisms, templates and pages; defines how to
  classify, name, structure and write each component; ships numbered rules, a token starter,
  templates and a verification workflow.
- **Use when:** structuring a component library or design system, deciding where a piece belongs,
  writing or reviewing components, extracting tokens from a design.
- **Files:**

| File | Content |
|---|---|
| `SKILL.md` | Methodology, decomposition workflow, boundaries, pitfalls, professional rules, verification, companions |
| `references/rules.md` | Numbered rules: naming (N), dependencies (D), props (P), state (S), styling (T), accessibility (A), performance (R), quality (Q), definition of done |
| `references/hierarchy.md` | Per-level definitions and boundary examples |
| `references/component-catalog.md` | Typical components and props per level |
| `references/component-templates.md` | Button, Input, FormField, header rules, other-stack mapping |
| `references/design-fidelity.md` | Zero-deviation protocol, provenance comments, allowed exceptions |
| `references/responsive-patterns.md` | Mobile-first layouts, container queries, dialogs, touch targets |
| `assets/tokens.css` | Starter semantic tokens, light and dark themes, reduced motion |
| `evals/evals.json` | Test prompts |

### `atomic-page-builder` (assembles)

- **Does:** builds pages only from existing components; extracts layout from the design source,
  inventories components, finds gaps, and either composes the page or stops and hands off to
  `atomic-design`.
- **Use when:** composing a view or feature from an existing design system.
- **Requires:** `atomic-design`.
- **Files:** `SKILL.md`, `references/design-source-extraction.md`,
  `references/inventory-and-gaps.md`, `references/composition-patterns.md`.

**Complements:** `ui-ux-pro-max` (choose style and palette first), `impeccable` (critique, polish),
`fixing-accessibility`, `playwright-cli` (verify in a browser), `design:design-handoff`.
**Sources and licenses:** see [plugins/design-kit/NOTICE.md](plugins/design-kit/NOTICE.md)
(MIT for whimzyLive and David-Li0406 material; AID Community License v1.0 for ilandahan material).

## Anthropic plugins

Installed from the Anthropic plugin directory (synced with the claude.ai account), so Anthropic
keeps them updated. Do not copy them here. Authorize their connectors in claude.ai > Customize >
Connectors.

### Engineering (v1.2.0, 10 skills)

Install: [claude.com](https://claude.com/es/marketplace/plugins/engineering) ·
[claude.ai](https://claude.ai/customize/plugins/id/2da0c8d9-1e96-4394-b0f4-3249613186f8%40anthropic-plugin-directory)

| Skill | Does |
|---|---|
| `architecture` | Create or evaluate an Architecture Decision Record (ADR) |
| `system-design` | Design systems, APIs, data models and service boundaries |
| `code-review` | Review changes for security, performance and correctness |
| `debug` | Structured reproduce, isolate, diagnose, fix |
| `testing-strategy` | Test strategies, plans and coverage |
| `deploy-checklist` | Pre-deployment verification and rollback triggers |
| `incident-response` | Triage, communicate, write a blameless postmortem |
| `tech-debt` | Identify, categorize and prioritize technical debt |
| `documentation` | READMEs, runbooks, API and architecture docs |
| `standup` | Standup update from recent activity |

Links: `architecture` references `system-design`. Pairs with `design-kit` for frontend structure and
with `testing-strategy` for component tests.

### Design (v1.2.0, 7 skills)

Install: [claude.com](https://claude.com/es/marketplace/plugins/design) ·
[claude.ai](https://claude.ai/customize/plugins/id/afe29730-8d0c-470c-801a-a52a510c0510%40anthropic-plugin-directory)

| Skill | Does |
|---|---|
| `design-critique` | Structured feedback on usability, hierarchy, consistency |
| `design-system` | Audit, document or extend a design system |
| `design-handoff` | Developer spec: layout, tokens, props, states, breakpoints |
| `accessibility-review` | WCAG 2.1 AA audit |
| `ux-copy` | Microcopy, errors, empty states, CTAs |
| `user-research` | Plan and run research (interviews, tests, surveys) |
| `research-synthesis` | Turn research data into themes and recommendations |

Links: `design-system` documents what `atomic-design` produces; `design-handoff` follows
`atomic-page-builder`; `accessibility-review` complements `fixing-accessibility`.

### Skill Creator

Install: [claude.com](https://claude.com/es/marketplace/plugins/skill-creator) ·
[claude.ai](https://claude.ai/customize/plugins/id/4af84cf1-fa7f-46f0-afd6-5de390facaf2%40anthropic-plugin-directory)

Creates, edits and evaluates skills: runs evals, benchmarks with variance analysis and optimizes
the `description` for better triggering. Use it on every new skill in this repo.

### Firebase (MCP server)

Maintained by Google; details and install commands are in [MCP servers](#mcp-servers). Also listed
in the claude.ai directory: [claude.com](https://claude.com/es/marketplace/plugins/firebase) ·
[claude.ai](https://claude.ai/customize/plugins/id/585936f9-ceab-4a4c-b868-6eec587e14b6%40anthropic-plugin-directory).

### Playwright (MCP server)

Install: [claude.com](https://claude.com/es/marketplace/plugins/playwright) ·
[claude.ai](https://claude.ai/customize/plugins/id/22bf1341-d051-4d92-9363-8d0dc8349035%40anthropic-plugin-directory)

Browser automation as MCP tools (navigate, click, type, snapshot, screenshot, console, network,
resize, evaluate). Overlaps with Playwright CLI; prefer the CLI skill for token-efficient work.

### LinkedIn Profile Review & Resume Converter (MCP server)

Install: [claude.ai](https://claude.ai/customize/plugins/id/fc05b187-0a7e-4386-96cd-e1ca5888f372%40anthropic-plugin-directory)

Scores a LinkedIn profile from pasted text and converts it to a resume stored for 7 days with a
private link. It does not connect to LinkedIn; you paste the profile text.

## Design tools (upstream)

These ship scripts, data or a binary, so they stay upstream and update there.

### Impeccable

[impeccable.style](https://impeccable.style/) · `pbakaus/impeccable`

```
/plugin marketplace add pbakaus/impeccable
/plugin
```

Professional design review and improvement: `critique`, `audit`, `polish`, `layout`, `typeset`,
`clarify`, `adapt`, `document`, live iteration. Includes four sub-agents (asset producer,
documenter, finish reviewer, manual edit applier) and a native engine. Hooks are off by default;
enable only on request with `/impeccable hooks on`.
Complements: runs after `atomic-design`/`atomic-page-builder` as the quality pass.

### UI/UX Pro Max

[uupm.cc](https://uupm.cc/) · `nextlevelbuilder/ui-ux-pro-max-skill`

```
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill
```

Searchable design intelligence: 79 styles, 192 palettes, 74 font pairings, 119 UX guidelines,
105 icons, 17 GSAP presets, 25 chart types, 22 stacks. Sub-skills: `ui-ux-pro-max`, `design`,
`design-system`, `ui-styling`, `brand`, `slides`, `banner-design`. Search with
`python "<skill>/scripts/search.py" "<query>" --domain <ux|color|typography|chart|style>`
(Python required). Its generated "design systems" are suggestions; validate before use.
Complements: run before `atomic-design` to choose style, palette and typography, then encode them
in `assets/tokens.css`.

### Playwright CLI

[playwright.dev/agent-cli](https://playwright.dev/agent-cli/introduction)

```
npm install -g @playwright/cli
playwright-cli install --skills
```

Real-browser automation for agents: `open`, `resize`, `snapshot`, `screenshot`, `console`, plus
references for tracing, video, request mocking, storage state and test generation.
Complements: the verification step of every visual skill here (desktop and mobile, light and dark).

## Standalone UI skills

Installed globally in `~/.claude/skills/` from the UI Skills registry (`npx ui-skills list` /
`npx ui-skills get <slug>`).

| Skill | Does | Pairs with |
|---|---|---|
| `baseline-ui` | Quick cleanup of spacing, hierarchy, typography | `impeccable polish` |
| `fixing-accessibility` | Audit and fix ARIA, keyboard, focus, contrast, forms | `design:accessibility-review` |
| `fixing-motion-performance` | Fix janky animations and layout thrashing | `atomic-design` rule T-7 |
| `fixing-metadata` | Titles, meta, Open Graph, favicons, JSON-LD | `atomic-page-builder` |
| `improve-ui` | Read-only audit with an implementation plan | `impeccable critique` |
| `create-design-md` | Document an existing visual system in DESIGN.md | `design:design-system` |
| `ui-skills-root` | Pick the smallest useful UI skill via the CLI | all |
| `find-skills` | Discover installable skills | all |
| `frontend-design` (official plugin) | General aesthetic direction | `ui-ux-pro-max` |

The earlier standalone copy of `atomic-design` was removed; the only copy is in `design-kit`.

## Connectors

Enabled in claude.ai > Customize > Connectors.

| Connector | Type | Used for |
|---|---|---|
| Claude in Chrome | Desktop (included) | Drive the real Chrome with its sign-ins |
| Desktop Commander | Desktop | Terminal and file control on the machine |
| Filesystem | Desktop | Read and write local files |
| GitHub integration | Web | Repos, issues, pull requests |

Plugin MCP servers (Firebase, Playwright, LinkedIn) are listed under their plugins. The Engineering
and Design plugins also expose connectors (10 and 9) that need authorization before use.

## MCP servers

MCP (Model Context Protocol) servers give an AI host extra tools. Install them per host; this
repo only documents them. Never commit tokens, `.env` files or an `mcp.json` that contains
credentials.

### Firebase MCP server (Claude Code)

Docs: [firebase.google.com/docs/ai-assistance/mcp-server](https://firebase.google.com/docs/ai-assistance/mcp-server)

Requires Node.js and npm. It runs locally and uses the Firebase CLI credentials (or Application
Default Credentials); the `firebase_login` tool signs in or checks status.

```
# Option 1 (recommended, what I use): plugin
claude plugin marketplace add firebase/firebase-tools
claude plugin install firebase@firebase

# Option 2: plain MCP server, run from the app folder
claude mcp add firebase npx -- -y firebase-tools@latest mcp
claude mcp list
```

Equivalent JSON (`mcpServers` format, for hosts configured by file):

```json
{ "mcpServers": { "firebase": { "command": "npx", "args": ["-y", "firebase-tools@latest", "mcp"] } } }
```

Optional flags, appended after `mcp`: `--dir <absolute path to the folder with firebase.json>` and
`--only <group,group>` to expose only some tool groups (core is always on).

| Group | Tools |
|---|---|
| core | login/logout, project and app info, SDK config, create project/app, environment, `firebase_init`, deploy and status, security rules, `firebase://` resources |
| apphosting | Backends and logs |
| auth | Get and update users, SMS region policy |
| firestore | Document CRUD, queries, aggregations, databases, indexes, backups |
| dataconnect | Build, list and run SQL Connect operations |
| crashlytics | Issues, events, notes, reports, state |
| realtimedatabase | Read and write data |
| functions | Logs and function listing |
| messaging | Send FCM messages |
| remoteconfig | Get and update templates |
| storage | Download URLs |
| developerknowledge | Search Google developer docs |

It also ships prompts (`/firebase:init`, `/firebase:deploy`) and agent resources. List them with
`npx firebase-tools@latest mcp --generate-tool-list` (also `--generate-prompt-list`,
`--generate-resource-list`).

Tip: enable only the groups a project needs (`--only auth,firestore`) to keep the tool list small
and reduce risk. Check security rules before deploying.
Complements: `engineering:deploy-checklist` before `firebase_deploy`; `engineering:architecture`
for data-model decisions.

### Adding MCP servers to Android Studio (Gemini)

Docs: [developer.android.com/studio/gemini/add-mcp-server](https://developer.android.com/studio/gemini/add-mcp-server)

This is a different host (Gemini's Agent mode in Android Studio), not Claude. Steps:

1. File > Settings > Tools > AI > MCP Servers (on macOS: Android Studio > Settings).
2. Tick **Enable MCP Servers**.
3. Paste the configuration; it is saved as `mcp.json` in Android Studio's configuration directory.
4. Click OK. If the server needs login, click **Start Login** and sign in through the browser.
5. Type `/mcp` in the chat to list the tools.

```json
{
  "mcpServers": {
    "figma":  { "httpUrl": "https://mcp.figma.com/mcp" },
    "notion": { "httpUrl": "https://mcp.notion.com/mcp" },
    "linear": { "httpUrl": "https://mcp.linear.app/mcp" },
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer <YOUR_PERSONAL_ACCESS_TOKEN>" }
    }
  }
}
```

| Option | Meaning |
|---|---|
| `httpUrl` | Required. Streamable HTTP endpoint |
| `url` | Use instead of `httpUrl` for SSE endpoints (usually ending in `/sse`) |
| `headers` | Extra HTTP headers, for example an Authorization token |
| `timeout` | Milliseconds; -1 means none (default) |
| `enabled` | `true` by default |

Limitations: no `stdio` transport, so local servers such as the Firebase one above (`npx ...`)
cannot be added there; no MCP resources or prompt templates; OAuth does not work with some servers
such as GitHub, which is why a personal access token is used. Keep that token out of the repo and
use a fine-grained token with the minimum scopes.

## How the pieces work together

Typical frontend flow, with the tool for each step:

```
1 Direction     ui-ux-pro-max        style, palette, typography, UX guidelines
2 Tokens        atomic-design        assets/tokens.css from the chosen direction
3 Components    atomic-design        atoms -> molecules -> organisms, rules N D P S T A R Q
4 Pages         atomic-page-builder  compose from existing components; gaps go back to step 3
5 Quality       impeccable, fixing-accessibility, baseline-ui, fixing-motion-performance
6 Verify        playwright-cli       375/768/1440px, light and dark, console clean
7 Document      design:design-system, create-design-md, design:design-handoff
```

Cross-cutting: `engineering:testing-strategy` for tests, `engineering:code-review` before merge,
`engineering:architecture` for ADRs, `skill-creator` when authoring or tuning any skill here.

## Adding or changing a skill

1. Check the catalog: if an upstream skill already does it, install that instead of copying.
2. Create `plugins/<plugin>/skills/<skill-name>/SKILL.md` (create the plugin and add it to
   `marketplace.json` if it is the first skill in that domain).
3. If it is derived from another source, check its license and record it in the plugin's
   `NOTICE.md`; keep copyright notices.
4. Write the `description` as "Use when ...", add numbered rules and a verification step, and put
   long detail in `references/`.
5. Evaluate it with `skill-creator`, run `claude plugin validate .`, bump the plugin version, and
   update this README.

## Maintenance

- After changing a plugin here: `claude plugin validate .`, then `/plugin update design-kit` (or
  reinstall) to refresh the installed copy.
- Review the catalog when a plugin updates upstream; versions here are those last seen.
- Watch for duplicates between standalone skills and plugins.
