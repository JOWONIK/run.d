from typing import Union

from fastapi import FastAPI
from api import router
from db import MongoDataBase
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    MongoDataBase()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


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
