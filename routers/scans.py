from binascii import a2b_base64
from fastapi import APIRouter, Form
from services import scans_services
from pydantic import BaseModel
import datetime

scan_router = APIRouter(
    prefix="/scans",
    tags=['scans']
)

IMAGEDIR="./img/"

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


@scan_router.post("/images/")

# Form est util pour la lecture des données envoyer avec le type FormData (voir front sur la capture de l'image)
async def UploadImage(img:str = Form(),name:str = Form()):

    data: bytes = img.split(",")[1]
    filename = name
    binary_data = a2b_base64(data)
    with open(f"{IMAGEDIR}{filename}", "wb") as f:
        f.write(binary_data)
    return  {"image" : f"{filename}", "action":"Saved"}