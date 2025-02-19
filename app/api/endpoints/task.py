import os

from fastapi import APIRouter, Depends, Response, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import task as schema
from app.services import task as service

router = APIRouter()


@router.post("/entry")
async def store_entry(
    entry: schema.StoreEntry,
    response: Response,
    session: Session = Depends(get_db),
):
    try:
        service.store_entry(session, entry)
        response.status_code = status.HTTP_200_OK
        return {"detail": "Entry stored successfully"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": f"Error: {str(e)}"}


@router.patch("/entry")
async def update_entry(
    entry: schema.UpdateEntry,
    response: Response,
    session: Session = Depends(get_db),
):
    try:
        service.update_entry(session, entry)
        response.status_code = status.HTTP_200_OK
        return {"detail": "Entry stored successfully"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": f"Error: {str(e)}"}


@router.delete("/entry")
async def delete_entry(
    entry: schema.DeleteEntry,
    response: Response,
    session: Session = Depends(get_db),
):
    try:
        service.delete_entry(session, entry)
        response.status_code = status.HTTP_200_OK
        return {"detail": "Entry stored successfully"}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": f"Error: {str(e)}"}
