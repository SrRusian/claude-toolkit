---
name: task-closure
description: Use for any task that changes files (code, configuration or documentation): understand first, do it, verify for real, and close with a fixed-order report and a ready-to-copy git commit command. Also use at delivery time. Not for questions or analysis that change nothing.
---

# Task closure

The project's rules (CLAUDE.md) take precedence over this skill; this one fills in what they leave unsaid.

## 1. Before touching anything

1. Read the project's CLAUDE.md and the files you will touch. Search whether the component, function or style already exists before creating one.
2. State in one line what is requested and what is NOT requested. Do not add features, screens or options nobody asked for.
3. If the decision belongs to the user and cannot be resolved from the code or a reasonable default, ask once with concrete options. Otherwise decide, and say so in the report.
4. Before deleting or overwriting, look at the target.
5. Run `git status` to know which changes already existed, so they are not mixed with your own.

## 2. While working

- Make small changes consistent with the existing style. No duplicates: if something appears in two places, unify it.
- When touching a file, fix in the same pass whatever is clearly bad and in plain sight (overlong comments, duplicates). Anything large, or any decision that belongs to the user, is proposed, not done.
- If a real failure outside the scope appears, fix it when it is small; otherwise report it with evidence.
- Reject with evidence ideas (your own or others') that are wrong, and say when something is not advisable.
- Do not touch files unrelated to the task. Never print or version secrets (.env, tokens, credentials).
- Destructive or outward-facing actions (delete, force push, publish, send) need the user's explicit confirmation every time; an earlier approval does not carry over.
- If a hook, permission or test blocks something, do not work around it: report it and let the user decide.

## 3. Verify for real (before saying "done")

- Run the build, types, lint and the project's tests. If the logic changed, add or adjust the test that covers it.
- See it working: start the service, call the endpoint with curl or a script, or take a screenshot if it is visual (desktop and mobile, light and dark theme if both exist).
- Clean up the test data you created.
- If something could not be tested, say so plainly. Never report as done what you did not see working.
- If a test fails, report it with the real output, trimmed. Do not weaken or delete the test to make it pass.
- Use the user's shell syntax (on Windows usually PowerShell, not bash).

## 4. What travels with the code (only if needed)

- Documentation for the topic that changed, and a note in CLAUDE.md if how something works, or a decision, changed.
- New tests when the logic changes.
- If the change does not warrant them, touch none of these.

## 5. Final report

Short and direct, without repeating what the conversation already said. In this order:

1. **What was done**: what changed and why, in brief bullets. Links to the key files.
2. **How it was verified**: what was run and the result (real numbers: tests, timings, sizes).
3. **Decisions I made**: what I chose without asking, so the user can correct it.
4. **What was not done or not tested**, and why.
5. **Pending for the user**: only actions that are theirs (credentials, DNS, approving a deploy...).
6. **Commit** (see below).
7. **Shared-zone files**: if the project requires it, the exact list of files touched in folders owned by someone else.

Before writing the report, run `git status` and `git diff --stat` to list the real files, not the ones you remember. If the task was only a question or analysis, answer briefly, without this structure.

## 6. Commit command

Never run `git commit` or `git push`, and never deploy, unless explicitly asked. Deliver the command ready to copy:

```
git commit -m "Short Title In Title Case" -m "- first bullet" -m "- second bullet"
```

- Title in English, Title Case, imperative (Add, Fix, Move, Remove...), under about 70 characters.
- Body in English, 2 to 4 short bullets: what changed and why, not the list of files.
- One `-m` per bullet. No Co-Authored-By or signatures unless the project says otherwise.
- If there are unrelated changes, propose separate commits, each with its own `git add`.
- Put the `git add` with exact paths first; do not use `git add -A` if unrelated files exist.
- Write the command in the user's shell syntax. In PowerShell double quotes work the same; avoid double quotes inside the text.

## 7. Writing style

- No filler, no repetition, no explaining the obvious. One idea per bullet.
- No emojis and no em dashes.
- All text written into the repository (code comments, docs, skills, commit messages) is in English.

## 8. Closing checklist

Before handing over, confirm:

- [ ] I did what was asked and nothing that was not
- [ ] There are no duplicates or test leftovers
- [ ] It builds and tests pass, or I say which could not be run
- [ ] I saw it working, or I say that I could not
- [ ] There are no secrets in the changes
- [ ] The report follows the order of section 5
- [ ] The commit is delivered as a command, not executed
