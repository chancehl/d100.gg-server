from typing import List
from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from instructor import patch

client = patch(OpenAI())


class CategoryEnum(str, Enum):
    objects = "objects"
    items = "items"
    names = "names"
    places = "places"


class ValueModel(BaseModel):
    value: str


class ResponseModel(BaseModel):
    values: List[ValueModel]
    # category: CategoryEnum


router = APIRouter()


@router.get("/generate/")
def generate_list(query: str, count: int = 20):
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

    return response
