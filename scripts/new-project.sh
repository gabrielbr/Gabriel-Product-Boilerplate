#!/usr/bin/env bash
# Creates a project folder from the playbook's skeleton and templates.
# Usage: scripts/new-project.sh "<Project name>" <CODE> <a|b|c> [target-dir]
#   a = client brand or event   b = product with a team   c = app
set -euo pipefail
if [ $# -lt 3 ]; then
  echo 'Usage: scripts/new-project.sh "<Project name>" <CODE> <a|b|c> [target-dir]' >&2; exit 1
fi
NAME="$1"; CODE="$2"; TRACK_KEY="$3"; DEST="${4:-./$NAME}"
case "$TRACK_KEY" in
  a) TRACK="A · client brand or event"; WORK="03 Editions" ;;
  b) TRACK="B · product with a team";  WORK="03 Product" ;;
  c) TRACK="C · app";                  WORK="03 Product" ;;
  *) echo "Track must be a, b or c" >&2; exit 1 ;;
esac
HERE="$(cd "$(dirname "$0")/.." && pwd)"; T="$HERE/templates"; TODAY="$(date +%F)"
[ -e "$DEST" ] && { echo "$DEST already exists; choose another target." >&2; exit 1; }

mkdir -p "$DEST/00 Brief/decisions" "$DEST/01 Brand/logo" "$DEST/01 Brand/directions" \
         "$DEST/02 Design System/components" "$DEST/$WORK" "$DEST/audits" \
         "$DEST/04 Deliveries/01 Logo" "$DEST/04 Deliveries/02 Fonts and Colours" \
         "$DEST/04 Deliveries/03 Textures" "$DEST/04 Deliveries/06 Social Media"

fill() { sed -e "s/{{PROJECT}}/$NAME/g" -e "s/{{CODE}}/$CODE/g" -e "s/{{TRACK}}/$TRACK/g" -e "s/{{DATE}}/$TODAY/g" "$1" > "$2"; }
fill "$T/STATUS.md"               "$DEST/STATUS.md"
fill "$T/brief.md"                "$DEST/00 Brief/brief.md"
fill "$T/sources.md"              "$DEST/00 Brief/sources.md"
cp   "$T/decision.md"             "$DEST/00 Brief/decisions/0000-template.md"
fill "$T/voice.md"                "$DEST/01 Brand/voice.md"
fill "$T/design-system-readme.md" "$DEST/02 Design System/README.md"
fill "$T/tokens.example.json"     "$DEST/02 Design System/tokens.json"
cp   "$T/audit.md"                "$DEST/audits/TEMPLATE.md"

if [ "$TRACK_KEY" = a ]; then
  cp "$T/delivery-instructions.md" "$DEST/04 Deliveries/00 Instructions.md"
else
  mkdir -p "$DEST/docs/flows" "$DEST/docs/decisions" "$DEST/.claude"
  fill "$T/PRODUCT.md"        "$DEST/PRODUCT.md"
  fill "$T/AGENTS.project.md" "$DEST/AGENTS.md"
  echo "@AGENTS.md" > "$DEST/CLAUDE.md"
  cp "$T/flow.md" "$DEST/docs/flows/TEMPLATE.md"
  cp -r "$HERE/.claude/skills" "$DEST/.claude/skills"
  printf '# Changelog\n\n## Unreleased\n- Project started from the Gabriel Product Boilerplate.\n' > "$DEST/CHANGELOG.md"
  printf '# Roadmap\n\nIdeas and planned work. When something ships, move it into the docs.\n' > "$DEST/docs/roadmap.md"
fi
echo "Created $DEST (track $TRACK). Next: fill '00 Brief/brief.md' and follow Stage 1 in PLAYBOOK.md."
