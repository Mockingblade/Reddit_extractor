"""
Weighted keyword dictionaries for the rule engine.

Higher score = stronger confidence.
"""

# ==========================================================
# HELP REQUEST
# ==========================================================

HELP_KEYWORDS = {
    "help": 3,
    "need help": 10,
    "please help": 12,
    "can someone help": 15,
    "guidance": 8,
    "advice": 8,
    "suggest": 7,
    "suggestions": 7,
    "recommend": 6,
    "recommendation": 6,
    "confused": 10,
    "lost": 10,
    "stuck": 8,
    "struggling": 8,
    "difficulty": 7,
    "problem": 6,
    "issue": 6,
    "urgent": 6,
    "advice needed": 12,
    "any tips": 8,
    "tips": 5,
    "looking for help": 12,
    "what should i do": 15,
    "what do i do": 15,
    "how should i": 10,
    "can anyone guide": 15,
    "mentor": 8,
    "coaching": 5,
    "tutor": 5,
}

# ==========================================================
# START PREPARATION
# ==========================================================

START_PREPARATION_KEYWORDS = {
    "start": 4,
    "starting": 6,
    "begin": 6,
    "beginner": 10,
    "new to gmat": 15,
    "first time": 10,
    "never studied": 12,
    "where do i start": 20,
    "how do i start": 20,
    "starting from scratch": 18,
    "roadmap": 12,
    "study roadmap": 15,
    "starting point": 10,
    "foundation": 8,
    "complete beginner": 18,
    "zero knowledge": 18,
    "fresh start": 12,
    "new here": 8,
    "getting started": 15,
    "initial strategy": 12,
    "first attempt": 10,
}

# ==========================================================
# STUDY PLAN
# ==========================================================

STUDY_PLAN_KEYWORDS = {
    "study plan": 20,
    "study schedule": 18,
    "study strategy": 16,
    "preparation strategy": 15,
    "plan": 4,
    "routine": 8,
    "daily routine": 12,
    "weekly plan": 10,
    "schedule": 6,
    "how many hours": 15,
    "hours per day": 15,
    "study hours": 12,
    "3 months": 12,
    "4 months": 12,
    "5 months": 10,
    "6 months": 8,
    "8 weeks": 10,
    "12 weeks": 10,
    "timeline": 10,
    "preparation time": 12,
    "working professional": 12,
    "full time job": 12,
    "9 to 5": 15,
    "job": 4,
    "office": 4,
    "college student": 8,
    "student": 3,
}

# ==========================================================
# UNCERTAINTY
# ==========================================================

UNCERTAINTY_KEYWORDS = {
    "should i": 20,
    "can i": 12,
    "is it worth": 18,
    "worth it": 18,
    "not sure": 20,
    "unsure": 20,
    "uncertain": 20,
    "confused": 18,
    "don't know": 15,
    "dont know": 15,
    "don't understand": 15,
    "lost": 18,
    "afraid": 10,
    "worried": 10,
    "nervous": 8,
    "possible": 8,
    "realistic": 10,
    "feasible": 10,
    "chance": 8,
    "am i too late": 18,
    "can i score": 15,
    "can i improve": 15,
    "need advice": 18,
    "looking for advice": 18,
}

# ==========================================================
# TIMELINE
# ==========================================================

TIMELINE_KEYWORDS = {
    "1 month": 6,
    "2 months": 8,
    "3 months": 10,
    "4 months": 10,
    "5 months": 8,
    "6 months": 6,
    "30 days": 10,
    "60 days": 10,
    "90 days": 10,
    "120 days": 10,
    "deadline": 8,
    "before application": 12,
    "before mba": 10,
    "before round 1": 12,
    "before r1": 12,
    "before round 2": 10,
}

# ==========================================================
# GOAL SCORE
# ==========================================================

GOAL_SCORE_KEYWORDS = {
    "target": 8,
    "goal": 8,
    "aiming": 8,
    "want to score": 15,
    "dream score": 12,
    "705": 10,
    "715": 10,
    "725": 10,
    "735": 10,
    "focus edition": 6,
}

# ==========================================================
# QUESTION INDICATORS
# ==========================================================

QUESTION_KEYWORDS = {
    "?": 4,
    "how": 2,
    "why": 2,
    "when": 2,
    "where": 2,
    "which": 2,
    "what": 2,
    "who": 2,
}
# ==========================================================
# MOCK ANALYSIS
# ==========================================================

MOCK_ANALYSIS_KEYWORDS = {
    "mock": 8,
    "official mock": 20,
    "mba.com mock": 18,
    "practice test": 12,
    "mock analysis": 20,
    "analyze my mock": 25,
    "analyse my mock": 25,
    "mock review": 18,
    "review my mock": 22,
    "attempt analysis": 18,
    "score breakdown": 18,
    "performance analysis": 18,
    "review my performance": 20,
    "test report": 15,
    "official practice exam": 18,
    "practice exam": 12,
    "exam analysis": 15,
    "esr": 25,
    "enhanced score report": 25,
    "diagnostics": 18,
    "diagnostic test": 18,
    "accuracy": 15,
    "accuracy rate": 18,
    "timing": 18,
    "time management": 20,
    "ran out of time": 18,
    "finished early": 8,
    "guessing": 15,
    "educated guess": 12,
    "review mistakes": 18,
    "mistake log": 20,
    "error log": 18,
    "wrong answers": 12,
    "careless mistakes": 20,
    "silly mistakes": 18,
}

# ==========================================================
# SCORE IMPROVEMENT
# ==========================================================

SCORE_IMPROVEMENT_KEYWORDS = {
    "improve": 10,
    "improvement": 10,
    "increase": 8,
    "raise my score": 18,
    "boost score": 18,
    "improve score": 20,
    "improve quant": 18,
    "improve verbal": 18,
    "improve di": 18,
    "stuck at": 18,
    "plateau": 18,
    "score plateau": 20,
    "breaking": 10,
    "next level": 10,
    "target score": 15,
    "need 705": 20,
    "need 695": 20,
    "need 655": 15,
    "score gap": 15,
    "jump from": 12,
    "increase by": 12,
    "retake": 15,
    "second attempt": 15,
    "third attempt": 15,
}

# ==========================================================
# QUANT HELP
# ==========================================================

QUANT_KEYWORDS = {
    "quant": 15,
    "quantitative": 12,
    "math": 8,
    "arithmetic": 15,
    "algebra": 15,
    "geometry": 15,
    "number properties": 18,
    "statistics": 15,
    "probability": 15,
    "permutations": 15,
    "combinations": 15,
    "percentages": 12,
    "ratios": 12,
    "fractions": 12,
    "work rate": 15,
    "speed distance": 15,
    "mixtures": 15,
    "interest": 10,
    "equations": 12,
    "inequalities": 12,
    "word problems": 12,
    "question bank": 8,
    "hard quant": 15,
    "quant strategy": 15,
}

# ==========================================================
# VERBAL HELP
# ==========================================================

VERBAL_KEYWORDS = {
    "verbal": 15,
    "reading comprehension": 18,
    "rc": 12,
    "critical reasoning": 18,
    "cr": 12,
    "assumption": 12,
    "strengthen": 12,
    "weaken": 12,
    "inference": 12,
    "boldface": 12,
    "evaluate": 12,
    "paradox": 12,
    "argument": 10,
    "passage": 8,
    "main idea": 10,
    "detail question": 10,
    "logic": 10,
    "verbal strategy": 15,
    "reading speed": 15,
}

# ==========================================================
# DATA INSIGHTS
# ==========================================================

DATA_INSIGHTS_KEYWORDS = {
    "data insights": 20,
    "di": 18,
    "data sufficiency": 18,
    "ds": 18,
    "table analysis": 18,
    "multi source reasoning": 18,
    "two part analysis": 18,
    "graphics interpretation": 18,
    "graph": 10,
    "chart": 10,
    "table": 10,
    "case analysis": 10,
    "logical reasoning": 10,
    "data analysis": 15,
    "interpretation": 10,
}

# ==========================================================
# PERFORMANCE INDICATORS
# ==========================================================

PERFORMANCE_KEYWORDS = {
    "weak area": 18,
    "strong area": 18,
    "strength": 10,
    "weakness": 10,
    "improving": 10,
    "declining": 10,
    "accuracy": 15,
    "speed": 12,
    "pace": 12,
    "consistency": 15,
    "performance": 15,
    "review": 8,
    "analysis": 10,
    "breakdown": 12,
    "section score": 18,
    "percentile": 12,
    "rank": 10,
    "overall score": 18,
}
# ==========================================================
# RESOURCE DISCUSSION
# ==========================================================

RESOURCE_KEYWORDS = {
    # Official Material
    "official guide": 20,
    "og": 10,
    "official questions": 18,
    "official mocks": 18,
    "mba.com": 18,

    # Target Test Prep
    "target test prep": 25,
    "ttp": 20,

    # GMAT Club
    "gmat club": 22,
    "gmatclub": 22,

    # Experts Global
    "experts global": 22,
    "expertsglobal": 22,
    "eg mocks": 22,

    # e-GMAT
    "e-gmat": 22,
    "egmat": 22,

    # TOP
    "top one percent": 22,
    "top 1 percent": 22,

    # Manhattan
    "manhattan": 20,
    "manhattan prep": 22,

    # Magoosh
    "magoosh": 20,

    # Princeton
    "princeton review": 20,

    # Kaplan
    "kaplan": 18,

    # Books
    "book": 8,
    "books": 8,
    "guide": 8,
    "material": 8,
    "materials": 8,
    "resource": 8,
    "resources": 8,

    # Courses
    "course": 10,
    "courses": 10,
    "video course": 15,
    "online course": 15,
    "self study": 12,

    # Tutors
    "private tutor": 15,
    "tutor": 8,
    "coach": 8,
    "coaching": 8,

    # Free Resources
    "youtube": 8,
    "playlist": 8,
    "free resources": 12,
    "free material": 12,
    "pdf": 5,
    "notes": 5,
}

# ==========================================================
# BUYING / COMPARISON
# ==========================================================

RESOURCE_COMPARISON_KEYWORDS = {
    "which is better": 18,
    "worth buying": 20,
    "worth it": 15,
    "should i buy": 20,
    "buy": 8,
    "purchase": 10,
    "subscription": 10,
    "lifetime": 10,
    "monthly": 8,
    "compare": 12,
    "comparison": 12,
    "vs": 10,
    "versus": 10,
    "alternative": 12,
    "replace": 10,
    "best resource": 18,
    "best course": 18,
    "best books": 18,
}

# ==========================================================
# PROFILE REVIEW
# ==========================================================

PROFILE_REVIEW_KEYWORDS = {
    "profile review": 30,
    "review my profile": 30,
    "profile evaluation": 28,
    "chance me": 28,
    "my profile": 12,
    "evaluate my profile": 28,
    "admission chances": 22,
    "what schools": 18,
    "target schools": 18,
    "safe schools": 18,
    "dream schools": 18,
    "reach schools": 18,
    "college shortlist": 18,
    "school selection": 18,
}

# ==========================================================
# MBA ADMISSION
# ==========================================================

MBA_KEYWORDS = {
    "mba": 8,
    "business school": 15,
    "b-school": 15,
    "application": 12,
    "applications": 12,
    "essays": 15,
    "sop": 15,
    "statement of purpose": 15,
    "lor": 12,
    "recommendation letter": 15,
    "interview": 15,
    "admit": 12,
    "admission": 15,
    "round 1": 18,
    "round 2": 18,
    "r1": 18,
    "r2": 18,
    "deferred mba": 20,
}

# ==========================================================
# BUSINESS SCHOOLS
# ==========================================================

SCHOOL_KEYWORDS = {
    "harvard": 20,
    "stanford": 20,
    "wharton": 20,
    "mit": 18,
    "sloan": 18,
    "insead": 20,
    "hec": 18,
    "hec paris": 20,
    "lbs": 18,
    "london business school": 20,
    "isb": 20,
    "iim": 18,
    "booth": 18,
    "kellogg": 18,
    "yale": 18,
    "columbia": 18,
    "fuqua": 18,
    "tuck": 18,
    "ross": 18,
    "darden": 18,
    "cornell": 18,
    "cambridge": 18,
    "oxford": 18,
    "ie": 18,
    "iese": 18,
    "esade": 18,
}

# ==========================================================
# PROFILE COMPONENTS
# ==========================================================

PROFILE_COMPONENT_KEYWORDS = {
    "gpa": 18,
    "cgpa": 18,
    "work experience": 18,
    "experience": 8,
    "internship": 12,
    "promotion": 12,
    "leadership": 15,
    "volunteering": 12,
    "volunteer": 12,
    "ngo": 10,
    "startup": 12,
    "entrepreneur": 15,
    "software engineer": 15,
    "consultant": 15,
    "product manager": 15,
    "analyst": 12,
    "manager": 12,
    "extracurricular": 18,
    "certification": 12,
    "cfa": 15,
    "ca": 12,
}

# ==========================================================
# APPLICATION TIMELINE
# ==========================================================

APPLICATION_KEYWORDS = {
    "application deadline": 18,
    "deadline": 10,
    "fall intake": 15,
    "spring intake": 15,
    "2027 intake": 18,
    "2028 intake": 18,
    "apply this year": 18,
    "next year": 12,
    "before applications": 18,
    "before round 1": 20,
    "before round 2": 20,
}
# ==========================================================
# SUCCESS STORIES
# ==========================================================

SUCCESS_KEYWORDS = {
    "official score": 30,
    "finally": 15,
    "finally done": 20,
    "finally took": 18,
    "i scored": 25,
    "scored": 18,
    "got": 8,
    "achieved": 18,
    "happy to share": 18,
    "excited": 12,
    "dream score": 20,
    "target achieved": 22,
    "mission accomplished": 25,
    "705": 18,
    "715": 18,
    "725": 18,
    "735": 18,
    "focus edition": 6,
    "thank you": 10,
}

# ==========================================================
# EXPERIENCE SHARING
# ==========================================================

EXPERIENCE_KEYWORDS = {
    "my experience": 25,
    "my journey": 25,
    "lessons learned": 25,
    "what worked": 22,
    "what didn't work": 22,
    "mistakes i made": 25,
    "things i wish i knew": 30,
    "tips": 15,
    "advice": 15,
    "recommendation": 12,
    "recommend": 10,
    "strategy": 15,
    "approach": 15,
    "reflection": 15,
    "looking back": 20,
    "after taking": 18,
    "retrospective": 20,
    "guide": 15,
    "my review": 18,
}

# ==========================================================
# FAILURE / RETAKE
# ==========================================================

FAILURE_KEYWORDS = {
    "failed": 20,
    "didn't get": 15,
    "did not get": 15,
    "missed my target": 20,
    "retake": 18,
    "retaking": 18,
    "second attempt": 15,
    "third attempt": 15,
    "another attempt": 15,
    "disappointed": 15,
    "frustrated": 15,
    "burnt out": 15,
    "burned out": 15,
    "demotivated": 15,
    "gave up": 20,
    "restart": 15,
}

# ==========================================================
# WORKING PROFESSIONAL
# ==========================================================

WORKING_PROFESSIONAL_KEYWORDS = {
    "working professional": 25,
    "full time job": 25,
    "full-time job": 25,
    "9 to 5": 22,
    "9-5": 22,
    "office": 8,
    "corporate": 12,
    "software engineer": 18,
    "developer": 15,
    "consultant": 15,
    "analyst": 15,
    "manager": 12,
    "product manager": 18,
    "while working": 25,
    "busy schedule": 18,
    "after work": 18,
    "weekends": 15,
}

# ==========================================================
# MOTIVATION
# ==========================================================

MOTIVATION_KEYWORDS = {
    "motivation": 15,
    "motivated": 15,
    "discipline": 18,
    "consistent": 15,
    "consistency": 18,
    "focus": 10,
    "burnout": 15,
    "confidence": 12,
    "mindset": 18,
    "stress": 12,
    "anxiety": 15,
    "pressure": 12,
    "fear": 12,
    "self doubt": 18,
    "self-doubt": 18,
}

# ==========================================================
# HIGH VALUE LEAD INDICATORS
# ==========================================================

LEAD_KEYWORDS = {
    "where do i start": 30,
    "study plan": 30,
    "need help": 25,
    "guidance": 22,
    "mentor": 20,
    "working professional": 25,
    "9 to 5": 25,
    "full time job": 25,
    "mock analysis": 30,
    "review my mock": 30,
    "analyze my mock": 30,
    "esr": 30,
    "enhanced score report": 30,
    "improve score": 25,
    "stuck": 18,
    "plateau": 20,
    "confused": 20,
    "lost": 20,
    "should i": 18,
    "what should i do": 25,
    "can someone help": 25,
    "study strategy": 20,
    "roadmap": 20,
}

# ==========================================================
# LOW VALUE INDICATORS
# ==========================================================

LOW_VALUE_KEYWORDS = {
    "meme": -20,
    "funny": -15,
    "joke": -20,
    "rant": -10,
    "news": -5,
    "announcement": -5,
    "poll": -10,
    "survey": -10,
    "celebration": -8,
}

# ==========================================================
# POSTS THAT SHOULD BE SUMMARIZED
# ==========================================================

SUMMARY_KEYWORDS = {
    "my experience": 30,
    "my journey": 30,
    "tips": 20,
    "lessons learned": 30,
    "things i wish i knew": 35,
    "what worked": 30,
    "what didn't work": 30,
    "mistakes i made": 30,
    "guide": 20,
    "strategy": 20,
    "advice": 20,
    "recommendation": 18,
    "how i scored": 30,
    "how i improved": 30,
}

# ==========================================================
# POSTS TO IGNORE
# ==========================================================

IGNORE_KEYWORDS = {
    "meme",
    "shitpost",
    "off topic",
    "off-topic",
    "spam",
    "promotion",
    "advertisement",
    "selling account",
    "buy account",
    "discord server",
}