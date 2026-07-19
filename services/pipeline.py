from ai.classifier import PostClassifier
from database.manager import DatabaseManager
from reddit.collector import fetch_latest_posts
from rules.entity_extractor import extract_entities
from rules.rule_classifier import classify as rule_classify, build_summary
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

        rule_classified = 0
        llm_classified = 0

        for post in posts:

            title = post["title"]
            body = post["body"]

            # Step 1: fast, free, structured pass over the post.
            entities = extract_entities(title, body)
            rule_result = rule_classify(title, body, entities)

            if not rule_result.needs_llm and rule_result.category != "OTHER":

                # Rule engine is confident enough — no LLM call needed.
                self.manager.update_ai_result(
                    reddit_id=post["reddit_id"],
                    category=rule_result.category,
                    subcategory=rule_result.subcategory,
                    confidence=rule_result.confidence,
                    summary=build_summary(entities),
                    lead_score=rule_result.lead_score,
                    classified_by="RULE",
                )

                rule_classified += 1

                logger.info(
                    "Classified %s -> %s (rule engine, lead_score=%d)",
                    post["reddit_id"],
                    rule_result.category,
                    rule_result.lead_score,
                )

                continue

            # Step 2: rule engine wasn't confident (or found nothing) —
            # fall back to the LLM, but keep the rule engine's lead_score
            # since the LLM doesn't compute one.
            ai_result = self.classifier.classify(title=title, body=body)

            self.manager.update_ai_result(
                reddit_id=post["reddit_id"],
                category=ai_result["category"],
                subcategory=ai_result["subcategory"],
                confidence=ai_result["confidence"],
                summary=ai_result["summary"],
                lead_score=rule_result.lead_score,
                classified_by="LLM",
            )

            llm_classified += 1

            logger.info(
                "Classified %s -> %s (LLM, lead_score=%d)",
                post["reddit_id"],
                ai_result["category"],
                rule_result.lead_score,
            )

        logger.info(
            "Classification complete: %d by rule engine, %d by LLM.",
            rule_classified,
            llm_classified,
        )