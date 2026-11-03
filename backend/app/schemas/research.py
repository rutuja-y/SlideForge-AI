from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl

class ResearchSource(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(..., min_length=2, max_length=300)

    url: HttpUrl

    source_type: Literal[
        "research_paper",
        "academic_article",
        "website",
        "report",
        "other"
    ] = "website"

    published_date: str | None = None

    retrieved_at: str | None = None


class ResearchEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid")

    claim: str = Field(..., min_length=5, max_length=1000)

    supporting_text: str = Field(
        ...,
        min_length=5,
        max_length=3000
    )

    source: ResearchSource

    relevance_score: float | None = Field(
        default=None,
        ge=0,
        le=1
    )
