from fastapi import APIRouter
from pydantic import BaseModel
import datetime
from services import users_services

user_router = APIRouter(
    prefix="/users",
    tags=['users']
)


class UserIn(BaseModel):
    pseudo: str
    email: str
    password: str
    last_updated: datetime.datetime = datetime.datetime.now()


class User(BaseModel):
    id: int
    pseudo: str
    email: str
    password: str
    last_updated: datetime.datetime


@user_router.get("/", tags=["users"], response_model=list[User])
async def get_users():
    return await users_services.get_all_users()


@user_router.get("/{pseudo}", tags=["users"], response_model=User)
async def read_user(pseudo: str):
    return await users_services.get_user_by_pseudo(pseudo)


@user_router.post("/", tags=["users"], response_model=User)
async def create_user(user_in: UserIn):
    return await users_services.create_user(user_in)


@user_router.put("/{pseudo}/reset_pwd", tags=["users"])
async def reset_pwd(pseudo: str, pwd: str,  new_pwd: str):
    return await users_services.reset_password(pseudo, pwd, new_pwd)


@user_router.delete("/{pseudo}", tags=["users"])
async def delete_user(pseudo: str, pwd: str):
    return await users_services.delete_user(pseudo, pwd)


@user_router.put("/forgot_password", tags=["users"])
async def forgot_password(email: str):
    return await users_services.send_new_password(email)

