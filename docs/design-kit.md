# design-kit (own plugin)

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)

---

Frontend component architecture. Two skills that work as a pair: one creates components, the other
assembles pages from them.

**Install**

```
/plugin marketplace add <path-or-github-user>/claude-toolkit
/plugin install design-kit@claude-toolkit
```

Technologies: framework-agnostic methodology; code templates in React + TypeScript + CSS Modules,
with a mapping table for Vue, Svelte, Angular and Web Components; CSS custom properties for tokens.

## `atomic-design` (creates)

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

## `atomic-page-builder` (assembles)

- **Does:** builds pages only from existing components; extracts layout from the design source,
  inventories components, finds gaps, and either composes the page or stops and hands off to
  `atomic-design`.
- **Use when:** composing a view or feature from an existing design system.
- **Requires:** `atomic-design`.
- **Files:** `SKILL.md`, `references/design-source-extraction.md`,
  `references/inventory-and-gaps.md`, `references/composition-patterns.md`.

**Complements:** `ui-ux-pro-max` (choose style and palette first), `impeccable` (critique, polish),
`fixing-accessibility`, `playwright-cli` (verify in a browser), `design:design-handoff`.
**Sources and licenses:** see [plugins/design-kit/NOTICE.md](../plugins/design-kit/NOTICE.md)
(MIT for whimzyLive and David-Li0406 material; AID Community License v1.0 for ilandahan material).

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)
