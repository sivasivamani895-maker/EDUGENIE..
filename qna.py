from gemini_client import generate

def ask_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.
Answer the student's question accurately and concisely.
Use simple language suitable for a learner.

Question:
{question}
"""
    return generate(prompt)
