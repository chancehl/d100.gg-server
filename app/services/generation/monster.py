from typing import List

from pydantic import BaseModel

from app.services.generation.generation import GenerationService


class AttackModel(BaseModel):
    name: str
    description: str
    hit: int | str
    num_targets: int
    attack_range: int | str
    damage_type: str = "N/A"


class MonsterStatBlockModel(BaseModel):
    armor_class: int
    hitpoints: int
    speed: int
    proficiency_bonus: int
    str: int
    dex: int
    con: int
    cha: int
    wis: int
    languages: List
    level: int


class MonsterModel(BaseModel):
    name: str
    description: str
    stats: MonsterStatBlockModel


class GeneratedMonsterModel(BaseModel):
    values: List[MonsterModel]


class MonsterGenerationService(GenerationService):
    def generate(
        self, query: str, level: int = 3, count: int = 1
    ) -> GeneratedMonsterModel:
        completion = self._client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=GeneratedMonsterModel,
            max_retries=2,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a list of {count} {query} (level {level} monster(s)) for a Dungeons and Dragons campaign.",
                }
            ],
        )

        return completion
