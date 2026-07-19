"""
Handles fetching Reddit RSS feeds.
"""

import requests
import feedparser

USER_AGENT = (
    "GMATRedditIntelligence/1.0 "
    "(by /u/YOUR_REDDIT_USERNAME)"
)

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
}


def fetch_feed(feed_url: str):

    response = requests.get(
        feed_url,
        headers=HEADERS,
        timeout=30,
    )

    print("=" * 60)
    print(feed_url)
    print("Status :", response.status_code)

    if response.status_code != 200:
        response.raise_for_status()

    feed = feedparser.parse(response.text)

    print("Bozo   :", feed.bozo)
    print("Entries:", len(feed.entries))

    if feed.bozo:
        print("Exception:", feed.bozo_exception)

    return feed