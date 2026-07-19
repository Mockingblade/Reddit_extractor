"""
Application configuration.

Loads all environment variables from the .env file
and exposes them through a single settings object.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # ---------- OpenAI ----------
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = ""
    # ---------- Reddit ----------
    REDDIT_CLIENT_ID: str = ""
    REDDIT_CLIENT_SECRET: str = ""
    REDDIT_USER_AGENT: str = "GMAT Intelligence v1.0"

    # ---------- Database ----------
    DATABASE_PATH: str = "data/reddit.db"

    # ---------- Scheduler ----------
    CHECK_INTERVAL_MINUTES: int = 10

    # ---------- Logging ----------
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/app.log"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()