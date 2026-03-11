from fastapi import APIRouter

from app.orchestration.agent_service import AgentExecutionService
from app.schemas.common import AgentResponse
from app.schemas.teacher import TeacherBlueprintRequest, TeacherQuestionPaperRequest

router = APIRouter(prefix="/teacher", tags=["teacher"])
service = AgentExecutionService()


@router.post("/question-paper", response_model=AgentResponse)
def generate_question_paper(request: TeacherQuestionPaperRequest):
    payload = request.model_dump()
    paper = service.generate_question_paper(payload)
    translated = paper if request.language == "English" else service.translate(paper, request.language)
    return AgentResponse(agent="QuestionPaperGeneratorAgent", output={"content": translated})


@router.post("/blueprint", response_model=AgentResponse)
def generate_blueprint(request: TeacherBlueprintRequest):
    content = service.analyze_blueprint(request.model_dump())
    return AgentResponse(agent="BlueprintAnalyzerAgent", output={"content": content})
