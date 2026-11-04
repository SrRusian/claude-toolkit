# Sources and licenses

| Skill / file | Based on | License |
|---|---|---|
| `atomic-design/SKILL.md`, `references/hierarchy.md`, `evals/` | [whimzyLive/nightshift-ai](https://github.com/whimzyLive/nightshift-ai) `skills/atomic-design` | MIT, Copyright (c) 2026 whimzyLive |
| `atomic-design/SKILL.md` (principles, structure) | [David-Li0406/meta-skill-evloving](https://github.com/David-Li0406/meta-skill-evloving) atomic-design | MIT, declared in its frontmatter |
| `atomic-design/references/{component-catalog,component-templates,design-fidelity,responsive-patterns}.md`, `assets/tokens.css`; all of `atomic-page-builder` | Adapted from [ilandahan/AID](https://github.com/ilandahan/AID) `skills/atomic-design` and `skills/atomic-page-builder` | AID Community License v1.0, Copyright (c) 2024-Present Ilan Dahan |

## Changes made to the AID material

Generalized from Figma-only to any design source; converted the JSON token files into one
`tokens.css` (with dark theme, valid CSS variable names and a muted text color that passes WCAG AA);
rewrote component templates for accessibility (`children` instead of `label`, real links in
navigation, `className` support, `useId` field wiring); made responsive patterns mobile-first with
container queries and `dvh` units; condensed overlapping references.

## AID Community License v1.0 summary

Free to use, adapt and share, including in commercial products, with attribution. It may not be
sold (as a product, course, certification or paid-access material), sublicensed under other terms,
or have its copyright notices removed. This toolkit is personal and not sold; if it is ever
published, keep this notice and the AID attribution above.

## MIT notice

The MIT-licensed material is used under the MIT License: permission is granted to use, copy,
modify and distribute it, provided the copyright notice and permission notice are kept.
