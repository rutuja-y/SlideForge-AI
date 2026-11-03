from app.services.llm_service import LLMService
from app.schemas.outline import PresentationOutline


def test_generate_structured_outline():
    llm_service = LLMService()

    result = llm_service.generate_structured_response(
        system_prompt=(
            "You are an academic presentation planner. "
            "Generate accurate and concise presentation outlines."
        ),
        user_prompt=(
            "Create a presentation outline about Artificial Intelligence. "
            "Generate exactly 3 slides inside one section named Introduction. "
            "Use unique slide numbers starting from 1."
        ),
        output_schema=PresentationOutline
    )

    print("\nGenerated Outline:")
    print(result.model_dump())

    assert isinstance(result, PresentationOutline)
    assert result.total_slides == 3
