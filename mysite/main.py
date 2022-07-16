from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Person(BaseModel):
    name: str
    lastname: str
    age: int


class Item(BaseModel):
    person: Person
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.person.name, "item_id": item_id}
