"""
Collects and normalizes Reddit posts from RSS feeds.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from bs4 import BeautifulSoup

from reddit.client import fetch_feed
from utils.logger import logger
import time


def clean_html(html: str) -> str:
    """
    Convert Reddit HTML content into clean plain text.
    """

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(separator=" ", strip=True)

    # Remove the RSS footer
    if "submitted by" in text:
        text = text.split("submitted by")[0].strip()

    return text


def normalize_entry(entry, subreddit: str) -> Dict:
    """
    Convert a Reddit RSS entry into our standard format.
    """

    body = ""

    if hasattr(entry, "content") and entry.content:
        body = clean_html(entry.content[0]["value"])

    elif hasattr(entry, "summary"):
        body = clean_html(entry.summary)

    # Example:
    # https://www.reddit.com/r/GMAT/t3_1uyvz08
    reddit_id = entry.id.split("_")[-1]

    created_utc = datetime.fromisoformat(
        entry.published.replace("Z", "+00:00")
    ).timestamp()

    return {
        "reddit_id": reddit_id,
        "title": entry.title,
        "body": body,
        "author": entry.author.replace("/u/", ""),
        "subreddit": subreddit,
        "url": entry.link,
        "created_utc": created_utc,
    }


def fetch_latest_posts(rss_feeds: Dict[str, str]) -> List[Dict]:
    """
    Fetch posts from all configured RSS feeds.

    Parameters
    ----------
    rss_feeds : Dict[str, str]
        Dictionary mapping subreddit names to RSS URLs.

    Returns
    -------
    List[Dict]
        List of normalized Reddit posts.
    """

    posts = []

    for subreddit, url in rss_feeds.items():

        logger.info("Fetching posts from r/%s", subreddit)

        try:
            feed = fetch_feed(url)

            logger.info(
                "Found %d posts in r/%s",
                len(feed.entries),
                subreddit,
            )

            for entry in feed.entries:
                posts.append(normalize_entry(entry, subreddit))
            time.sleep(2)
        except Exception as e:
            logger.exception(
                "Failed to fetch posts from r/%s: %s",
                subreddit,
                e,
            )

    logger.info("Collected %d total posts.", len(posts))

    return posts