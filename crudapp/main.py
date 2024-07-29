
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from schemas import NoteModel, NoteCreateModel
from http import HTTPStatus
from typing import List
from models import Note
import uuid

app = FastAPI(
    title="Noted API", description="This is a simple note-taking service", docs_url="/"
)

# Create an async session object for CRUD
session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()

@app.get("/notes", response_model=List[NoteModel])
async def get_all_notes():
    """API endpoint for listing all note resources"""
    notes = await db.get_all(session)
    return [NoteModel.from_orm(note) for note in notes]

@app.post("/notes", status_code=HTTPStatus.CREATED, response_model=NoteModel)
async def create_note(note_data: NoteCreateModel) -> NoteModel:
    """API endpoint for creating a note resource"""
    new_note = Note(
        id=str(uuid.uuid4()), title=note_data.title, content=note_data.content
    )
    note = await db.add(session, new_note)
    return NoteModel.from_orm(note)

@app.get("/note/{note_id}", response_model=NoteModel)
async def get_note_by_id(note_id: str):
    """API endpoint for retrieving a note by its ID"""
    note = await db.get_by_id(session, note_id)
    return NoteModel.from_orm(note)

@app.patch("/note/{note_id}", response_model=NoteModel)
async def update_note(note_id: str, data: NoteCreateModel):
    """Update by ID"""
    note = await db.update(
        session, note_id, data={"title": data.title, "content": data.content}
    )
    return NoteModel.from_orm(note)

@app.delete("/note/{note_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_note(note_id: str) -> None:
    """Delete note by id"""
    note = await db.get_by_id(session, note_id)
    await db.delete(session, note)
    return None
