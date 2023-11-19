from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
from instructor import patch

client = patch(OpenAI())


class ResponseModel(BaseModel):
    confidence: float
    is_valid: bool


router = APIRouter()


@router.get("/validate/")
def validate_query(query: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=ResponseModel,
        messages=[
            {
                "role": "user",
                "content": f"Determine whether or not this is a valid thing you'd find within a Dungeons and Dragons universe: {query}",
            }
        ],
    )

    return response
