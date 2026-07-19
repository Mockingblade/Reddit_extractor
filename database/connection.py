"""
SQLite database connection.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from config.settings import settings
from utils.logger import logger


class DatabaseConnection:
    """Creates and manages the SQLite connection."""

    def __init__(self) -> None:
        db_path = Path(settings.DATABASE_PATH)

        # Ensure parent directory exists
        db_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row

        logger.info("Connected to SQLite database.")

    def get_connection(self) -> sqlite3.Connection:
        return self.connection

    def close(self) -> None:
        self.connection.close()
        logger.info("Database connection closed.")