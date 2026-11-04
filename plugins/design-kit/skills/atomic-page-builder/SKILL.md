---
name: atomic-page-builder
description: Use when composing a page, view or feature from components that already exist in the project's design system. Assembles layout only; never invents new atoms, molecules or organisms. If a needed component is missing, stops and hands off to the atomic-design skill.
---

# Atomic Page Builder

Compose pages from **existing** components. This skill assembles; `atomic-design` creates.

## Rules

| Do | Don't |
|---|---|
| Import components from the design system | Create new atoms, molecules or organisms |
| Take layout values from the design source (Figma, spec, mockup) | Guess grid, gaps or padding |
| Use scoped styles that read from tokens | Hardcode values (`#333`, `24px`) |
| Match the design exactly, including responsive behavior | Round values or add "improvements" |
| Use the project's component library only | Pull in an external UI library the project does not use |

## Hand-off to atomic-design

Switch to `atomic-design` when:

- a needed atom, molecule or organism does not exist;
- a new token is required;
- a token value changed in the design and must be updated first.

## Workflow

1. **Get the layout spec.** If a design source exists (Figma via MCP, a spec, a screenshot), extract
   grid, gaps, padding, margins and breakpoints from it. If none exists, ask for one or state the
   assumptions explicitly. Note page-specific overrides.
2. **Inventory.** List the components the project already has (atoms, molecules, organisms,
   templates) with their props.
3. **Gap analysis.** Map each region of the page to an existing component. List anything unmatched.
4. **Build or stop.**
   - Everything exists: compose the page, matching the spec 1:1.
   - Something is missing: stop, report the gaps, and switch to `atomic-design`.
5. **Verify.** Compare against the design at mobile, tablet and desktop widths.

## Page pattern

```tsx
/** Dashboard page. Layout from: <design link or node id> */
import { DashboardLayout } from '@/design-system/templates/DashboardLayout';
import { Card } from '@/design-system/molecules/Card';
import { DataTable } from '@/design-system/organisms/DataTable';
import styles from './Dashboard.module.css';

export const Dashboard = () => (
  <DashboardLayout>
    <div className={styles.statsGrid}>
      <Card title="Revenue">$12,450</Card>
    </div>
    <DataTable columns={columns} data={data} />
  </DashboardLayout>
);
```

```css
.statsGrid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--spacing-4);
}
@media (min-width: 768px) {
  .statsGrid { grid-template-columns: repeat(3, 1fr); gap: var(--spacing-6); }
}
```

Adapt import paths and styling approach to the project.

## Verification

Render the page in a real browser (playwright-cli) at 375, 768 and 1440px in light and dark, read
the console, and compare with the design source. Also check heading order, landmarks, keyboard
flow, and loading, empty and error states.

## Works with

| Need | Skill or tool |
|---|---|
| Missing component or token | `atomic-design` (required companion) |
| Page-level critique or polish | `impeccable` |
| Accessibility audit | `fixing-accessibility`, `design:accessibility-review` |
| Page metadata, titles, Open Graph | `fixing-metadata` |
| Hand-off to engineering | `design:design-handoff` |

## Extra rules

- Compose in the template's slots; do not reach into a component's internals or override its styles.
- Page-specific styles are limited to layout (grid, gaps, placement); anything visual belongs in a
  component or token.
- Never copy-paste a component to tweak it; request a variant through `atomic-design`.
- Pass real, representative content (long names, empty lists, errors) when checking the page.
- Set the document title and one `h1` per page.
- A page file contains composition and data wiring only; no reusable UI logic.

## References

| File | Read when |
|---|---|
| [references/design-source-extraction.md](references/design-source-extraction.md) | Extracting layout values and writing the page spec |
| [references/inventory-and-gaps.md](references/inventory-and-gaps.md) | Inventorying components and finding gaps |
| [references/composition-patterns.md](references/composition-patterns.md) | Layouts, slots, data states, import order |

## Output checklist

- [ ] Layout values come from the design source, not guesses
- [ ] Responsive behavior matches the design
- [ ] All imports come from the project's design system
- [ ] Zero hardcoded values
- [ ] Zero new components
- [ ] Design link documented in the page file
