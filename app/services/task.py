from sqlalchemy.orm import Session

from app.db.models import task as model
from app.schemas import task as schema


def store_entry(session: Session, entry: schema.StoreEntry):
    db_entry = model.Entry(entryDetails=entry.entryDetails)
    session.add(db_entry)
    session.commit()


def retrieve_entries(session: Session):
    db_entries = session.query(model.Entry).all()
    return db_entries


def retrieve_entry(session: Session, entry: schema.DeleteEntry):
    db_entry = (
        session.query(model.Entry).filter(model.Entry.entryId == entry.entryId).first()
    )
    return db_entry


def update_entry(session: Session, entry: schema.UpdateEntry):
    db_entry = session.query(model.Entry).filter(model.Entry.entryId == entry.entryId)
    db_entry.update({"entryDetails": entry.entryDetails})
    session.commit()


def delete_entry(session: Session, entry: schema.DeleteEntry):
    db_entry = session.query(model.Entry).filter(model.Entry.entryId == entry.entryId)
    db_entry.delete()
    session.commit()
