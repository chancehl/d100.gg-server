from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Annotated

from app.db.models.queries import QueryDatabaseClient
from app.services.generation.monster import MonsterGenerationService
from app.services.generation.image import ImageGenerationService
from app.services.generation.type import GenerationType


router = APIRouter()

db_client = QueryDatabaseClient()


@router.post("/generate/monster")
def generate_names(
    query: str,
    level: Annotated[int, Query(title="The level of the monster", ge=1, lt=20)] = 1,
    count: int = 1,
):
    # instantiate the appropriate generator service(s)
    monster_service = MonsterGenerationService()
    image_service = ImageGenerationService()

    # generate new completion with query
    monsters = monster_service.generate(query, level, count)

    # generate new image with query
    image = image_service.generate(GenerationType.MONSTER, monsters.values[0])

    # save query
    # db_client.save_query(
    #     QueryDatabaseModel(
    #         values=response.values, q=query, timestamp=datetime.now().isoformat()
    #     )
    # )

    # create response dict
    response = {"monster": monsters.values[0], "image": image}

    # json encode
    response_json = jsonable_encoder(response)

    # return response
    return JSONResponse(content=response_json)
