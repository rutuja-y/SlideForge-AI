import pytest
from pydantic import ValidationError

from app.schemas.presentation import PresentationRequest
from app.schemas.section import PresentationSection, PresentationStructure
from app.schemas.research import ResearchSource, ResearchEvidence
from app.schemas.outline import PresentationOutline
from app.schemas.slide import SlideContent
from app.schemas.visual import VisualSpecification
from app.schemas.evaluation import PresentationEvaluation
from app.schemas.job import PresentationJob, PresentationExport


# 1. Presentation request validation

def test_valid_presentation_request():
    request = PresentationRequest(
        topic="Artificial Intelligence",
        slide_count=10
    )
    assert request.slide_count == 10


def test_invalid_slide_count():
    with pytest.raises(ValidationError):
        PresentationRequest(
            topic="Artificial Intelligence",
            slide_count=30
        )


# 2. Section validation

def test_valid_section():
    section = PresentationSection(
        title="Introduction",
        order=0
    )
    assert section.title == "Introduction"


def test_duplicate_section_titles():
    with pytest.raises(ValidationError):
        PresentationStructure(
            sections=[
                {"title": "Introduction", "order": 0},
                {"title": " introduction ", "order": 1}
            ]
        )


def test_duplicate_section_order():
    with pytest.raises(ValidationError):
        PresentationStructure(
            sections=[
                {"title": "Introduction", "order": 0},
                {"title": "Conclusion", "order": 0}
            ]
        )


# 3. Research validation

def test_valid_research_source():
    source = ResearchSource(
        title="AI Research",
        url="https://example.com/research"
    )
    assert source.source_type == "website"


def test_invalid_relevance_score():
    with pytest.raises(ValidationError):
        ResearchEvidence(
            claim="AI improves productivity",
            supporting_text="Research supports this claim.",
            source={
                "title": "AI Research",
                "url": "https://example.com"
            },
            relevance_score=1.5
        )


# 4. Outline validation

def test_outline_slide_count_mismatch():
    with pytest.raises(ValidationError):
        PresentationOutline(
            presentation_title="AI Presentation",
            total_slides=2,
            sections=[
                {
                    "section_title": "Introduction",
                    "order": 0,
                    "slides": [
                        {
                            "slide_number": 1,
                            "title": "What is AI?",
                            "key_points": ["Definition"],
                            "purpose": "Introduce artificial intelligence."
                        }
                    ]
                }
            ]
        )


# 5. Slide content validation

def test_invalid_slide_content_block():
    with pytest.raises(ValidationError):
        SlideContent(
            slide_number=1,
            section_title="Introduction",
            title="What is AI?",
            content_blocks=[
                {
                    "block_type": "bullet_list",
                    "text": "This should be a list."
                }
            ]
        )


# 6. Visual specification validation

def test_invalid_visual_layout():
    with pytest.raises(ValidationError):
        VisualSpecification(
            slide_number=1,
            layout_type="unknown_layout"
        )


# 7. Evaluation validation

def test_invalid_evaluation_score():
    with pytest.raises(ValidationError):
        PresentationEvaluation(
            overall_score=11,
            structure_score=8,
            research_quality_score=8,
            consistency_score=8,
            slide_evaluations=[
                {
                    "slide_number": 1,
                    "relevance_score": 8,
                    "factual_accuracy_score": 8,
                    "clarity_score": 8,
                    "visual_quality_score": 8,
                    "passed": True
                }
            ],
            revision_required=False
        )


# 8. Job and export validation

def test_invalid_job_progress():
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc)

    with pytest.raises(ValidationError):
        PresentationJob(
            job_id="job-001",
            progress=120,
            created_at=now,
            updated_at=now
        )


def test_invalid_export_format():
    from datetime import datetime, timezone

    with pytest.raises(ValidationError):
        PresentationExport(
            export_id="export-001",
            job_id="job-001",
            format="docx",
            created_at=datetime.now(timezone.utc)
        )
