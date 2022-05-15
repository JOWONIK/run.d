from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/blah")
def blah():
    return "blah"
  
  
@app.get("/apple")
def apple():
    return "apple JJang~?"


@app.get("/items")
def read_items():
    results = {
        "01": "Hello",
        "02": "World!"
    }
    return results


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
