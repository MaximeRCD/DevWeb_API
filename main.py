from fastapi import FastAPI
from database import database
from routers import users
app = FastAPI()
app.include_router(users.user_router)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

