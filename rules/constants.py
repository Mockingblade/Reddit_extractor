"""
Project-wide constants for the rule engine.

All categories, subcategories and thresholds should be defined here.
Never hardcode these values elsewhere in the project.
"""

# ==========================================================
# PRIMARY CATEGORIES
# ==========================================================

HELP_REQUEST = "HELP_REQUEST"
SUCCESS_STORY = "SUCCESS_STORY"
RESOURCE_DISCUSSION = "RESOURCE_DISCUSSION"
PROFILE_REVIEW = "PROFILE_REVIEW"
GENERAL_DISCUSSION = "GENERAL_DISCUSSION"
QUESTION = "QUESTION"
EXPERIENCE_SHARING = "EXPERIENCE_SHARING"
MBA_DISCUSSION = "MBA_DISCUSSION"
OTHER = "OTHER"


# ==========================================================
# HELP SUBCATEGORIES
# ==========================================================

START_PREPARATION = "START_PREPARATION"
STUDY_PLAN = "STUDY_PLAN"
MOCK_ANALYSIS = "MOCK_ANALYSIS"
SCORE_IMPROVEMENT = "SCORE_IMPROVEMENT"

QUANT_HELP = "QUANT_HELP"
VERBAL_HELP = "VERBAL_HELP"
DATA_INSIGHTS = "DATA_INSIGHTS"

TIMELINE = "TIMELINE"
BOOK_RECOMMENDATION = "BOOK_RECOMMENDATION"
RESOURCE_SELECTION = "RESOURCE_SELECTION"

UNCERTAINTY = "UNCERTAINTY"
MOTIVATION = "MOTIVATION"

TEST_DAY = "TEST_DAY"
RETARGETING = "RETARGETING"

OTHER_SUBCATEGORY = "OTHER"


# ==========================================================
# RESOURCE TYPES
# ==========================================================

OFFICIAL_GUIDE = "OFFICIAL_GUIDE"
GMAT_CLUB = "GMAT_CLUB"
TARGET_TEST_PREP = "TARGET_TEST_PREP"
EG_MOCKS = "EXPERTS_GLOBAL"
TOP_ONE_PERCENT = "TOP_ONE_PERCENT"
E_GMAT = "E_GMAT"
MANHATTAN = "MANHATTAN"
MAGOOSH = "MAGOOSH"
YOUTUBE = "YOUTUBE"
PRIVATE_TUTOR = "PRIVATE_TUTOR"
BOOK = "BOOK"
COURSE = "COURSE"


# ==========================================================
# PROFILE REVIEW TYPES
# ==========================================================

MBA_PROFILE = "MBA_PROFILE"
COLLEGE_SELECTION = "COLLEGE_SELECTION"
GMAT_REQUIREMENT = "GMAT_REQUIREMENT"


# ==========================================================
# QUESTION TYPES
# ==========================================================

SHOULD_I = "SHOULD_I"
HOW_TO = "HOW_TO"
WHAT_TO_DO = "WHAT_TO_DO"
IS_IT_WORTH_IT = "IS_IT_WORTH_IT"


# ==========================================================
# LEAD SCORE
# ==========================================================

HIGH_VALUE = "HIGH_VALUE"
MEDIUM_VALUE = "MEDIUM_VALUE"
LOW_VALUE = "LOW_VALUE"


# ==========================================================
# CONFIDENCE THRESHOLDS
# ==========================================================

HIGH_CONFIDENCE = 0.90
MEDIUM_CONFIDENCE = 0.75
LOW_CONFIDENCE = 0.60


# ==========================================================
# LLM DECISION
# ==========================================================

LLM_CONFIDENCE_THRESHOLD = 0.75


# ==========================================================
# MAXIMUM SCORING
# ==========================================================

MAX_LEAD_SCORE = 100


# ==========================================================
# PIPELINE FLAGS
# ==========================================================

NEEDS_LLM = True
RULE_BASED = False


# ==========================================================
# OUTPUT KEYS
# ==========================================================

KEY_CATEGORY = "category"
KEY_SUBCATEGORY = "subcategory"
KEY_CONFIDENCE = "confidence"
KEY_LEAD_SCORE = "lead_score"
KEY_REASON = "reason"
KEY_NEEDS_LLM = "needs_llm"
KEY_SUMMARY = "summary"
KEY_DETECTED_ENTITIES = "entities"


# ==========================================================
# POST TYPES
# ==========================================================

POST_TYPE_HELP = "HELP"
POST_TYPE_EXPERIENCE = "EXPERIENCE"
POST_TYPE_RESOURCE = "RESOURCE"
POST_TYPE_PROFILE = "PROFILE"
POST_TYPE_DISCUSSION = "DISCUSSION"


# ==========================================================
# GMAT SECTIONS
# ==========================================================

QUANT = "QUANT"
VERBAL = "VERBAL"
DATA_INSIGHTS_SECTION = "DATA_INSIGHTS"


# ==========================================================
# DEFAULT RESPONSE
# ==========================================================

DEFAULT_RESULT = {
    KEY_CATEGORY: OTHER,
    KEY_SUBCATEGORY: OTHER_SUBCATEGORY,
    KEY_CONFIDENCE: 0.0,
    KEY_LEAD_SCORE: 0,
    KEY_REASON: [],
    KEY_NEEDS_LLM: True,
    KEY_SUMMARY: "",
    KEY_DETECTED_ENTITIES: {},
}