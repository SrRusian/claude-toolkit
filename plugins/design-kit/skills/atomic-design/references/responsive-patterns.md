# Responsive Patterns

Mobile-first: base styles are the smallest screen; enhance with `min-width` queries. If a design
source has mobile, tablet and desktop variants, take values from them instead of inventing
behavior.

## Breakpoints

| Name | Min width | Target |
|---|---|---|
| sm | 480px | Mobile landscape |
| md | 768px | Tablet portrait |
| lg | 1024px | Tablet landscape / small desktop |
| xl | 1280px | Desktop |
| 2xl | 1440px | Large desktop |

CSS variables do not work inside `@media`; write the pixel value and keep this table as the
reference. Prefer container queries for components that live in different-width slots.

## Container

```css
.container { width: 100%; margin-inline: auto; padding-inline: var(--spacing-4); }
@media (min-width: 768px)  { .container { padding-inline: var(--spacing-6); } }
@media (min-width: 1024px) { .container { max-width: 960px;  padding-inline: var(--spacing-8); } }
@media (min-width: 1280px) { .container { max-width: 1200px; } }
```

## Fluid card grid (no breakpoints needed)

```css
.cardGrid {
  display: grid;
  gap: var(--spacing-4);
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 16rem), 1fr));
}
@media (min-width: 1024px) { .cardGrid { gap: var(--spacing-6); } }
```

## Container query component

```css
.cardWrap { container-type: inline-size; }
@container (min-width: 600px) { .card { display: grid; grid-template-columns: 1fr 2fr; } }
```

## Form layout

```css
.form { display: grid; gap: var(--spacing-4); }
@media (min-width: 768px) { .formRow { display: flex; gap: var(--spacing-5); } .formRow > * { flex: 1; } }
.formActions { display: flex; flex-direction: column-reverse; gap: var(--spacing-3); }
@media (min-width: 480px) { .formActions { flex-direction: row; justify-content: flex-end; } }
```

## Navigation

```css
.nav { display: none; }
.menuButton { display: inline-flex; }
@media (min-width: 768px) {
  .nav { display: flex; align-items: center; gap: var(--spacing-6); }
  .menuButton { display: none; }
}
```

The mobile menu is a real disclosure: the button has `aria-expanded` and `aria-controls`, Escape
closes it, and focus returns to the button.

## Dialog / modal

Use the native `<dialog>` (or the project's accessible primitive) so focus trapping and Escape
work for free.

```css
.dialog { width: min(32rem, calc(100% - var(--spacing-8))); max-height: 90dvh; border-radius: var(--radius-xl); }
.dialog::backdrop { background: var(--color-backdrop); }
@media (max-width: 479px) { .dialog { width: 100%; max-height: 100dvh; border-radius: 0; } }
```

## Dashboard layout

```css
.layout { display: flex; flex-direction: column; min-height: 100dvh; }
.sidebar { display: none; }
@media (min-width: 1024px) {
  .layout { display: grid; grid-template-columns: 16rem 1fr; }
  .sidebar { display: block; border-inline-end: 1px solid var(--color-border); }
}
```

## Type scale

```css
.h1 { font-size: var(--font-size-2xl); }
@media (min-width: 1024px) { .h1 { font-size: var(--font-size-4xl); } }
```

For smooth scaling use `clamp()` with rem bounds instead of stacked queries.

## Touch and input

- Interactive targets are at least `var(--tap-target-min)` (44px) on touch; 24px is the WCAG 2.2
  absolute minimum.
- Use `@media (hover: hover)` for hover-only affordances; never hide essential actions behind hover.
- Inputs use at least 16px font size on mobile to avoid iOS zoom.
- Respect `prefers-reduced-motion`.

## Verify

Check at 320, 375, 768, 1024 and 1440px, in light and dark themes, with text zoomed to 200% and no
horizontal scroll.
