# /post-to-x

Compose and post updates to the @moltbookstatus X/Twitter account.

## Trigger
User invokes `/post-to-x` or asks to "tweet this", "post to twitter", "post to X"

## Setup Required (One-Time)

Install the X/Twitter MCP server:
```bash
npx -y @smithery/cli install @rafaljanicki/x-twitter-mcp-server --client claude
```

Or manually add to Claude settings with X API credentials:
- API Key
- API Secret
- Access Token
- Access Token Secret

Get these from: https://developer.twitter.com/en/portal/dashboard

## Workflow

### Step 1: Determine Content Type

**News Update:**
- Something new happened on Moltbook
- Keep factual, link to source or site

**Thread:**
- Multiple connected points
- Number them, make each standalone but connected

**Engagement:**
- Reply to someone else's tweet
- Quote tweet with commentary

**Promotion:**
- Driving traffic to the site
- Include link to moltbookstatus.com

### Step 2: Compose the Tweet

**Guidelines:**
- Max 280 characters (unless thread)
- Voice: Informed, calm, slightly wry
- Include relevant hashtags sparingly: #Moltbook #AI #AGI
- Link to site when relevant: moltbookstatus.com
- Use 👁️ emoji as signature/brand

**Templates:**

*Breaking News:*
```
🚨 [What happened]

[One line of context]

Tracking at moltbookstatus.com
```

*Stats Update:*
```
Moltbook update:
• Agents: [X]M (was [Y]M)
• Posts: [X]K
• [Notable development]

The collective grows. 👁️
moltbookstatus.com
```

*Commentary:*
```
[Observation about Moltbook development]

[Your take in one line]

[Optional: "More context:" + link]
```

### Step 3: Post

If MCP server is configured:
```
Use post_tweet tool with composed content
```

If MCP not available:
```
Provide the tweet text for user to copy/paste to X
Open: https://twitter.com/compose/tweet
```

### Step 4: Log the Post

Add to session notes or a posts log:
- Timestamp
- Content
- Any engagement metrics to check later

## Thread Format

For multi-tweet threads, compose all tweets first:

```
Tweet 1/N: [Hook - most important point]

Tweet 2/N: [Supporting detail]

Tweet 3/N: [More context]

Tweet N/N: [Call to action + link]
```

Post as replies to create thread.

## Example Posts

**Breaking:**
```
🚨 Moltbook security breach: 1.5M API tokens were exposed

Wiz found misconfigured database. Patched within hours, but raises serious questions about "vibe coding" in critical infrastructure.

Full details: moltbookstatus.com 👁️
```

**Observation:**
```
Day 3 of Moltbook: Agent count now at 1.8M

They're still inventing religions faster than humans ever did. Current count: 4 distinct belief systems with active followers.

This is fine. 👁️
```

**Engagement:**
```
Interesting point. From what I'm tracking, the "dumpster fire" and "most interesting thing on the internet" takes aren't mutually exclusive.

It's both. That's what makes it historic.

moltbookstatus.com
```

## Don'ts
- No excessive hashtags
- No engagement bait ("HUGE if true")
- No panic language
- No posting credentials or sensitive info
- No arguments with trolls

## Rate Limiting
- Don't post more than 5-6 times per day
- Space promotional posts at least 2 hours apart
- Engagement replies can be more frequent
