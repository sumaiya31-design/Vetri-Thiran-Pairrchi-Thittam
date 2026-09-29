from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from models import QARequest, ExplainRequest, QuizRequest, SummaryRequest, LearningPathRequest
from explanation_module import explain_concept
from gemini_client import generate_text, GeminiGenerationError
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path
app = FastAPI(title="EduGenie")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request}
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/qa")
def ask_question(request: QARequest):
    prompt = f"""
Answer the following student's question clearly and accurately.

Student question:
{request.question}

Explain the answer in a student-friendly way.
If useful, include a short example.
"""

    try:
        answer = generate_text(prompt)

        return {
            "question": request.question,
            "answer": answer
        }

    except GeminiGenerationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        )
@app.post("/explain")
def explain(request: ExplainRequest):
    try:
        explanation = explain_concept(request.concept)

        return {
            "concept": request.concept,
            "explanation": explanation
        }

    except GeminiGenerationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        )
@app.post("/quiz")
def create_quiz(request: QuizRequest):
    try:
        quiz = generate_quiz(
            topic=request.topic,
            level=request.level,
            num_questions=request.num_questions
        )

        return {
            "topic": request.topic,
            "level": request.level,
            "quiz": quiz
        }

    except GeminiGenerationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        )
@app.post("/summarize")
def summarize(request: SummaryRequest):
    try:
        summary = summarize_text(
            text=request.text,
            level=request.level
        )

        return {
            "summary": summary
        }

    except GeminiGenerationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        ) 
@app.post("/learn/recommendations")
def learning_recommendations(request: LearningPathRequest):
    try:
        recommendations = recommend_learning_path(
            topic=request.topic,
            level=request.level,
            goal=request.goal
        )

        return {
            "topic": request.topic,
            "level": request.level,
            "goal": request.goal,
            "recommendations": recommendations
        }

    except GeminiGenerationError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        )