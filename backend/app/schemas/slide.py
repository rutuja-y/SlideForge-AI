from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator
)

from app.schemas.research import ResearchEvidence


class SlideContentBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")

    block_type: Literal[
        "paragraph",
        "bullet_list",
        "numbered_list",
        "quote",
        "key_takeaway"
    ]

    text: str | None = Field(
        default=None,
        max_length=2000
    )

    items: list[str] | None = Field(
        default=None,
        min_length=1,
        max_length=10
    )

    evidence: list[ResearchEvidence] = Field(
        default_factory=list
    )

    @model_validator(mode="after")
    def validate_block_content(self):
        list_types = {"bullet_list", "numbered_list"}

        if self.block_type in list_types:
            if not self.items:
                raise ValueError(
                    "List blocks must contain at least one item."
                )
            if self.text is not None:
                raise ValueError(
                    "List blocks should use items, not text."
                )
        else:
            if not self.text or not self.text.strip():
                raise ValueError(
                    "This block type requires non-empty text."
                )
            if self.items is not None:
                raise ValueError(
                    "This block type should use text, not items."
                )

        return self


class SlideContent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    slide_number: int = Field(..., ge=1)

    section_title: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    title: str = Field(
        ...,
        min_length=2,
        max_length=150
    )

    subtitle: str | None = Field(
        default=None,
        max_length=200
    )

    content_blocks: list[SlideContentBlock] = Field(
        ...,
        min_length=1,
        max_length=6
    )

    speaker_notes: str | None = Field(
        default=None,
        max_length=3000
    )
