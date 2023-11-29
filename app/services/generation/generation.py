from instructor import patch
from openai import OpenAI, AsyncOpenAI


class GenerationService:
    _client: OpenAI | AsyncOpenAI

    def __init__(self) -> None:
        self._client = patch(OpenAI())
