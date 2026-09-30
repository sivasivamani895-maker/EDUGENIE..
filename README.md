# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant with:
- Question & Answer
- Topic explanation
- MCQ quiz generation
- Text summarization
- Personalized learning paths

## Project structure

EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── templates/
│   └── index.html
└── static/
    └── style.css

## Setup

1. Install Python 3.10+.
2. Open terminal inside this folder.
3. Create a virtual environment:

   python -m venv venv

4. Activate it.

Windows:
   venv\Scripts\activate

macOS/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

6. Create a `.env` file by copying `.env.example`.
7. Put your Gemini API key in `.env`:

   GEMINI_API_KEY=your_key_here

8. Start the server:

   uvicorn main:app --reload

9. Open:

   http://127.0.0.1:8000

## API endpoints

POST /qa
POST /explain
POST /quiz
POST /summarize
POST /learn/recommendations
