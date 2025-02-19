from fastapi import APIRouter

from app.api.endpoints import task

v1_router = APIRouter()

v1_router.include_router(task.router, prefix="/main", tags=["main"])
