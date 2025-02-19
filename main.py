from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import v1_router
from app.db.base import Base
from app.db.session import engine


@asynccontextmanager
async def lifespan(fastapp: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    print("Server shutting down...")


fastapp = FastAPI(lifespan=lifespan)

fastapp.include_router(v1_router, prefix="/api/v1")


@fastapp.get("/")
async def root():
    return {"message": "Welcome to RESTQL!"}
