"""
Text normalization for Reddit posts.

Every post should pass through this module before
keyword matching and regex detection.
"""

from __future__ import annotations

import re


# ==========================================================
# COMMON REPLACEMENTS
# ==========================================================

REPLACEMENTS = {

    # GMAT Resources
    "gmatclub": "gmat club",
    "gmat-club": "gmat club",

    "egmat": "e-gmat",
    "e gmat": "e-gmat",

    "ttp": "target test prep",

    "og": "official guide",

    "eg mocks": "experts global",

    "eg": "experts global",

    # Working
    "9-5": "9 to 5",
    "9to5": "9 to 5",
    "full-time": "full time",

    # MBA
    "b-school": "business school",
    "bschool": "business school",

    # ESR
    "enhanced score report": "esr",

    # Focus Edition
    "gmat fe": "gmat focus edition",
    "focus edition": "gmat focus edition",

    # Common spelling
    "analyse": "analyze",
    "colour": "color",
    "favourite": "favorite",

    # Misc
    "dont": "don't",
    "cant": "can't",
    "wont": "won't",
    "im": "i'm",

}


# ==========================================================
# REMOVE URLS
# ==========================================================

URL_PATTERN = re.compile(r"https?://\S+")


# ==========================================================
# REMOVE MARKDOWN LINKS
# ==========================================================

MARKDOWN_LINK = re.compile(r"\[.*?\]\(.*?\)")


# ==========================================================
# REMOVE HTML
# ==========================================================

HTML_TAGS = re.compile(r"<.*?>")


# ==========================================================
# MULTIPLE SPACES
# ==========================================================

MULTIPLE_SPACES = re.compile(r"\s+")


# ==========================================================
# REMOVE PUNCTUATION
# ==========================================================

PUNCTUATION = re.compile(r"[^\w\s\?]")


# ==========================================================
# NORMALIZE TEXT
# ==========================================================

def normalize(text: str) -> str:
    """
    Normalize Reddit text for rule matching.
    """

    if text is None:
        return ""

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = URL_PATTERN.sub(" ", text)

    # Remove markdown
    text = MARKDOWN_LINK.sub(" ", text)

    # Remove HTML
    text = HTML_TAGS.sub(" ", text)

    # Resource replacements
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    # Remove punctuation
    text = PUNCTUATION.sub(" ", text)

    # Collapse whitespace
    text = MULTIPLE_SPACES.sub(" ", text)

    return text.strip()


# ==========================================================
# COMBINE TITLE + BODY
# ==========================================================

def build_document(title: str, body: str) -> str:
    """
    Combine title and body into a single normalized document.
    """

    title = normalize(title)

    body = normalize(body)

    return f"{title}\n{body}"