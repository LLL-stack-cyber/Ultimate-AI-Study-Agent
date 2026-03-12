from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class StudyPlannerRequest(BaseModel):
    user_id: str
    exam_date: date
    class_name: str
    board: str
    subjects: list[str]


class BlueprintAnalyzeRequest(BaseModel):
    user_id: str
    subject: str
    board: str
    previous_papers_text: list[str] = Field(default_factory=list)


class QuestionPaperGenerateRequest(BaseModel):
    user_id: str
    board: str
    class_name: str
    subject: str
    syllabus_text: str
    blueprint_summary: str
    difficulty: Literal["easy", "medium", "hard"]
    language: str = "English"


class ProbabilityPredictRequest(BaseModel):
    user_id: str
    subject: str
    board: str
    textbook_text: str
    previous_papers_text: list[str]
    blueprint_summary: str


class TrainingRequest(BaseModel):
    user_id: str
    stream: Literal["jee", "neet"]
    subject: str
    topic: str
    difficulty: Literal["mains", "advanced", "foundation"] = "mains"


class DoubtSolverRequest(BaseModel):
    user_id: str
    doubt_text: str | None = None
    image_path: str | None = None


class NotesGenerateRequest(BaseModel):
    user_id: str
    board: str
    class_name: str
    subject: str
    chapter: str
    source_text: str


class FullWorkflowRequest(BaseModel):
    user_id: str
    exam_date: date
    class_name: str
    board: str
    subject: str
    textbook_text: str
    previous_papers_text: list[str]
    syllabus_text: str
    chapter: str
    preferred_language: str = "English"
