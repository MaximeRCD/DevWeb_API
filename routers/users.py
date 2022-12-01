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


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("pseudo", sqlalchemy.String(length=30)),
    sqlalchemy.Column("email", sqlalchemy.String(length=100)),
    sqlalchemy.Column("password", sqlalchemy.String(length=20)),
    sqlalchemy.Column("last_updated", sqlalchemy.TIMESTAMP)
)


@user_router.get("/", tags=["users"], response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@user_router.post("/", tags=["users"], response_model=User)
async def create_user(user_in: UserIn):
    query = users.insert().values(
        pseudo=user_in.pseudo,
        email=user_in.email,
        password=user_in.password,
        last_updated=user_in.last_updated
    )
    try:
        insertion = await database.execute(query)
        return {**user_in.dict(), "id": insertion}
    except Exception as e:
        print(e)
        return {**user_in.dict(), "id": 0}


@user_router.get("/{pseudo}", tags=["users"], response_model=User)
async def read_user(pseudo: str):
    query = users.select().where(users.c.pseudo == pseudo)
    return await database.fetch_one(query)

@user_router.put("/{pseudo}/reset_pwd", tags=["users"])
async def reset_pwd(pseudo: str, pwd: str,  new_pwd: str):
    query = users.update().where((users.c.pseudo == pseudo) & (users.c.password == pwd)).values(password=new_pwd)
    reset_status =  await database.execute(query)
    if reset_status == 1:
        return {"message" : f"Password for user {pseudo} has been successfully set to {new_pwd}"}
    else:
        return {"message" : f" Wrong password given ! Can not modify it !"}

@user_router.delete("/{pseudo}", tags=["users"])
async def delete_user(pseudo: str, pwd: str):
    query = users.delete().where((users.c.pseudo == pseudo) & (users.c.password == pwd))
    # delete also all the data concerning the user in scan table
    delete_status =  await database.execute(query)
    if delete_status == 1:
        return {"message" : f"User {pseudo} has been successfully deleted"}
    else:
        return {"message" : f" Wrong password given ! Can not delete this user !"}


