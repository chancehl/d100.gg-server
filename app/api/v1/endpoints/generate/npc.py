from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel

from app.services.generation.npc import NpcGenerationService
from app.services.generation.image import ImageGenerationService
from app.services.generation.type import GenerationType


router = APIRouter()


db_client = QueryDatabaseClient()


@router.post("/generate/npc")
def generate_weapons(query: str, count: int = 1):
    # instantiate the appropriate generator service(s)
    npc_service = NpcGenerationService()
    image_service = ImageGenerationService()

    # generate new completion with query
    npcs = npc_service.generate(query, count)

    # generate image
    image = image_service.generate(GenerationType.NPC, npcs.values[0])

    # save query
    # db_client.save_query(
    #     QueryDatabaseModel(
    #         values=response.values, q=query, timestamp=datetime.now().isoformat()
    #     )
    # )

    # create response dict
    response = {"npc": npcs.values[0], "image": image}

    # json encode
    response_json = jsonable_encoder(response)

    # return response
    return JSONResponse(content=response_json)
