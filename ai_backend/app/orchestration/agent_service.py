from crewai import Crew, Process, Task

from app.agents.definitions import AgentFactory


class AgentExecutionService:
    def __init__(self) -> None:
        self.factory = AgentFactory()

    @staticmethod
    def _run(agent_task: Task):
        crew = Crew(agents=[agent_task.agent], tasks=[agent_task], process=Process.sequential, verbose=False)
        crew.kickoff()
        return str(agent_task.output)

    def generate_study_plan(self, payload: dict) -> str:
        task = Task(
            description=(
                f"Create flexible daily timetable until exam date {payload['exam_date']} for class {payload['class_name']} "
                f"under {payload['board']} board across subjects {payload['subjects']}."
            ),
            expected_output="JSON schedule with day-wise tasks, revision blocks, and mock tests.",
            agent=self.factory.study_planner(),
        )
        return self._run(task)

    def analyze_blueprint(self, payload: dict) -> str:
        task = Task(
            description=(
                f"Analyze papers to derive topic-wise blueprint for {payload['subject']} in {payload['board']} board. "
                f"Papers: {payload['previous_papers_text']}"
            ),
            expected_output="Topic-wise marks distribution and blueprint insights.",
            agent=self.factory.blueprint_analyzer(),
        )
        return self._run(task)

    def generate_question_paper(self, payload: dict) -> str:
        task = Task(
            description=(
                f"Generate question paper for {payload['class_name']} {payload['subject']} with difficulty {payload['difficulty']}. "
                f"Syllabus: {payload['syllabus_text']}. Blueprint: {payload['blueprint_summary']}"
            ),
            expected_output="Full paper with sections, marks allocation, and answer key.",
            agent=self.factory.question_generator(),
        )
        return self._run(task)

    def predict_probability_questions(self, payload: dict) -> str:
        task = Task(
            description=(
                f"Predict high-probability questions for {payload['subject']} using papers, blueprint, and textbook. "
                f"Blueprint: {payload['blueprint_summary']}"
            ),
            expected_output="Prioritized question list with confidence scores.",
            agent=self.factory.probability_predictor(),
        )
        return self._run(task)

    def generate_training_questions(self, payload: dict) -> str:
        stream = payload["stream"]
        agent = self.factory.jee_test_agent() if stream == "jee" else self.factory.neet_test_agent()
        task = Task(
            description=(
                f"Generate {stream.upper()} practice questions for subject {payload['subject']} and topic {payload['topic']} "
                f"at {payload['difficulty']} level with answer explanations."
            ),
            expected_output="Batch of MCQs and numericals with final answers and explanations.",
            agent=agent,
        )
        return self._run(task)

    def solve_doubt(self, payload: dict) -> str:
        task = Task(
            description=(
                "Solve student doubt using provided text and OCR context. "
                f"Doubt: {payload.get('doubt_text')}, OCR text: {payload.get('ocr_text')}"
            ),
            expected_output="Stepwise solution and conceptual clarification.",
            agent=self.factory.jarvis_doubt_solver(),
        )
        return self._run(task)

    def generate_notes(self, payload: dict) -> str:
        task = Task(
            description=(
                f"Generate structured notes for chapter {payload['chapter']} for {payload['class_name']} {payload['subject']} "
                f"based on source text: {payload['source_text']}"
            ),
            expected_output="Hierarchical notes with summary, key terms, solved examples, and revision checklist.",
            agent=self.factory.notes_generator(),
        )
        return self._run(task)

    def translate(self, content: str, language: str) -> str:
        task = Task(
            description=f"Translate the following educational content to {language}: {content}",
            expected_output="Accurate translated content preserving equations and scientific terms.",
            agent=self.factory.language_agent(),
        )
        return self._run(task)
