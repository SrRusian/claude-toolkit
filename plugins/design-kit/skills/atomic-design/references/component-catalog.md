# Component Catalog

Typical contents and prop shapes per level. Treat them as starting points; the project's design
system decides the real list. Props describe content and behavior; looks come from tokens.

## Atoms (tokens only, no business logic)

| Atom | Key props |
|---|---|
| Button | `variant` (primary, secondary, ghost, danger), `size`, `loading`, `disabled`, `type` |
| Input | `size`, `invalid`, `type`, plus native input attributes |
| Typography | `variant` (h1-h6, body, body-sm, caption, label), `as` |
| Icon | `name`, `size`, `label` (required when it is the only content) |
| Badge | `variant` (default, primary, success, warning, error) |
| Avatar | `src`, `alt`, `initials`, `size` |
| Checkbox / Radio / Switch | `checked`, `onChange`, `disabled`, `indeterminate` |
| Spinner, Divider | `size`, `orientation` |

## Molecules (2+ atoms, one purpose)

| Molecule | Composition |
|---|---|
| FormField | Label + Input + hint/error text |
| SearchBar | Input + Icon + Button |
| Card | container with optional header, body and footer slots |
| MenuItem / ListItem | Icon or Avatar + text + action |
| Tabs, Breadcrumb, Pagination | buttons or links + active state |
| Toast / Alert | Icon + message + close |

## Organisms (standalone regions)

| Organism | Composition |
|---|---|
| Header | Logo + navigation + user menu + mobile menu |
| Sidebar | Navigation + user section |
| Form | FormFields + actions |
| DataTable | Headers + rows + sorting + pagination |
| Modal | Overlay + container + header, body and actions |
| Hero, FeatureGrid, PricingTable, Footer | marketing sections |

## Templates and pages

- **Template**: layout skeleton with named regions (`header`, `sidebar`, `children`, `footer`).
  Examples: DashboardLayout, AuthLayout, SettingsLayout, ListPageLayout, DetailPageLayout.
- **Page**: a template filled with real content and data.

```tsx
export const DashboardPage = () => {
  const { user } = useAuth();
  return (
    <DashboardLayout header={<Header />} sidebar={<Sidebar items={SIDEBAR_ITEMS} />}>
      <Typography variant="h1">Welcome, {user.firstName}</Typography>
      <StatsGrid stats={stats} />
    </DashboardLayout>
  );
};
```

## Accessibility notes per level

- Atoms own their semantics: real `<button>`, `<input>`, `<label>`; icon-only controls need an
  accessible name.
- Molecules wire relationships (`label` + `htmlFor`, `aria-describedby` for hints and errors).
- Organisms manage focus and keyboard behavior (menus, dialogs, tables).
- Navigation items are links (`<a>`), not clickable `div`s.
