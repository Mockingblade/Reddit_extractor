from rules.entity_extractor import extract_entities

title = "Need GMAT Help"

body = """
Working professional.

Official Mock 2

Current score 615

Target 705

Q81 V82 DI79

4 months left.

Thinking of buying Target Test Prep.

Planning to apply to ISB and INSEAD.

Should I buy TTP?
"""

entities = extract_entities(title, body)

print(entities)