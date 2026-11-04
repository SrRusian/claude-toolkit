# Rules

Numbered so reviews and commits can cite them ("violates N-2"). Precedence when rules conflict:

1. The project's existing design system and conventions
2. Accessibility (A-rules)
3. The design source's values (see design-fidelity.md)
4. The rules below

State an exception in one line in the code or PR; never skip a rule silently.

## N. Naming

- **N-1** Components are `PascalCase`; the folder name equals the component name.
- **N-2** Do not put the level in the name: `Button`, not `ButtonAtom`.
- **N-3** Avoid vague names: `Base`, `Common`, `Generic`, `Wrapper`, `Container`, `Misc`, `Utils`
  as component names. Name by purpose (`PageSection`, `FormActions`).
- **N-4** Event props are `onX` (`onChange`, `onClose`); handlers inside are `handleX`.
- **N-5** Boolean props are positive adjectives (`disabled`, `loading`, `fullWidth`); never
  negatives (`notEditable`, `hideIcon`).
- **N-6** Variants are string unions (`variant="danger"`), never one boolean per variant
  (`danger`, `primary`).
- **N-7** CSS class names in modules are camelCase; token names are kebab-case.

## D. Dependencies and structure

- **D-1** Imports flow down only: page -> template -> organism -> molecule -> atom -> tokens.
- **D-2** No upward imports and no imports between sibling organisms; extract the shared piece to
  a lower level instead.
- **D-3** No circular dependencies; run a cycle check in CI when available.
- **D-4** Atoms never import data, routing or state libraries.
- **D-5** Shared logic goes in hooks or utilities outside the hierarchy.
- **D-6** One barrel `index.ts` per component; import from the barrel, never deep into another
  component's internals.
- **D-7** One component per file; co-locate styles, tests and stories.

## P. Props API

- **P-1** Extend the native element's attributes, forward the `ref` and spread the rest onto the
  root element.
- **P-2** Text content comes through `children`, not a `label` prop (except where the label is
  structurally separate, as in FormField).
- **P-3** More than ~8 props means the component is doing too much; split it or use slots.
- **P-4** Compose with slots or compound components (`Card.Header`) rather than render-prop
  explosions or many `*Content` props.
- **P-5** State whether a component is controlled or uncontrolled; never switch at runtime.
- **P-6** Defaults live in the destructuring, are documented in the prop's doc comment, and
  match the design's default state.
- **P-7** No visual props (`color`, `fontSize`, `margin`); tokens and variants cover them.
  `className` is allowed for layout placement only.
- **P-8** A polymorphic `as` prop is allowed only on text and box primitives, and the element type
  is constrained.
- **P-9** Every prop is typed; no implicit `any`; export the prop types.

## S. State and data

- **S-1** Atoms are stateless apart from trivial UI state; molecules hold local UI state only.
- **S-2** Organisms may fetch data through hooks, but reusable ones receive data via props.
- **S-3** Pages own routing, fetching and side effects.
- **S-4** Do not store derived values in state; compute them.
- **S-5** Every data-driven view handles loading, empty, error and success.
- **S-6** Optimistic or async actions disable repeat submits and announce the result.

## T. Styling

- **T-1** Components read semantic tokens only; no hex, rgb or raw px in component styles.
- **T-2** No `!important` and no inline `style` for design values (dynamic CSS variables are fine).
- **T-3** Prefer logical properties (`margin-inline`, `padding-block`, `inset-inline-start`) so
  right-to-left works.
- **T-4** Do not fix the height of text containers; use `min-height` so zoom and translation do
  not clip.
- **T-5** Provide every state: default, hover, focus-visible, active, disabled, loading, invalid.
- **T-6** Dark mode is achieved by token overrides, never by per-component color branches.
- **T-7** Animate `transform` and `opacity`; avoid animating layout properties. Respect
  `prefers-reduced-motion`.
- **T-8** Z-index values come from a token scale; no ad hoc `9999`.
- **T-9** Nothing essential is revealed only on hover.
- **T-10** Write styles mobile-first and enhance with `min-width` queries.

## A. Accessibility

- **A-1** Semantic HTML first (`button`, `a`, `label`, `nav`, `main`); ARIA only to fill gaps.
- **A-2** Every control has an accessible name; icon-only controls require `aria-label`.
- **A-3** Never remove the focus indicator without replacing it; use `:focus-visible`.
- **A-4** Everything operable by keyboard in a logical order; no keyboard traps except modal
  dialogs, which trap and restore focus.
- **A-5** Contrast: 4.5:1 for body text, 3:1 for large text and UI component boundaries.
- **A-6** Never convey meaning by color alone; pair with text or an icon.
- **A-7** Labels are persistent and visible; a placeholder is not a label.
- **A-8** Async errors and status messages use `role="alert"` or `aria-live`.
- **A-9** Interactive targets are at least 24px (WCAG 2.2) and 44px on touch.
- **A-10** Headings descend without skipping levels; one `h1` per page; landmarks are labeled when
  repeated.
- **A-11** Content reflows at 320px and at 200% zoom without horizontal scroll.
- **A-12** Images have meaningful `alt`, or `alt=""` when decorative.

## R. Performance

- **R-1** Set image width and height (or aspect-ratio) to prevent layout shift.
- **R-2** Lazy-load heavy organisms (charts, editors, maps) below the fold.
- **R-3** Memoize only after measuring a real cost.
- **R-4** Load fonts with `font-display: swap` and subset them.
- **R-5** Keep third-party UI dependencies out of atoms.

## Q. Quality and documentation

- **Q-1** Every atom and molecule has tests for each variant and state, plus an automated
  accessibility check.
- **Q-2** Every variant and state has a story or example page.
- **Q-3** Props are documented with TSDoc comments; types are exported.
- **Q-4** Visual changes are verified in a real browser at 320/375, 768, 1024 and 1440px in light
  and dark.
- **Q-5** Breaking prop changes bump the major version; deprecate with `@deprecated` and a
  migration note before removing.
- **Q-6** Keep a changelog of tokens and component API changes.

## Definition of done

A component is done when: correct level (N, D) · API follows P · tokens only (T) · every state
(T-5) · accessible (A) · tested and documented (Q) · verified in the browser (Q-4).
