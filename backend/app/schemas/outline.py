from pydantic import BaseModel, ConfigDict, Field, model_validator

class OutlineSlide(BaseModel):
    model_config = ConfigDict(extra="forbid")

    slide_number: int = Field(..., ge=1)

    title: str = Field(..., min_length=2, max_length=150)

    key_points: list[str] = Field(
        ...,
        min_length=1,
        max_length=10
    )

    purpose: str = Field(
        ...,
        min_length=5,
        max_length=500
    )


class OutlineSection(BaseModel):
    model_config = ConfigDict(extra="forbid")

    section_title: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    order: int = Field(..., ge=0)

    slides: list[OutlineSlide] = Field(min_length=1)


class PresentationOutline(BaseModel):
    model_config = ConfigDict(extra="forbid")

    presentation_title: str = Field(
        ...,
        min_length=3,
        max_length=200
    )

    sections: list[OutlineSection] = Field(min_length=1)

    total_slides: int = Field(..., ge=1, le=25)

    @model_validator(mode="after")
    def validate_total_slides(self):
        actual_count = sum(
            len(section.slides)
            for section in self.sections
        )

        if actual_count != self.total_slides:
            raise ValueError(
                f"total_slides is {self.total_slides}, "
                f"but the outline contains {actual_count} slides."
            )

        slide_numbers = [
            slide.slide_number
            for section in self.sections
            for slide in section.slides
        ]

        if len(slide_numbers) != len(set(slide_numbers)):
            raise ValueError("Slide numbers must be unique.")

        return self
