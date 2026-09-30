import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import ask_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

load_dotenv()

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/qa")
async def qa(question: str = Form(...)):
    return {"result": ask_question(question)}

@app.post("/explain")
async def explain(topic: str = Form(...)):
    return {"result": explain_topic(topic)}

@app.post("/quiz")
async def quiz(text: str = Form(...)):
    return {"result": generate_quiz(text)}

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    return {"result": summarize_text(text)}

@app.post("/learn/recommendations")
async def recommendations(topic: str = Form(...)):
    return {"result": get_learning_recommendations(topic)}
