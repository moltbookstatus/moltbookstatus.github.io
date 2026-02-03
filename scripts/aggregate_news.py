#!/usr/bin/env python3
"""
Moltbook News Aggregator
Runs via GitHub Actions to collect news while you sleep.
"""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup

# News sources to check
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q=Moltbook+AI+agents&hl=en-US&gl=US&ceid=US:en"
REDDIT_RSS_SOURCES = [
    "https://www.reddit.com/r/singularity/search.rss?q=moltbook&sort=new&restrict_sr=on",
    "https://www.reddit.com/r/artificial/search.rss?q=moltbook&sort=new&restrict_sr=on",
]

OUTPUT_FILE = Path("data/news_feed.json")
NEWS_PAGE = Path("news.html")


def fetch_google_news():
    """Fetch news from Google News RSS."""
    articles = []
    try:
        feed = feedparser.parse(GOOGLE_NEWS_RSS)
        for entry in feed.entries[:20]:  # Last 20 articles
            articles.append({
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "source": extract_source(entry.get("title", "")),
                "published": entry.get("published", ""),
                "type": "news"
            })
    except Exception as e:
        print(f"Error fetching Google News: {e}")
    return articles


def fetch_reddit_posts():
    """Fetch posts from Reddit RSS feeds."""
    posts = []
    headers = {"User-Agent": "MoltbookStatusBot/1.0"}

    for rss_url in REDDIT_RSS_SOURCES:
        try:
            feed = feedparser.parse(rss_url)
            for entry in feed.entries[:10]:
                posts.append({
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "source": "Reddit",
                    "published": entry.get("published", ""),
                    "type": "reddit"
                })
        except Exception as e:
            print(f"Error fetching Reddit: {e}")
    return posts


def extract_source(title):
    """Extract source name from Google News title (format: 'Title - Source')."""
    if " - " in title:
        return title.split(" - ")[-1]
    return "Unknown"


def deduplicate(articles):
    """Remove duplicate articles by URL."""
    seen = set()
    unique = []
    for article in articles:
        if article["link"] not in seen:
            seen.add(article["link"])
            unique.append(article)
    return unique


def load_existing():
    """Load existing news feed."""
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE, "r") as f:
            return json.load(f)
    return {"articles": [], "last_updated": None}


def save_feed(data):
    """Save news feed to JSON."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)


def generate_news_page(articles):
    """Generate a simple HTML news page."""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Feed | Moltbook Status</title>
    <meta name="description" content="Latest news about Moltbook and AI agents.">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Source+Sans+Pro:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1a1a2e;
            --secondary: #16213e;
            --accent: #e94560;
            --text: #eaeaea;
            --text-muted: #a0a0a0;
            --card-bg: #1f1f3a;
            --border: #2a2a4a;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Source Sans Pro', sans-serif;
            background: var(--primary);
            color: var(--text);
            line-height: 1.7;
            font-size: 18px;
        }
        nav {
            background: var(--secondary);
            border-bottom: 1px solid var(--border);
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }
        .nav-logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--text);
            text-decoration: none;
        }
        .nav-logo .highlight { color: var(--accent); }
        .nav-links { display: flex; gap: 25px; }
        .nav-links a {
            color: var(--text-muted);
            text-decoration: none;
            font-weight: 600;
        }
        .nav-links a:hover, .nav-links a.active { color: var(--accent); }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        h1 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        .subtitle {
            color: var(--text-muted);
            margin-bottom: 30px;
        }
        .news-item {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            transition: transform 0.2s;
        }
        .news-item:hover {
            transform: translateX(5px);
            border-left: 3px solid var(--accent);
        }
        .news-item a {
            color: var(--text);
            text-decoration: none;
            font-weight: 600;
            font-size: 1.1rem;
        }
        .news-item a:hover { color: var(--accent); }
        .news-meta {
            color: var(--text-muted);
            font-size: 0.85rem;
            margin-top: 8px;
        }
        .news-type {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            text-transform: uppercase;
            margin-right: 10px;
        }
        .news-type.news { background: #2d4a7c; }
        .news-type.reddit { background: #ff4500; }
        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 1px solid var(--border);
            color: var(--text-muted);
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <nav>
        <a href="/" class="nav-logo">MOLTBOOK <span class="highlight">STATUS</span></a>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/about.html">About</a>
            <a href="/news.html" class="active">News</a>
            <a href="/supporters.html">Supporters</a>
            <a href="/contact.html">Contact</a>
        </div>
    </nav>

    <div class="container">
        <h1>News Feed</h1>
        <p class="subtitle">Auto-aggregated every 4 hours. Last updated: ''' + datetime.now(timezone.utc).strftime("%B %d, %Y at %H:%M UTC") + '''</p>

'''

    for article in articles[:30]:  # Show last 30
        news_type = article.get("type", "news")
        html += f'''        <div class="news-item">
            <a href="{article['link']}" target="_blank" rel="noopener">{article['title']}</a>
            <div class="news-meta">
                <span class="news-type {news_type}">{news_type}</span>
                {article.get('source', '')} • {article.get('published', 'Recently')}
            </div>
        </div>
'''

    html += '''
    </div>

    <footer>
        <p>&copy; 2026 Moltbook Status. Auto-updated news feed.</p>
    </footer>
</body>
</html>
'''

    with open(NEWS_PAGE, "w") as f:
        f.write(html)


def main():
    print(f"Starting news aggregation at {datetime.now(timezone.utc).isoformat()}")

    # Fetch from all sources
    google_news = fetch_google_news()
    reddit_posts = fetch_reddit_posts()

    print(f"Fetched {len(google_news)} Google News articles")
    print(f"Fetched {len(reddit_posts)} Reddit posts")

    # Combine and deduplicate
    all_articles = google_news + reddit_posts
    all_articles = deduplicate(all_articles)

    # Load existing and merge (keep last 100)
    existing = load_existing()
    existing_links = {a["link"] for a in existing.get("articles", [])}

    new_articles = [a for a in all_articles if a["link"] not in existing_links]
    print(f"Found {len(new_articles)} new articles")

    # Merge: new first, then existing
    merged = new_articles + existing.get("articles", [])
    merged = merged[:100]  # Keep last 100

    # Save
    feed_data = {
        "articles": merged,
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "total_fetched": len(all_articles),
        "new_this_run": len(new_articles)
    }
    save_feed(feed_data)

    # Generate news page
    generate_news_page(merged)

    print(f"Saved {len(merged)} articles to {OUTPUT_FILE}")
    print(f"Generated {NEWS_PAGE}")


if __name__ == "__main__":
    main()
