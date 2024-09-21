from typing import List

from pydantic import BaseModel
from app.services.generation.generation import GenerationService


class NameModel(BaseModel):
    values: List[str]


class NameGenerationService(GenerationService):
    def generate(self, query: str, count: int = 1) -> NameModel:
        completion = self._client.chat.completions.create(
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
