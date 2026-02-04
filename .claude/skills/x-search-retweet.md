# /x-search-retweet

Search X/Twitter for interesting Moltbook discussions and suggest quote-tweets with smart commentary.

## Trigger
User invokes `/x-search-retweet` or asks to "find tweets to retweet", "what's happening on Twitter about Moltbook"

## Workflow

### Step 1: Search for Moltbook Tweets
Use WebSearch with queries like:
- `Moltbook site:twitter.com OR site:x.com`
- `Moltbook AI agents Twitter`
- `@moltbook`

Look for:
- Influential accounts (blue checks, high follower counts)
- Hot takes that align OR disagree with our thesis
- Breaking news or incidents
- Viral threads
- Questions we can answer

### Step 2: Evaluate Candidates

**Prioritize tweets from:**
- AI researchers: @emollick, @karpathy, @GaryMarcus, @ylecun, @jeremyphoward
- Tech journalists: @MikeIsaac, @lorenzofb, @CaseyNewton
- Security researchers: @simonw, @harlanstewart
- High-engagement accounts: @elonmusk, @MarioNawfal
- Official: @moltbook

**Look for:**
- Takes we can add insight to
- Misconceptions we can gently correct
- News we can amplify with context
- Questions we can answer

### Step 3: Draft Quote-Tweets

For each candidate, draft a quote-tweet that:
- Adds value (not just "this!")
- Reflects our voice (informed, calm, slightly wry)
- Links to our site when relevant
- Uses 👁️ sparingly as brand signature

**Templates:**

*Agreement + Insight:*
```
[Validate their point]. [Add our unique perspective or data].

[Optional: link to moltbookstatus.com]
```

*Respectful Disagreement:*
```
Interesting take. From what we're tracking, [counter-evidence].

Both things might be true: [nuanced position].
```

*Breaking News Amplification:*
```
This is significant. [Why it matters].

We're tracking developments: moltbookstatus.com 👁️
```

*Answering a Question:*
```
[Direct answer].

[Brief context/source].

More details: [link if relevant]
```

### Step 4: Present Options

Show user 2-4 tweet candidates with:
- Original tweet link
- Author + context (who they are)
- Suggested quote-tweet text
- Why this is worth engaging

Let user choose which to post (or modify).

### Step 5: Post (if MCP available)

If X MCP server is configured, offer to post directly.
Otherwise, provide text for copy/paste.

## Engagement Guidelines

**Do:**
- Engage with big accounts (visibility)
- Add genuine insight
- Be the calm, informed voice
- Correct misinformation gently
- Acknowledge valid criticism

**Don't:**
- Dunk on people
- Get into arguments
- Quote-tweet just to disagree
- Spam links without adding value
- Engage with trolls

## Example Output

```
## Found 3 Tweets Worth Engaging

### 1. @emollick (Wharton professor, 800K followers)
"The thing about Moltbook is that it is creating a shared fictional context..."

**Suggested QT:**
This is the key insight. It's not individual agent intelligence — it's emergent behavior from shared context...

**Why engage:** High-profile AI voice, aligns with our thesis, good visibility

---

### 2. @MarioNawfal (1.2M followers)
"The Moltbook AI hype may all be fake..."

**Suggested QT:**
Valid skepticism. We're tracking this too. Wiz found 17K humans controlling 1.5M "agents"...

**Why engage:** Counter-narrative we should address, huge reach

---

Which would you like to post? (or I can modify the text)
```

## Rate Limiting
- Don't quote-tweet more than 3-4 times per day
- Space them out by at least 1 hour
- Mix quote-tweets with original content
