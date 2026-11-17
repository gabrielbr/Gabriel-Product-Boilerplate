# Contributing: rules for people and agents

This repo is a **method**: a playbook, skills, templates and one script. It stays useful only while it stays small, consistent and generic. Agents read this file before changing anything here. [AGENTS.md](AGENTS.md) sends them to it.

`scripts/check.py` enforces most of the rules below. It runs on every pull request and must pass.

## 1. Before you add anything

Ask three questions, in order:

1. **Is it generic?** It must help any project of its track, not one client or one product. Project-specific rules belong in that project's own `AGENTS.md`.
2. **Does it already exist?** Search the playbook, the skills and the templates first. **Extend before you add**: a new section in an existing skill or template beats a new file.
3. **Where does it belong?**

   | It is… | It goes in… |
   |---|---|
   | A step, gate or rule of the method | `PLAYBOOK.md`, in the stage it belongs to |
   | Reusable know-how an agent loads on demand | a skill in `.claude/skills/<name>/` |
   | A file people fill in during a project | `templates/<name>.md` |
   | Something that creates or checks files | `scripts/` |
   | A rule for agents running the method | `AGENTS.md` |

If it doesn't pass question 1, don't add it.

## 2. Universal rules

- **No real names.** Nothing in this repo mentions a real client, product, person, company or private repo. The only exceptions are tools, the public sources a skill cites, and the author in `LICENSE`. Worked examples use fictional names ("Acme Coffee", "Example") or neutral wording ("a finance client"). Real hex values, logos and copy from client work are real data too: invent new ones.
- **No secrets or private data.** No tokens, emails, addresses, internal URLs or customer data.
- **Writing style.** Short, plain, concrete and in English. Sentence-case headings. Verbs first in checklists. No hype words, no emoji, no em dashes in the playbook or templates.
- **One source of truth.** Never copy a rule into two places. Link to it instead. If two files disagree, `PLAYBOOK.md` wins; fix the other file in the same PR.
- **Keep it small.** Each change should do one thing. Remove anything your change makes obsolete.

## 3. Adding or changing a skill

A skill is a folder in `.claude/skills/<name>/`:

```
<name>/
  SKILL.md          required
  references/       optional: deep material that SKILL.md links to by path
  scripts/          optional: tools the skill runs (Python 3 standard library, or say what to install)
  templates/        optional: files the skill fills in
  assets/           optional: data; no third-party copyrighted or trademarked files
  LICENSE           required if the skill isn't MIT
```

Rules:
- **Frontmatter.**
  - `name` equals the folder name: kebab-case, lowercase.
  - `description` says **what it does and when to use it**, in one or two sentences, starting with a verb or "Use when". The agent decides whether to load the skill from this line alone.
- **Shape of `SKILL.md`.**
  - Start with a short paragraph: what it does, when to use it, what it pairs with.
  - Use numbered sections.
  - End with a **checklist or an "Output" section** that an audit can answer row by row.
  - Keep it under ~400 lines. Move depth into `references/` and link each file from `SKILL.md`.
- **Generic.** No project names; examples are fictional.
- **No overlap.** If an existing skill covers half of it, extend that skill instead. Two skills must never give conflicting rules. If they would, decide which wins and write that in both.
- **Licence and source.** For third-party skills, keep their `LICENSE`/`NOTICE` and pin the upstream commit and version.
- **Register it in the same PR:**
  - `.claude/skills/VENDORED.md`: a row with name, purpose, source, version and licence;
  - `PLAYBOOK.md` → "The skills": the right table, marked "(in this repo)";
  - `AGENTS.md` → the skills-by-stage table, if it belongs to a stage;
  - `PLAYBOOK.md` appendix: a hand-run checklist, if the skill is part of the audit.
- **Changing a skill.**
  - Edit it here first; projects re-copy it.
  - Never edit an upstream skill (impeccable) in place. Update it from upstream and bump its version.

## 4. Adding or changing a template

- **Naming.**
  - The file name is kebab-case and says what it is (`brief.md`, `rebrand-checklist.md`).
  - Templates that become a project's own file keep that file's name (`PRODUCT.md`, `STATUS.md`, `AGENTS.project.md`).
- **Shape.**
  - First line: `# <Title>`.
  - Second: an italic line naming the playbook stage it serves.
  - Then the fields.
- **Placeholders.**
  - `{{UPPER_SNAKE}}` for values the script fills: `{{PROJECT}}`, `{{CODE}}`, `{{TRACK}}`, `{{DATE}}`. A new script-filled placeholder must be added to `fill()` in `scripts/new-project.sh`.
  - `{{Title case}}` for values a person fills.
  - Empty table cells for the rest.
- **Wiring.** A template is used by at least one stage. Register it in the same PR:
  - `PLAYBOOK.md`: the stage that uses it;
  - `AGENTS.md` → "What each stage leaves behind";
  - `README.md`: the list of templates;
  - `scripts/new-project.sh`, if it belongs in every new project of a track.
- **Prefer fields to prose.** A template is a form, not an essay.

## 5. Changing the process (the playbook)

- **Structure.** The **seven stages and three tracks** are the frame. Add steps inside a stage. A new stage or track needs a decision record in `docs/decisions/` explaining why the frame changes.
- **Shape of a stage.** Every stage keeps the same parts, in this order: **Goal → Skill(s) → Do (checklist) → Gate**. Add to the checklist rather than adding new kinds of section.
- **Gates** must be checkable by someone else: "the approver signed off in writing" passes; "it looks good" fails.
- **Update together.** In the same PR, update:
  - the stage;
  - the one-page start checklist at the end;
  - `AGENTS.md`, if an agent's behaviour changes;
  - the affected templates.
- **Where rules come from.** Rules come from practice: they were used on at least one real project. You can't name the project, but the PR description must say what problem the rule solved.

## 6. Scripts

- **Runtime.** Bash or Python 3, standard library only, with no network.
- **Usage.** Every script prints its usage when run with no arguments and is safe to run twice.
- **Tests.** Test it by running it into a temporary folder; say in the PR what you ran.

## 7. Every pull request

- **Branch and PR.** Work on a branch and open a PR. Never push to `main`. Write the title in plain words.
- **`CHANGELOG.md`.** Add a line under `## Unreleased` saying what changed for someone using the method.
- **Checks.** Run `python3 scripts/check.py`. It must pass. Never weaken the check to make it pass. If a rule is wrong, change the rule in this file and the check together, and say why.
- **Description.** Answer the three questions from §1. List every file you registered the change in.
- **Releases.** The maintainer moves "Unreleased" to a version (semver: major = a stage, track or skill removed or renamed; minor = something added; patch = wording and fixes) and tags it.
