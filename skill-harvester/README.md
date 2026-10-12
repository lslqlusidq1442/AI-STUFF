# Skill Harvester

Saved Instagram/YouTube skill videos → your own tailored Claude skills in `skills/`.

```
share / save video ──► inbox (GitHub issue or YouTube playlist)
                          │
            daily Routine or "/skill-harvester inbox"
                          ▼
   find repo (caption, description, comments, video) → study it
                          ▼
   write skills/<name>/SKILL.md tailored to MY_WORKFLOW.md → commit
```

## Setup (one time)

1. **Fill in `MY_WORKFLOW.md`** — every skill is tailored to it.
2. **Phone share button (Instagram + YouTube)** — makes a GitHub issue labeled `harvest`:
   - Create a GitHub fine-grained token: this repo only, permission *Issues: read & write*.
   - iPhone: Shortcuts app → new shortcut → *Show in Share Sheet* (accepts URLs) → action
     **Get Contents of URL**:
     - URL `https://api.github.com/repos/lslqlusidq1442/AI-STUFF/issues`
     - Method `POST`, header `Authorization: Bearer <token>`
     - JSON body: `title` = *Shortcut Input*, `labels` = `["harvest"]`
     - Name it **Harvest Skill**.
   - Android: same request with the *HTTP Shortcuts* app (share target enabled).
   - Use: on any reel/video tap **Share → Harvest Skill**.
3. **YouTube** — the API can't read Watch Later or private lists. Make a playlist named
   *Claude Skills*, set it to **Unlisted**, save skill videos there, and put its ID
   (the `list=` value) in `config.json`.
4. **Instagram backlog** — Instagram has no API for saved posts. Request your data:
   Settings → Accounts Center → Your information and permissions → Download your information →
   format **JSON**, include **Saved**. Then: `/skill-harvester instagram-export <zip path>`.
5. **Load the skills locally**: `skill-harvester/scripts/install.sh` (links `skills/*` into `~/.claude/skills`).

## Run

| Command (in Claude Code, this repo) | Does |
|---|---|
| `/skill-harvester <url>` | one video |
| `/skill-harvester inbox` | all shared links |
| `/skill-harvester playlist` | the YouTube playlist |
| `/skill-harvester instagram-export <path>` | Instagram backlog |

Automate: a daily Routine running `/skill-harvester inbox` then `/skill-harvester playlist`.

## Limits

- Instagram blocks cloud servers; the skill falls back to video analysis. Running locally with
  `find_repos.py <url> --cookies-from-browser chrome` is most reliable.
- Posts that say "comment X for the link" often hide the repo; these are logged `needs-link`.
