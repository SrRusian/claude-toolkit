# Design tools

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)

---

## Upstream tools

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

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)
