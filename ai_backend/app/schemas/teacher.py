from typing import Literal

from pydantic import BaseModel


class TeacherQuestionPaperRequest(BaseModel):
    teacher_id: str
    board: str
    class_name: str
    subject: str
    syllabus_text: str
    blueprint_summary: str
    difficulty: Literal["easy", "medium", "hard"]
    language: str = "English"


class TeacherBlueprintRequest(BaseModel):
    teacher_id: str
    board: str
    class_name: str
    subject: str
    previous_papers_text: list[str]
