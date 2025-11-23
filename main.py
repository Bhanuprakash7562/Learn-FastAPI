from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"data":{"wish":"Hello world"}}

@app.get("/about")
def data():
    return {"data":{"Name": "Kocharla Bhanuprakash"}}