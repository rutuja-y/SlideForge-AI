from langchain_groq import ChatGroq

from app.core.config import settings

def create_llm():
    provider = settings.LLM_PROVIDER.lower()

    if provider == "groq":
        if not settings.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY is missing from environment configuration."
            )

        return ChatGroq(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_tokens=settings.LLM_MAX_TOKENS,
            timeout=settings.LLM_TIMEOUT,
            max_retries=settings.LLM_MAX_RETRIES,
            api_key=settings.GROQ_API_KEY
        )

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )
