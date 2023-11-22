from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from instructor import patch
from datetime import datetime
from enum import Enum

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel
from app.services.generation.name import NameGenerationService

client = patch(OpenAI())

class GenerationType(str, Enum):
    item = 'item'
    name = 'name'
    place = 'place'
    monster = 'monster'
    other = 'other'

class ResponseModel(BaseModel):
    values: List[str]


router = APIRouter()

"""
This connects to our DynamoDb table
"""
db_client = QueryDatabaseClient()


@router.get("/generate/")
def generate_list(query: str, count: int = 20, type: GenerationType = GenerationType.other):
    # instantiate the appropriate generator service
    service = NameGenerationService()

    # generate new completion with query
    response = service.generate(query, count)

    # save query
    db_client.save_query(
        QueryDatabaseModel(
            values=response.values, q=query, timestamp=datetime.now().isoformat()
        )
    )

    return response
