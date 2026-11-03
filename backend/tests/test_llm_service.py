from app.services.llm_service import LLMService

def test_groq_llm_connection():
    llm_service = LLMService()

    response = llm_service.generate_response(
        system_prompt="You are a helpful assistant.",
        user_prompt="Reply with exactly: SlideForge AI is connected."
    )
    

    print("\nLLM Response:", response)

    assert isinstance(response, str)
    assert len(response.strip()) > 0
