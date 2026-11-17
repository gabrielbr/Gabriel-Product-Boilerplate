# Skills in this boilerplate

These skills load in Claude Code automatically from `.claude/skills/`. In other agents, read the `SKILL.md` and the reference files it names.

| Skill | What it's for | Source | Licence |
|---|---|---|---|
| `ux-user-flows/` | Flows, states, forms, errors, onboarding, IA; ends with a 15-point flow review (§13) | The author's own skill | MIT (this repo) |
| `graphic-design-fundamentals/` | Composition, type, colour, grids, identity, editorial, UI, motion, production; ends with a 13-point critique (§13) | The author's own skill | MIT (this repo) |
| `less-is-more/` | Five questions per element; what stays, moves or goes | The author's own skill (1.0) | MIT (this repo) |
| `brand-identity-kit/` | A full identity or rebrand in 14 phases (0–13): sources, strategy, logo, tokens, graphic rule, texture and animation, voice, design system, brand-foundations page, AGENTS.md, prototypes, presentation, quality passes, delivery | The author's own skill | MIT (this repo) |
| `logo-design/` | Brief → concepts → mark type → geometric SVG → tests → presentation → export variants; scripts to audit SVGs and make test sheets, boards and icon sets | The author's own skill | MIT (this repo); see the note on the library |
| `anti-slop/` | Rules that stop UI and copy from looking AI-generated | The author's own skill | MIT (this repo) |
| `impeccable/` | Design, critique, audit and polish for web and native apps; scores five dimensions 0–4 and tags findings P0–P3 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable): skill 4.9.2, launcher 0.1.25 | Apache-2.0 (`impeccable/LICENSE`, `impeccable/NOTICE.md`) |

## The logo library

`logo-design` refers to a reference library of 1,400+ real-world SVG logos. Only its index ships here (`assets/library/catalog.json`, `classifications.json`, `stats.json`): the SVG files themselves are trademarks of their owners and aren't redistributed.

- `search_library.py --summary` and the category insights work from the index.
- File paths, preview sheets and comparisons need your own copy of `assets/library/svg/`.

## Not included

The optional specialists in the playbook aren't shipped here: `frontend-design` (Anthropic's public skills), `create-design-md`, `design-taste-frontend` and the others. Install them yourself or use the hand-run checklists in `PLAYBOOK.md`.

## Keeping them current

- Use one version of each skill across all your projects.
- Update impeccable from its upstream repo. When you do, bump the version in this table.
- To change one of the author's skills, edit it here first, then re-copy it into your projects.
