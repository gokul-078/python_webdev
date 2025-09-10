# import fastapi
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# To run the application
app = FastAPI()

# Pydantic base model it is the model used to define the required data to post or store in our DB.
class Items(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[bool] = False

@app.post("/items")
def items(item: Items):
    return item

@app.post("/items/name")
def items(item: Items):
    return {f'The items is {item.name}'}