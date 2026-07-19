from ai.classifier import PostClassifier
from database.manager import DatabaseManager
from reddit.collector import fetch_latest_posts
from utils.logger import logger


class RedditPipeline:

    def __init__(self, manager: DatabaseManager):

        self.manager = manager
        self.classifier = PostClassifier()

    def ingest_posts(self, rss_feeds):

        posts = fetch_latest_posts(rss_feeds)

        logger.info("Fetched %d posts.", len(posts))

        new_posts = 0
        duplicates = 0

        for post in posts:

            if self.manager.post_exists(post["reddit_id"]):
                duplicates += 1
                continue

            self.manager.insert_post(**post)
            new_posts += 1

        logger.info("Inserted %d new posts.", new_posts)
        logger.info("Skipped %d duplicates.", duplicates)

    def classify_posts(self):

        posts = self.manager.get_unprocessed_posts()

        logger.info(
            "Found %d unprocessed posts.",
            len(posts),
        )

        for post in posts:

            result = self.classifier.classify(
                title=post["title"],
                body=post["body"],
            )

            self.manager.update_ai_result(
                reddit_id=post["reddit_id"],
                category=result["category"],
                subcategory=result["subcategory"],
                confidence=result["confidence"],
                summary=result["summary"],
            )

            logger.info(
                "Classified %s -> %s",
                post["reddit_id"],
                result["category"],
            )