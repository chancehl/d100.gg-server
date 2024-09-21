from typing import List

from pydantic import BaseModel


class QueryDatabaseModel(BaseModel):
    q: str
    values: List[str]
    timestamp: str


class QueryDatabaseClient:
    def __init__(self):
        pass

    def save_query(self, query: QueryDatabaseModel):
        pass

    def get_recent_queries(self, count: int = 10):
        pass

    def lookup_query(self, query: str):
        pass

    def update_query(self, query: str, values: List[str]):
        pass
