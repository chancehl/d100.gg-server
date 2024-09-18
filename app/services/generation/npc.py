from typing import List

from pydantic import BaseModel
from generation import GenerationService


class NpcModel(BaseModel):
    name: str
    description: str
    race: str
    languages: List[str]
    quirks: List[str] | None
    short_backstory: str


class GeneratedNpcModel(BaseModel):
    values: List[NpcModel]


class NpcGenerationService(GenerationService):
    def generate(self, query: str, count: int = 1) -> GeneratedNpcModel:
        completion = self._client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=GeneratedNpcModel,
            max_retries=2,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a list of {count} {query} (non-player chracter(s)) for a Dungeons and Dragons campaign",
                }
            ],
        )

        return completion
