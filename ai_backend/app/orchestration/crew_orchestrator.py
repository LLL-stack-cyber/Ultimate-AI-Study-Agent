from uuid import uuid4

from crewai import Crew, Process, Task

from app.agents.definitions import AgentFactory
from app.schemas.common import AgentResponse, WorkflowResponse
from app.schemas.student import FullWorkflowRequest


class StudyCrewOrchestrator:
    def __init__(self) -> None:
        self.factory = AgentFactory()

    def run_full_workflow(self, request: FullWorkflowRequest) -> WorkflowResponse:
        blueprint_agent = self.factory.blueprint_analyzer()
        predictor_agent = self.factory.probability_predictor()
        paper_agent = self.factory.question_generator()
        planner_agent = self.factory.study_planner()
        notes_agent = self.factory.notes_generator()
        language_agent = self.factory.language_agent()

        blueprint_task = Task(
            description=(
                "Analyze previous papers and produce chapter-wise marks distribution, "
                "question types, and blueprint summary."
                f" Subject: {request.subject}, Board: {request.board}, Papers: {request.previous_papers_text}"
            ),
            expected_output="Structured JSON with chapter, marks-weight, and trend notes.",
            agent=blueprint_agent,
        )

        prediction_task = Task(
            description=(
                "Predict high-probability exam questions using textbook + 5-year papers + blueprint summary. "
                f"Textbook: {request.textbook_text}"
            ),
            expected_output="Top probable questions with confidence score and rationale.",
            agent=predictor_agent,
            context=[blueprint_task],
        )

        paper_task = Task(
            description=(
                "Generate full question paper aligned to blueprint and predictions. "
                f"Language: {request.preferred_language}, Syllabus: {request.syllabus_text}"
            ),
            expected_output="Complete question paper with sectioning, marks, and answer key.",
            agent=paper_agent,
            context=[blueprint_task, prediction_task],
        )

        planner_task = Task(
            description=(
                "Create daily adaptive study plan until exam date using generated question paper difficulty and predicted topics. "
                f"Exam date: {request.exam_date}, Class: {request.class_name}"
            ),
            expected_output="Daily timetable with revision cycles and buffer slots.",
            agent=planner_agent,
            context=[prediction_task, paper_task],
        )

        notes_task = Task(
            description=(
                f"Generate chapter notes for {request.chapter} with summaries, formulas, examples, and flashcards."
            ),
            expected_output="Structured notes markdown with revision checklist.",
            agent=notes_agent,
            context=[prediction_task],
        )

        translation_task = Task(
            description=(
                f"Translate generated question paper and notes to {request.preferred_language} while preserving technical terms."
            ),
            expected_output="Localized outputs with glossary mapping.",
            agent=language_agent,
            context=[paper_task, notes_task],
        )

        crew = Crew(
            agents=[
                blueprint_agent,
                predictor_agent,
                paper_agent,
                planner_agent,
                notes_agent,
                language_agent,
            ],
            tasks=[
                blueprint_task,
                prediction_task,
                paper_task,
                planner_task,
                notes_task,
                translation_task,
            ],
            process=Process.sequential,
            verbose=False,
        )

        raw_output = crew.kickoff()

        results = [
            AgentResponse(agent="BlueprintAnalyzerAgent", output={"content": str(blueprint_task.output)}),
            AgentResponse(agent="ProbabilityPredictorAgent", output={"content": str(prediction_task.output)}),
            AgentResponse(agent="QuestionPaperGeneratorAgent", output={"content": str(paper_task.output)}),
            AgentResponse(agent="StudyPlannerAgent", output={"content": str(planner_task.output)}),
            AgentResponse(agent="NotesGeneratorAgent", output={"content": str(notes_task.output)}),
            AgentResponse(agent="LanguageAgent", output={"content": str(translation_task.output)}),
            AgentResponse(agent="CrewFinalOutput", output={"content": str(raw_output)}),
        ]

        return WorkflowResponse(workflow_id=str(uuid4()), results=results)
