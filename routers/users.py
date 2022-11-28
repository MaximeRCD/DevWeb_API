from fastapi import APIRouter
import sqlalchemy
from pydantic import BaseModel
import datetime
from database import database, metadata

user_router = APIRouter(
    prefix="/users",
    tags=['users']
)


class UserIn(BaseModel):
    last_name: str
    first_name: str
    email: str
    last_updated: datetime.datetime = datetime.datetime.now()


class User(BaseModel):
    id: int
    last_name: str
    first_name: str
    email: str
    last_updated: datetime.datetime


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=30)),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=30)),
    sqlalchemy.Column("email", sqlalchemy.String(length=100)),
    sqlalchemy.Column("last_updated", sqlalchemy.TIMESTAMP)
)


@user_router.get("/", tags=["users"], response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@user_router.post("/", tags=["users"], response_model=User)
async def create_user(user_in: UserIn):
    query = users.insert().values(
        last_name=user_in.last_name,
        first_name=user_in.first_name,
        email=user_in.email,
        last_updated=user_in.last_updated
    )
    insertion = await database.execute(query)
    return {**user_in.dict(), "id": insertion}


@user_router.get("/{username}", tags=["users"], response_model=User)
async def read_user(username: str):
    query = users.select().where(users.c.last_name == username)
    return await database.fetch_one(query)
