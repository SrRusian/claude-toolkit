# Contributing and maintenance

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)

---

## Adding or changing a skill

1. Check the catalog: if an upstream skill already does it, install that instead of copying.
2. Create `plugins/<plugin>/skills/<skill-name>/SKILL.md` (create the plugin and add it to
   `marketplace.json` if it is the first skill in that domain).
3. If it is derived from another source, check its license and record it in the plugin's
   `NOTICE.md`; keep copyright notices.
4. Write the `description` as "Use when ...", add numbered rules and a verification step, and put
   long detail in `references/`.
5. Evaluate it with `skill-creator`, run `claude plugin validate .`, bump the plugin version, and
   update this README.

## Maintenance

- After changing a plugin here: `claude plugin validate .`, then `/plugin update design-kit` (or
  reinstall) to refresh the installed copy.
- Review the catalog when a plugin updates upstream; versions here are those last seen.
- Watch for duplicates between standalone skills and plugins.

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Workflow](workflow.md) · [Contributing](contributing.md)
