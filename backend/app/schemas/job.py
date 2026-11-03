from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class PresentationJob(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_id: str

    status: Literal[
        "pending",
        "running",
        "completed",
        "failed",
        "cancelled"
    ] = "pending"

    current_stage: str | None = None

    progress: int = Field(
        default=0,
        ge=0,
        le=100
    )

    error_message: str | None = None

    created_at: datetime

    updated_at: datetime


class PresentationExport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    export_id: str

    job_id: str

    format: Literal["pptx", "pdf"]

    status: Literal[
        "pending",
        "processing",
        "completed",
        "failed"
    ] = "pending"

    file_name: str | None = None

    file_path: str | None = None

    error_message: str | None = None

    created_at: datetime
