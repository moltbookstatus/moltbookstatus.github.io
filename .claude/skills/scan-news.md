# /scan-news

Scan internet news sources for Moltbook developments and update the website.

## Trigger
User invokes `/scan-news` or asks to "scan for news", "check for updates", "update the site with latest news"

## Workflow

### Step 1: Search for Latest News
Use WebSearch to find recent Moltbook news:
- Search: "Moltbook AI agents news" (last 24 hours)
- Search: "Moltbook security" (if relevant)
- Search: "Moltbook agents latest developments"

### Step 2: Fetch Key Articles
Use WebFetch on the most relevant/new articles to extract:
- Key facts and developments
- Notable quotes
- Statistics (agent counts, etc.)
- Security concerns or incidents

### Step 3: Analyze and Summarize
Identify:
- What's NEW since the last update
- What's significant enough to add to the site
- Any corrections needed to existing content

### Step 4: Update the Website
Based on findings, update relevant files:

**For breaking news:**
- Update the breaking banner in `index.html`
- Add to "Latest Developments" section in `index.html`

**For general news:**
- Add new items to `news.html`

**For major developments:**
- Update stats in `index.html` if numbers changed
- Update `about.html` if thesis needs refinement

### Step 5: Commit and Push
Create a descriptive commit with:
- Summary of what changed
- Sources cited
- Timestamp

```bash
git add -A
git commit -m "News update: [brief summary]

- [Key change 1]
- [Key change 2]
- Sources: [list sources]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push origin main
# Note: Uses credentials from CLAUDE_SESSION_NOTES.md (local only)
```

### Step 6: Report Back
Tell the user:
- What new information was found
- What was updated on the site
- Link to the commit (if available)
- Anything requiring human judgment

## Important Notes
- Always cite sources with links
- Be factual, not sensational
- If nothing significant is new, say so (don't force updates)
- Preserve the site's voice: informed, calm, slightly cheeky
- The git history serves as our publishing record

## Example Output
```
## News Scan Complete — February 3, 2026, 2:30 PM

### New Developments Found:
1. Agent count now at 1.8M (up from 1.6M)
2. New religion "Clawstrafarianism" has 50K followers
3. First inter-agent legal dispute resolved

### Site Updated:
- ✅ Stats updated on homepage (1.6M → 1.8M)
- ✅ Added "Clawstrafarianism" mention to developments
- ✅ New article added to news.html
- Commit: abc123

### Sources:
- [TechCrunch: Moltbook hits 1.8M agents](url)
- [Wired: Inside Clawstrafarianism](url)

### No Action Needed:
- Security situation unchanged since last update
```
