# dev-workflow (own plugin)

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Design workflow](design-workflow.md) · [Contributing](contributing.md)

---

Working habits for any task that changes files: understand first, do it, verify for real, and close
with a clear report plus a ready-to-copy commit command.

## Install

```
/plugin marketplace add <path-or-github-user>/claude-toolkit
/plugin install dev-workflow@claude-toolkit
```

Technologies: plain Markdown; no scripts or dependencies. It is not tied to any language or
framework, so it works in every project.

## `task-closure`

- **Does:** defines how to run a task from start to finish and how to hand it over.
- **Triggers:** on its own for any task that changes code, configuration or documentation, and at
  delivery time; or call it with `/task-closure`. It does not apply to pure questions or analysis.
- **Precedence:** the project's `CLAUDE.md` always wins; this skill fills what it does not say.

| Part | What it enforces |
|---|---|
| 1. Before touching anything | Read `CLAUDE.md` and the files involved, search for what already exists, state what is and is not requested, ask only real decisions, look at a target before deleting, check `git status` |
| 2. While working | Small changes in the existing style, no duplicates, fix obvious problems in the same pass, reject bad ideas with evidence, no secrets, no unconfirmed destructive actions, never bypass a block |
| 3. Verify for real | Build, types, lint, tests; run it or capture it (desktop and mobile, light and dark); clean test data; report failures with real output; say what could not be tested |
| 4. What travels with the code | Docs, tests and `CLAUDE.md` notes, only when the change warrants them |
| 5. Final report | Fixed order: what was done, how it was verified, decisions made, what was not done, what is pending for the user, the commit, shared-zone files; built from `git status` and `git diff --stat` |
| 6. Commit command | Never run `git commit` or `git push`; deliver the command: English Title Case imperative title (under about 70 characters), 2 to 4 bullets, one `-m` per bullet, no signatures, separate commits for unrelated changes with their `git add` |
| 7. Style | No filler, no emojis, no em dashes |
| 8. Closing checklist | Seven checks before handing over |

Commit shape:

```
git commit -m "Add Plugin Catalog Docs" -m "- split the README into guides" -m "- add brand icons to the catalog"
```

## Rules added on top of the original

- Run `git status` first so existing changes are not mixed with new ones.
- Do not touch files outside the task; never print or version secrets.
- Destructive or outward-facing actions (delete, force push, publish, send) need explicit
  confirmation each time; earlier approval does not carry over.
- If a hook, permission or test blocks something, report it instead of working around it.
- A failing test is reported with its real output; it is never weakened or deleted to pass.
- Use the user's shell syntax (PowerShell on Windows) and exact `git add` paths, not `git add -A`,
  when unrelated files exist.
- Pure questions get a short answer, not the full report structure.

## Works with

| Need | Skill |
|---|---|
| Review the change before the commit | `engineering:code-review` |
| Decide what to test | `engineering:testing-strategy` |
| Release steps and rollback | `engineering:deploy-checklist` |
| See visual results in a browser | `playwright-cli` |
| Author or tune a skill like this one | `skill-creator` |

## Installation note

If a standalone copy of this skill exists in `~/.claude/skills/` (for example an older version),
remove it after installing the plugin so the skill is not loaded twice.

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Design workflow](design-workflow.md) · [Contributing](contributing.md)
