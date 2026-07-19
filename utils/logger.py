"""
Centralized logging configuration.

Every module in the application should import the logger
from this file instead of creating its own.
"""

from __future__ import annotations

import logging
from pathlib import Path

from config.settings import settings


def setup_logger() -> logging.Logger:
    """
    Configure and return the application logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    # Create the logs directory if it doesn't exist
    log_file = Path(settings.LOG_FILE)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Get the application logger
    logger = logging.getLogger("reddit_gmat_intelligence")

    # Prevent duplicate handlers if setup_logger() is called again
    if logger.handlers:
        return logger

    logger.setLevel(settings.LOG_LEVEL)

    # Common format for all log messages
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File output
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


logger = setup_logger()