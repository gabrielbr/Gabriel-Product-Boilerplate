# Gabriel Product Boilerplate

_By Gabriel Lopes · [gabriellopes.com](https://gabriellopes.com)_

A method, templates and AI skills for taking a **brand, product or app** from a blank page to delivery, in seven stages:

```
1 Brief & sources → 2 Strategy & name → 3 Identity → 4 Design system
  → 5 Screens & assets → 6 Audit → 7 Deliver & keep alive
```

It works for three kinds of project (tracks):

| Track | You're making |
|---|---|
| **A** | a client's brand, event, report or social kit |
| **B** | a product with a team: brand, website, platform |
| **C** | an app |

## What's here

| Path | What it is |
|---|---|
| [PLAYBOOK.md](PLAYBOOK.md) | The method. Each stage gives its goal, skills, checklist and gate. An appendix holds checklists you can run by hand. |
| [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) | Instructions for an AI agent (Claude Code, Cursor, Codex…) to guide you through the playbook |
| [.claude/skills/](.claude/skills/) | Seven skills. Core: `ux-user-flows`, `impeccable`, `graphic-design-fundamentals`, `less-is-more`. Brand: `brand-identity-kit`, `logo-design`, `anti-slop`. Details in [VENDORED.md](.claude/skills/VENDORED.md). |
| [templates/](templates/) | Brief, sources, decision record, PRODUCT.md, voice, design-system README, tokens, project AGENTS.md, flow, audit, client delivery instructions, rebrand checklist, status |
| [scripts/new-project.sh](scripts/new-project.sh) | Creates a project folder from the skeleton and templates |
| [scripts/check.py](scripts/check.py) | Checks the repo against [CONTRIBUTING.md](CONTRIBUTING.md); runs on every pull request |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Rules for adding skills, templates and process changes |

## Quick start

**With an agent (recommended).** Clone this repo, open it in Claude Code (or any agent that reads `AGENTS.md`), and say:

> Start a new project with the playbook. It's a <client brand / product / app> called <name>.

The agent picks the track, creates the project folder and walks you through each stage. It loads the right skill at each step and stops at each gate for your approval.

**By hand.**
```sh
git clone https://github.com/<you>/Gabriel-Product-Boilerplate.git
cd Gabriel-Product-Boilerplate
scripts/new-project.sh "Acme Coffee" ACME a ../acme-coffee
```
Then open `PLAYBOOK.md` and start at Stage 1.

## Skills

- **Included:** the four core skills and the three brand skills. Claude Code loads them automatically when you work in this repo, or in a project created from it (tracks B and C copy them in).
- **Logo library:** `logo-design` ships the index of its reference library but not the logo files, which are trademarks of their owners.
- **Not included:** the optional specialists. The playbook names them; install them if you have them.

## Contributing

Want to add a skill, a template or a step? Read [CONTRIBUTING.md](CONTRIBUTING.md) first. Agents read it too. Every pull request runs `python3 scripts/check.py`.

## Licence

- Everything in this repo is [MIT](LICENSE), except `.claude/skills/impeccable/`.
- `.claude/skills/impeccable/` is Apache-2.0 (see its `LICENSE` and `NOTICE.md`).
