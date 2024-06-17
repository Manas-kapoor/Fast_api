from fastapi import APIRouter, Request, Response
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pymongo import MongoClient
from config.db import conn
templates=Jinja2Templates(directory="Templates")


note=APIRouter()


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Notes.notes.find({})
    print(docs,"yo")
    new_docs=[]

    for doc in docs:
        new_docs.append({
            "id":doc["_id"],
            "title"  : doc["title"],
            "desc"  : doc["desc"],
            "important": doc["important"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "new_docs":new_docs})

@note.post("/")
async def create_item(request: Request):
    form=await request.form()
    formdict=dict(form)
    print(formdict)
    if "important" not in formdict:
        formdict["important"]=False
    formdict["important"]=True if formdict["important"]=='on' else False
    note=conn.Notes.notes.insert_one(formdict)
    return {"message":"Note created successfully"}

    