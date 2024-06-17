from typing import Union

from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pymongo import MongoClient


app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="Templates")
conn=MongoClient('mongodb+srv://manaskapoor3000:Manaskapoor1@cluster0.hlivcrp.mongodb.net/')

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Notes.notes.find({})
    
    new_docs=[]
    for doc in docs:
        new_docs.append({
            "id":doc["_id"],
            "note"  : doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "new_docs":new_docs})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}