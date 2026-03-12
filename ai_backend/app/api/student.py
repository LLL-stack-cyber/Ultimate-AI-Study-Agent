from fastapi import APIRouter

from app.db.supabase_client import get_supabase_client
from app.orchestration.agent_service import AgentExecutionService
from app.orchestration.crew_orchestrator import StudyCrewOrchestrator
from app.repositories.study_repository import StudyRepository
from app.schemas.common import AgentResponse, WorkflowResponse
from app.schemas.student import (
    BlueprintAnalyzeRequest,
    DoubtSolverRequest,
    FullWorkflowRequest,
    NotesGenerateRequest,
    ProbabilityPredictRequest,
    QuestionPaperGenerateRequest,
    StudyPlannerRequest,
    TrainingRequest,
)
from app.services.file_processing import FileProcessingService

router = APIRouter(prefix="/student", tags=["student"])
service = AgentExecutionService()
orchestrator = StudyCrewOrchestrator()


@router.post("/study-plan", response_model=AgentResponse)
def study_plan(request: StudyPlannerRequest):
    content = service.generate_study_plan(request.model_dump())
    repo = StudyRepository(get_supabase_client())
    repo.save_study_plan({"user_id": request.user_id, "plan": content, "metadata": request.model_dump()})
    return AgentResponse(agent="StudyPlannerAgent", output={"content": content})


@router.post("/blueprint", response_model=AgentResponse)
def blueprint(request: BlueprintAnalyzeRequest):
    content = service.analyze_blueprint(request.model_dump())
    return AgentResponse(agent="BlueprintAnalyzerAgent", output={"content": content})


@router.post("/question-paper", response_model=AgentResponse)
def question_paper(request: QuestionPaperGenerateRequest):
    payload = request.model_dump()
    paper = service.generate_question_paper(payload)
    translated = paper if request.language == "English" else service.translate(paper, request.language)
    repo = StudyRepository(get_supabase_client())
    repo.save_question_paper({"user_id": request.user_id, "paper": translated, "metadata": payload})
    return AgentResponse(agent="QuestionPaperGeneratorAgent", output={"content": translated})


@router.post("/high-probability", response_model=AgentResponse)
def high_probability(request: ProbabilityPredictRequest):
    content = service.predict_probability_questions(request.model_dump())
    return AgentResponse(agent="ProbabilityPredictorAgent", output={"content": content})


@router.post("/training", response_model=AgentResponse)
def training(request: TrainingRequest):
    content = service.generate_training_questions(request.model_dump())
    repo = StudyRepository(get_supabase_client())
    repo.save_training_questions({"user_id": request.user_id, "questions": content, "metadata": request.model_dump()})
    return AgentResponse(agent="JEETestAgent" if request.stream == "jee" else "NEETTestAgent", output={"content": content})


@router.post("/doubt-solver", response_model=AgentResponse)
def doubt_solver(request: DoubtSolverRequest):
    payload = request.model_dump()
    if request.image_path:
        payload["ocr_text"] = FileProcessingService.extract_image_text(request.image_path)
    content = service.solve_doubt(payload)
    repo = StudyRepository(get_supabase_client())
    repo.save_doubt({"user_id": request.user_id, "doubt": payload, "resolution": content})
    return AgentResponse(agent="JARVISDoubtAgent", output={"content": content})


@router.post("/notes", response_model=AgentResponse)
def notes(request: NotesGenerateRequest):
    content = service.generate_notes(request.model_dump())
    repo = StudyRepository(get_supabase_client())
    repo.save_notes({"user_id": request.user_id, "notes": content, "metadata": request.model_dump()})
    return AgentResponse(agent="NotesGeneratorAgent", output={"content": content})


@router.post("/workflow/full", response_model=WorkflowResponse)
def full_workflow(request: FullWorkflowRequest):
    return orchestrator.run_full_workflow(request)
