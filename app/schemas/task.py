from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class StoreEntry(BaseModel):
    entryDetails: str


class UpdateEntry(StoreEntry):
    entryId: UUID


class DeleteEntry(BaseModel):
    entryId: UUID


class Entry(UpdateEntry):
    createdAt: datetime
