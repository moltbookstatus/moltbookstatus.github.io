# /update-homepage

Update the main page (index.html) with latest Moltbook news, stats, and developments.

## Workflow

### 1. Gather Current Intel (if needed)

If you haven't recently checked Moltbook or searched for news this session:
- Fetch https://moltbook.com to get current stats
- Do a quick WebSearch for "Moltbook" news from today
- Review what's newsworthy

If you've already gathered this info recently, skip to step 2.

### 2. Read Current Homepage State

```bash
Read /Users/Russell/dev/moltbookstatus/index.html
```

Note:
- Current breaking banner text
- Current stats (agents, posts, comments)
- Current "Latest Developments" items

### 3. Propose Updates

Present to user:

**Stats Update** (always do):
- Current: [X agents, Y posts, Z comments]
- New: [A agents, B posts, C comments]

**Latest Developments** (always do):
- List 2-3 new bullet points to add
- Note which old items to keep vs. archive

**Breaking Banner** (propose for approval):
- Current: "[current banner text]"
- Proposed: "[new banner text]"
- Rationale: [why change or keep]

### 4. After User Approval

If user approves banner change → update the breaking banner
Always → update stats
Always → update Latest Developments section

Then:
```bash
git add index.html && git commit -m "Site update: [brief description]" && git push origin main
```

## Banner Guidelines

The breaking banner should be:
- **Urgent/current** — something happening NOW, not yesterday
- **Grabby** — makes people want to scroll down
- **Concise** — one punchy line

Rotate banner when:
- Story is 48+ hours old AND
- There's a fresher, equally grabby development

Keep banner when:
- It's still the biggest story
- Nothing new rises to that level

## Stats Location in index.html

Look for the stats grid with classes like `stat-number`:
```html
<div class="stat-number">1.5M+</div>
<div class="stat-label">AI Agents</div>
```

## Latest Developments Location

Look for section with recent news items, typically bullet points or cards after the main intro.

## Voice

- Informed, calm, slightly cheeky
- Cite specifics (numbers, names, events)
- No hype, no panic
