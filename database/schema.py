"""
Database schema creation.
"""

from sqlite3 import Connection

from utils.logger import logger


def initialize_database(connection: Connection) -> None:
    """
    Creates all database tables if they do not exist.
    """

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reddit_id TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        body TEXT,
        author TEXT,
        subreddit TEXT,
        url TEXT,
        created_utc REAL,
        classification TEXT,
        category TEXT,
        subcategory TEXT,
        confidence REAL,
        summary TEXT,
        processed INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS help_posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER NOT NULL,
        category TEXT,
        confidence REAL,
        FOREIGN KEY(post_id) REFERENCES posts(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS experience_posts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER NOT NULL,
        summary TEXT,
        FOREIGN KEY(post_id) REFERENCES posts(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        insight TEXT,
        source_post INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    connection.commit()

    logger.info("Database schema initialized.")