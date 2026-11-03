# claude-toolkit

Personal monorepo to version, organize and audit my Claude setup.

It has two jobs:

1. **Source of truth for my own skills**, grouped by domain as Claude Code plugins.
2. **Inventory of everything else** (connectors/MCP, third-party plugins, extensions), so I always know what I have, why, and where it came from.

## Structure

```
.claude-plugin/marketplace.json   Marketplace manifest (lists the plugins below)
plugins/                          One plugin per domain
  <domain>/
    .claude-plugin/plugin.json
    skills/<skill-name>/SKILL.md
inventory/                        What I use but do not own
  connectors.md                   MCP servers and connectors
  third-party-plugins.md          External plugins and skills (source, version)
  extensions.md                   Editor / browser extensions
templates/SKILL.template.md       Starting point for every new skill
docs/CONVENTIONS.md               Naming, description format, versioning
```

## Domains

| Plugin | Scope |
|---|---|
| `cybersecurity` | Reviews, threat modeling, hardening |
| `design` | UI/UX, design systems, frontend |
| `database` | Schema design, queries, migrations |
| `architecture` | System design, ADRs, structure |
| `personal` | Anything that does not fit a domain |

## Usage

Register the marketplace (local path or GitHub):

```
/plugin marketplace add <path-or-user>/claude-toolkit
```

Install only the domains a project needs:

```
/plugin install cybersecurity@claude-toolkit
```

## Adding a skill

1. Copy `templates/SKILL.template.md` to `plugins/<domain>/skills/<skill-name>/SKILL.md`.
2. Write a precise `description`: it decides when Claude activates the skill.
3. Update the domain's `plugin.json` version if behavior changed.
4. Commit using the conventions in `docs/CONVENTIONS.md`.

## Rules

- Own skills live in `plugins/`. Third-party ones are **not copied**; they are listed in `inventory/` with source and version so they keep updating upstream.
- No secrets in the repo: tokens, `.env`, and `settings.local.json` are ignored.
- Every connector in the inventory records: purpose, auth method, status, last review date.

## License

Private, personal use.
