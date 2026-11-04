# Design Fidelity

Implement the design as specified. The design source (Figma, a spec, a style guide) is the single
source of truth for values. The developer translates; they do not redesign.

## Order of work

1. **Extract** values from the source before writing styles.
2. **Document** them (a link or node id plus the values, in a short comment).
3. **Compare** with existing tokens. If the source differs, update the tokens first.
4. **Implement** with exact values, through tokens.
5. **Verify** against the source at every breakpoint.

## What to extract

| Category | Details |
|---|---|
| Dimensions | width, height, min/max |
| Spacing | padding (4 sides), margin, gap |
| Color | fill, stroke, background, every state |
| Typography | family, size, weight, line-height, letter-spacing |
| Effects | shadow, blur, opacity |
| Shape | radius, border width |
| Layout | direction, alignment, wrap |
| Responsive | the mobile, tablet and desktop variants |

## Zero-deviation rules

| Do not | Do |
|---|---|
| Round 13px to 12px | Use 13px (or add a token for it) |
| Nudge `#3B82F6` to a "nicer" shade | Use the exact value |
| Add a shadow the design lacks | Use none |
| Assume a breakpoint behavior | Read it from the responsive variants |
| Silently fix an inconsistency | Report it |

Hard-coding is never the fix: if a value has no token, add one.

## When something looks wrong

1. Stop; do not change anything.
2. Capture the issue (screenshot, frame, value).
3. Ask: "In frame X the padding is 13px. Intentional, or should it be 12px on the 4px grid?"
4. Implement the answer and record the decision.

## Allowed exceptions (still report them)

- **Platform fixes**: vendor prefixes, browser bugs.
- **Accessibility gaps**: if the design fails WCAG (for example contrast below 4.5:1 for body
  text), ship the closest compliant value and flag it to the designer. Accessibility outranks
  pixel fidelity.
- **Missing states**: when focus, hover or disabled states are absent, use the token defaults and
  request the real design.

## Provenance comments

```tsx
/**
 * @design <link or node id>
 * @extracted 2025-01-15
 * Values come from the design source; change them only after a design update.
 */
```

```css
.button {
  padding: var(--spacing-3) var(--spacing-6); /* design: 12px 24px */
}
```

## Token sync

When the design changes: detect the change, update the token file, verify affected components,
commit with a message like `sync: update primary color from design v12`.

## Review checklist

- [ ] Design link present and correct
- [ ] Every value traces to the design or a token
- [ ] No hard-coded colors or sizes
- [ ] All states checked (default, hover, focus, active, disabled, error)
- [ ] Verified at mobile, tablet and desktop; visual diff is clean
- [ ] No unrequested colors, rounded values or effects
