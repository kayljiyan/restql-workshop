from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class StoreEntry(BaseModel):
    entryDetails: str


class Entry(StoreEntry):
    entryId: UUID
    createdAt: datetime
