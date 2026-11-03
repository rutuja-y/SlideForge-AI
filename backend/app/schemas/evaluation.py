from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class SlideEvaluation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    slide_number: int = Field(..., ge=1)

    relevance_score: float = Field(..., ge=0, le=10)

    factual_accuracy_score: float = Field(..., ge=0, le=10)

    clarity_score: float = Field(..., ge=0, le=10)

    visual_quality_score: float = Field(..., ge=0, le=10)

    feedback: list[str] = Field(
        default_factory=list,
        max_length=10
    )

    improvement_suggestions: list[str] = Field(
        default_factory=list,
        max_length=10
    )

    passed: bool


class PresentationEvaluation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    overall_score: float = Field(..., ge=0, le=10)

    structure_score: float = Field(..., ge=0, le=10)

    research_quality_score: float = Field(..., ge=0, le=10)

    consistency_score: float = Field(..., ge=0, le=10)

    slide_evaluations: list[SlideEvaluation] = Field(
        ...,
        min_length=1
    )

    overall_feedback: list[str] = Field(
        default_factory=list,
        max_length=15
    )

    revision_required: bool

    revision_priority: Literal[
        "low",
        "medium",
        "high"
    ] = "medium"
