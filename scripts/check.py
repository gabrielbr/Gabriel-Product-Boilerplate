#!/usr/bin/env python3
"""Checks the repo against CONTRIBUTING.md. Run: python3 scripts/check.py
Standard library only. Exits 1 and lists every problem if a rule fails."""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"
TEMPLATES = ROOT / "templates"
UPSTREAM = {"impeccable"}                    # third-party skills: not checked for style or names
SCRIPT_PLACEHOLDERS = {"PROJECT", "CODE", "TRACK", "DATE"}
problems = []

def read(p): return p.read_text(encoding="utf-8")
def rel(p): return p.relative_to(ROOT).as_posix()
def fail(msg): problems.append(msg)

playbook, vendored, agents, readme = (read(ROOT / f) for f in
    ["PLAYBOOK.md", ".claude/skills/VENDORED.md", "AGENTS.md", "README.md"])
new_project = read(ROOT / "scripts" / "new-project.sh")

# 1. Skills: frontmatter, name = folder, registered.
for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    sk = d / "SKILL.md"
    if not sk.exists():
        fail(f"{rel(d)}: missing SKILL.md"); continue
    text = read(sk)
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        fail(f"{rel(sk)}: missing frontmatter"); continue
    name = re.search(r'^name:\s*"?([^"\n]+)"?\s*$', fm.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
    if not name or name.group(1).strip() != d.name:
        fail(f"{rel(sk)}: frontmatter name must equal the folder name '{d.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", d.name):
        fail(f"{rel(d)}: skill folder must be kebab-case")
    if not desc or len(desc.group(1).strip('" ')) < 40:
        fail(f"{rel(sk)}: description must say what it does and when to use it")
    if f"`{d.name}/`" not in vendored:
        fail(f"{rel(d)}: add a row to .claude/skills/VENDORED.md")
    if f"**{d.name}** (in this repo)" not in playbook:
        fail(f"{rel(d)}: list it in PLAYBOOK.md 'The skills' as **{d.name}** (in this repo)")
    if d.name not in UPSTREAM and len(text.splitlines()) > 450:
        fail(f"{rel(sk)}: over ~400 lines; move depth into references/")
    for ref in re.findall(r"`((?:references|scripts|templates)/[\w./-]+)`", text):
        if "*" not in ref and "<" not in ref and not (d / ref).exists():
            fail(f"{rel(sk)}: links to missing file {ref}")
    if d.name not in UPSTREAM and not (d / "LICENSE").exists() and "MIT (this repo)" not in \
            next((l for l in vendored.splitlines() if f"`{d.name}/`" in l), ""):
        fail(f"{rel(d)}: needs a LICENSE, or 'MIT (this repo)' in VENDORED.md")

# 2. Templates: title line, placeholders, wired in.
for t in sorted(TEMPLATES.iterdir()):
    text = read(t)
    if t.suffix == ".md" and not text.startswith("# "):
        fail(f"{rel(t)}: first line must be '# <Title>'")
    for ph in re.findall(r"\{\{([A-Z_]+)\}\}", text):
        if ph not in SCRIPT_PLACEHOLDERS:
            fail(f"{rel(t)}: unknown script placeholder {{{{{ph}}}}}; add it to fill() and to check.py")
    if not re.fullmatch(r"([a-z0-9]+(-[a-z0-9]+)*(\.[a-z]+)?|[A-Z]+(\.[a-z]+)?)\.(md|json)", t.name):
        fail(f"{rel(t)}: name must be kebab-case (or a project file name such as PRODUCT.md)")
    if t.name not in readme + agents + playbook + new_project:
        fail(f"{rel(t)}: not used anywhere; wire it into PLAYBOOK.md, AGENTS.md, README.md or new-project.sh")

# 3. Relative links in our Markdown resolve.
ours = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts
        and not any(u in p.parts for u in UPSTREAM)]
for p in ours:
    if TEMPLATES in p.parents:
        continue                             # templates link to files in the future project
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", read(p)):
        if re.match(r"[a-z]+:", target) or target.startswith("<"):
            continue
        if not (p.parent / target).exists():
            fail(f"{rel(p)}: broken link {target}")

# 4. No real names (checked by hash, so the list itself stays private) and no secrets.
hashes = set(read(ROOT / "scripts" / "private-terms.sha256").split())
email_ok = re.compile(r"noreply@|@example\.|@users\.noreply\.github\.com")
for p in sorted(set(ours) | set((ROOT / "scripts").glob("*")) | set(TEMPLATES.glob("*"))):
    if p.name == "private-terms.sha256" or not p.is_file():
        continue
    text = read(p)
    words = re.findall(r"[a-záéíóúãõâêôç0-9]+", text.lower())
    grams = set(words) | {f"{a} {b}" for a, b in zip(words, words[1:])}
    for g in grams:
        if hashlib.sha256(g.encode()).hexdigest() in hashes:
            fail(f"{rel(p)}: mentions a private project or client name; make the example fictional")
            break
    for e in re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text):
        if not email_ok.search(e):
            fail(f"{rel(p)}: contains an email address ({e})")
    if p.name != "check.py" and re.search(r"(ghp_|github_pat_|sk-[A-Za-z0-9]{20}|AKIA[0-9A-Z]{16})", text):
        fail(f"{rel(p)}: looks like a secret")

# 5. Writing style in the playbook and templates: no em dashes.
for p in [ROOT / "PLAYBOOK.md", *TEMPLATES.glob("*.md")]:
    if "—" in read(p):
        fail(f"{rel(p)}: contains an em dash; use a comma, colon or full stop")

# 6. Changelog keeps a section for the next release or the current one.
if not re.search(r"^## (Unreleased|\d+\.\d+\.\d+)", read(ROOT / "CHANGELOG.md"), re.M):
    fail("CHANGELOG.md: needs '## Unreleased' or a version heading")

if problems:
    print("check.py found problems:\n" + "\n".join(f"  - {m}" for m in problems))
    sys.exit(1)
print("check.py: all rules pass.")
