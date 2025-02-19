from datetime import datetime

from sqlalchemy import UUID
from sqlalchemy.dialects.sqlite import TEXT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Entry(Base):
    __tablename__ = "entries"

    entryId: Mapped[UUID] = mapped_column(UUID, primary_key=True)
    entryDetails: Mapped[str] = mapped_column(TEXT(200), nullable=True)
    createdAt: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=datetime.now()
    )
