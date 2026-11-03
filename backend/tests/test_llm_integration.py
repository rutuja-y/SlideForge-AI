from app.services.llm_service import LLMService
from app.schemas.outline import PresentationOutline

def test_complete_llm_integration():

    llm_service = LLMService()

    # Test normal text generation
    response = llm_service.generate_response(
        system_prompt="You are an academic presentation assistant.",
        user_prompt="Explain Artificial Intelligence in two sentences."
    )

    assert isinstance(response, str)
    assert len(response.strip()) > 0

    # Test structured output generation
    outline = llm_service.generate_structured_response(
        system_prompt=(
            "You are an academic presentation planner. "
            "Return a valid presentation outline."
        ),
        user_prompt=(
            "Create an academic presentation about Machine Learning. "
            "Generate exactly 3 slides in one section named Introduction. "
            "Use slide numbers 1, 2, and 3."
        ),
        output_schema=PresentationOutline
    )

    assert isinstance(outline, PresentationOutline)
    assert outline.total_slides == 3

    print("\nNormal response:", response)
    print("\nStructured outline:", outline.model_dump())
