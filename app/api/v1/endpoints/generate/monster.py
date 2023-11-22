from fastapi import APIRouter, Query
from datetime import datetime
from typing import Annotated

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel
from app.services.generation.monster import MonsterGenerationService


router = APIRouter()

db_client = QueryDatabaseClient()


@router.post("/generate/monster")
def generate_names(query: str, level: Annotated[int, Query(title="The level of the monster", ge=1, lt=20)] = 1, count: int = 1):
    # instantiate the appropriate generator service
    service = MonsterGenerationService()

    # generate new completion with query
    response = service.generate(query, level, count)

    # save query
    # db_client.save_query(
    #     QueryDatabaseModel(
    #         values=response.values, q=query, timestamp=datetime.now().isoformat()
    #     )
    # )

    return response
