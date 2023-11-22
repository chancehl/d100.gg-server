from instructor import patch
from openai import OpenAI, AsyncOpenAI


class GenerationService:
    client: OpenAI | AsyncOpenAI

    def __init__(self) -> None:
        self.client = patch(OpenAI())
