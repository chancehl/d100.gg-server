from pydantic import BaseModel
from typing import List

from .generation import GenerationService

class NameModel(BaseModel):
    values: List[str]

class NameGenerationService(GenerationService):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, query: str, count: int = 1) -> NameModel:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=NameModel,
            max_retries=2,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a list of {count} {query} for a Dungeons and Dragons campaign",
                }
            ],
        )

        return completion
