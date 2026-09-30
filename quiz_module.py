import json
import re
from gemini_client import generate

def clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()

def generate_quiz(passage: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.
Each question must have exactly 4 options and one correct answer.

Return ONLY valid JSON in this format:
[
  {{
    "question": "Question",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{passage}
"""
    raw = generate(prompt)
    try:
        return json.loads(clean_json_block(raw))
    except Exception:
        return {"error": "Quiz response could not be parsed.", "raw_response": raw}
