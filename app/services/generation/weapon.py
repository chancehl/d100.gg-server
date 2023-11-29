from pydantic import BaseModel
from typing import List

from .generation import GenerationService


class DamageModel(BaseModel):
    num_dice: int
    dice_sides: int
    damage_type: str


class StatBlockModel(BaseModel):
    attack_type: str
    reach: int
    melee_range: int
    thrown_range: int
    damage: DamageModel
    weight: int
    properties: List[str]


class WeaponModel(BaseModel):
    name: str
    description: str
    stat_block: StatBlockModel


class GeneratedWeaponModel(BaseModel):
    values: List[WeaponModel]


class WeaponGenerationService(GenerationService):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, query: str, count: int = 1) -> GeneratedWeaponModel:
        completion = self._client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=GeneratedWeaponModel,
            max_retries=2,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a list of {count} {query} (weapon(s)) for a Dungeons and Dragons campaign",
                }
            ],
        )

        return completion
