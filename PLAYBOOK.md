# Brand & Product Playbook

A step-by-step method for taking any project from a blank page to a delivered brand, product or app. It works the same for:

- a client's brand,
- an event,
- a software product,
- your own app.

Use it with an AI assistant (Claude) and a small set of **skills**: reusable instruction packs that the assistant loads at each step. Every step below says which skill to load, what goes in, what comes out, and how you know it's done.

---

## How to use this playbook

1. **Pick your track.** The seven stages are the same for everyone; only stages 5–7 change:

   | Track | You're making | Stage 5 produces | Stage 7 delivers |
   |---|---|---|---|
   | **A. Client brand or event** | identity, report, event visuals, social kit, simple website | covers, posts, banners, decks, web pages | a delivery folder with an instructions doc |
   | **B. Product (with a team)** | brand + website + web app or platform | homepage, launch kit, pitch deck, product UI | brand package in the code, launch posts |
   | **C. App (yours or a client's)** | mobile or web app | flows and screens, kept in step with the real app | a repo with rules, checks and a release on every merge |

2. **Work in order.** Each stage feeds the next. Skipping a stage is how projects drift: two reds, three fonts, a rebrand that's half done.
3. **Write things down where they win.** Every project has *one* source of truth per topic. If two places disagree, the source of truth wins and the other gets fixed.
4. **Run the gate at the end of each stage.** A stage is done when its checklist passes, not when it looks finished.

```
1 Brief & sources → 2 Strategy & name → 3 Identity → 4 Design system
  → 5 Screens & assets → 6 Audit → 7 Deliver & keep alive
```

---

## Set up once

**Folder skeleton** (Drive, Dropbox or a repo; same names everywhere):

```
<Project>/
  00 Brief/            brief.md, sources.md, decisions/
  01 Brand/            logo/, voice.md, directions/
  02 Design System/    README.md, tokens.json, components/
  03 Product | Editions/
  04 Deliveries/       01 Logo/, 02 Fonts and Colours/, 03 Textures/, 04 <Main piece>/, 05 <Supporting>/, 06 Social Media/
  audits/              YYYY-MM-DD-<version-or-edition>-<topic>.md
```

**File names**: `<CODE>_<Edition>_<Asset>_<Ratio>_<NN>.<ext>`, for example `ACME_2027_Carousel_4x5_03.png`. Anyone can find, sort and replace files without asking you.

**Templates**: everything below has a template in [`templates/`](templates/); `scripts/new-project.sh` creates the skeleton for you.

**Skills installed**: see [The skills](#the-skills) at the end. Install them before you start, and keep one version of each across all your projects.

---

## Stage 1 · Brief & sources

**Goal:** know who it's for, what it must do, and what already exists. Never invent what you can measure.

**Do**
- [ ] Write a one-page **brief** (template below).
- [ ] Ask the client for **3–5 keywords** and an **aesthetic direction**. Ask them to name similar work they liked, as you would for any branding job.
- [ ] Write the **"never looks like"** list. Example for a finance client: no coins, rockets, glowing charts, stock handshakes.
- [ ] List every **source**: existing logo files, live site, decks, design-tool files (Canva/Figma/Framer IDs), brand folders. Record where each value comes from ("sampled from the cover PDF", "measured on the live site, date").
- [ ] Name the **approver** and the **feedback channel** (one chat thread or one doc per project or edition).
- [ ] Apps only: write a `PRODUCT.md` (who uses it, the job, the context: one-handed? at night? in a hurry?, the success measure).

**Brief template**
```
Project:            Code (3–4 letters):
Audience:           Job to be done:
Keywords (3–5):     Never looks like:
Channels:           Deadline:            Approver:
Languages/locale:   Sources (with dates):
Out of scope:
```

**Gate:** you can say in one sentence who it's for and what it must do, and every value you'll use later has a named source.

---

## Stage 2 · Strategy & name

**Goal:** one idea, said in a few words, and a name you can own.

**Skill:** `brand-identity-kit` (phase 1).

**Do**
- [ ] **One idea** in 2–4 words. Example: "precise, discreet, factual".
- [ ] **Tagline** and **positioning line**: what it is, for whom, and why it's better than the alternatives.
- [ ] **Personality** as 4–5 "this, not that" pairs.
- [ ] **What the brand never implies.** Examples: no outcome promises, no medical claims, no hype.
- [ ] If naming, check availability before falling in love:
  - domain;
  - social handles;
  - package and app ids;
  - marketplace slugs;
  - pronunciation in your markets.
- [ ] Record the decision in `00 Brief/decisions/0001-name.md`: the name, its meaning, how to say it, the options you rejected and why.
- [ ] Choose permanent ids (app id, package name) **once**. Never rename them later.

**Gate:** the approver has signed off the idea and the name in writing, with a date.

---

## Stage 3 · Identity

**Goal:** a recognisable identity built from very few, very deliberate elements.

**Skills:** `brand-identity-kit` (phases 2–6), `logo-design`, `graphic-design-fundamentals`.

**The rule of one.** Strong identities use one of each element below, and each one has a job:

| Element | The rule | Example |
|---|---|---|
| Accent colour | **One** accent, **one** meaning, ≤10% of any surface | "Exactly one red element per page; red marks the most important thing" |
| Graphic device | **One** motif, taken from the logo | an angle cut taken from a letter of the logo |
| Type | **One** family (or one sans + one mono) | a light weight for display, regular for body, medium for labels |
| Texture / animation | Derived from the logo; pausable; respects reduced motion | a field of dots forming the event's location |

**Do**
- [ ] Show **three directions**, side by side, in one place. Get one approved, and record the date.
- [ ] Build the **logo pack**:
  - full logo, monogram (for widths under ~120 px), inverted;
  - SVG, PNG @1x/@2x/@4x, PDF, EPS;
  - favicons at 32, 180 and 512 px;
  - clear space (e.g. the height of one letter), minimum sizes, and the don'ts (stretch, recolour, shadow, busy photo).
- [ ] Write the **voice doc**:
  - three words;
  - sentence length;
  - a banned-word list ("unlock, seamless, leverage, next-generation, game-changer, cutting-edge");
  - no emoji, no exclamation marks, no em dashes;
  - numbers always with their label ("54 companies", never a bare "54");
  - language and locale rules (spelling, quotation marks, thousands separator);
  - link hygiene: strip tracking parameters from every URL.
- [ ] Define the **imagery** treatment (subject, colour treatment, what's banned) and the **icons** (one line set, one stroke weight, function only).

**Gate:** the identity passes the `graphic-design-fundamentals` critique: it works in greyscale, works at 16 px, and works in one colour.

---

## Stage 4 · Design system

**Goal:** one browsable reference that people *and* AI agents build from. Values are written once and used everywhere.

**Skills:** `brand-identity-kit` (phase 7), `impeccable` (design-system mode), `create-design-md` (optional).

**Do**
- [ ] Create the design system (a Claude **Design System** artifact, or a repo folder) with a `README.md` in **this fixed outline**:
  1. Character (one idea, three words, the "never" list)
  2. Voice
  3. Logo
  4. Colour (table: token · light · dark · role, **with contrast ratios**)
  5. Typography (web scale, and print scale if there's print)
  6. Grid & space (spacing scale, page grids per format)
  7. Graphic device
  8. Imagery
  9. Icons
  10. Components (each with a one-paragraph rule and a preview)
  11. Production (print colour mode, export settings, where files go)
- [ ] Put every value in `tokens.json`, each with a one-line **usage note**. Generate CSS or code from it; never hand-edit generated files.
- [ ] Meet these **contrast** minimums in *every* theme: text 4.5:1, graphics 3:1. Write the ratios into the colour table.
- [ ] Give each **semantic colour** one meaning, always next to a word. Colour is never the only carrier of meaning.
- [ ] **Recurring brands** (events, annual reports): keep one master brand plus one file per edition (`editions/<edition>.md`). Only the subject, the edition's motif and the copy change between editions. The master wins on any conflict.
- [ ] **Code projects:** layer the system:

  ```
  core     shared by all your apps    (spacing, radii, motion, type scale, components, rules)
  brand    the client's look          (colour roles + the type family + the mark, nothing else)
  product  this app only              (its own tokens and components)
  ```

  Decide where each change belongs: *Could any app use it? → core. Is it the client's look? → brand. Only this product? → product.* Run a `--check` in CI that fails on drift, broken scale, too-small type, or failed contrast.
- [ ] Write an **`AGENTS.md`** (brand rules for coding agents) in every repo that uses the brand. Use this outline:
  1. The one idea
  2. Voice & copy
  3. Tokens
  4. Type
  5. Logo
  6. Graphic rule
  7. Texture
  8. Components & layout
  9. Before you finish, check

**Gate:** a person or an agent who has never seen the project can build a correct page from the system alone.

---

## Stage 5 · Screens & assets

**Goal:** real pieces, built only from the system.

**Skills:** `ux-user-flows` first, then `frontend-design`/`impeccable` while building, `value-focused-landing-page` for marketing pages.

**Do: apps and websites**
- [ ] **Flows before screens.** For each flow, write down:
  - entry points;
  - steps;
  - branches;
  - every state (empty, loading, partial, error, success, offline);
  - exits.

  Count the **taps** for common actions. Store each flow as `docs/flows/<flow>.md`.
- [ ] Prototype at **1440 and 390 px**, in **light and dark**.
- [ ] Keep a **design canvas** (a Claude Design artifact, or Figma) where the client comments. Feed it real screenshots from the build, so the design and the product move together both ways.
- [ ] Use **components only**: no hand-drawn buttons, no literal colours or sizes in screens. Give each screen **one primary action**.
- [ ] **Remember what was done last.** Pre-fill the last choice and show "Last time: …".
- [ ] Prefer **undo** over "are you sure?" wherever it's safe.

**Do: brand and campaign assets**

Standard sizes:

| Asset | Size |
|---|---|
| Post / carousel | 1080 × 1350 (4:5) |
| Story | 1080 × 1920 (9:16) |
| LinkedIn page banner | 1584 × 396 |
| Deck / link post | 1920 × 1080 |
| Report | A4, 3 mm bleed |

- [ ] Plan a **launch kit as a schedule**: teaser (−7 days) → launch day → carousel or explainer after launch.
- [ ] Keep editable sources in one folder per edition. Upload the brand fonts to the shared tool (e.g. Canva) so others can edit without breaking the type.

**Gate:** every piece uses only system tokens, components and approved assets.

---

## Stage 6 · Audit

**Goal:** catch problems before the client or the users do. The audit is a written record, not a feeling.

Run the skills **in this order**. Use them while designing too, not only at the end.

| # | Skill | When | What you record |
|---|---|---|---|
| 1 | `ux-user-flows` | apps, sites, forms | its 15-point flow review |
| 2 | `impeccable` | anything visual | `critique` + `audit`: five dimensions scored 0–4, findings tagged **P0–P3** |
| 3 | `graphic-design-fundamentals` | everything | its 13-point critique |
| 4 | `less-is-more` | screens, flows, pages | the five questions per element; **what was cut** |
| 5 | `anti-slop` | all copy and UI | generic-AI patterns removed |

- [ ] Write it to `audits/YYYY-MM-DD-<version>-<topic>.md`: one section per skill, plus **What was cut**.
- [ ] **Fix every P0 and P1** before delivering or merging.
- [ ] Translated or second-language copy gets its own **copy review**, by a native reader if possible.
- [ ] **Honesty rule:** never write that a skill was applied unless it was actually loaded and read. If one wasn't available, say so and apply its checklist by hand (see the appendix).
- [ ] Do a **real-size test**: logo at 16 px, poster from 3 m, app on a real phone with large text, the screen reader and "remove animations" turned on.

**Gate:** the audit file exists, P0/P1 are fixed, and the checklists pass.

---

## Stage 7 · Deliver & keep alive

### Track A: client delivery
- [ ] Use numbered folders (see the skeleton above) and add an **`00 Instructions – <Client> Design Assets`** doc. It covers:
  - **Folders:** what's in each, and what it's for.
  - **Logo:** which version, which colour, which format (SVG for web and tools, PNG when SVG isn't accepted, PDF/EPS for print), favicon sizes, and the don'ts.
  - **Fonts and colours:** how to install the fonts; the colour table with each colour's use; the accent rule.
  - **Textures:** which go on dark grounds and which on light; never put text on dense patterns.
  - **The main piece:** the approved direction, and which file is for print, web or social.
  - **Social:** which post, which date, which size, the exact link (no tracking tags).
  - **Editing:** the folder in the shared design tool.
  - **Ground rules:** four lines at most.
  - **Contact:** who to ask.
- [ ] Hand over `tokens.json` too, for the client's own tools.

### Track B/C: code
- [ ] `AGENTS.md` is the entry point for every agent (`CLAUDE.md` contains just `@AGENTS.md`).
- [ ] **Docs on every change:** a change without its docs isn't done. Update:
  - `README.md` (what it does);
  - `CHANGELOG.md` (plain words);
  - `docs/<feature>.md`;
  - `docs/roadmap.md` (ideas move out of it as they ship);
  - `docs/decisions/` (decision records).
- [ ] **CI checks:**
  - tokens `--check`;
  - unit tests;
  - screenshot tests;
  - lint;
  - a permission allow-list (the build fails if permissions grow);
  - an audit file required on UI changes.
- [ ] **Merge and release** as soon as checks are green and reviews are resolved. Never leave finished work waiting. Publish checksums (`SHA256SUMS.txt`) with each release.
- [ ] Write **product law** into `AGENTS.md`: privacy (what data may never leave), what the product must never claim, and what agents must stop and ask about.
- [ ] **Promote upward:** when one product invents something every product could use, move it into the shared core. Each core release lists "what each app has to do".

### Rebrands
Run this checklist **before** announcing:

- [ ] domain + 301 redirects + search console
- [ ] social handles
- [ ] marketplace / plugin slugs
- [ ] repos and package names
- [ ] SDKs
- [ ] screenshots
- [ ] decks
- [ ] demos
- [ ] READMEs
- [ ] email sending domain
- [ ] announcement posts
- [ ] update banner on old articles

Half-done rebrands linger for months.

**Gate:** someone else can use the deliverable without asking you a question.

---

## The skills

All the skills below marked **in this repo** are in `.claude/skills/`. Skills are folders with a `SKILL.md` file: a `name`, a `description` (when to use it), then numbered sections ending in a checklist. Keep them in one central repo, install them in each project (e.g. `.claude/skills/`), record the version you copied in a `VENDORED.md`, and update all projects together.

### Core four (every screen, page and flow)

| Skill | What it's for | Use at |
|---|---|---|
| **ux-user-flows** (in this repo) | Frame the problem, choose research methods, map flows, design every state, write forms, errors and onboarding, check accessibility in flows; ends with a 15-point flow review | Stage 1 (PRODUCT.md), 5, 6 |
| **impeccable** (in this repo) | Design, critique, audit and polish interfaces (web and native iOS/Android). Commands such as `critique`, `audit`, `polish`; scores five dimensions 0–4; tags findings P0–P3. Public: github.com/pbakaus/impeccable | Stage 4, 5, 6 |
| **graphic-design-fundamentals** (in this repo) | Composition, typography, colour, grids, identity, editorial, packaging, campaigns, signage, UI and motion, production; ends with a 13-point critique | Stage 3, 4, 6 |
| **less-is-more** (in this repo) | Removes what doesn't earn its place: five questions per element, screen rules, flow rules, a "what was cut" list | Stage 5, 6 |

### Brand

| Skill | What it's for |
|---|---|
| **brand-identity-kit** (in this repo) | The whole identity, or a rebrand, in phases: 0 sources, 1 strategy, 2 logo, 3 tokens, 4 graphic rule, 5 texture and animation, 6 voice, 7 design system, 8 brand-foundations page, 9 AGENTS.md, 10 prototypes, 11 presentation, 12 quality passes, 13 delivery |
| **logo-design** (in this repo) | Brief → concepts → mark type → clean geometric SVG → optical fixes → tests (16 px, one colour, reversed) → presentation → export variants and guidelines |
| **anti-slop** (in this repo) | Rules that keep UI and copy from looking AI-generated |

### Optional specialists (pick one per project, for its weak point)

| Skill | What it's for |
|---|---|
| frontend-design | Baseline for distinctive UI (Anthropic's public skill) |
| create-design-md | A `DESIGN.md` from an existing site or repo |
| design-taste-frontend | Art direction for landing pages (use this **or** a DESIGN.md layer, never both) |
| ui-design-brain | A library of component patterns |
| make-interfaces-feel-better / emil-design-eng | Micro-interactions and polish |
| baseline-ui | A fast clean-up pass |
| better-icons | Finding icons |
| web-design-skills | SEO, `llms.txt`, accessibility, launch audits |
| value-focused-landing-page | Turns a feature-led page into an outcome-led one |
| logo-focused-announcement-post | Partnership announcement images |

### Claude surfaces used along the way

| Surface | What it's for |
|---|---|
| **Design System** artifact | The brand's home (Stage 4) |
| **Design** artifact | Canvas for screens, posts and posters, where the client comments (Stage 5) |
| **Slides** | Rebrand rationale and pitch decks |
| **Docs** | Briefs, audits, copy reviews, dev handoff notes |
| **Claude Code** | Builds and ships the code, following `AGENTS.md` |

---

## Appendix · Run the checklists by hand

Use these if a skill isn't installed. Report every issue by severity (critical / important / polish), with the principle it breaks and a concrete fix.

### Flow review (ux-user-flows)
1. **Job:** one actor, one job story, a clear success measure?
2. **Entries:** every real entry point covered, including deep links, notifications, returning mid-task?
3. **Happy path:** as short as it can be; nothing asked before it's needed?
4. **Branches:** every outcome drawn, including cancel, back, failure?
5. **States:** empty, loading, partial, error, success, offline, for each step?
6. **Errors:**
   - prevented where possible;
   - shown inline, in plain words;
   - what was typed is kept;
   - a recovery path is clear?
7. **Control:** a way back and out at every step; undo preferred over confirm?
8. **Progress and resume:** progress shown and state saved in multi-step flows?
9. **Memory:** nothing must be remembered across steps; nothing asked twice?
10. **Exits:** no dead ends; success leads to a useful next step?
11. **Conventions:** platform patterns followed unless clearly better?
12. **Speed:** feedback within the 0.1 / 1 / 10 s limits; long waits cancellable?
13. **Accessibility:**
    - WCAG 2.2;
    - keyboard and screen reader;
    - target sizes;
    - no drag-only actions?
14. **Ethics:** no deceptive patterns; costs and commitments clear up front?
15. **Evidence:** assumptions marked; a test planned for the riskiest one?

### Critique (graphic-design-fundamentals)
1. **Brief:** does it solve the stated problem, for the stated audience, in the stated medium?
2. **Concept:** is there a clear idea, or only decoration?
3. **Hierarchy:** squint test. Is there a clear first, second and third read?
4. **Contrast:** are differences decisive, not timid?
5. **Alignment and grid:** any accidental near-misses?
6. **Spacing:** consistent, from the system; does proximity group correctly?
7. **Typography:** at most 2 typefaces; good line length, leading and rag; correct punctuation characters?
8. **Colour:** works in greyscale; accent sparing and meaningful; passes WCAG?
9. **Consistency:** the same treatment for the same role everywhere?
10. **Simplicity:** what can be removed without loss?
11. **Real-size test:** checked at actual size, distance and device?
12. **Accessibility and ergonomics:** legible; meaning not carried by colour alone; keyboard focus; touch targets; reduced motion?
13. **Production:** colour mode, resolution, bleed, formats, fonts?

### Audit (impeccable)
Score five dimensions from 0 to 4 (total out of 20):

| Platform | Dimensions |
|---|---|
| Native apps | accessibility, performance, appearance & theming, platform conformance, adaptivity |
| Web | the equivalent web dimensions in the skill |

Tag each finding:
- **P0:** blocks the task
- **P1:** serious
- **P2:** should fix
- **P3:** polish

Fix P0 and P1 before shipping.

### Less is more
For every label, number, line, card, button, chip, hint, ask:
1. Does it help the **next thing** the person does, or a decision they make today? → keep it, ordered by how often it's used.
2. Is it **already shown** on this screen or one tap away? → show it once, nearest its action.
3. Is it needed **every time**, or only to understand once? → one tap away, or shown until first use.
4. Does it serve the product's **goal**? If weakly → group it or move it.
5. Is it used **weekly or less**? → settings or a sheet.
6. None of these → **remove it**.

**Screen rules**
- One subject and one primary action per screen.
- A number only with its meaning.
- No permanent hints.
- At most one "i" per screen.
- Defaults over questions.
- No duplicate paths.

**Flow rules**
- Removing clutter never adds a tap to a common action.
- No dead ends.
- Undo instead of confirm.

---

## One-page start checklist

```
□ Folder skeleton + project code
□ Brief: audience, job, 3–5 keywords, never-looks-like, approver, channel, deadline, sources
□ Strategy: one idea, tagline, positioning, this-not-that, never-implies   [brand-identity-kit]
□ Name: availability check → decision record → permanent ids chosen once
□ Identity: 3 directions → approval (dated) → logo pack + voice doc       [logo-design, GDF]
□ Design system: fixed README outline + tokens.json + contrast table + AGENTS.md
□ Code: core / brand / product layers, --check in CI
□ Flows → screens/assets (1440/390, light/dark, standard sizes)            [ux-user-flows, impeccable]
□ Audit file: flows → impeccable → GDF → less-is-more → anti-slop; fix P0/P1
□ Deliver: numbered folders + 00 Instructions | merge + release + checksums
□ Promote anything reusable into the shared core; rebrand checklist if renaming
```
