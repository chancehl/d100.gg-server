from pydantic import BaseModel
from typing import List

from .generation import GenerationService
from .monster import MonsterModel

class ImageGenerationService(GenerationService):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, monster: MonsterModel) -> str:
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=f"The following monster for a Dungeons and Dragons campaign: {monster.name} ({monster.description}). The style should match that of images found in Wizards of the Coast Dungeons and Dragons reference material (e.g. The Dungeon Masters Guide & The Players Handbook)",
            size="1024x1024",
            quality="standard",
            n=1
        )

        return response.data[0].url
