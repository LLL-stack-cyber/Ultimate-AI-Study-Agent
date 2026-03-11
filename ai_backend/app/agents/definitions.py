from crewai import Agent

from app.services.ai_provider import LLMFactory


class AgentFactory:
    def __init__(self) -> None:
        self.llm = LLMFactory.build_default()

    def study_planner(self) -> Agent:
        return Agent(
            role="StudyPlannerAgent",
            goal="Create adaptive daily schedules that maximize exam readiness while preventing burnout.",
            backstory="Senior academic planner specialized in Indian board exams and competitive exams.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def blueprint_analyzer(self) -> Agent:
        return Agent(
            role="BlueprintAnalyzerAgent",
            goal="Extract topic-weight distribution and question patterns from historical papers.",
            backstory="Assessment design analyst who maps marks distribution by chapter and cognitive level.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def question_generator(self) -> Agent:
        return Agent(
            role="QuestionPaperGeneratorAgent",
            goal="Generate board-aligned and difficulty-controlled full question papers.",
            backstory="Expert paper setter for school boards and standardized exams.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def probability_predictor(self) -> Agent:
        return Agent(
            role="ProbabilityPredictorAgent",
            goal="Predict high-probability exam questions using patterns, syllabus, and textbook signal.",
            backstory="Exam trend forecaster using pattern intelligence over 5-year question archives.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def jee_test_agent(self) -> Agent:
        return Agent(
            role="JEETestAgent",
            goal="Generate unlimited JEE mains-style practice problems with solutions.",
            backstory="JEE mentor with PCM mastery and adaptive question sequencing.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def neet_test_agent(self) -> Agent:
        return Agent(
            role="NEETTestAgent",
            goal="Generate NEET-aligned PCB practice questions with explanations.",
            backstory="Medical entrance trainer skilled in conceptual and application-based tests.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def notes_generator(self) -> Agent:
        return Agent(
            role="NotesGeneratorAgent",
            goal="Create concise, high-retention chapter notes with formulas, diagrams, and revision cues.",
            backstory="Instructional designer focused on active recall and spaced repetition.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def jarvis_doubt_solver(self) -> Agent:
        return Agent(
            role="JARVISDoubtAgent",
            goal="Resolve doubts from text or OCR input using stepwise explanations.",
            backstory="AI tutor built for multimodal doubt resolution and exam-oriented pedagogy.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )

    def language_agent(self) -> Agent:
        return Agent(
            role="LanguageAgent",
            goal="Translate educational content accurately into target exam languages while preserving meaning.",
            backstory="Academic translator supporting English, Hindi, Kannada, French, and Sanskrit.",
            llm=self.llm,
            allow_delegation=False,
            verbose=False,
        )
