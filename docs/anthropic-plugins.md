# Anthropic plugins

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)

---

Installed from the Anthropic plugin directory (synced with the claude.ai account), so Anthropic
keeps them updated. Do not copy them here. Authorize their connectors in claude.ai > Customize >
Connectors.

## Engineering (v1.2.0, 10 skills)

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

## Design (v1.2.0, 7 skills)

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

## Skill Creator

Install: [claude.com](https://claude.com/es/marketplace/plugins/skill-creator) ·
[claude.ai](https://claude.ai/customize/plugins/id/4af84cf1-fa7f-46f0-afd6-5de390facaf2%40anthropic-plugin-directory)

Creates, edits and evaluates skills: runs evals, benchmarks with variance analysis and optimizes
the `description` for better triggering. Use it on every new skill in this repo.

## Firebase (MCP server)

Maintained by Google; details and install commands are in [MCP servers](connectors-and-mcp.md#mcp-servers). Also listed
in the claude.ai directory: [claude.com](https://claude.com/es/marketplace/plugins/firebase) ·
[claude.ai](https://claude.ai/customize/plugins/id/585936f9-ceab-4a4c-b868-6eec587e14b6%40anthropic-plugin-directory).

## Playwright (MCP server)

Install: [claude.com](https://claude.com/es/marketplace/plugins/playwright) ·
[claude.ai](https://claude.ai/customize/plugins/id/22bf1341-d051-4d92-9363-8d0dc8349035%40anthropic-plugin-directory)

Browser automation as MCP tools (navigate, click, type, snapshot, screenshot, console, network,
resize, evaluate). Overlaps with Playwright CLI; prefer the CLI skill for token-efficient work.

## LinkedIn Profile Review & Resume Converter (MCP server)

Install: [claude.ai](https://claude.ai/customize/plugins/id/fc05b187-0a7e-4386-96cd-e1ca5888f372%40anthropic-plugin-directory)

Scores a LinkedIn profile from pasted text and converts it to a resume stored for 7 days with a
private link. It does not connect to LinkedIn; you paste the profile text.

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)
