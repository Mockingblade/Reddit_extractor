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
                processed = 1
            WHERE reddit_id = ?
            """,
            (
                category,
                subcategory,
                confidence,
                summary,
                reddit_id,
            ),
        )

        self.connection.commit()