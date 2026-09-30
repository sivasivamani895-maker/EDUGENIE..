import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
_client = genai.Client(api_key=API_KEY) if API_KEY else None

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def generate(prompt: str) -> str:
    if not _client:
        return "Error: GEMINI_API_KEY is not configured. Add it to the .env file."
    try:
        response = _client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text or "No response generated."
    except Exception as e:
        return f"Gemini API error: {e}"
