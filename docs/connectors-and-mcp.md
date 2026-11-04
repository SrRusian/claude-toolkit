# Connectors and MCP servers

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Design workflow](design-workflow.md) · [Contributing](contributing.md)

---

## Connectors

Enabled in claude.ai > Customize > Connectors.

| Connector | Type | Used for |
|---|---|---|
| Claude in Chrome | Desktop (included) | Drive the real Chrome with its sign-ins |
| Desktop Commander | Desktop | Terminal and file control on the machine |
| Filesystem | Desktop | Read and write local files |
| GitHub integration | Web | Repos, issues, pull requests |

Plugin MCP servers (Firebase, Playwright, LinkedIn) are listed under their plugins. The Engineering
and Design plugins also expose connectors (10 and 9) that need authorization before use.

## MCP servers

MCP (Model Context Protocol) servers give an AI host extra tools. Install them per host; this
repo only documents them. Never commit tokens, `.env` files or an `mcp.json` that contains
credentials.

### Firebase MCP server (Claude Code)

Docs: [firebase.google.com/docs/ai-assistance/mcp-server](https://firebase.google.com/docs/ai-assistance/mcp-server)

Requires Node.js and npm. It runs locally and uses the Firebase CLI credentials (or Application
Default Credentials); the `firebase_login` tool signs in or checks status.

```
# Option 1 (recommended, what I use): plugin
claude plugin marketplace add firebase/firebase-tools
claude plugin install firebase@firebase

# Option 2: plain MCP server, run from the app folder
claude mcp add firebase npx -- -y firebase-tools@latest mcp
claude mcp list
```

Equivalent JSON (`mcpServers` format, for hosts configured by file):

```json
{ "mcpServers": { "firebase": { "command": "npx", "args": ["-y", "firebase-tools@latest", "mcp"] } } }
```

Optional flags, appended after `mcp`: `--dir <absolute path to the folder with firebase.json>` and
`--only <group,group>` to expose only some tool groups (core is always on).

| Group | Tools |
|---|---|
| core | login/logout, project and app info, SDK config, create project/app, environment, `firebase_init`, deploy and status, security rules, `firebase://` resources |
| apphosting | Backends and logs |
| auth | Get and update users, SMS region policy |
| firestore | Document CRUD, queries, aggregations, databases, indexes, backups |
| dataconnect | Build, list and run SQL Connect operations |
| crashlytics | Issues, events, notes, reports, state |
| realtimedatabase | Read and write data |
| functions | Logs and function listing |
| messaging | Send FCM messages |
| remoteconfig | Get and update templates |
| storage | Download URLs |
| developerknowledge | Search Google developer docs |

It also ships prompts (`/firebase:init`, `/firebase:deploy`) and agent resources. List them with
`npx firebase-tools@latest mcp --generate-tool-list` (also `--generate-prompt-list`,
`--generate-resource-list`).

Tip: enable only the groups a project needs (`--only auth,firestore`) to keep the tool list small
and reduce risk. Check security rules before deploying.
Complements: `engineering:deploy-checklist` before `firebase_deploy`; `engineering:architecture`
for data-model decisions.

### Adding MCP servers to Android Studio (Gemini)

Docs: [developer.android.com/studio/gemini/add-mcp-server](https://developer.android.com/studio/gemini/add-mcp-server)

This is a different host (Gemini's Agent mode in Android Studio), not Claude. Steps:

1. File > Settings > Tools > AI > MCP Servers (on macOS: Android Studio > Settings).
2. Tick **Enable MCP Servers**.
3. Paste the configuration; it is saved as `mcp.json` in Android Studio's configuration directory.
4. Click OK. If the server needs login, click **Start Login** and sign in through the browser.
5. Type `/mcp` in the chat to list the tools.

```json
{
  "mcpServers": {
    "figma":  { "httpUrl": "https://mcp.figma.com/mcp" },
    "notion": { "httpUrl": "https://mcp.notion.com/mcp" },
    "linear": { "httpUrl": "https://mcp.linear.app/mcp" },
    "github": {
      "httpUrl": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer <YOUR_PERSONAL_ACCESS_TOKEN>" }
    }
  }
}
```

| Option | Meaning |
|---|---|
| `httpUrl` | Required. Streamable HTTP endpoint |
| `url` | Use instead of `httpUrl` for SSE endpoints (usually ending in `/sse`) |
| `headers` | Extra HTTP headers, for example an Authorization token |
| `timeout` | Milliseconds; -1 means none (default) |
| `enabled` | `true` by default |

Limitations: no `stdio` transport, so local servers such as the Firebase one above (`npx ...`)
cannot be added there; no MCP resources or prompt templates; OAuth does not work with some servers
such as GitHub, which is why a personal access token is used. Keep that token out of the repo and
use a fine-grained token with the minimum scopes.

---

[← README](../README.md) · [Getting started](getting-started.md) · [design-kit](design-kit.md) · [dev-workflow](dev-workflow.md) · [Anthropic plugins](anthropic-plugins.md) · [Design tools](design-tools.md) · [Connectors & MCP](connectors-and-mcp.md) · [Design workflow](design-workflow.md) · [Contributing](contributing.md)
