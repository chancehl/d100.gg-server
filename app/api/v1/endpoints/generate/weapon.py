from fastapi import APIRouter
from datetime import datetime

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel
from app.services.generation.weapon import WeaponGenerationService


router = APIRouter()

"""
This connects to our DynamoDb table
"""
db_client = QueryDatabaseClient()


@router.post("/generate/weapon")
def generate_weapons(query: str, count: int = 20):
    # instantiate the appropriate generator service
    service = WeaponGenerationService()

    # generate new completion with query
    response = service.generate(query, count)

    # save query
    # db_client.save_query(
    #     QueryDatabaseModel(
    #         values=response.values, q=query, timestamp=datetime.now().isoformat()
    #     )
    # )

    return response
