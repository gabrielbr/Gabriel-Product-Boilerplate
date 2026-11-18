# Working in this repo (for agents)

{{PROJECT}}: one paragraph on what it is and who it's for. Read [README.md](README.md) first.

This project follows the Gabriel Product Boilerplate playbook (PLAYBOOK.md in that repo).

## Brand rules
1. **The one idea:** idea, tagline, what the brand never implies.
2. **Voice and copy:** the rules from `voice.md`, banned words, buttons verb-first, no invented data.
3. **Tokens:** every colour, size, radius and duration comes from the tokens. No literals in screens. Never hand-edit generated token files.
4. **Type:** families, scale, one h1 per page, line length.
5. **Logo:** use the files only; never retype or redraw. Clear space, minimum sizes.
6. **Graphic rule:** the one device and where it may appear.
7. **Texture and motion:** pausable; honours reduced motion; nothing that carries meaning is animated only.
8. **Components and layout:** screens compose the component kit; one primary action per screen; 390 px works.
9. **Before you finish, check:** contrast in every theme, colour never alone, targets ≥44–48, copy against the voice, the audit file written.

## Working with the person
- **Guide with questions.** Use the agent's question tool when it has one (`AskUserQuestion` in Claude Code); otherwise ask in chat with numbered options.
- **Keep rounds small:** at most four questions, 2–4 options each, the recommended one first with a one-line reason.
- **Ask, don't invent.** Facts and brand values come from the person or a named source.
- **End every turn with the next step:** one question or one clear action.
- **Stop-and-ask items** (see "Product law") always go through a question; never assume a yes.

## Design work
Every new or changed screen, flow, page or asset is designed with, and audited against, the skills in `.claude/skills/`, in this order:
1. ux-user-flows
2. impeccable
3. graphic-design-fundamentals
4. less-is-more

The audit goes in `audits/YYYY-MM-DD-<version>-<topic>.md`. Fix P0 and P1 before merging. Never claim a skill was used without loading it.

## How changes go in
- Work on a branch and open a PR. Merge when checks are green and reviews are resolved; then release.
- **Docs on every change.** A change without its docs isn't done. Update: README, CHANGELOG (plain words), `docs/<feature>.md`, `docs/roadmap.md`, `docs/decisions/`.
- Never skip or loosen a test to get green.

## Product law
- **Data:** what may never leave the device or the account.
- **Claims:** what the product must never claim (medical, financial, outcomes).
- **Stop and ask before:** deploying, sending messages, moving money, deleting data, renaming ids.

## Before you push
```sh
# replace with this project's real commands
<token check>  &&  <unit tests>  &&  <lint>  &&  <build>  &&  <screenshot tests>
```
