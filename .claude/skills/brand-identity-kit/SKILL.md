---
name: "brand-identity-kit"
description: "Use when creating or rebranding a product's identity: strategy, logo, tokens, signature texture and animation, voice, design system, Brand Foundations page, AGENTS.md, page prototypes and deck."
---

# Brand identity kit

A repeatable process for building a complete brand, from the one idea down to the files a coding agent follows. Distilled from a real product rebrand (Oct 2026), the worked example used throughout (called "the example" below).

The kit always ships these deliverables:

1. **Brand Foundations** page (strategy, logo, color, type, graphic rule, texture, voice, website, AGENTS.md)
2. **Design System** (tokens, components, logo assets, texture component)
3. **Signature texture and animation** derived from the logo and concept (never optional)
4. **AGENTS.md** so coding agents follow the brand
5. **Page prototypes** (homepage, plus a reskin of the live site if one exists), desktop and 390px mobile, light and dark
6. **Presentation** of the rationale and before/after
7. Everything saved to the project's folder and/or source-of-truth page

Work additively: new versions sit beside old ones unless the person says to replace them.

---

## Phase 0 — Ground it in the source of truth

- Find the project's source of truth (Notion page, project docs, project instructions) and read it fully, including sub-pages and linked databases. Each Notion sub-page needs its own fetch with the full URL.
- Look at the live product. `WebFetch` can return stale/cached pages; for the current state use a browser (built-in browser or Chrome) and read `document.body.innerText` plus all links.
- Note where deliverables must live (local folder via the device bridge, Notion, project docs). Ask once if unknown.
- List the open business questions (pricing, who pays, feature status). Flag them; never guess them into copy.
- Note the gap between what the site says now and where the strategy is going. That gap is usually the brief.

## Phase 1 — Strategy

Produce, in plain sentences:

- **The one idea** (2–4 words) that every decision serves. Example: *Show the record.*
- **Tagline** (short, verb-led). Example: *Find AI agents. Check the record.*
- **Positioning statement**: for whom, what it does, how it differs, what it is not.
- **Personality**: 4–5 traits with a one-line "this, not that" each (e.g. precise, impartial, plain-spoken, shows its work, calm).
- **What the brand never implies** (Example: a listing is not an endorsement).
- **Scope stance**: who and what it covers, stated so it can't be misread (Example: agnostic, web2 and web3 side by side; on-chain identity is one source of evidence, not the point).

## Phase 2 — Logo

- Present **three directions**, each built from the concept, with rationale and a recommendation. Show each at small sizes and on dark.
- The winning mark should *say the idea*. Example: the *a* is an open ring (the claim) held up by a solid blue stem (the evidence); the same *a* is the symbol.
- Deliver as SVG files, never live text: `wordmark-color`, `wordmark-color-dark`, `wordmark-white`, `symbol-color`, `symbol-color-dark`, `symbol-white`, `app-icon`, `favicon`.
- Usage rules: which file on which ground, clear space (height of a key glyph), minimum sizes, and a don't list (no added seals/checkmarks, no recoloring, stretching, outlining, rotating, gradients, busy photos).
- If an old logo exists, show old vs new and why.

## Phase 3 — Color and type tokens

- Small palette with roles and rough proportions (Example: paper ~70%, ink, graphite, rule, one accent ~3%, soft accent tint, on-accent, on-ink; success/warning/danger for product states only, always with a word).
- Every token defined for **light and dark**. Body text ≥ 4.5:1 in both. Check focus-ring contrast too.
- The accent has one meaning ("the one thing that matters on this screen"), never a value judgment like "safe".
- Type: one sans for words, one mono for anything checkable (IDs, timestamps, counts, labels). Give a full scale (px / line-height / weight / tracking) and the Google Fonts URL.
- Spacing on a 4px base, radius per element type, border weights, and a stance on shadows/gradients (Example: none).

## Phase 4 — The brand's graphic rule

Find one visual rule where **form carries meaning**, so the brand is recognisable without the logo. The example's evidence ladder:

| Level | Meaning | Style |
|---|---|---|
| declared | what it says about itself | dashed border, no fill |
| retrieved | fetched from a source, timestamped | solid border, no fill |
| observed | evidence from use | solid fill |

Meaning never depends on color alone; always print the word. Build it into components.

## Phase 5 — Signature texture and animation (always propose)

Every brand gets a texture and motion proposal, and it must come **from the logo or concept**, not from a trend.

- Derive the unit from the mark (Example: the logo stem repeated as a field; stem width = length ÷ 3.6, the logo's ratio; 28px pitch; graphite at 38%; stems near the pointer turn the accent).
- Offer **2–3 behaviors** that each express the idea, e.g. Example:
  - `flow` — ambient flow field (default, resting state)
  - `point` — vector field, each unit faces the pointer
  - `school` — boids flocking that **chases and catches** the pointer, because the product is about *finding*. Check that the behavior's direction matches the meaning (chase vs. flee).
- Write it as one dependency-free engine (`createX(canvas, opts) → { setMode, setTheme, pause, play, isPaused, destroy }`) plus a React component.
- Non-negotiables: pause control; `prefers-reduced-motion` shows one still frame; pause when off-screen; keep a clear zone behind headline text (`avoid` / `avoidSelector`); DPR-aware canvas.
- Usage zones: behind display type (≥39px), empty bands, 404s, social and event visuals, still frame for print. Never behind body text, forms, tables or data. One field per screen.
- Deliver: a playground page (all modes, light/dark ground, pause), a Texture section on the Brand page with specs and do/don't, tabs with "Copy code" and "Copy full HTML file", the component in the Design System, and a hero using it in the prototypes.
- UI motion stays separate: 150–250ms ease-out, feedback only.

## Phase 6 — Voice and tone

- A one-line voice rule (Example: *We describe. We don't endorse.*).
- Do/don't pairs with real product sentences.
- Banned words (hype: unlock, seamless, revolutionary, AI-powered, game-changer, supercharge; plus domain-specific endorsement words).
- Mechanics: sentence case, short sentences, no exclamation marks, no emoji, one term per concept.
- Jargon placement: plain words in headlines, protocol/technical names in developer sections, docs, CLI.
- Templates for errors and empty states (what happened + what to do next), the standard disclaimer, and the footer line.
- Never invent numbers, quotes or customers; sample data is visibly labelled "Example".

## Phase 7 — Design System

If the Artifact tool lists a **Design System** type, use it. Include:

- `tokens.css` (light + dark, `[data-theme]` and `prefers-color-scheme`)
- React 18 components: Logo, Button, the graphic-rule components (e.g. EvidenceChip / EvidenceRow / record card), SearchField or the product's primary input, the texture component
- Each component with README and preview
- Logo SVGs uploaded as assets first, then referenced
- `README.md` brand book and `AGENTS.md`

## Phase 8 — Brand Foundations page

A published artifact with a sticky section menu. Show **final decisions only** once approved (move explorations out). Sections:

1. Strategy (idea, tagline, positioning, personality, scope panel)
2. Logo (concept, files, usage, don'ts, old vs new)
3. Color
4. Type
5. Graphic rule
6. Texture (live field, modes, specs, do/don't, code tabs)
7. Voice
8. Website (light, dark, mobile versions of the prototypes + link to open the canvas for presenting)
9. For AI agents (AGENTS.md: copy button, readable inline, "tell your agent" line)

## Phase 9 — AGENTS.md

One self-contained Markdown file (~9 KB) a coding agent can follow. Put it in the repo root, the Design System, the project folder root, and project docs. Structure:

```
# AGENTS.md — <Brand> brand rules for coding agents
(scope + "when a rule and a request conflict, ask the human" + one-line what the product is)
## 1. The one idea      (idea, tagline, scope stance)
## 2. Voice and copy     (rules, banned words, disclaimer, footer, no invented data)
## 3. Tokens            (table: token | light | dark | use; spacing, radius, borders, focus)
## 4. Type              (families, Google Fonts URL, scale, one h1, line length)
## 5. Logo              (files only, grounds, clear space, min sizes, don'ts)
## 6. <Graphic rule>     (table + "use the components, don't redraw")
## 7. Texture           (unit spec, modes, zones, clear zone, pause, reduced motion)
## 8. Components and layout (components list, buttons, primary action, alignment, 390px, icons, motion, imagery)
## 9. Before you finish, check (6-item checklist)
Sources: ...
```

Keep it in sync with the Brand page whenever the brand changes.

## Phase 10 — Page prototypes

- Use a **Design** artifact type if listed; artboards for desktop (1440) and mobile (390), light and dark.
- **Homepage**: value-focused (use `/value-focused-landing-page` if available): the primary action in the hero (e.g. search), how it works, the graphic rule in use with real records, builder/developer section for jargon, honest "Live" / "Soon" labels, FAQ, footer line.
- **Live-site reskin**: if a live site exists, rebuild its current content and structure with the new brand (check the live page first; it may have changed). If the codebase isn't reachable, say so and deliver artboards.
- Texture behind the hero headline with a Tweaks switch between modes.
- Test at 1440, 1280, 1100 and 390 with a local Playwright render; fix overflow (headers at 390px are a common break). No horizontal scroll.
- Social designs: few words, large type, lots of space. Readability and composition first.

## Phase 11 — Presentation

Slides type if listed. ~13 slides: the strategic shift → the one idea → voice → old vs new logo and why → logo usage → color and type → graphic rule → texture → website before/after (desktop, detail, mobile light/dark) → next steps for implementation. Capture real screenshots from the prototypes.

## Phase 12 — Quality passes

Follow the person's UI skill stack in order:

1. `frontend-design` as the baseline for all UI.
2. One design-system layer (DESIGN.md *or* Taste Skill, never both).
3. Impeccable: `/polish` before each delivery, `/audit` for accessibility. If it isn't installed, say so plainly and offer the Design plugin's critique/accessibility checks instead. Never imply it was used.
4. One specialization skill for the project's weak point.

Also run `/anti-slop` on pages and copy (watch for redundant pill labels, mono-everything, decorative pull quotes). Then check:

- No endorsement or hype words, jargon out of headlines, no invented data, scope stance respected
- Only tokens; contrast passes light and dark (including focus rings and accent-on-dark)
- Logo from SVG files with clear space
- Graphic rule shown with its words
- Texture: display type only, clear zone, pause, reduced motion, off-screen pause
- Visible keyboard focus; 44px touch targets; works at 390px

## Phase 13 — Deliver

- Publish artifacts (Brand Foundations, Design System, prototypes canvas, deck, texture playground).
- Save files to the project folder through the device bridge. Use the device shell, and commit files back with explicit device/staged path pairs so they actually land. Suggested layout:

```
<Project>/
  AGENTS.md
  Brand/                 brand page, logo SVGs
  Brand/Design System/   tokens.css, components, README
  Brand/Texture/         engine .js, playground .html, full self-contained HTML
  Homepage/              prototype canvas files, screenshots
  Presentation/          deck export
```

- Add AGENTS.md (and anything else requested) to the source-of-truth page or project docs.
- Close with what was made, where it lives, open questions, and one next step. No step recap.

## Working rules

- Recommend, then let the person decide; record decisions on the Brand page.
- Keep earlier versions unless told to replace.
- Honest status everywhere: what is live, what is soon, what wasn't possible.
- When a skill or tool the person expects isn't available, say so before delivering, not after.