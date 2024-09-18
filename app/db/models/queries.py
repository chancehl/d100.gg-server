from typing import List

from boto3 import resource
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.table import TableResource
from pydantic import BaseModel


class QueryDatabaseModel(BaseModel):
    q: str
    values: List[str]
    timestamp: str


class QueryDatabaseClient:
    table: TableResource = None

    def __init__(self):
        self.resource = resource("dynamodb")
        self.table = self.resource.Table("queries")

    def save_query(self, query: QueryDatabaseModel):
        self.table.put_item(
            Item={"timestamp": query.timestamp, "q": query.q, "values": query.values}
        )

    def get_recent_queries(self, count: int = 10):
        response = self.table.scan(Limit=count)

        if response["Count"] > 0:
            return response["Items"]

        return []

    def lookup_query(self, query: str):
        response = self.table.query(KeyConditionExpression=Key("q").eq(query))

        if response["Count"] > 0:
            return response["Items"][0]

        return None

    def update_query(self, query: str, values: List[str]):
        response = self.table.update_item(
            Key={"q": query},
            UpdateExpression="SET values = :v",
            ExpressionAttributeValues={":v": values},
        )

        return response
