from pydantic import BaseModel


class Order(BaseModel):
    weight: int
    date: str
    address: str
    note: str



