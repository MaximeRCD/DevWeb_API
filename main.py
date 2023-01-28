from fastapi import FastAPI
from database import database
from routers import users, scans, model,stats
from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.user_router)
app.include_router(model.model_router)
app.include_router(scans.scan_router)
app.include_router(stats.stats_router)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

