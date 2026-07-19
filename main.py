from database.connection import DatabaseConnection
from database.manager import DatabaseManager
from database.schema import initialize_database

from services.pipeline import RedditPipeline

RSS_FEEDS = {
    "GMAT": "https://www.reddit.com/r/GMAT/.rss",
    "MBA": "https://www.reddit.com/r/MBA/.rss",
}


def main():
    database = DatabaseConnection()

    initialize_database(database.get_connection())

    manager = DatabaseManager(database.get_connection())

    pipeline = RedditPipeline(manager)

    pipeline.ingest_posts(RSS_FEEDS)

    pipeline.classify_posts()

    database.close()


if __name__ == "__main__":
    main()