from fastapi import APIRouter
from services import scans_services
from pydantic import BaseModel
import datetime

scan_router = APIRouter(
    prefix="/scans",
    tags=['scans']
)


class ScanIn(BaseModel):
    predicted_class: str
    date: datetime.datetime
    score: float


class Scan(BaseModel):
    user_id: int
    predicted_class: str
    date: datetime.datetime
    score: float


@scan_router.get("/", tags=["scans"], response_model=list[Scan])
async def get_user_scans(user_id: int = None):
    if user_id:
        return await scans_services.get_scans_by_user_id(user_id)
    else:
        return await scans_services.get_all_scans()


@scan_router.get("/predicted_class_stats", tags=["scans"])
async def get_pcs_scans_stats(user_id: int = None):
    return await scans_services.get_pcs_scans_stats(user_id)
