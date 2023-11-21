from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

from app.db.models.queries import QueryDatabaseClient, QueryDatabaseModel


class ResponseModel(BaseModel):
    queries: List[QueryDatabaseModel]


router = APIRouter()

"""
This connects to our DynamoDb table
"""
db_client = QueryDatabaseClient()


@router.get("/recent/queries")
def get_recent_queries(count: int = 10):
    return db_client.get_recent_queries(count=count)
