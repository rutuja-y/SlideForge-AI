from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str = "SlideForge AI"
    APP_ENV: str = "development"
    DEBUG: bool = True

    GROQ_API_KEY: str = ""
    TAVILY_API_KEY: str = ""

    DATABASE_URL: str = ""
    REDIS_URL: str = ""

    # LLM Provider Configuration

    LLM_PROVIDER: str = "groq"
    LLM_MODEL: str = "openai/gpt-oss-120b"
    LLM_TEMPERATURE: float = 0.3
    LLM_MAX_TOKENS: int = 4096
    LLM_TIMEOUT: int = 60
    LLM_MAX_RETRIES: int = 2


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

settings = Settings()
