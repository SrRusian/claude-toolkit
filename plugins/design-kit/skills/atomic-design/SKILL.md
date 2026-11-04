---
name: atomic-design
description: Use when structuring or decomposing any frontend UI into reusable components, regardless of framework. Applies Brad Frost's atomic design methodology — atoms, molecules, organisms, templates, and pages — to guide consistent component hierarchy, naming, and composition decisions. Also use when building or extending a component library or design system.
---

# Atomic Design — Component Hierarchy Methodology

Atomic design is a mental model for breaking any user interface into five distinct levels of
structural complexity — atoms, molecules, organisms, templates, and pages — borrowed from
chemistry's atoms-to-matter progression. It gives teams a shared vocabulary for talking about UI
structure and a repeatable way to decide "does this need to be its own piece, and how big should
that piece be?" The methodology itself is **framework-agnostic**: it describes how to think about
composition, not which library or platform renders the result.

## Why atomic design (rationale)

Without a shared hierarchy, teams tend to build UI ad hoc: some pieces get over-extracted into
components nobody reuses, others get duplicated because nobody realized a smaller shared piece
already existed, and naming drifts (is this a "card," a "widget," a "block"?). Atomic design solves
three recurring problems:

- **Consistency** — the same five labels describe every piece of UI, so a design system and its
  implementation stay aligned no matter who's talking about it.
- **Reuse** — decomposing top-down into smaller named levels surfaces the shared building blocks
  (a label, a button) that would otherwise get re-created inside every larger piece that needs one.
- **Scalable vocabulary** — "this is a molecule, not an organism" is a fast, unambiguous design
  conversation once the levels are understood, replacing long back-and-forth about scope.

The levels are a thinking tool, not a rigid folder structure to enforce everywhere — use them to
reason about granularity, not as a law that every project must nest five matching directories.

## The five levels (overview)

1. **Atoms** — the smallest indivisible UI building blocks: a label, a single input field, a single
   control. An atom has no meaningful sub-parts; splitting it further removes function rather than
   simplifying it.
2. **Molecules** — a small group of atoms bonded together to do one thing, such as a labelled input
   paired with a submit control. A grouping becomes a molecule once two or more atoms combine for a
   single, reusable purpose.
3. **Organisms** — relatively complex groups of molecules and/or atoms that form a distinct,
   recognisable section of an interface, such as a page header or a grid of item summaries. A
   grouping becomes an organism once it reads as a standalone region rather than a helper piece.
4. **Templates** — page-level layout skeletons that arrange organisms into a structure using
   placeholder content. Templates are about arrangement, not real content.
5. **Pages** — specific instances of a template populated with real, representative content. Pages
   are the concrete end state used to validate that the whole system actually works with real data.

See [references/hierarchy.md](references/hierarchy.md) for the expanded per-level guidance —
definitions, boundary rules, and additional neutral examples for each level.

## How to apply it (decomposition workflow)

Follow this ordered procedure to decompose an arbitrary UI description into the five levels:

1. **Start from the whole screen.** Identify the page as the top-level unit — the thing a user
   actually sees, with real content.
2. **Strip content to find the template.** Mentally replace the real content with placeholders.
   What's left — the arrangement of regions — is the template.
3. **Identify the distinct regions inside the template.** Each standalone, recognisable section
   (a header, a listing area, a footer) is a candidate organism.
4. **Break each organism into its functional groupings.** Look for clusters of elements that work
   together for one purpose (a labelled field plus its control). Each cluster is a candidate
   molecule.
5. **Break each molecule into its individual elements.** The remaining pieces that can't be
   meaningfully split further are the atoms.
6. **Name every level consistently** so the same piece is referred to the same way whether you're
   discussing the design, the content, or the composition.

This procedure works top-down (screen → page → template → organism → molecule → atom) or
bottom-up (start cataloguing atoms first, then group them upward) — pick whichever direction
matches how much of the UI already exists versus is being designed fresh.

## Decision heuristics / boundaries

- **Atom vs. molecule:** if removing a piece breaks the element's basic function, it's still an
  atom; if two or more atoms only make sense combined for one purpose, promote the grouping to a
  molecule.
- **Molecule vs. organism:** a molecule is a small, single-purpose helper; an organism is a
  standalone section a user would recognise on its own, even if it contains several molecules.
- **Organism vs. template:** an organism is content-bearing and reusable; a template is the
  arrangement of organisms with placeholder content, not a piece of content itself.
- **Template vs. page:** a template has no real content; a page is the same structure filled with
  actual, representative content.
- **When in doubt, prefer the smaller level.** Over-classifying something as an organism when it's
  really a molecule tends to produce fewer reusable pieces overall.

## Common pitfalls / anti-patterns

- **Over-nesting organisms** — wrapping every organism inside another organism "for organization"
  defeats the purpose of a flat, recognisable set of regions; keep organism nesting shallow.
- **Treating pages as templates** — a template must stay free of real content; once specific
  content is baked in, it has become a page, not a reusable template.
- **Framework leakage** — the five levels describe structural complexity, not implementation
  detail; don't let a specific rendering technology's constraints redefine what counts as an atom
  or an organism.
- **Skipping levels** — jumping straight from atoms to organisms (skipping molecules) usually
  hides a reusable grouping that other organisms could have shared.

## Professional rules (apply when writing code)

These rules turn the methodology into consistent implementation. Skip any that conflict with the
project's existing conventions; the project's own design system always wins.

### Component design

- **Single responsibility.** One component, one job. Atoms stay pure: no business logic, little or
  no state, well-typed props.
- **Composition over inheritance.** Build larger pieces by composing smaller ones; avoid prop
  drilling by passing children or using context.
- **Props describe content and behavior, not looks.** Expose `variant`, `size`, `disabled`,
  `onClick`, `children`. Do not expose raw `color`, `fontSize` or `backgroundColor` props.
- **Styles live inside the component** (CSS Modules, scoped styles or the project's equivalent) and
  read from tokens.
- **Organisms may own state and data fetching**, but should stay reusable; molecules stay
  self-contained and expose a small API.

### Design tokens

- Use **semantic tokens** (`--color-primary`, `--spacing-component-padding`), never primitives
  (`--blue-500`) or hardcoded values (`#3B82F6`, `16px`) inside components.
- When a design source (Figma, a style guide) differs from the existing tokens, update the tokens
  first, then the component. Never round or "improve" values the design specifies.
- Record where values came from (a link or node id in a short comment) so they can be re-verified.

### Quality baseline

- **Accessibility is part of the component**: semantic elements first, then ARIA only where needed
  (`aria-label` for icon-only controls, `aria-invalid` / `aria-describedby` for field errors,
  `aria-busy` for loading), visible focus states, keyboard operability.
- **Responsive by default**: mobile-first styles, enhanced at tablet and desktop breakpoints.
- **TypeScript interfaces** for every component's props; no implicit `any`.
- **Co-locate** component, styles, tests and stories; add a barrel `index.ts` per component or per
  level.

### Suggested layout (adapt to the project)

```
src/components/
  atoms/Button/{Button.tsx, Button.module.css, Button.test.tsx, Button.stories.tsx, index.ts}
  molecules/  organisms/  templates/  pages/
```

### When breaking the hierarchy is acceptable

- A page may use an atom directly for a trivial case.
- A molecule may be used straight inside a template when an organism would add nothing.
- Shared hooks and utilities live outside the hierarchy.

Document the exception in one line instead of silently skipping a level.

### Delivery checklist

- [ ] Classified at the correct level, with the smallest level preferred
- [ ] Only semantic tokens, no hardcoded values
- [ ] Props are content and behavior only
- [ ] Accessible (semantics, labels, focus, keyboard)
- [ ] Responsive at the project's breakpoints
- [ ] Props typed; tests added or updated
- [ ] Design source linked when one exists

For composing full pages from existing components, use the **atomic-page-builder** skill.

## Verification workflow

After writing or changing a component, verify it instead of assuming:

1. Run the project's tests and type check.
2. Open it in a real browser (playwright-cli: `open`, `resize`, `screenshot`, `console`) at 375,
   768 and 1440px, in light and dark themes, and read the console for errors.
3. Check keyboard operation (Tab order, Enter/Space, Escape) and an automated accessibility pass.
4. Compare with the design source; report differences instead of silently fixing them.

Do not call visual work finished without seeing it rendered.

## Works with (optional companions)

| Need | Skill or tool |
|---|---|
| Pick palette, type pairing and style before writing tokens | `ui-ux-pro-max` |
| Critique, audit or polish the result | `impeccable` (`critique`, `audit`, `polish`) |
| Accessibility audit and fixes | `fixing-accessibility`, `design:accessibility-review` |
| Fast spacing and typography cleanup | `baseline-ui` |
| Janky animations | `fixing-motion-performance` |
| Document the resulting system | `design:design-system`, `create-design-md` |
| Developer hand-off spec | `design:design-handoff` |
| Test strategy | `engineering:testing-strategy` |
| Real-browser checks | `playwright-cli` |

Companions are suggestions: if the project already has its own design skill or system, that takes
precedence.

## References

| File | Read when |
|---|---|
| [references/rules.md](references/rules.md) | Writing or reviewing any component (numbered rules N, D, P, S, T, A, R, Q) |
| [references/hierarchy.md](references/hierarchy.md) | Deciding which level something belongs to |
| [references/component-catalog.md](references/component-catalog.md) | Listing typical components and props per level |
| [references/component-templates.md](references/component-templates.md) | Writing Button, Input, FormField or Header code |
| [references/design-fidelity.md](references/design-fidelity.md) | Implementing values from a design source |
| [references/responsive-patterns.md](references/responsive-patterns.md) | Building layouts, breakpoints, touch targets |
| [assets/tokens.css](assets/tokens.css) | The project has no tokens yet (starter set, light and dark) |
