from pydantic import BaseModel, ConfigDict, Field, model_validator

class PresentationSection(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    order: int = Field(
        ...,
        ge=0
    )

    instructions: str | None = Field(
        default=None,
        max_length=500
    )


class PresentationStructure(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sections: list[PresentationSection] = Field(min_length=1)

    @model_validator(mode="after")
    def validate_sections(self):
        # Check for duplicate section titles (case-insensitive)
        titles = [
            section.title.strip().casefold()
            for section in self.sections
        ]

        if len(titles) != len(set(titles)):
            raise ValueError("Section titles must be unique.")

        # Check for duplicate ordering positions
        orders = [
            section.order
            for section in self.sections
        ]

        if len(orders) != len(set(orders)):
            raise ValueError("Section order values must be unique.")

        return self
