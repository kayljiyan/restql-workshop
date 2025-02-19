from datetime import datetime
from typing import List

import strawberry
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from app.db.session import get_db, graphql_db
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
        response.status_code = status.HTTP_201_CREATED
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
        response.status_code = status.HTTP_202_ACCEPTED
        return {"detail": "Entry updated successfully"}
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
        response.status_code = status.HTTP_204_NO_CONTENT
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": f"Error: {str(e)}"}


@strawberry.type
class Entry:
    entryId: str
    entryDetails: str
    createdAt: datetime


@strawberry.type
class Query:
    @strawberry.field
    def root(self) -> str:
        return "Welcome to RESTQL!"

    @strawberry.field
    def entries(self) -> List[Entry]:
        with graphql_db() as session:
            return service.retrieve_entries(session)

    @strawberry.field
    def entry(self, entryId: str) -> Entry:
        with graphql_db() as session:
            return service.retrieve_entry(session, entryId)


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
