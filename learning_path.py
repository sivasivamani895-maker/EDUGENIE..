from gemini_client import generate

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic below.
Organize it from beginner to intermediate to advanced.
For each stage include important concepts, a suggested timeline,
and useful resource types such as videos, articles, or books.

Topic:
{topic}
"""
    return generate(prompt)
