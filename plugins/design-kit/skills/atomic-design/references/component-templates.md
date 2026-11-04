# Component Templates

React + TypeScript + CSS Modules starting points, reading `assets/tokens.css`. Swap in the
project's stack and token names if they differ.

## Button (atom)

```tsx
// atoms/Button/Button.tsx
import { forwardRef, type ButtonHTMLAttributes } from 'react';
import clsx from 'clsx';
import styles from './Button.module.css';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  fullWidth?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', loading = false, fullWidth = false,
     disabled, type = 'button', className, children, ...props }, ref) => (
    <button
      ref={ref}
      type={type}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      className={clsx(styles.button, styles[variant], styles[size], fullWidth && styles.fullWidth, className)}
      {...props}
    >
      {loading && <span className={styles.spinner} aria-hidden="true" />}
      {children}
    </button>
  ),
);
Button.displayName = 'Button';
```

Icon-only buttons must pass `aria-label`. `className` is an escape hatch for layout (margins,
grid placement) only, never for visual overrides.

```css
/* atoms/Button/Button.module.css */
.button {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--spacing-2);
  border: 1px solid transparent; border-radius: var(--radius-md);
  font: var(--font-weight-medium) var(--font-size-sm)/var(--line-height-tight) var(--font-sans);
  cursor: pointer; transition: background-color var(--transition-fast), border-color var(--transition-fast);
}
.button:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 2px; }
.button:disabled { opacity: 0.5; cursor: not-allowed; }

.primary { background: var(--color-primary); color: var(--color-text-inverse); }
.primary:hover:not(:disabled) { background: var(--color-primary-hover); }
.secondary { background: transparent; color: var(--color-text-primary); border-color: var(--color-border-strong); }
.secondary:hover:not(:disabled) { background: var(--color-surface-muted); }
.ghost { background: transparent; color: var(--color-text-secondary); }
.ghost:hover:not(:disabled) { background: var(--color-surface-muted); }
.danger { background: var(--color-error); color: var(--color-text-inverse); }
.danger:hover:not(:disabled) { background: var(--color-error-hover); }

.sm { min-height: 2rem;  padding: var(--spacing-2) var(--spacing-3); }
.md { min-height: var(--tap-target-min); padding: var(--spacing-2) var(--spacing-4); }
.lg { min-height: 3.25rem; padding: var(--spacing-3) var(--spacing-6); font-size: var(--font-size-base); }
.fullWidth { width: 100%; }

.spinner { width: 1em; height: 1em; border: 2px solid currentColor; border-right-color: transparent;
  border-radius: 50%; animation: spin 0.6s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .spinner { animation-duration: 2s; } }
```

## Input (atom)

```tsx
// atoms/Input/Input.tsx
import { forwardRef, type InputHTMLAttributes } from 'react';
import clsx from 'clsx';
import styles from './Input.module.css';

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  invalid?: boolean;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ invalid = false, className, ...props }, ref) => (
    <input ref={ref} aria-invalid={invalid || undefined}
      className={clsx(styles.input, invalid && styles.invalid, className)} {...props} />
  ),
);
Input.displayName = 'Input';
```

```css
.input {
  width: 100%; min-height: var(--tap-target-min); padding: var(--spacing-2) var(--spacing-3);
  background: var(--color-surface); color: var(--color-text-primary);
  border: 1px solid var(--color-border-strong); border-radius: var(--radius-md);
  font: var(--font-size-base) var(--font-sans);
}
.input::placeholder { color: var(--color-text-muted); }
.input:focus-visible { outline: 2px solid var(--color-focus); outline-offset: 1px; }
.input:disabled { background: var(--color-surface-muted); cursor: not-allowed; }
.invalid { border-color: var(--color-error); }
```

## FormField (molecule)

```tsx
// molecules/FormField/FormField.tsx
import { useId } from 'react';
import { Input, type InputProps } from '../../atoms/Input';
import styles from './FormField.module.css';

interface FormFieldProps extends Omit<InputProps, 'id' | 'invalid'> {
  label: string;
  hint?: string;
  error?: string;
}

export const FormField = ({ label, hint, error, required, ...inputProps }: FormFieldProps) => {
  const id = useId();
  const hintId = hint ? `${id}-hint` : undefined;
  const errorId = error ? `${id}-error` : undefined;
  return (
    <div className={styles.field}>
      <label htmlFor={id} className={styles.label}>
        {label}{required && <span aria-hidden="true"> *</span>}
      </label>
      <Input id={id} required={required} invalid={!!error}
        aria-describedby={[errorId, hintId].filter(Boolean).join(' ') || undefined} {...inputProps} />
      {hint && <p id={hintId} className={styles.hint}>{hint}</p>}
      {error && <p id={errorId} role="alert" className={styles.error}>{error}</p>}
    </div>
  );
};
```

## Header (organism): navigation rules

- Logo and nav items are real links (`<a href>`), not `div` with `onClick`.
- `<nav aria-label="Main">` wraps the list; the current page link has `aria-current="page"`.
- The mobile toggle is a `<button>` with `aria-expanded` and `aria-controls`.
- Actions (user menu, theme toggle) are passed in as slots.

## Other stacks

The structure and rules are stack-independent. Equivalents when the project is not React:

| React | Vue | Svelte | Angular | Web Components |
|---|---|---|---|---|
| props | `defineProps` | `export let` / `$props` | `@Input()` / `input()` | attributes and properties |
| `children` | default `<slot>` | `<slot>` / snippets | `<ng-content>` | `<slot>` |
| `onClick` prop | `emit('click')` | `createEventDispatcher` / callback prop | `@Output()` | `CustomEvent` |
| CSS Modules | `<style scoped>` or modules | scoped `<style>` | component styles | shadow DOM styles |
| `forwardRef` | `ref` on root, `inheritAttrs` | `bind:this` | `ElementRef` | native element access |
| `useId` | `useId()` (3.5+) | generated id | generated id | generated id |

Keep the accessibility wiring (labels, `aria-describedby`, `aria-invalid`, focus handling)
identical in every stack.

## Starter tokens

Import `assets/tokens.css` once at the app root, then reference only semantic variables.
