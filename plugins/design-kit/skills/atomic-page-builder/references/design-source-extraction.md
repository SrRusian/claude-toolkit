# Design Source Extraction (page level)

Get the page layout from the design source before writing any style. The source can be Figma (via
MCP), a spec, or a mockup; if there is none, ask for one or list your assumptions.

## Needed up front

1. Link to the source (file URL and frame or node id).
2. Access to read it (Figma MCP `get_node`, or the spec document).
3. The inventory from `inventory-and-gaps.md`.

## Extract

```markdown
### Container
- Width, max-width, padding, margin
### Grid
- Columns, column gap, row gap
### Sections
- Padding, gap, background (token or value)
### Per breakpoint (mobile, tablet, desktop)
- Columns, sidebar behavior, gaps, hidden or reordered elements
### States
- Loading, empty, error, and hover/focus of the components used
```

Auto-layout in the source maps to flexbox or grid exactly; do not approximate.

## Map values to tokens

| Source value | Token | Note |
|---|---|---|
| 24px | `--spacing-6` | standard gap |
| 48px | `--spacing-12` | section padding |
| #F5F5F5 | `--color-surface-muted` | section background |

If a value matches no token: stop, add the token via `atomic-design`, then continue. Never inline
the raw value.

## Page spec (write this down)

```markdown
# Page: <name>
Source: <link> · frame <id> · extracted <date>

| Property | Desktop | Tablet | Mobile |
|---|---|---|---|
| Max width | 1200px | 100% | 100% |
| Padding | 48px | 32px | 16px |
| Grid columns | 12 | 8 | 4 |
| Gap | 24px | 16px | 12px |

Sections: 1 Header (sticky, 64px) · 2 Hero · 3 Content grid · 4 Footer
Components: Header (organism), Card x6 (molecule), Button x3 (atom)
Tokens needed: spacing 4, 6, 12 · colors surface, surface-muted · type heading-xl, body
```

## Common mistakes

| Mistake | Instead |
|---|---|
| Rounding 23px to 24px | Use the exact value and add a token |
| Assuming breakpoints | Read them from the source variants |
| Ignoring auto-layout | Reproduce it with flex/grid |
| Missing hover, focus or empty states | Check every state |
| Skipping spacing | Extract all gaps and padding |

## Validate before implementing

- [ ] Layout values extracted and mapped to tokens
- [ ] Components identified; missing ones flagged
- [ ] All breakpoints documented
- [ ] Source link and extraction date recorded
