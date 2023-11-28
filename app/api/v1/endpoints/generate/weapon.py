from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel
from app.services.generation.weapon import WeaponGenerationService
from app.services.generation.image import ImageGenerationService
from app.services.generation.type import GenerationType


router = APIRouter()


db_client = QueryDatabaseClient()


@router.post("/generate/weapon")
def generate_weapons(query: str, count: int = 20):
    # instantiate the appropriate generator service(s)
    weapon_service = WeaponGenerationService()
    image_service = ImageGenerationService()

    # generate new completion with query
    weapons = weapon_service.generate(query, count)

    # generate image
    image = image_service.generate(GenerationType.WEAPON , weapons.values[0])

    # save query
    # db_client.save_query(
    #     QueryDatabaseModel(
    #         values=response.values, q=query, timestamp=datetime.now().isoformat()
    #     )
    # )

    # create response dict
    response = { "weapon": weapons.values[0], "image": image }

    # json encode
    response_json = jsonable_encoder(response)

    # return response
    return JSONResponse(content=response_json)
