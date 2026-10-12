#!/usr/bin/env bash
# Link every generated skill in ../../skills into ~/.claude/skills so Claude Code loads them everywhere.
set -euo pipefail
src="$(cd "$(dirname "$0")/../../skills" && pwd)"
mkdir -p ~/.claude/skills
for d in "$src"/*/; do
  [ -f "$d/SKILL.md" ] || continue
  ln -sfn "$d" ~/.claude/skills/"$(basename "$d")"
  echo "linked $(basename "$d")"
done
