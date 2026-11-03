from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class PresentationRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    topic: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Topic of the academic presentation"
    )

    target_audience: str = Field(
        default="General academic audience",
        min_length=3,
        max_length=100
    )

    slide_count: int = Field(
        default=10,
        ge=3,
        le=25,
        description="Desired number of slides"
    )

    tone: Literal[
        "formal",
        "technical",
        "simple",
        "research-oriented"
    ] = "formal"

    content_preferences: list[str] = Field(
        default_factory=list,
        description="Specific content preferences"
    )

    theme: str = Field(
        default="professional",
        min_length=2,
        max_length=50
    )

    additional_instructions: str | None = Field(
        default=None,
        max_length=1000
    )
