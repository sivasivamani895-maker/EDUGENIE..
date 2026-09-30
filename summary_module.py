from gemini_client import generate

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text.
Keep the important information, remove repetition,
and make the result concise and easy to revise.

Text:
{text}
"""
    return generate(prompt)
