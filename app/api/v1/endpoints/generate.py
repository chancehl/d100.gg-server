from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from instructor import patch

client = patch(OpenAI())


class ValueModel(BaseModel):
    value: str


class ResponseModel(BaseModel):
    values: List[ValueModel]


router = APIRouter()


@router.get("/generate/")
def generate_list(q: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=ResponseModel,
        messages=[
            {
                "role": "user",
                "content": f"Generate a list of 25 {q} for a Dungeons and Dragons campaign",
            }
        ],
    )

    return response
