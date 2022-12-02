from typing import List

from fastapi import APIRouter
from services import model_services
model_router = APIRouter(
    prefix="/model",
    tags=['model']
)

@model_router.get("/", tags=['model'])
async def prediction(imageUrl: str):
    predict_class = model_services.predict(imageUrl)
    return {"image" : f"{imageUrl}", "class": f"{predict_class}"}

