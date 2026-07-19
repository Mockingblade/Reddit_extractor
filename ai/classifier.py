"""
Gemini classifier for Reddit posts.
"""

from pathlib import Path
import json

from google import genai

from config.settings import settings
from utils.logger import logger


class PostClassifier:
    """
    Uses Gemini to classify Reddit posts.
    """

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

        prompt_path = Path("prompts") / "classification_prompt.txt"

        self.system_prompt = prompt_path.read_text(encoding="utf-8")

        logger.info("Gemini classifier initialized.")

    def classify(self, title: str, body: str) -> dict:
        """
        Classify a Reddit post.
        """

        prompt = f"""
{self.system_prompt}

Post Title:
{title}

Post Body:
{body}
"""

        try:
            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt,
            )

            text = response.text.strip()

            # Gemini sometimes wraps JSON in markdown
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

            return json.loads(text)

        except Exception as e:
            logger.exception("Classification failed: %s", e)

            return {
                "category": "OTHER",
                "subcategory": "OTHER",
                "confidence": 0.0,
                "summary": "",
            }