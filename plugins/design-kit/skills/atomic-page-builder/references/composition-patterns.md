# Composition Patterns

All patterns assemble existing components; adapt paths and styling to the project. Values shown
are placeholders for whatever the design source specifies.

## Layouts (mobile-first)

### Grid

```css
.grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--spacing-3); padding: var(--spacing-4); }
@media (min-width: 768px)  { .grid { grid-template-columns: repeat(8, 1fr);  gap: var(--spacing-4); padding: var(--spacing-6); } }
@media (min-width: 1024px) { .grid { grid-template-columns: repeat(12, 1fr); gap: var(--spacing-6); padding: var(--spacing-8); } }
```

### Dashboard (sidebar + main)

```tsx
export const DashboardLayout = ({ header, sidebar, children }: Props) => (
  <div className={styles.dashboard}>
    <aside className={styles.sidebar}>{sidebar}</aside>
    <div className={styles.main}>
      <header className={styles.header}>{header}</header>
      <main className={styles.content}>{children}</main>
    </div>
  </div>
);
```

```css
.dashboard { min-height: 100dvh; }
.sidebar { display: none; }
.header { position: sticky; top: 0; }
@media (min-width: 1024px) {
  .dashboard { display: grid; grid-template-columns: 17.5rem 1fr; }
  .sidebar { display: block; position: sticky; top: 0; height: 100dvh; }
}
```

### Split view (master-detail)

```tsx
export const SplitLayout = ({ list, detail }: Props) => (
  <div className={styles.split}>
    <aside aria-label="List">{list}</aside>
    <main>{detail}</main>
  </div>
);
```

On small screens show the list, then the detail as a separate view.

## Slot (compound component) patterns

```tsx
<Card>
  <Card.Header><h3>Title</h3><Badge>Status</Badge></Card.Header>
  <Card.Body>Content</Card.Body>
  <Card.Footer><Button>Action</Button></Card.Footer>
</Card>

<Modal open={open} onClose={onClose}>
  <Modal.Title>Confirm action</Modal.Title>
  <Modal.Body>Are you sure?</Modal.Body>
  <Modal.Actions>
    <Button variant="secondary" onClick={onClose}>Cancel</Button>
    <Button onClick={onConfirm}>Confirm</Button>
  </Modal.Actions>
</Modal>
```

## Data states: every data-driven page handles all four

```tsx
export const UsersPage = () => {
  const { data, isLoading, error } = useUsers();
  if (isLoading) return <PageSkeleton />;
  if (error) return <ErrorState error={error} />;
  if (!data.length) return <EmptyState message="No users yet" />;
  return (
    <PageLayout title="Users">
      <DataTable columns={userColumns} data={data} />
    </PageLayout>
  );
};
```

With Suspense, wrap independent sections so each loads on its own:

```tsx
<Suspense fallback={<StatsSkeleton />}><StatsSection /></Suspense>
<Suspense fallback={<TableSkeleton />}><RecentActivity /></Suspense>
```

## Import order

```tsx
// 1. External libraries
import { useState } from 'react';
// 2. Design system, large to small
import { PageLayout } from '@/design-system/templates/PageLayout';
import { DataTable } from '@/design-system/organisms/DataTable';
import { Card } from '@/design-system/molecules/Card';
import { Button } from '@/design-system/atoms/Button';
// 3. Hooks and utilities
import { useUsers } from '@/hooks/useUsers';
// 4. Local styles, then types
import styles from './UsersPage.module.css';
import type { User } from '@/types';
```

## Page-level accessibility

- One `<h1>` per page; headings descend without skipping levels.
- Landmarks: `header`, `nav`, `main`, `aside`, `footer`, each labeled when repeated.
- Provide a skip link to `main`; set the document title per page.
