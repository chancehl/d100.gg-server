from app.services.generation.generation import GenerationService
from app.services.generation.monster import MonsterModel
from app.services.generation.weapon import WeaponModel
from app.services.generation.type import GenerationType


class ImageGenerationService(GenerationService):
    def generate(self, type: GenerationType, data: MonsterModel | WeaponModel) -> str:
        response = self._client.images.generate(
            prompt=f"The following {type.value} for a Dungeons and Dragons campaign: {data.name} ({data.description}). The style should match that of images found in Wizards of the Coast Dungeons and Dragons reference material (e.g. The Dungeon Masters Guide & The Players Handbook). Please do not include any text in the image.",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        return response.data[0].url
