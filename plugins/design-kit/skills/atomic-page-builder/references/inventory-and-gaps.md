# Inventory and Gap Analysis

Fill this in before building a page. It decides whether to compose (stay in
`atomic-page-builder`) or stop and hand off to `atomic-design`.

## 1. Inventory

Scan the project instead of assuming:

```bash
ls src/components/atoms src/components/molecules src/components/organisms src/components/templates
grep -rn "import.*Button" src/pages | head
```

Record what exists:

| Level | Component | Variants / key props | Status |
|---|---|---|---|
| Atom | Button | primary, secondary, ghost, danger / size, loading | ready |
| Molecule | FormField | label, hint, error | ready |
| Organism | DataTable | columns, data, sorting | ready |
| Template | DashboardLayout | header, sidebar, children | ready |

Mark anything incomplete as `partial` and say what is missing.

## 2. Map the page to components

```markdown
## Page: User Dashboard
### Stats row
- StatsCard x4 (molecule: Card variant, exists)
### Activity feed
- ActivityList (organism, MISSING)
  - ActivityItem (molecule, MISSING): Avatar + Text + Timestamp
### Quick actions
- ButtonGroup (molecule, exists)
```

## 3. Gaps

| Need | Have | Gap? | Action |
|---|---|---|---|
| Stats card | Card | variant missing | add variant in atomic-design |
| Activity feed | none | yes | build in atomic-design |
| `--color-chart-1` | none | token missing | add to tokens first |

## 4. Decision

- [ ] Nothing missing: compose the page.
- [ ] Gaps found: stop, report them, switch to `atomic-design`, then return.
