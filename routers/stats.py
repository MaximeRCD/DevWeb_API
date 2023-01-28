from typing import List
from pydantic import BaseModel
from fastapi import APIRouter
from services import database_services

stats_router = APIRouter(
    prefix="/stats",
    tags=['stats']
)

class Prediction(BaseModel):
    user_id : int
    predicted_class : str
    score : float
@stats_router.get("/", tags=['stats'],response_model=Prediction)
async def prediction(prediction: Prediction):
    return await database_services.save_prediction(prediction)