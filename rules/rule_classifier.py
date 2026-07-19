"""
Rule-based classifier.

Uses:
1. Extracted entities
2. Keyword scoring
3. Rule scoring

No LLM calls happen here.
"""

from __future__ import annotations
from typing import Dict
from dataclasses import dataclass

from rules.entity_extractor import ExtractedEntities
from rules.normalizer import build_document
from rules import keywords


# ==========================================================
# CLASSIFICATION RESULT
# ==========================================================

@dataclass
class ClassificationResult:

    category: str

    subcategory: str

    confidence: float

    lead_score: int

    needs_llm: bool


# ==========================================================
# CATEGORIES
# ==========================================================

HELP_REQUEST = "HELP_REQUEST"

# Aligned with the categories used in prompts/classification_prompt.txt
# so rule-classified and LLM-classified posts share one vocabulary.
EXPERIENCE = "SUCCESS_STORY"

MBA = "PROFILE_REVIEW"

DISCUSSION = "GENERAL_DISCUSSION"

UNKNOWN = "OTHER"


# ==========================================================
# SUBCATEGORIES
# ==========================================================

START_PREPARATION = "START_PREPARATION"

STUDY_PLAN = "STUDY_PLAN"

MOCK_ANALYSIS = "MOCK_ANALYSIS"

SCORE_IMPROVEMENT = "SCORE_IMPROVEMENT"

RESOURCE_ADVICE = "RESOURCE_ADVICE"

SUCCESS_STORY = "SUCCESS_STORY"

EXPERIENCE_SHARE = "EXPERIENCE_SHARE"

PROFILE_REVIEW = "PROFILE_REVIEW"

COLLEGE_SELECTION = "COLLEGE_SELECTION"

GENERAL_DISCUSSION = "GENERAL_DISCUSSION"


# ==========================================================
# KEYWORD SCORING
# ==========================================================

def keyword_score(
    text: str,
    keyword_dict: dict[str, int],
) -> int:

    score = 0

    for keyword, weight in keyword_dict.items():

        if keyword in text:
            score += weight

    return score


# ==========================================================
# LEAD SCORE
# ==========================================================

def calculate_lead_score(
    entities: ExtractedEntities,
) -> int:

    score = 0

    if entities.is_question:
        score += 25

    if entities.working_professional:
        score += 20

    if entities.timeline_value is not None:
        score += 15

    if entities.target_score is not None:
        score += 10

    if entities.mock_number is not None:
        score += 15

    if entities.current_score is not None:
        score += 10

    if entities.resources:
        score += 5

    return min(score, 100)


# ==========================================================
# CONFIDENCE
# ==========================================================

def calculate_confidence(
    best_score: int,
) -> float:

    confidence = best_score / 100

    return min(confidence, 1.0)


# ==========================================================
# PREPARE DOCUMENT
# ==========================================================

def prepare_document(
    title: str,
    body: str,
) -> str:

    return build_document(title, body)
# ==========================================================
# HELP REQUEST CLASSIFIER
# ==========================================================

def classify_help_request(
    text: str,
    entities: ExtractedEntities,
) -> tuple[str | None, int]:

    scores = {}

    # ------------------------------------------------------
    # START PREPARATION
    # ------------------------------------------------------

    start_score = keyword_score(
        text,
        keywords.START_PREPARATION_KEYWORDS,
    )

    if entities.timeline_value is not None:
        start_score += 5

    if entities.is_question:
        start_score += 10

    scores[START_PREPARATION] = start_score

    # ------------------------------------------------------
    # STUDY PLAN
    # ------------------------------------------------------

    study_score = keyword_score(
        text,
        keywords.STUDY_PLAN_KEYWORDS,
    )

    if entities.timeline_value is not None:
        study_score += 10

    scores[STUDY_PLAN] = study_score

    # ------------------------------------------------------
    # MOCK ANALYSIS
    # ------------------------------------------------------

    mock_score = keyword_score(
        text,
        keywords.MOCK_ANALYSIS_KEYWORDS,
    )

    if entities.mock_number is not None:
        mock_score += 25

    if entities.sections:
        mock_score += 20

    if entities.current_score is not None:
        mock_score += 10

    scores[MOCK_ANALYSIS] = mock_score

    # ------------------------------------------------------
    # SCORE IMPROVEMENT
    # ------------------------------------------------------

    improve_score = keyword_score(
        text,
        keywords.SCORE_IMPROVEMENT_KEYWORDS,
    )

    if (
        entities.current_score is not None
        and entities.target_score is not None
    ):
        improve_score += 20

    scores[SCORE_IMPROVEMENT] = improve_score

    # ------------------------------------------------------
    # RESOURCE ADVICE
    # ------------------------------------------------------

    resource_score = keyword_score(
        text,
        keywords.RESOURCE_KEYWORDS,
    )

    if entities.resources:
        resource_score += 20

    scores[RESOURCE_ADVICE] = resource_score

    # ------------------------------------------------------
    # RESULT
    # ------------------------------------------------------

    best_category = max(scores.items(), key=lambda x: x[1])[0]

    best_score = scores[best_category]

    best_score = scores[best_category]

    if best_score < 20:
        return None, 0

    return best_category, best_score


# ==========================================================
# HELP REQUEST DETECTION
# ==========================================================

def is_help_request(
    text: str,
    entities: ExtractedEntities,
) -> bool:

    if entities.is_question:
        return True

    help_score = keyword_score(
        text,
        keywords.HELP_KEYWORDS,
    )

    return help_score >= 15
# ==========================================================
# EXPERIENCE CLASSIFIER
# ==========================================================

def classify_experience(
    text: str,
    entities: ExtractedEntities,
) -> tuple[str | None, int]:

    experience_score = keyword_score(
        text,
        keywords.EXPERIENCE_KEYWORDS,
    )

    if entities.current_score is not None:
        experience_score += 10

    if entities.timeline_value is not None:
        experience_score += 10

    if experience_score >= 25:
        return SUCCESS_STORY, experience_score

    return None, 0


# ==========================================================
# MBA CLASSIFIER
# ==========================================================

def classify_mba(
    text: str,
    entities: ExtractedEntities,
) -> tuple[str | None, int]:

    profile_score = keyword_score(
        text,
        keywords.PROFILE_REVIEW_KEYWORDS,
    )

    college_score = (
    keyword_score(text, keywords.MBA_KEYWORDS)
    + keyword_score(text, keywords.SCHOOL_KEYWORDS)
)

    if len(entities.schools) >= 2:
        college_score += 20

    if profile_score >= college_score:

        if profile_score >= 20:
            return PROFILE_REVIEW, profile_score

    else:

        if college_score >= 20:
            return COLLEGE_SELECTION, college_score

    return None, 0


# ==========================================================
# DISCUSSION CLASSIFIER
# ==========================================================

def classify_discussion(
    text: str,
) -> tuple[str | None, int]:

    discussion_score = (
    keyword_score(text, keywords.MOTIVATION_KEYWORDS)
    + keyword_score(text, keywords.SUCCESS_KEYWORDS)
    + keyword_score(text, keywords.FAILURE_KEYWORDS)
)

    if discussion_score >= 20:
        return GENERAL_DISCUSSION, discussion_score

    return None, 0


# ==========================================================
# SUMMARY BUILDER (for rule-classified posts, no LLM call)
# ==========================================================

def build_summary(entities: ExtractedEntities) -> str:
    """
    Build a short human-readable summary from extracted entities,
    used when a post is classified without calling the LLM.
    """

    parts = []

    if entities.working_professional:
        parts.append("Working professional")

    if entities.current_score is not None:
        parts.append(f"Current score {entities.current_score}")

    if entities.target_score is not None:
        parts.append(f"Target {entities.target_score}")

    if entities.sections:
        section_str = ", ".join(
            f"{k}{v}" for k, v in entities.sections.items()
        )
        parts.append(f"Sections {section_str}")

    if entities.mock_number is not None:
        parts.append(f"Mock #{entities.mock_number}")

    if entities.timeline_value is not None and entities.timeline_unit:
        parts.append(
            f"{entities.timeline_value} {entities.timeline_unit} left"
        )

    if entities.resources:
        parts.append("Resources: " + ", ".join(entities.resources))

    if entities.schools:
        parts.append("Schools: " + ", ".join(entities.schools))

    return ". ".join(parts)


# ==========================================================
# MAIN CLASSIFIER
# ==========================================================

def classify(
    title: str,
    body: str,
    entities: ExtractedEntities,
) -> ClassificationResult:

    text = prepare_document(title, body)

    # --------------------------------------------------

    if is_help_request(text, entities):

        subcategory, score = classify_help_request(
            text,
            entities,
        )

        if subcategory:

            confidence = calculate_confidence(score)

            return ClassificationResult(
                category=HELP_REQUEST,
                subcategory=subcategory,
                confidence=confidence,
                lead_score=calculate_lead_score(entities),
                needs_llm=confidence < 0.85,
            )

    # --------------------------------------------------

    subcategory, score = classify_experience(
        text,
        entities,
    )

    if subcategory:

        confidence = calculate_confidence(score)

        return ClassificationResult(
            category=EXPERIENCE,
            subcategory=subcategory,
            confidence=confidence,
            lead_score=calculate_lead_score(entities),
            needs_llm=confidence < 0.85,
        )

    # --------------------------------------------------

    subcategory, score = classify_mba(
        text,
        entities,
    )

    if subcategory:

        confidence = calculate_confidence(score)

        return ClassificationResult(
            category=MBA,
            subcategory=subcategory,
            confidence=confidence,
            lead_score=calculate_lead_score(entities),
            needs_llm=confidence < 0.85,
        )

    # --------------------------------------------------

    subcategory, score = classify_discussion(text)

    if subcategory:

        confidence = calculate_confidence(score)

        return ClassificationResult(
            category=DISCUSSION,
            subcategory=subcategory,
            confidence=confidence,
            lead_score=calculate_lead_score(entities),
            needs_llm=confidence < 0.85,
        )

    # --------------------------------------------------

    return ClassificationResult(
        category=UNKNOWN,
        subcategory="OTHER",
        confidence=0.0,
        lead_score=calculate_lead_score(entities),
        needs_llm=True,
    )