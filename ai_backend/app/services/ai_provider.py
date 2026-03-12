from crewai import LLM

from app.core.config import get_settings


class LLMFactory:
    @staticmethod
    def build_default() -> LLM:
        settings = get_settings()
        return LLM(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            temperature=0.2,
        )
