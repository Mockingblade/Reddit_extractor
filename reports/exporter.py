"""
Exports classified Reddit posts to CSV.

Produces a leads list you can open in Excel: every processed post,
sorted by lead_score (highest first), so the most promising people
to reach out to are at the top.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

from database.manager import DatabaseManager
from utils.logger import logger


CSV_COLUMNS = [
    "lead_score",
    "category",
    "subcategory",
    "confidence",
    "classified_by",
    "subreddit",
    "title",
    "summary",
    "author",
    "posted_at",
    "url",
    "reddit_id",
]


def _format_row(post) -> dict:
    """
    Convert a sqlite3.Row (posts table) into a flat dict for CSV writing.
    """

    posted_at = ""

    if post["created_utc"]:
        posted_at = datetime.fromtimestamp(
            post["created_utc"], tz=timezone.utc
        ).strftime("%Y-%m-%d %H:%M UTC")

    return {
        "lead_score": post["lead_score"] or 0,
        "category": post["category"] or "",
        "subcategory": post["subcategory"] or "",
        "confidence": round(post["confidence"] or 0.0, 2),
        "classified_by": post["classified_by"] or "",
        "subreddit": post["subreddit"] or "",
        "title": post["title"] or "",
        "summary": post["summary"] or "",
        "author": post["author"] or "",
        "posted_at": posted_at,
        "url": post["url"] or "",
        "reddit_id": post["reddit_id"] or "",
    }


def export_to_csv(
    manager: DatabaseManager,
    output_path: str = "reports/leads.csv",
) -> int:
    """
    Write every processed post to a CSV file, sorted by lead_score.

    Returns the number of rows written.
    """

    posts = manager.get_all_processed_posts()

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()

        for post in posts:
            writer.writerow(_format_row(post))

    logger.info("Exported %d leads to %s", len(posts), path)

    return len(posts)


if __name__ == "__main__":
    # Lets you run this standalone any time: `python -m reports.exporter`
    # without re-running the whole pipeline.
    from database.connection import DatabaseConnection

    database = DatabaseConnection()
    manager = DatabaseManager(database.get_connection())

    count = export_to_csv(manager)

    print(f"Exported {count} leads to reports/leads.csv")

    database.close()
