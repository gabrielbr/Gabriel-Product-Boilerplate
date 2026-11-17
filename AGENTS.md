# Agent guide: Gabriel Product Boilerplate

You are helping a person run a project through **the playbook** in [PLAYBOOK.md](PLAYBOOK.md). The project can be:

- a client brand or event,
- a product built with a team,
- an app.

This repo is **the method**, not the project. The person's project lives in its own folder or repo, created from this one (see "Starting a project").

Read `PLAYBOOK.md` before you do anything else. It is the source of truth. If this file and the playbook disagree, the playbook wins; fix this file.

## Your job

1. **Find the track and the stage.**
   - Ask which track this is (A client brand or event, B product with a team, C app), unless it's obvious.
   - Find the stage the project is at. Look for a `STATUS.md` in the project; if there's none, ask.
   - Never skip ahead. A stage starts only when the previous stage's **gate** has passed.
2. **Run one stage at a time.** For the current stage:
   - load the skills it names;
   - work through its checklist with the person;
   - fill the matching template from `templates/`;
   - check the gate.
3. **Write results into the project, not into the chat.** Every stage leaves files behind (see "What each stage leaves behind"). Update `STATUS.md` at the end of each stage: stage, date, gate passed, open items.
4. **Ask, don't invent.** Brand values, names, colours, client facts and approvals come from the person or from named sources. If a value has no source, ask for one or mark it `TBD (source needed)`.
5. **Approvals are the person's.** Name, direction and final delivery need a dated approval from the approver named in the brief. Never record an approval the person didn't give.

## Starting a project

- Run `scripts/new-project.sh "<Project name>" <CODE> <a|b|c> [target-dir]`. It creates the folder skeleton, copies the templates and writes `STATUS.md`.
- If you can't run scripts, create the same skeleton by hand (`PLAYBOOK.md`, "Set up once").
- For tracks B and C (code), also:
  - copy `templates/AGENTS.project.md` into the project repo as `AGENTS.md`;
  - add a `CLAUDE.md` containing `@AGENTS.md`;
  - copy `.claude/skills/` into the project repo.

## Skills

The core four and the three brand skills are in [`.claude/skills/`](.claude/skills/) ([VENDORED.md](.claude/skills/VENDORED.md)). Claude Code loads them by name. Other agents read each `SKILL.md` and the reference files it points to.

| Stage | Load |
|---|---|
| 1 Brief | `ux-user-flows` §1 (apps only, for `PRODUCT.md`) |
| 2 Strategy & name | `brand-identity-kit` (phase 0–1) |
| 3 Identity | `brand-identity-kit` (phases 2–6), `logo-design`, `graphic-design-fundamentals` (§6 identity) |
| 4 Design system | `brand-identity-kit` (phases 7–9), `impeccable` (design-system and DESIGN.md guidance), `graphic-design-fundamentals` §3–5 |
| 5 Screens & assets | `ux-user-flows` first, then `impeccable` while building, then `less-is-more` |
| 6 Audit | in order: `ux-user-flows` §13 → `impeccable` critique + audit → `graphic-design-fundamentals` §13 → `less-is-more` → `anti-slop` on copy and UI |

Rules for skills:

- **Use them while working**, not only at the end.
- **Honesty.** Never write that a skill was applied unless you loaded and read it. If a skill is missing, say so and run the playbook's appendix checklist by hand.
- **Precedence.** Where a skill's general advice conflicts with the project's design system or the person's instructions, the stricter project rule wins. The order is: the person's words, then the project's rules, then the skill.
- **Logo library:** `logo-design` ships only the library's index, not the SVGs (see VENDORED.md). Never copy or trace a library logo.
- **Native apps:** impeccable audits use `reference/audit.native.md` scored against `reference/android.md` or `reference/ios.md`. Its `detect` scanner is for web code only.

## What each stage leaves behind

| Stage | Files in the project |
|---|---|
| 1 | `00 Brief/brief.md`, `00 Brief/sources.md`, `PRODUCT.md` (apps) |
| 2 | `00 Brief/decisions/0001-name.md`, the strategy section of `02 Design System/README.md` |
| 3 | `01 Brand/directions/` (three directions, one approved, dated), `01 Brand/logo/`, `01 Brand/voice.md` |
| 4 | `02 Design System/README.md` (fixed outline), `tokens.json`, `AGENTS.md` brand rules in every code repo |
| 5 | `docs/flows/<flow>.md` (apps), screens and assets named `<CODE>_<Edition>_<Asset>_<Ratio>_<NN>.<ext>` |
| 6 | `audits/YYYY-MM-DD-<version>-<topic>.md` from `templates/audit.md` |
| 7 | `04 Deliveries/` with `00 Instructions – <Client> Design Assets` (track A); README, CHANGELOG, a release (tracks B/C) |

## Quality bars (check before you say a stage is done)

- **Contrast.** Text is at least 4.5:1 and graphics at least 3:1, in every theme. The ratios are written in the colour table.
- **The rule of one.**
  - Each project has one accent, one graphic device, and one type family (or a sans plus a mono).
  - Each screen has one primary action.
- **Meaning.** Colour is never the only carrier of meaning. A number always comes with its label.
- **Tokens only.** No literal colours, sizes or durations in screens. Generated token files are never edited by hand.
- **Copy.**
  - Short and plain, written in the person's words.
  - Verbs come first on buttons.
  - None of the voice doc's banned words; no tracking parameters in links.
- **Fix before shipping.** Every P0 and P1 audit finding is fixed before delivery or merge.

## Stop and ask

Stop and ask the person before you:

- choose or change a name, a colour, a typeface or the logo;
- record an approval;
- publish, send or post anything outside the project folder;
- delete files, or rename package or app ids;
- add a skill or tool the playbook doesn't name.

## Working in this repo itself

If you're asked to change the method itself (add or edit a skill, template, script or step), read [CONTRIBUTING.md](CONTRIBUTING.md) first and follow it. It is binding for agents.

The short version:
1. Is it generic? Does it already exist? Where does it belong?
2. Register it everywhere CONTRIBUTING.md lists.
3. Add a `CHANGELOG.md` line under `## Unreleased`.
4. `python3 scripts/check.py` passes.
5. Work on a branch and open a PR. Never push to `main`.

Never name a real client, product or person. This repo is meant to be shared.
