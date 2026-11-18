# Changelog

## Unreleased
- CONTRIBUTING.md: rules for adding skills, templates, scripts and process changes, for people and agents.
- scripts/check.py and a pull-request workflow that enforce them.
- The design-system README template is now `templates/design-system-readme.md`.
- The rebrand checklist template is linked from the playbook.
- Author byline with gabriellopes.com on the playbook and README.
- Agents now guide the person with interactive questions: a "Guide the person" section in `AGENTS.md` (question tool or numbered options, small rounds, a recommended option, the next step at the end of every turn, where each stage starts) and a matching section in `templates/AGENTS.project.md`.

## 0.1.0 · 2026-11-17
- The playbook: seven stages, three tracks, gates, skills, hand-run checklists.
- Agent guide (`AGENTS.md`, `CLAUDE.md`) for running the playbook with an AI agent.
- Seven skills in `.claude/skills/`: the core four, plus brand-identity-kit, logo-design (library index only) and anti-slop.
- Templates and `scripts/new-project.sh`.
