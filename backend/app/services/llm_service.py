import logging
import time

from langchain_core.messages import HumanMessage, SystemMessage
from app.services.llm_factory import create_llm

logger = logging.getLogger(__name__)


class LLMService:

    def __init__(self):
        self.llm = create_llm()

    def _invoke_with_retry(self, llm, messages):
        max_attempts = 3

        for attempt in range(1, max_attempts + 1):
            try:
                return llm.invoke(messages)

            except Exception:
                logger.exception(
                    "LLM request failed on attempt %s/%s",
                    attempt,
                    max_attempts
                )

                if attempt == max_attempts:
                    raise

                time.sleep(2 ** (attempt - 1))

    def generate_response(
        self,
        system_prompt: str,
        user_prompt: str
    ) -> str:

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        response = self._invoke_with_retry(self.llm, messages)

        return response.content

    def generate_structured_response(
        self,
        system_prompt: str,
        user_prompt: str,
        output_schema
    ):

        structured_llm = self.llm.with_structured_output(
            output_schema,
            method="json_schema"
        )

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]

        response = self._invoke_with_retry(
            structured_llm,
            messages
        )

        return response
