
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class VisualSpecification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    slide_number: int = Field(..., ge=1)

    layout_type: Literal[
        "title",
        "title_content",
        "two_column",
        "comparison",
        "timeline",
        "process_flow",
        "architecture",
        "image_text",
        "chart",
        "table",
        "key_takeaways",
        "conclusion"
    ] = "title_content"

    visual_description: str | None = Field(
        default=None,
        max_length=500
    )

    visual_elements: list[str] = Field(
        default_factory=list,
        max_length=10
    )

    color_scheme: Literal[
        "professional_blue",
        "minimal_light",
        "dark_academic",
        "earthy",
        "monochrome"
    ] = "professional_blue"

    image_required: bool = False

    chart_required: bool = False

    diagram_required: bool = False

    emphasis: Literal[
        "low",
        "medium",
        "high"
    ] = "medium"
