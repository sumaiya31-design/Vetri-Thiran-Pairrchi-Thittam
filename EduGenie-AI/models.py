from typing import Literal

from pydantic import BaseModel, Field


class QARequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=30000)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"


class ExplainRequest(BaseModel):
    concept: str = Field(
        ...,
        min_length=2,
        max_length=30000
    )

class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=10000)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"
    num_questions: int = Field(default=3, ge=1, le=10)


class SummaryRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=30000)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"


class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=10000)
    level: Literal["beginner", "intermediate", "advanced"] = "beginner"
    weeks: int = Field(default=4, ge=1, le=12)
    goal: str = Field(..., min_length=2, max_length=500)