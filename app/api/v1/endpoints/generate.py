from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from instructor import patch
from datetime import datetime

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel

client = patch(OpenAI())


class ResponseModel(BaseModel):
    values: List[str]


router = APIRouter()

"""
This connects to our DynamoDb table
"""
db_client = QueryDatabaseClient()


@router.get("/generate/")
def generate_list(query: str, count: int = 20):
    # generate new completion with query
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=ResponseModel,
        max_retries=2,
        messages=[
            {
                "role": "user",
                "content": f"Generate a list of {count} {query} for a Dungeons and Dragons campaign",
            }
        ],
    )

    # save query
    db_client.save_query(
        QueryDatabaseModel(
            values=response.values, q=query, timestamp=datetime.now().isoformat()
        )
    )

    return response
