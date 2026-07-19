"""
Database manager.

Contains all database operations.
"""

from sqlite3 import Connection


class DatabaseManager:

    def __init__(self, connection: Connection):
        self.connection = connection

    def insert_post(
        self,
        reddit_id: str,
        title: str,
        body: str,
        author: str,
        subreddit: str,
        url: str,
        created_utc: float,
    ) -> None:

        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO posts(
            reddit_id,
            title,
            body,
            author,
            subreddit,
            url,
            created_utc
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            reddit_id,
            title,
            body,
            author,
            subreddit,
            url,
            created_utc,
        ))

        self.connection.commit()

    def get_unprocessed_posts(self):

        cursor = self.connection.cursor()

        cursor.execute("""
        SELECT *
        FROM posts
        WHERE processed=0
        """)

        return cursor.fetchall()

    def mark_processed(self, reddit_id: str):

        cursor = self.connection.cursor()

        cursor.execute("""
        UPDATE posts
        SET processed=1
        WHERE reddit_id=?
        """,(reddit_id,))

        self.connection.commit()
    def post_exists(self, reddit_id: str) -> bool:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT 1
            FROM posts
            WHERE reddit_id = ?
            """,
            (reddit_id,),
        )
        return cursor.fetchone() is not None
    def update_ai_result(
        self,
        reddit_id: str,
        category: str,
        subcategory: str,
        confidence: float,
        summary: str,
        lead_score: int = 0,
        classified_by: str = "LLM",
        ):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            UPDATE posts
            SET
                category = ?,
                subcategory = ?,
                confidence = ?,
                summary = ?,
                lead_score = ?,
                classified_by = ?,
                processed = 1
            WHERE reddit_id = ?
            """,
            (
                category,
                subcategory,
                confidence,
                summary,
                lead_score,
                classified_by,
                reddit_id,
            ),
        )

        self.connection.commit()

    def get_all_processed_posts(self):
        """
        Returns every processed post, ordered by lead_score (highest
        first). Used by the CSV exporter to produce the full leads list.
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM posts
            WHERE processed = 1
            ORDER BY lead_score DESC, confidence DESC
            """
        )

        return cursor.fetchall()

    def get_top_leads(self, limit: int = 20):
        """
        Returns processed posts ordered by lead_score, highest first.
        Useful for pulling out the people most worth reaching out to.
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM posts
            WHERE processed = 1
            ORDER BY lead_score DESC, confidence DESC
            LIMIT ?
            """,
            (limit,),
        )

        return cursor.fetchall()