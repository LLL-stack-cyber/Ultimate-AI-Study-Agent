from typing import Any

from supabase import Client


class StudyRepository:
    def __init__(self, client: Client):
        self.client = client

    def save_study_plan(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.client.table("study_plans").insert(payload).execute().data[0]

    def save_question_paper(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.client.table("question_papers").insert(payload).execute().data[0]

    def save_notes(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.client.table("notes").insert(payload).execute().data[0]

    def save_doubt(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.client.table("doubts").insert(payload).execute().data[0]

    def save_training_questions(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.client.table("training_questions").insert(payload).execute().data[0]
