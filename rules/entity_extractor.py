"""
Extract structured entities from Reddit posts.

This module does NOT classify posts.

Its only responsibility is to extract structured information
from raw Reddit text.
"""

from __future__ import annotations

import re

from dataclasses import dataclass, field
from typing import Optional

from rules.normalizer import build_document


# ==========================================================
# ENTITY MODEL
# ==========================================================

@dataclass
class ExtractedEntities:
    """
    Structured representation of a Reddit post.
    """

    current_score: Optional[int] = None
    target_score: Optional[int] = None

    timeline_value: Optional[int] = None
    timeline_unit: Optional[str] = None

    resources: list[str] = field(default_factory=list)

    schools: list[str] = field(default_factory=list)

    working_professional: bool = False

    sections: dict[str, int] = field(default_factory=dict)

    mock_number: Optional[int] = None

    is_question: bool = False


# ==========================================================
# REGEX PATTERNS
# ==========================================================

# GMAT Focus score
SCORE_PATTERN = re.compile(r"\b([2-7]\d{2}|805)\b")

# Timeline
TIMELINE_PATTERN = re.compile(
    r"\b(\d+)\s*(day|days|week|weeks|month|months)\b"
)

# Target score
TARGET_PATTERN = re.compile(
    r"(target|goal|aim|aiming|want)\D{0,20}([2-7]\d{2}|805)",
    re.IGNORECASE,
)

# Current score
CURRENT_PATTERN = re.compile(
    r"(current|mock|scored|score|got)\D{0,20}([2-7]\d{2}|805)",
    re.IGNORECASE,
)


# ==========================================================
# SCORE EXTRACTION
# ==========================================================

def extract_scores(
    text: str,
    entities: ExtractedEntities,
) -> None:
    """
    Extract current score and target score.
    """

    target = TARGET_PATTERN.search(text)

    if target:
        entities.target_score = int(target.group(2))

    current = CURRENT_PATTERN.search(text)

    if current:
        entities.current_score = int(current.group(2))

    # Fallback

    if entities.current_score is None:

        scores = SCORE_PATTERN.findall(text)

        if scores:

            entities.current_score = int(scores[0])

    # If target wasn't detected but there are
    # multiple scores, assume highest score is target.

    if (
        entities.target_score is None
        and entities.current_score is not None
    ):

        scores = [
            int(score)
            for score in SCORE_PATTERN.findall(text)
        ]

        if len(scores) >= 2:

            highest = max(scores)

            if highest != entities.current_score:
                entities.target_score = highest


# ==========================================================
# TIMELINE EXTRACTION
# ==========================================================

def extract_timeline(
    text: str,
    entities: ExtractedEntities,
) -> None:
    """
    Extract preparation timeline.
    """

    match = TIMELINE_PATTERN.search(text)

    if not match:
        return

    entities.timeline_value = int(match.group(1))

    entities.timeline_unit = match.group(2)


# ==========================================================
# MASTER EXTRACTION (Part 1)
# ==========================================================
def extract_basic_entities(
    title: str,
    body: str,
) -> ExtractedEntities:

    document = build_document(title, body)

    entities = ExtractedEntities()

    extract_scores(document, entities)

    extract_timeline(document, entities)

    extract_resources(document, entities)

    extract_schools(document, entities)

    extract_work_profile(document, entities)

    extract_sections(document, entities)

    return entities
# ==========================================================
# RESOURCE DICTIONARY
# ==========================================================

RESOURCE_MAP = {
    "official guide": "Official Guide",
    "target test prep": "Target Test Prep",
    "gmat club": "GMAT Club",
    "experts global": "Experts Global",
    "e-gmat": "e-GMAT",
    "magoosh": "Magoosh",
    "manhattan prep": "Manhattan Prep",
    "kaplan": "Kaplan",
    "princeton review": "Princeton Review",
    "top one percent": "Top One Percent",
}


# ==========================================================
# SCHOOL DICTIONARY
# ==========================================================

SCHOOL_MAP = {
    "isb": "ISB",
    "insead": "INSEAD",
    "hec": "HEC Paris",
    "hec paris": "HEC Paris",
    "wharton": "Wharton",
    "stanford": "Stanford GSB",
    "harvard": "Harvard Business School",
    "mit": "MIT Sloan",
    "sloan": "MIT Sloan",
    "lbs": "London Business School",
    "london business school": "London Business School",
    "booth": "Chicago Booth",
    "kellogg": "Kellogg",
    "columbia": "Columbia Business School",
    "ross": "Michigan Ross",
    "darden": "Virginia Darden",
    "tuck": "Tuck",
    "ie": "IE Business School",
    "iese": "IESE",
    "esade": "ESADE",
}


# ==========================================================
# WORK PROFILE KEYWORDS
# ==========================================================

WORK_KEYWORDS = [
    "working professional",
    "software engineer",
    "developer",
    "consultant",
    "analyst",
    "product manager",
    "full time",
    "9 to 5",
    "office job",
    "corporate",
    "while working",
]


# ==========================================================
# SECTION SCORES
# ==========================================================

SECTION_PATTERN = re.compile(
    r"\b(Q|V|DI)\s*[:\-]?\s*(\d{2})\b",
    re.IGNORECASE,
)


# ==========================================================
# RESOURCE EXTRACTION
# ==========================================================

def extract_resources(
    text: str,
    entities: ExtractedEntities,
) -> None:

    for keyword, name in RESOURCE_MAP.items():

        if keyword in text and name not in entities.resources:
            entities.resources.append(name)


# ==========================================================
# SCHOOL EXTRACTION
# ==========================================================

def extract_schools(
    text: str,
    entities: ExtractedEntities,
) -> None:

    for keyword, school in SCHOOL_MAP.items():

        if keyword in text and school not in entities.schools:
            entities.schools.append(school)


# ==========================================================
# WORK PROFILE
# ==========================================================

def extract_work_profile(
    text: str,
    entities: ExtractedEntities,
) -> None:

    for keyword in WORK_KEYWORDS:

        if keyword in text:
            entities.working_professional = True
            return


# ==========================================================
# SECTION SCORE EXTRACTION
# ==========================================================

def extract_sections(
    text: str,
    entities: ExtractedEntities,
) -> None:

    matches = SECTION_PATTERN.findall(text)

    for section, score in matches:

        entities.sections[section.upper()] = int(score)
# ==========================================================
# MOCK NUMBER
# ==========================================================

MOCK_PATTERN = re.compile(
    r"(?:official\s+)?(?:practice\s+test|mock)\s*#?\s*(\d+)",
    re.IGNORECASE,
)


def extract_mock_number(
    text: str,
    entities: ExtractedEntities,
) -> None:

    match = MOCK_PATTERN.search(text)

    if match:
        entities.mock_number = int(match.group(1))


# ==========================================================
# QUESTION DETECTION
# ==========================================================

QUESTION_PATTERNS = [

    "should i",
    "can i",
    "can someone",
    "need help",
    "help me",
    "advice",
    "guidance",
    "what should i do",
    "where do i start",
    "how do i",
    "how should i",
    "is it worth",
]


def extract_question(
    text: str,
    entities: ExtractedEntities,
) -> None:

    if "?" in text:
        entities.is_question = True
        return

    for phrase in QUESTION_PATTERNS:

        if phrase in text:
            entities.is_question = True
            return


# ==========================================================
# COMPLETE EXTRACTION
# ==========================================================

def extract_entities(
    title: str,
    body: str,
) -> ExtractedEntities:

    document = build_document(title, body)

    entities = ExtractedEntities()

    extract_scores(document, entities)

    extract_timeline(document, entities)

    extract_resources(document, entities)

    extract_schools(document, entities)

    extract_work_profile(document, entities)

    extract_sections(document, entities)

    extract_mock_number(document, entities)

    extract_question(document, entities)

    return entities