"""
Database schema creation.
"""

from sqlite3 import Connection

from utils.logger import logger


def _migrate_posts_table(connection: Connection) -> None:
    """
    Adds any columns that don't exist yet on an already-created
    posts table (safe to run every startup; existing data is kept).
    """

    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(posts)")
    existing_columns = {row[1] for row in cursor.fetchall()}

    new_columns = {
        "lead_score": "INTEGER DEFAULT 0",
        "classified_by": "TEXT",
    }

    for column, definition in new_columns.items():
        if column not in existing_columns:
            cursor.execute(
                f"ALTER TABLE posts ADD COLUMN {column} {definition}"
            )
            logger.info("Added missing column '%s' to posts table.", column)

    connection.commit()


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
        lead_score INTEGER DEFAULT 0,
        classified_by TEXT,
        processed INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    _migrate_posts_table(connection)

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