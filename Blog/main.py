from fastapi import FastAPI
from pydantic import BaseModel
from . import schemas

app = FastAPI()

@app.post("/Blog")
def create_blog(blog: schemas.Blog):
    return {"Response":"Creating", "Data": {blog.title:blog.body}}