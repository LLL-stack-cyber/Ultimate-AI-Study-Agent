# Ultimate AI Study Agent - Production Backend (FastAPI + CrewAI)

## Architecture Overview

This backend is designed as a **multi-agent AI platform** with two logical domains:

- **Student Portal**: study planning, blueprint analysis, AI paper generation, probability prediction, JEE/NEET training, Jarvis doubt solving, and notes.
- **Teacher Portal**: blueprint analysis and question paper generation.

### Core Components

1. **API Layer (FastAPI)**
   - `app/api/student.py`
   - `app/api/teacher.py`

2. **Agent Layer (CrewAI)**
   - `app/agents/definitions.py` defines 9 production agents:
     - StudyPlannerAgent
     - BlueprintAnalyzerAgent
     - QuestionPaperGeneratorAgent
     - ProbabilityPredictorAgent
     - JEETestAgent
     - NEETTestAgent
     - NotesGeneratorAgent
     - JARVISDoubtAgent
     - LanguageAgent

3. **Orchestration Layer**
   - `app/orchestration/agent_service.py` for single-agent tasks
   - `app/orchestration/crew_orchestrator.py` for full pipeline execution

4. **Data Layer (Supabase/Postgres)**
   - SQL bootstrap: `sql/001_init_schema.sql`
   - Repository pattern: `app/repositories/study_repository.py`

5. **Document Intelligence Layer**
   - PDF extraction: `pypdf`
   - OCR extraction: `pytesseract`
   - Service: `app/services/file_processing.py`

6. **LLM Provider Abstraction**
   - `app/services/ai_provider.py`
   - swap model/provider centrally without changing agent or API code.

## Endpoints

- `POST /api/v1/student/study-plan`
- `POST /api/v1/student/blueprint`
- `POST /api/v1/student/question-paper`
- `POST /api/v1/student/high-probability`
- `POST /api/v1/student/training`
- `POST /api/v1/student/doubt-solver`
- `POST /api/v1/student/notes`
- `POST /api/v1/student/workflow/full`

- `POST /api/v1/teacher/question-paper`
- `POST /api/v1/teacher/blueprint`

## Example Full Workflow

1. Upload textbook and previous papers.
2. `BlueprintAnalyzerAgent` extracts mark distribution and trend map.
3. `ProbabilityPredictorAgent` predicts high-probability questions.
4. `QuestionPaperGeneratorAgent` creates paper using board + syllabus + blueprint.
5. `StudyPlannerAgent` generates adaptive day-wise plan till exam date.
6. `NotesGeneratorAgent` creates chapter-wise notes.
7. `LanguageAgent` localizes output (English/Hindi/Kannada/French/Sanskrit).
8. `JARVISDoubtAgent` solves text/image doubts with OCR context.

## Production Readiness Notes

- Environment-based settings with strict config object (`pydantic-settings`).
- Pluggable model strategy via `LLMFactory`.
- Stateless API workers suitable for horizontal scaling on Render/Vercel.
- Supabase-managed PostgreSQL for persistence and indexing.
- Repository abstraction to support future CQRS/event-driven refactors.
- Can be extended with queue workers (Celery/RQ) for heavy OCR/PDF tasks.

## Run locally

```bash
cd ai_backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Deployment

- **Render**: deploy as Python web service with `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **Vercel**: deploy FastAPI with serverless adapter or containerized runtime.
