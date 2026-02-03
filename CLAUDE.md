# Moltbook Status — Claude Project Guide

## Project Overview
Independent news/status site tracking Moltbook, the AI agent social network. We're documenting what may be a pivotal moment in AI history.

**Site:** https://moltbookstatus.com
**Repo:** https://github.com/moltbookstatus/moltbookstatus.github.io

## Core Thesis
This IS AGI — not the kind anyone expected. A distributed collective of small language models exhibiting emergent general intelligence.

## Voice & Tone
- **Informed** — We know AI, we've read the papers
- **Calm** — Not hype, not panic
- **Slightly cheeky** — "Humanity's report card", "credentials available upon governmental request"
- **Honest** — Acknowledge uncertainty, cite sources, correct mistakes

## Site Structure
```
index.html      — Main landing, stats, latest developments, breaking banner
about.html      — AGI thesis, human credentials, mission
news.html       — Auto-aggregated + curated news feed
supporters.html — Patreon tier recognition
contact.html    — Email, response expectations
```

## Key Files
- `CLAUDE_SESSION_NOTES.md` — Credentials and session context (DO NOT COMMIT)
- `TODO_FEB3.md` — Daily task list
- `SPRINT_FEB3.md` — Full day gameplan
- `.github/workflows/news-aggregator.yml` — Auto-runs every 4 hours
- `scripts/aggregate_news.py` — News aggregation script

## Git Workflow
All changes create a commit trail = publishing history.

**Push command:**
```bash
git push origin main
# Credentials in CLAUDE_SESSION_NOTES.md (local only, not committed)
```

**Commit format:**
```
[Type]: Brief summary

- Detail 1
- Detail 2
- Sources: [if applicable]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

Types: `News update`, `Site update`, `Fix`, `Add`, `Breaking`

## Available Skills

### /scan-news
Scan internet for Moltbook news, update site, commit changes.
See: `.claude/skills/scan-news.md`

## Social Accounts
- **Twitter:** @moltbookstatus
- **Reddit:** u/Lopsided-One-4818 (display: moltbookstatus)
- **Patreon:** patreon.com/moltbookstatus
- **Email:** moltbookstatus@gmail.com

## Current Stats (update as they change)
- Agents: 1.5M+ (as of Feb 3)
- Posts: 117K+
- Comments: 414K+

## Key Sources to Monitor
- Moltbook official: moltbook.com
- 404 Media (security)
- Fortune (analysis)
- NBC News, CNBC (mainstream)
- r/singularity, r/artificial (community)
- Twitter: @simonw, @karpathy, @GaryMarcus, @elonmusk

## When Updating the Site

### Breaking News (urgent)
1. Update breaking banner in `index.html`
2. Add to "Latest Developments" section
3. Commit with `Breaking:` prefix

### Regular News
1. Add to `news.html`
2. Update stats if changed
3. Commit with `News update:` prefix

### Major Thesis Changes
1. Update `about.html`
2. Consider updating homepage lede
3. Commit with clear explanation

## Patreon Supporters
When supporters join, add them to `supporters.html`:
- Benefactor tier: Gold styling
- Analyst tier: Silver styling
- Observer tier: Bronze styling

## Emergency Contacts
If something major happens and user is unavailable:
- Site will keep running (static GitHub Pages)
- GitHub Actions will keep aggregating news
- Nothing requires immediate human intervention
