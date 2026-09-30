from gemini_client import generate

def explain_topic(topic: str) -> str:
    prompt = f"""
Explain the following topic for a beginner.
Use simple language, short sections, examples where useful,
and avoid unnecessary technical complexity.

Topic:
{topic}
"""
    return generate(prompt)
