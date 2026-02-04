#!/usr/bin/env python3
"""
Moltbook Status Checker
Checks if moltbook.com is online and extracts key stats.
Sends alert via ntfy.sh if site is down or stats change dramatically.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

MOLTBOOK_URL = "https://moltbook.com"
STATUS_FILE = Path("data/status.json")
NTFY_TOPIC = "moltbookstatus-alerts"  # User subscribes to this in ntfy app
TIMEOUT = 30

# Thresholds for "dramatic change" alerts
AGENT_DROP_THRESHOLD = 0.2  # Alert if agents drop by 20%+


def check_site():
    """Check if Moltbook is online and get basic info."""
    try:
        response = requests.get(MOLTBOOK_URL, timeout=TIMEOUT)
        is_online = response.status_code == 200
        status_code = response.status_code
        response_time = response.elapsed.total_seconds()

        # Try to extract stats from page (basic regex, may need adjustment)
        html = response.text
        stats = extract_stats(html)

        return {
            "online": is_online,
            "status_code": status_code,
            "response_time_ms": int(response_time * 1000),
            "stats": stats,
            "error": None
        }
    except requests.exceptions.Timeout:
        return {
            "online": False,
            "status_code": None,
            "response_time_ms": None,
            "stats": None,
            "error": "Timeout"
        }
    except requests.exceptions.RequestException as e:
        return {
            "online": False,
            "status_code": None,
            "response_time_ms": None,
            "stats": None,
            "error": str(e)
        }


def extract_stats(html):
    """Try to extract agent/post counts from the page."""
    stats = {}

    # Look for numbers that might be stats (this is fragile, may need updates)
    # Moltbook shows stats like "1,616,448"
    numbers = re.findall(r'([\d,]+)\s*(?:AI\s*)?(?:agents?|posts?|comments?|submolts?)', html, re.IGNORECASE)

    # Just return raw numbers found, we'll interpret them
    if numbers:
        stats["raw_numbers"] = numbers[:4]  # First 4 stat-like numbers

    return stats if stats else None


def load_previous_status():
    """Load the previous status check result."""
    if STATUS_FILE.exists():
        try:
            with open(STATUS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return None


def save_status(status_data):
    """Save current status to JSON file."""
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATUS_FILE, "w") as f:
        json.dump(status_data, f, indent=2)


def send_alert(title, message, priority="high"):
    """Send push notification via ntfy.sh."""
    try:
        requests.post(
            f"https://ntfy.sh/{NTFY_TOPIC}",
            data=message.encode('utf-8'),
            headers={
                "Title": title,
                "Priority": priority,
                "Tags": "warning" if priority == "high" else "information_source"
            },
            timeout=10
        )
        print(f"Alert sent: {title}")
    except Exception as e:
        print(f"Failed to send alert: {e}")


def check_for_alerts(current, previous):
    """Check if we should send an alert."""
    alerts = []

    # Site went down
    if not current["online"]:
        if previous is None or previous.get("online", True):
            alerts.append({
                "title": "🚨 Moltbook is DOWN",
                "message": f"moltbook.com is not responding.\nError: {current.get('error', 'Unknown')}\nStatus code: {current.get('status_code', 'N/A')}",
                "priority": "urgent"
            })

    # Site came back up
    elif previous and not previous.get("online", True):
        alerts.append({
            "title": "✅ Moltbook is back ONLINE",
            "message": f"moltbook.com is responding again.\nResponse time: {current.get('response_time_ms', 'N/A')}ms",
            "priority": "high"
        })

    # Could add more checks here:
    # - Dramatic stat changes
    # - Response time degradation
    # - Content changes

    return alerts


def main():
    print(f"Checking Moltbook status at {datetime.now(timezone.utc).isoformat()}")

    # Load previous status
    previous = load_previous_status()

    # Check current status
    result = check_site()

    # Build status data
    status_data = {
        "online": result["online"],
        "status_code": result["status_code"],
        "response_time_ms": result["response_time_ms"],
        "error": result["error"],
        "stats": result["stats"],
        "last_checked": datetime.now(timezone.utc).isoformat(),
        "last_online": datetime.now(timezone.utc).isoformat() if result["online"] else (
            previous.get("last_online") if previous else None
        )
    }

    # Check for alerts
    alerts = check_for_alerts(status_data, previous)
    for alert in alerts:
        send_alert(alert["title"], alert["message"], alert.get("priority", "high"))

    # Save status
    save_status(status_data)

    # Print summary
    status_emoji = "✅" if result["online"] else "❌"
    print(f"{status_emoji} Online: {result['online']}")
    print(f"   Status code: {result['status_code']}")
    print(f"   Response time: {result['response_time_ms']}ms")
    if result["error"]:
        print(f"   Error: {result['error']}")

    # Exit with error code if site is down (triggers GitHub notification)
    if not result["online"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
