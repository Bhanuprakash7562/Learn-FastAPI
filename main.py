from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import uvicorn


app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool  = True, sort: Optional[str] = None):
    # ENDPOINT will be like "http://localhost:8000/blog?limit=50&published=true/false ===> these are called query parameters"
    if published:
        return {"data":{"Blog-List":f"{limit} published Blogs from the List of all Blogs {sort}"}}
    else:
        return {"data":{"Blog-List":f"{limit} Un-Published Blogs from the List of all Blogs {sort}"}}

@app.get("/blog/unpublished")
def data():
    return {"data":{"Blog-Details": "List of all Unpublished Blogs"}}

@app.get("/blog/{id}")
def data(id: int):
    return {"data":{"Blog-Id": id}}

'''
It will through Invalid data type error,
because the request will go to the above endpoint because python goes line by line.
(The above end point looks for int datatype but we have passed "unpublished"). So we should put this end point above the /blog/{id} endpoint
'''
# @app.get("/blog/unpublished")
# def data():
#     return {"data":{"Blog-Details": "List of all Unpublished Blogs"}}

@app.get("/blog/{id}/{name}/comments")
def data(id: int, name: str):
    # ENDPOINT will be like "http://localhost:8000/blog/100/bhanu/comments ===> these are called path parameters"
    return {"data":
            {"Blog-Id": id,
             "Name": name,
             "Comments": "this is the Blog-"+str(id)+" and the client-Name is "+name}
             }


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[datetime] = None



@app.post("/create-blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with Title as {request.title}, and the body is {request.body}. The Blog was published at {request.published_at}."}


# if __name__ == "__main__":
#     uvicorn.run(app=app, host="localhost", port=7562, reload=True)